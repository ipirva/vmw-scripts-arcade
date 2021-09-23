# IpDiscoverySwitchingProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arp_snooping_enabled** | **bool** | Indicates whether ARP snooping is enabled | [optional] [default to True]
**arp_bindings_limit** | **int** | Indicates the number of arp snooped IP addresses to be remembered per LogicalPort. Decreasing this value, will retain the latest bindings from the existing list of address bindings. Increasing this value will retain existing bindings and also learn any new address bindings discovered on the port until the new limit is reached. This limit only applies to IPv4 addresses and is independent of the nd_bindings_limit used for IPv6 snooping. | [optional] [default to 1]
**dhcpv6_snooping_enabled** | **bool** | This option is the IPv6 equivalent of DHCP snooping. | [optional] [default to False]
**nd_snooping_enabled** | **bool** | This option is the IPv6 equivalent of ARP snooping. | [optional] [default to False]
**vm_tools_v6_enabled** | **bool** | This option is only supported on ESX where vm-tools is installed. | [optional] [default to False]
**dhcp_snooping_enabled** | **bool** | Indicates whether DHCP snooping is enabled | [optional] [default to True]
**arp_nd_binding_timeout** | **int** | This property controls the ARP and ND cache timeout period.It is recommended that this property be greater than the ARP/ND cache timeout on the VM.  | [optional] [default to 10]
**vm_tools_enabled** | **bool** | This option is only supported on ESX where vm-tools is installed. | [optional] [default to True]
**trust_on_first_use_enabled** | **bool** | ARP snooping being inherently susceptible to ARP spoofing, uses a turst-on-fisrt-use (TOFU) paradigm where only the first IP address discovered via ARP snooping is trusted. The remaining are ignored. In order to allow for more flexibility, we allow the user to configure how many ARP snooped address bindings should be trusted for the lifetime of the logical port. This is controlled by the arp_bindings_limit property in the IP Discovery profile. We refer to this extension of TOFU as N-TOFU. However, if TOFU is disabled, then N ARP snooped IP addresses will be trusted until they are timed out, where N is configured by arp_bindings_limit.  | [optional] [default to True]
**nd_bindings_limit** | **int** | Indicates the number of neighbor-discovery snooped IP addresses to be remembered per LogicalPort. Decreasing this value, will retain the latest bindings from the existing list of address bindings. Increasing this value will retain existing bindings and also learn any new address bindings discovered on the port until the new limit is reached. This limit only applies to IPv6 addresses and is independent of the arp_bindings_limit used for IPv4 snooping. | [optional] [default to 3]
**duplicate_ip_detection** | [**DuplicateIPDetection**](DuplicateIPDetection.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

