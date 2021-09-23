# NodeUserProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | User login name (must be \&quot;root\&quot; if userid is 0) | [optional] 
**status** | **str** | Status of the user. This value can be ACTIVE indicating authentication attempts will be successful if the correct credentials are specified. The value can also be PASSWORD_EXPIRED indicating authentication attempts will fail because the user&#x27;s password has expired and must be changed. Or, this value can be NOT_ACTIVATED indicating the user&#x27;s password has not yet been set and must be set before the user can authenticate. | [optional] 
**last_password_change** | **int** | Number of days since password was last changed | [optional] 
**full_name** | **str** | Full name for the user | [optional] 
**password_change_frequency** | **int** | Number of days password is valid before it must be changed. This can be set to 0 to indicate no password change is required or a positive integer up to 9999. By default local user passwords must be changed every 90 days. | [optional] 
**password** | **str** | Password for the user (optionally specified on PUT, unspecified on GET) | [optional] 
**userid** | **int** | Numeric id for the user | [optional] 
**old_password** | **str** | Old password for the user (required on PUT if password specified) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

