# ServiceAttachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logical_routers** | [**list[ResourceReference]**](ResourceReference.md) | List of LogicalRouters to be connected to the ServicePlane logical switch via a ServiceLink. | [optional] 
**logical_switch** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**local_ips** | [**list[IPInfo]**](IPInfo.md) | Local IPs associated with this Service Attachment. | [optional] 
**service_port** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**deployed_to** | [**ResourceReference**](ResourceReference.md) |  | 
**attachment_status** | **str** | UP - A Service Attachment will have its Service Port - UP and with a configured IP address. DOWN - An Inactive ServiceAttachment has its Service Port - DOWN. It can be used to connect set of appliances that do not need to exchange traffic to/from/through the Edge node. | [optional] [default to 'UP']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

