# TraceflowObservationRelayedLogical

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | **str** | This field specified the message type of the relay service REQUEST - The relay service will relay a request message to the destination server REPLY - The relay service will relay a reply message to the client | [optional] [default to 'REQUEST']
**dst_server_address** | **str** | This field specified the IP address of the destination which the packet will be relayed. | [optional] 
**logical_comp_uuid** | **str** | This field specified the logical component that relay service located. | [optional] 
**relay_server_address** | **str** | This field specified the IP address of the relay service. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

