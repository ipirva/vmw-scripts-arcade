# MirrorStackStatusListResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_status** | **str** | SUCCESS if all the TN&#x27;s stack status are SUCCESS, FAILED if some of the TN&#x27;s stack status are FAILED.  | 
**results** | [**list[TnNodeStackSpanStatus]**](TnNodeStackSpanStatus.md) | List all TN nodes which spaned in remote L3 mirror session mirror stack health status detailed info, including mirror stack status, vmknic status, TN node ID, TN node name and last updated status timestamp.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

