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
variable "nsxt_tier0_name" {
    type = string
    description = "NSX-T Tier0 Name for BGP Configuration"
    default = ""
}
variable "nsxt_route_type" {
    type = string
    description = "NSX-T Route Type to Redistribute"
    default =  "TIER1_CONNECTED,TIER1_STATIC"
}