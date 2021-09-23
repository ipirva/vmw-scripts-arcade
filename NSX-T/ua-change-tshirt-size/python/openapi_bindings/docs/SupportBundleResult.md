# SupportBundleResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_properties** | [**SupportBundleRequest**](SupportBundleRequest.md) |  | [optional] 
**failed_nodes** | [**list[FailedNodeSupportBundleResult]**](FailedNodeSupportBundleResult.md) | Nodes where bundles were not generated or not copied to remote server | [optional] 
**success_nodes** | [**list[SuccessNodeSupportBundleResult]**](SuccessNodeSupportBundleResult.md) | Nodes whose bundles were successfully copied to remote file server | [optional] 
**remaining_nodes** | [**list[RemainingSupportBundleNode]**](RemainingSupportBundleNode.md) | Nodes where bundle generation is pending or in progress | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

