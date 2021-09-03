# Variables
variable "nsxt_manager_vip" {
    type = string
    description = "NSX-T Manager VIP or DNS"
}
variable "nsxt_manager_username" {
    type = string
    description = "NSX-T Manager Username"
    default = "admin"
}
variable "nsxt_manager_password" {
    type = string
    description = "NSX-T Manager Password"
}
variable "bgp_enabled" {
    type = bool
    description = "BGP Enabled?"
    default = true
}
variable "bgp_inter_sr_ibgp" {
    type = bool
    description = "BGP Inter SR iBGP Enabled?"
    default = "true"

}
variable "bgp_local_as_num" {
    type = string
    description = "BGP Local AS Number"
    default = ""
}  
variable "bgp_graceful_restart_mode" {
    type = string
    description = "BGP Graceful Restart Mode"
    default = "HELPER_ONLY"
    validation {
        condition     = contains(["HELPER_ONLY", "DISABLE", "GR_AND_HELPER"], var.bgp_graceful_restart_mode)
        error_message = "Valid values for var: bgp_graceful_restart_mode are (HELPER_ONLY, DISABLE, GR_AND_HELPER)."
    }
}
variable "bgp_graceful_restart_timer" {
    type = number
    description = "BGP Graceful Restart Timer"
    default = 180
}
variable "bgp_graceful_restart_stale_route_timer" {
    type = number
    description = "BGP Graceful Restart Stale Route Timer"
    default = 600
}
variable "bgp_ecmp" {
    type = bool
    description = "BGP ECMP Enabled?"
    default = true
}
variable "bgp_multipath_relax" {
    type = bool
    description = "BGP Multipath Relax Enabled?"
    default = true
}
variable "nsxt_tier0_name" {
    type = string
    description = "NSX-T Tier0 Name for BGP Configuration"
    default = ""
}
variable "nsxt_tag" {
    type = string
    description = "NSX-T Tag Applied to BGP Configuration"
    default = ""
}