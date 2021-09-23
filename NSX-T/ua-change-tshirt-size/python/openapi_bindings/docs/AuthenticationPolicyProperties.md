# AuthenticationPolicyProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_failed_auth_reset_period** | **int** | In order to trigger an account lockout, all authentication failures must occur in this time window. If the reset period expires, the failed login count is reset to zero. Only applies to NSX Manager nodes. Ignored on other node types. | [optional] [default to 900]
**minimum_password_length** | **int** | Minimum number of characters required in account passwords | [optional] [default to 8]
**cli_failed_auth_lockout_period** | **int** | Once a lockout occurs, the account remains locked out of the CLI for this time period. While the lockout period is in effect, additional authentication attempts restart the lockout period, even if a valid password is specified. | [optional] [default to 900]
**api_max_auth_failures** | **int** | Only applies to NSX Manager nodes. Ignored on other node types. | [optional] [default to 5]
**api_failed_auth_lockout_period** | **int** | Once a lockout occurs, the account remains locked out of the API for this time period. Only applies to NSX Manager nodes. Ignored on other node types. | [optional] [default to 900]
**cli_max_auth_failures** | **int** | Number of authentication failures that trigger CLI lockout | [optional] [default to 5]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

