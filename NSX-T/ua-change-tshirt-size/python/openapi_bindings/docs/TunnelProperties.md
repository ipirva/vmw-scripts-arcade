# TunnelProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of tunnel | [optional] 
**egress_interface** | **str** | Corresponds to the interface where local_ip_address is routed. | [optional] 
**remote_node_id** | **str** | UUID of the remote transport node | [optional] 
**bfd** | [**BFDProperties**](BFDProperties.md) |  | [optional] 
**local_ip** | **str** | Local IP address of tunnel | [optional] 
**last_updated_time** | **int** | Time at which the Tunnel status has been fetched last time. | [optional] 
**name** | **str** | Name of tunnel | [optional] 
**remote_node_display_name** | **str** | Represents the display name of the remote transport node at the other end of the tunnel. | [optional] 
**encap** | **str** | Tunnel encap | [optional] 
**latency_type** | **str** | Latency type. | [optional] 
**latency_value** | **int** | The latency value is set only when latency_type is VALID. | [optional] 
**remote_ip** | **str** | Remote IP address of tunnel | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

