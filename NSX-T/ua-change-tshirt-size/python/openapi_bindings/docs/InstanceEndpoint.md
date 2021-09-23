# InstanceEndpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_attachments** | [**list[ResourceReference]**](ResourceReference.md) | Id(s) of the Service Attachment where this enndpoint is connected to. Service Attachment is mandatory for LOGICAL Instance Endpoint. | [optional] 
**target_ips** | [**list[IPInfo]**](IPInfo.md) | Target IPs on an interface of the Service Instance. | 
**endpoint_type** | **str** | LOGICAL - It must be created with a ServiceAttachment and identifies a destination connected to the Service Port of the ServiceAttachment, through the ServiceAttachment&#x27;s Logical Switch. VIRTUAL - It represents a L3 destination the router can route to but does not provide any further information about its location in the network. Virtual InstanceEndpoints are used for redirection targets that are not connected to Service Ports, such as the next-hop routers on the Edge uplinks. | [optional] [default to 'LOGICAL']
**service_instance_id** | **str** | The Service instancee with which the instance endpoint is associated. | [optional] 
**link_ids** | [**list[ResourceReference]**](ResourceReference.md) | Link Ids are mandatory for VIRTUAL Instance Endpoint. Even though VIRTUAL, the Instance Endpoint should be connected/accessible through an NSX object. The link id is this NSX object id. Example - For North-South Service Insertion, this is the LogicalRouter Id through which the targetIp/L3 destination accessible. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

