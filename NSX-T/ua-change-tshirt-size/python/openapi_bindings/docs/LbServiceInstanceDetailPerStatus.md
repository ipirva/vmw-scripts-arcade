# LbServiceInstanceDetailPerStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The type of load balancer instance status.  | [optional] 
**instance_number** | **int** | It means the total number of instances in this status type for the given transport node.  | [optional] 
**instance_details** | [**list[LbServiceInstanceDetail]**](LbServiceInstanceDetail.md) | The detailed information of the load balancer instance. This field will be only returned on realtime status API.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

