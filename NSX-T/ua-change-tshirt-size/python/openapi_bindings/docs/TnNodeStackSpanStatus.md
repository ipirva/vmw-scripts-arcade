# TnNodeStackSpanStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tn_node_name** | **str** | For L3PortMirrorSession configured mirror stack, show the TN node friendly name which spaned in L3PortMirrorSession.  | 
**vmknic_status** | **str** | Show the vmknic health status, if the vmknic has been bouned to mirror stack, it will show SUCCESS or it will show FAILED.  | 
**dedicated_stack_status** | **str** | Show the dedicated mirror stack health status, if the TN node has the mirror stack, it will show SUCCESS or it will show FAILED.  | 
**tn_node_id** | **str** | For L3PortMirrorSession configured mirror stack, show the TN node UUID which spaned in L3PortMirrorSession.  | [optional] 
**detail** | **str** | Give the detail info for mirror stack and vmknic health status. If the stack or vmknic is FAILED, detail info will tell user reason why the stauts is FAILED. So that user can correct their configuration.  | 
**last_updated_time** | **int** | TN miror stack status will be updated periodically, this item indicates the lastest timestamp of TN node stack status is updated.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

