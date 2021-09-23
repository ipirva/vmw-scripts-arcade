# ComputeManagerStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Version of the compute manager | [optional] 
**connection_status** | **str** | Status of connection with the compute manager | [optional] 
**connection_errors** | [**list[ErrorInfo]**](ErrorInfo.md) | Errors when connecting with compute manager | [optional] 
**oidc_end_point_id** | **str** | If Compute manager is trusted as authorization server, then this Id will be Id of corresponding oidc end point.  | [optional] 
**last_sync_time** | **int** | Timestamp of the last successful update of Inventory, in epoch milliseconds. | [optional] 
**connection_status_details** | **str** | Details about connection status | [optional] 
**registration_errors** | [**list[ErrorInfo]**](ErrorInfo.md) | Errors when registering with compute manager | [optional] 
**registration_status** | **str** | Registration status of compute manager | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

