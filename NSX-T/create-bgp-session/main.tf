# Terraform Provider
terraform {
  required_providers {
    nsxt = {
      source = "vmware/nsxt"
      version = "3.2.4"
    }
  }
}
# Variables
locals {
  nsxt_tags_custom = flatten((split(",", trimspace(var.nsxt_tag))))
  nsxt_tags = [ 
    for custom_value in local.nsxt_tags_custom : {
      scope = try(trimspace(split("=", trimspace(custom_value))[0]), null)
      tag   = try(trimspace(split("=", trimspace(custom_value))[1]), null)
    }
  ]
  # default values for le, ge and network to use in prefix-list
  le = upper(var.bgp_neighbor_type) == "IPV4" ? 32 : 128
  ge = upper(var.bgp_neighbor_type) == "IPV4" ? 32 : 128
  network = upper(var.bgp_neighbor_type) == "IPV4" ? "0.0.0.0/0" : "::/0"
  # replace multiple spaces
  bgp_neighbor_in_prefixlist = upper(replace(trimspace(var.bgp_neighbor_in_prefixlist), "/\\s{1,}/", " "))
  bgp_neighbor_out_prefixlist = upper(replace(trimspace(var.bgp_neighbor_out_prefixlist), "/\\s{1,}/", " "))
  # compose the inbound prefix list prefix {}
  bgp_neighbor_in_prefixlist_custom = flatten((split(",", local.bgp_neighbor_in_prefixlist)))
  bgp_neighbor_in_prefixlist_entries = length(local.bgp_neighbor_in_prefixlist) == 0 ? [{action = "PERMIT", network = local.network, le = local.le, ge = local.ge}] : [
    for custom_value in local.bgp_neighbor_in_prefixlist_custom : {
      action = try(split(" ", trimspace(custom_value))[0], "PERMIT")
      network = try(split(" ", trimspace(custom_value))[1], null)
      mask = try(split("/", split(" ", trimspace(custom_value))[1])[1], null)
      ge = try(split(" ", split("GE", trimspace(custom_value))[1])[1], try(split("/", split(" ", trimspace(custom_value))[1])[1], null))
      le = try(split(" ", split("LE", trimspace(custom_value))[1])[1], try(split("/", split(" ", trimspace(custom_value))[1])[1], null))
    }
  ]
  # compose the outbound prefix list prefix {}
  bgp_neighbor_out_prefixlist_custom = flatten((split(",", local.bgp_neighbor_out_prefixlist)))
  bgp_neighbor_out_prefixlist_entries = length(local.bgp_neighbor_out_prefixlist) == 0 ? [{action = "PERMIT", network = local.network, le = local.le, ge = local.ge}] : [
    for custom_value in local.bgp_neighbor_out_prefixlist_custom : {
      action = try(split(" ", trimspace(custom_value))[0], "PERMIT")
      network = try(split(" ", trimspace(custom_value))[1], null)
      mask = try(split("/", split(" ", trimspace(custom_value))[1])[1], null)
      ge = try(split(" ", split("GE", trimspace(custom_value))[1])[1], try(split("/", split(" ", trimspace(custom_value))[1])[1], null))
      le = try(split(" ", split("LE", trimspace(custom_value))[1])[1], try(split("/", split(" ", trimspace(custom_value))[1])[1], null))
    }
  ]
}
# NSX-T Manager Credentials
provider "nsxt" {
    host                     = var.nsxt_manager_vip
    username                 = var.nsxt_manager_username
    password                 = var.nsxt_manager_password
    allow_unverified_ssl     = true
    max_retries              = 10
    retry_min_delay          = 500
    retry_max_delay          = 5000
    retry_on_status_codes    = [429]
    global_manager           = false
}
# Data source
data "nsxt_policy_tier0_gateway" "tier0gw" {
  display_name = var.nsxt_tier0_name
}
# Resources
resource "nsxt_policy_gateway_prefix_list" "in_prefix_list" {
  display_name = "IN Prefix-list ${var.bgp_neighbor_address}_${var.bgp_remote_as_num}"
  gateway_path = data.nsxt_policy_tier0_gateway.tier0gw.path
  # prefix {}
  dynamic "prefix" {
    for_each = local.bgp_neighbor_in_prefixlist_entries
    content {
      action = prefix.value["action"]
      network = prefix.value["network"]
      ge = prefix.value["ge"]
      le = prefix.value["le"]
    }
  }
}
resource "nsxt_policy_gateway_prefix_list" "out_prefix_list" {
  display_name = "OUT Prefix-list ${var.bgp_neighbor_address}_${var.bgp_remote_as_num}"
  gateway_path = data.nsxt_policy_tier0_gateway.tier0gw.path
  # prefix {}
  dynamic "prefix" {
    for_each = local.bgp_neighbor_out_prefixlist_entries
    content {
      action = prefix.value["action"]
      network = prefix.value["network"]
      ge = prefix.value["ge"]
      le = prefix.value["le"]
    }
  }
}
resource "nsxt_policy_bgp_neighbor" "bgp_neighbor" {
  display_name = "BGP Neighbor Configuration"
  description = var.bgp_neighbor_description
  bgp_path = "/infra/tier-0s/${var.nsxt_tier0_name}/locale-services/default/bgp"
  allow_as_in = var.bgp_allow_as_in
  graceful_restart_mode = var.bgp_graceful_restart_mode
  hold_down_time = var.bgp_hold_down_time
  keep_alive_time = var.bgp_keep_alive_time
  neighbor_address = var.bgp_neighbor_address
  password = trimspace(var.bgp_neighbor_password)
  remote_as_num = var.bgp_remote_as_num
  maximum_hop_limit = var.bgp_maximum_hop_limit

  bfd_config {
    enabled = var.bgp_bfd_enabled
    interval = var.bgp_bfd_interval
    multiple = var.bgp_bfd_multiple
  }

  route_filtering {
    address_family = upper(var.bgp_neighbor_type)
    in_route_filter  = nsxt_policy_gateway_prefix_list.in_prefix_list.path
    out_route_filter = nsxt_policy_gateway_prefix_list.out_prefix_list.path
  }

  dynamic "tag" {
    for_each = local.nsxt_tags
    content {
      scope = tag.value["scope"]
      tag = tag.value["tag"]
    }
  }
}