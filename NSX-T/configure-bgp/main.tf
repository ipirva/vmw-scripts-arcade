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
resource "nsxt_policy_bgp_config" "bgp_configuration" {
  gateway_path = data.nsxt_policy_tier0_gateway.tier0gw.path
  enabled = var.bgp_enabled
  inter_sr_ibgp = var.bgp_inter_sr_ibgp
  local_as_num = var.bgp_local_as_num
  multipath_relax = var.bgp_multipath_relax
  ecmp = var.bgp_ecmp
  graceful_restart_mode = var.bgp_graceful_restart_mode
  graceful_restart_timer = var.bgp_graceful_restart_timer
  graceful_restart_stale_route_timer = var.bgp_graceful_restart_stale_route_timer
  dynamic "tag" {
    for_each = local.nsxt_tags
    content {
      scope = tag.value["scope"]
      tag = tag.value["tag"]
    }
  }
}