# NodeUserSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cli_username** | **str** | To configure username, you must provide this property together with &lt;b&gt;cli_password&lt;/b&gt;. Username must contain ASCII characters only.  | [optional] [default to 'admin']
**audit_username** | **str** | The default username is \&quot;audit\&quot;. To configure username, you must provide this property together with &lt;b&gt;audit_password&lt;/b&gt;. Username must contain ASCII characters only.  | [optional] 
**root_password** | **str** | Password for the node root user. For deployment, this property is required. After deployment, this property is ignored, and the node cli must be used to change the password. The password specified must be at least 12 characters in length and must contain at least one lowercase, one uppercase, one numeric character and  one special character (except quotes). Passwords based on dictionary words and palindromes are invalid.  | [optional] 
**cli_password** | **str** | Password for the node cli user. For deployment, this property is required. After deployment, this property is ignored, and the node cli must be used to change the password. The password specified must be at least 12 characters in length and must contain at least one lowercase, one uppercase, one numeric character and one special character (except quotes). Passwords based on dictionary words and palindromes are invalid.  | [optional] 
**audit_password** | **str** | Password for the node audit user. For deployment, this property is required. After deployment, this property is ignored, and the node cli must be used to change the password. The password specified must be at least 12 characters in length and must contain at least one lowercase, one uppercase, one numeric character and one special character (except quotes). Passwords based on dictionary words and palindromes are invalid.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

