# IdfwUserSessionData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | AD user ID (may not exist). | [optional] 
**user_session_id** | **int** | User session ID.  This also indicates whether this is VDI / RDSH. | 
**vm_ext_id** | **str** | Virtual machine (external ID or BIOS UUID) where login/logout events occurred. | [optional] 
**id** | **str** | Identifier of user session data. | [optional] 
**login_time** | **int** | Login time. | 
**user_name** | **str** | AD user name. | 
**logout_time** | **int** | Logout time if applicable.  An active user session has no logout time. Non-active user session is stored (up to last 5 most recent entries) per VM and per user.  | [optional] 
**domain_name** | **str** | AD Domain of user. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

