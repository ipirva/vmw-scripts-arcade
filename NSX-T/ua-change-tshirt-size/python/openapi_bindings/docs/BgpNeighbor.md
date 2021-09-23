# BgpNeighbor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graceful_restart_mode** | **str** | BGP Graceful Restart mode. If specified, then it will take precedence over global Graceful Restart mode configured in logical router BgpConfig otherwise BgpConfig level Graceful Restart mode will be applicable for peer.  | [optional] 
**remote_as** | **int** | This is a deprecated property, Please use &#x27;remote_as_num&#x27; instead. | [optional] 
**filter_out_ipprefixlist_id** | **str** | This is a deprecated property, Please use &#x27;address_family&#x27; instead. | [optional] 
**hold_down_timer** | **int** | Wait period (seconds) before declaring peer dead | [optional] [default to 180]
**source_addresses** | **list[str]** | BGP neighborship will be formed from all these source addresses to this neighbour. | [optional] 
**maximum_hop_limit** | **int** | This value is set on TTL(time to live) of BGP header. When router receives the BGP packet, it decrements the TTL. The default value of TTL is one when BPG request is initiated.So in the case of a BGP peer multiple hops away and and value of TTL is one, then  next router in the path will decrement the TTL to 0, realize it cant forward the packet and will drop it. If the hop count value to reach neighbor is equal to or less than the maximum_hop_limit value then intermediate router decrements the TTL count by one and forwards the request to BGP neighour. If the hop count value is greater than the maximum_hop_limit value then intermediate router discards the request when TTL becomes 0.  | [optional] [default to 1]
**enabled** | **bool** | Flag to enable this BGP Neighbor | [optional] [default to True]
**remote_as_num** | **str** | 4 Byte ASN of the neighbor in ASPLAIN/ASDOT Format | [optional] 
**address_families** | [**list[BgpNeighborAddressFamily]**](BgpNeighborAddressFamily.md) | User can enable the neighbor for the specific address families and also define filters per address family. When the neighbor is created, it is default enabled for IPV4_UNICAST address family for backward compatibility reasons. User can change that if required, by defining the address family configuration.  | [optional] 
**bfd_config** | [**BfdConfigParameters**](BfdConfigParameters.md) |  | [optional] 
**logical_router_id** | **str** | Logical router id | [optional] 
**filter_in_ipprefixlist_id** | **str** | This is a deprecated property, Please  use &#x27;address_family&#x27; instead. | [optional] 
**filter_out_routemap_id** | **str** | This is a deprecated property, Please use &#x27;address_family&#x27; instead. | [optional] 
**filter_in_routemap_id** | **str** | This is a deprecated property, Please use &#x27;address_family&#x27; instead. | [optional] 
**keep_alive_timer** | **int** | Frequency (seconds) with which keep alive messages are sent to peers | [optional] [default to 60]
**password** | **str** | User can create (POST) the neighbor with or without the password. The view (GET) on the neighbor, would never reveal if the password is set or not. The password can be set later using edit neighbor workFlow (PUT) On the edit neighbor (PUT), if the user does not specify the password property, the older value is retained. Maximum length of this field is 20 characters.  | [optional] 
**source_address** | **str** | Deprecated - do not provide a value for this field. Use source_addresses instead. | [optional] 
**allow_as_in** | **bool** | Flag to enable allowas_in option for BGP neighbor | [optional] [default to False]
**enable_bfd** | **bool** | Flag to enable BFD for this BGP Neighbor. Enable this if the neighbor supports BFD as this will lead to faster convergence. | [optional] [default to False]
**neighbor_address** | **str** | Neighbor IP Address | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

