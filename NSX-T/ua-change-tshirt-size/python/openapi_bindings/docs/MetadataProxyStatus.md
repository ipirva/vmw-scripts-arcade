# MetadataProxyStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxy_status** | **str** | UP means the metadata proxy is working fine on both transport-nodes(if have); DOWN means the metadata proxy is is down on both transport-nodes(if have), hence the metadata proxy will not repsonse any metadata request; Error means error happens on transport-node(s) or no status is reported from transport-node(s). The metadata proxy may be working (or not working); NO_BACK means metadata proxy is working in one of the transport node while not in the other transport-node (if have). Hence if the metadata proxy in the working transport-node goes down, the metadata proxy will go down.  | 
**error_message** | **str** | Error message, if available | [optional] 
**transport_nodes** | **list[str]** | Order of the transport nodes is insensitive because Metadata Proxy is running in Active-Active mode among target transport nodes.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

