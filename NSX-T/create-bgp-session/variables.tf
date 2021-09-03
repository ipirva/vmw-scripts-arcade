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
variable "bgp_neighbor_description" {
    type = string
    description = "BGP Neighbor Description"
    default = "My BGP Neighbor"
}
variable "bgp_allow_as_in" {
    type = bool
    description = "BGP Allow AS In"
    default = false
}
variable "bgp_graceful_restart_mode" {
    type = string
    description = "BGP Graceful Restart Mode"
    default = "DISABLE"
    validation {
        condition     = contains(["HELPER_ONLY", "DISABLE", "GR_AND_HELPER"], var.bgp_graceful_restart_mode)
        error_message = "Valid values for var: bgp_graceful_restart_mode are (HELPER_ONLY, DISABLE, GR_AND_HELPER)."
    }
}
variable "bgp_hold_down_time" {
    type = number
    description = "BGP Hold Down Time"
    default = 180
}
variable "bgp_keep_alive_time" {
    type = number
    description = "BGP Keep Alive Time"
    default = 60
}
variable "bgp_neighbor_address" {
    type = string
    description = "BGP Neighbor Address"
}
# value expected: IPV4 or IPV6
variable "bgp_neighbor_type" {
    type = string
    description = "BGP Neighbor Type: IPV4 or IPV6"
    default = "IPV6"
    validation {
        condition     = contains(["IPV4", "IPV6"], var.bgp_neighbor_type)
        error_message = "Valid values for var: bgp_neighbor_type are (IPV4, IPV6)."
    }
}
# bgp_neighbor_in/out_prefixlist
# value expected: empty, PERMIT/DENY [IPV4/IPV6 prefix a.b.c.d/mask] LE xx GE xx
# LE and/or GE can be in any order and can as well be omitted
variable "bgp_neighbor_in_prefixlist" {
    type = string
    description = "BGP Neighbor IN Prefix-list"
    default = ""
}
variable "bgp_neighbor_out_prefixlist" {
    type = string
    description = "BGP Neighbor OUT Prefix-list"
    default = ""
}
variable "bgp_neighbor_password" {
    type = string
    description = "BGP Neighbor password"
    default = null
}
variable "bgp_remote_as_num" {
    type = string
    description = "BGP Remote AS Number"
    default = ""
}
variable "bgp_maximum_hop_limit" {
    type = number
    description = "BGP Neighbor Maximum Hop Limit"
    default = 1
}
variable "bgp_bfd_enabled" {
    type = bool
    description = "BGP BFD Enabled?"
    default = false
}
variable "bgp_bfd_interval" {
    type = number
    description = "BGP BFD Interval"
    default = 500
}
variable "bgp_bfd_multiple" {
    type = number
    description = "BGP BFD Multiple"
    default = 3
}
variable "nsxt_tier0_name" {
    type = string
    description = "NSX-T Tier0 Name for BGP Neighbor Configuration"
    default = ""
}
variable "nsxt_tag" {
    type = string
    description = "NSX-T Tag Applied to BGP Neighbor"
    default = ""
}