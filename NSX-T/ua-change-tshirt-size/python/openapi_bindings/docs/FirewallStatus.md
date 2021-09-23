# FirewallStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_status** | **str** | Firewall status for a fabric entity or in global context where firewall is supported. | 
**context** | **str** | Types of firewall contexts. | 
**target_statuses** | [**list[TargetResourceStatus]**](TargetResourceStatus.md) | List of firewall status on various target logical resources. This will override the global status of corresponding firewall context (e.g it will override the gloabal status of logical_routers). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

