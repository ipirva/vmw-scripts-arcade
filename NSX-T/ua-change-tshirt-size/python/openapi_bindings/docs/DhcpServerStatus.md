# DhcpServerStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Error message, if available | [optional] 
**service_status** | **str** | UP means the dhcp service is working fine on both active transport-node and stand-by transport-node (if have), hence fail-over can work at this time if there is failure happens on one of the transport-node; DOWN means the dhcp service is down on both active transport-node and stand-by node (if have), hence the dhcp-service will not repsonse any dhcp request; Error means error happens on transport-node(s) or no status is reported from transport-node(s). The dhcp service may be working (or not working); NO_STANDBY means dhcp service is working in one of the transport node while not in the other transport-node (if have). Hence if the dhcp service in the working transport-node is down, fail-over will not happen and the dhcp service will go down.  | 
**stand_by_node** | **str** | uuid of stand_by transport node. null if non-HA mode | [optional] 
**active_node** | **str** | uuid of active transport node | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

