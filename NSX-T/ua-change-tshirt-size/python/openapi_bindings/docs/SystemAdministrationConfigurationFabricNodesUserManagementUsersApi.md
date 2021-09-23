# swagger_client.SystemAdministrationConfigurationFabricNodesUserManagementUsersApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_node_user_ssh_key_add_ssh_key**](SystemAdministrationConfigurationFabricNodesUserManagementUsersApi.md#add_node_user_ssh_key_add_ssh_key) | **POST** /node/users/{userid}/ssh-keys?action&#x3D;add_ssh_key | Add SSH public key to authorized_keys file for node user
[**delete_node_user_ssh_key_remove_ssh_key**](SystemAdministrationConfigurationFabricNodesUserManagementUsersApi.md#delete_node_user_ssh_key_remove_ssh_key) | **POST** /node/users/{userid}/ssh-keys?action&#x3D;remove_ssh_key | Remove SSH public key from authorized_keys file for node user
[**list_node_user_ssh_keys**](SystemAdministrationConfigurationFabricNodesUserManagementUsersApi.md#list_node_user_ssh_keys) | **GET** /node/users/{userid}/ssh-keys | List SSH keys from authorized_keys file for node user
[**list_node_users**](SystemAdministrationConfigurationFabricNodesUserManagementUsersApi.md#list_node_users) | **GET** /node/users | List node users
[**read_node_user**](SystemAdministrationConfigurationFabricNodesUserManagementUsersApi.md#read_node_user) | **GET** /node/users/{userid} | Read node user
[**reset_node_user_own_password_reset_own_password**](SystemAdministrationConfigurationFabricNodesUserManagementUsersApi.md#reset_node_user_own_password_reset_own_password) | **POST** /node/users?action&#x3D;reset_own_password | Reset a user&#x27;s own password. Requires current password
[**reset_node_user_password_reset_password**](SystemAdministrationConfigurationFabricNodesUserManagementUsersApi.md#reset_node_user_password_reset_password) | **POST** /node/users/{userid}?action&#x3D;reset_password | Reset a user&#x27;s password without requiring their current password
[**update_node_user**](SystemAdministrationConfigurationFabricNodesUserManagementUsersApi.md#update_node_user) | **PUT** /node/users/{userid} | Update node user

# **add_node_user_ssh_key_add_ssh_key**
> add_node_user_ssh_key_add_ssh_key(body, userid)

Add SSH public key to authorized_keys file for node user

Add SSH public key to authorized_keys file for node user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesUserManagementUsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.SshKeyProperties() # SshKeyProperties | 
userid = 'userid_example' # str | User id of the user

try:
    # Add SSH public key to authorized_keys file for node user
    api_instance.add_node_user_ssh_key_add_ssh_key(body, userid)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesUserManagementUsersApi->add_node_user_ssh_key_add_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SshKeyProperties**](SshKeyProperties.md)|  | 
 **userid** | **str**| User id of the user | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_user_ssh_key_remove_ssh_key**
> delete_node_user_ssh_key_remove_ssh_key(body, userid)

Remove SSH public key from authorized_keys file for node user

Remove SSH public key from authorized_keys file for node user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesUserManagementUsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.SshKeyBaseProperties() # SshKeyBaseProperties | 
userid = 'userid_example' # str | User id of the user

try:
    # Remove SSH public key from authorized_keys file for node user
    api_instance.delete_node_user_ssh_key_remove_ssh_key(body, userid)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesUserManagementUsersApi->delete_node_user_ssh_key_remove_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SshKeyBaseProperties**](SshKeyBaseProperties.md)|  | 
 **userid** | **str**| User id of the user | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_user_ssh_keys**
> SshKeyPropertiesListResult list_node_user_ssh_keys(userid)

List SSH keys from authorized_keys file for node user

Returns a list of all SSH keys from authorized_keys file for node user 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesUserManagementUsersApi(swagger_client.ApiClient(configuration))
userid = 'userid_example' # str | User id of the user

try:
    # List SSH keys from authorized_keys file for node user
    api_response = api_instance.list_node_user_ssh_keys(userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesUserManagementUsersApi->list_node_user_ssh_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User id of the user | 

### Return type

[**SshKeyPropertiesListResult**](SshKeyPropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_users**
> NodeUserPropertiesListResult list_node_users()

List node users

Returns the list of users configued to log in to the NSX appliance. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesUserManagementUsersApi(swagger_client.ApiClient(configuration))

try:
    # List node users
    api_response = api_instance.list_node_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesUserManagementUsersApi->list_node_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeUserPropertiesListResult**](NodeUserPropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_user**
> NodeUserProperties read_node_user(userid)

Read node user

Returns information about a specified user who is configued to log in to the NSX appliance. The valid user IDs are: 0, 10000, 10002. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesUserManagementUsersApi(swagger_client.ApiClient(configuration))
userid = 'userid_example' # str | User id of the user

try:
    # Read node user
    api_response = api_instance.read_node_user(userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesUserManagementUsersApi->read_node_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User id of the user | 

### Return type

[**NodeUserProperties**](NodeUserProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_node_user_own_password_reset_own_password**
> reset_node_user_own_password_reset_own_password(body)

Reset a user's own password. Requires current password

Enables a user to reset their own password. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesUserManagementUsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeUserPasswordProperty() # NodeUserPasswordProperty | 

try:
    # Reset a user's own password. Requires current password
    api_instance.reset_node_user_own_password_reset_own_password(body)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesUserManagementUsersApi->reset_node_user_own_password_reset_own_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeUserPasswordProperty**](NodeUserPasswordProperty.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_node_user_password_reset_password**
> reset_node_user_password_reset_password(body, userid)

Reset a user's password without requiring their current password

Unlike the PUT version of this call (PUT /node/users/<userid>), this API does not require that the current password for the user be provided. The account of the target user must be \"ACTIVE\" for the call to succeed. This API only supports user ID 10002. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesUserManagementUsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeUserPasswordProperty() # NodeUserPasswordProperty | 
userid = 'userid_example' # str | User id of the user

try:
    # Reset a user's password without requiring their current password
    api_instance.reset_node_user_password_reset_password(body, userid)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesUserManagementUsersApi->reset_node_user_password_reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeUserPasswordProperty**](NodeUserPasswordProperty.md)|  | 
 **userid** | **str**| User id of the user | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_user**
> NodeUserProperties update_node_user(body, userid)

Update node user

Updates attributes of an existing NSX appliance user. This method cannot be used to add a new user. Modifiable attributes include the username, full name of the user, and password. If you specify a password in a PUT request, it is not returned in the response. Nor is it returned in a GET request. The specified password does not meet the following complexity requirements: - minimum 12 characters in length - minimum 1 uppercase character - minimum 1 lowercase character - minimum 1 numeric character - minimum 1 special character - minimum 5 unique characters - default password complexity rules as enforced by the Linux PAM module The valid user IDs are: 0, 10000, 10002. Note that invoking this API does not update any user-related properties of existing objects in the system and does not modify the username field in existing audit log entries. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesUserManagementUsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeUserProperties() # NodeUserProperties | 
userid = 'userid_example' # str | User id of the user

try:
    # Update node user
    api_response = api_instance.update_node_user(body, userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesUserManagementUsersApi->update_node_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeUserProperties**](NodeUserProperties.md)|  | 
 **userid** | **str**| User id of the user | 

### Return type

[**NodeUserProperties**](NodeUserProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

