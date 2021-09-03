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
  nsxt_route_type_custom = split(",", upper(var.nsxt_route_type))
  nsxt_route_types = [for v in local.nsxt_route_type_custom: trimspace(v)]
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
resource "nsxt_policy_gateway_redistribution_config" "bgp_route_redistribution_configuration" {
  gateway_path = data.nsxt_policy_tier0_gateway.tier0gw.path
  bgp_enabled = var.bgp_enabled
  
  rule {
    name  = "default"
    types = local.nsxt_route_types
  }
}