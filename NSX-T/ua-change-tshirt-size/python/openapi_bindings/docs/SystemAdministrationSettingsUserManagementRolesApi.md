# swagger_client.SystemAdministrationSettingsUserManagementRolesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_role_clone**](SystemAdministrationSettingsUserManagementRolesApi.md#clone_role_clone) | **POST** /aaa/roles/{role}?action&#x3D;clone | Clone an already present role
[**create_or_update_role**](SystemAdministrationSettingsUserManagementRolesApi.md#create_or_update_role) | **PUT** /aaa/roles/{role} | Update custom role
[**create_role_binding**](SystemAdministrationSettingsUserManagementRolesApi.md#create_role_binding) | **POST** /aaa/role-bindings | Assign roles to User or Group
[**delete_all_stale_role_bindings_delete_stale_bindings**](SystemAdministrationSettingsUserManagementRolesApi.md#delete_all_stale_role_bindings_delete_stale_bindings) | **POST** /aaa/role-bindings?action&#x3D;delete_stale_bindings | Delete all stale role assignments
[**delete_role**](SystemAdministrationSettingsUserManagementRolesApi.md#delete_role) | **DELETE** /aaa/roles/{role} | Delete custom role
[**delete_role_binding**](SystemAdministrationSettingsUserManagementRolesApi.md#delete_role_binding) | **DELETE** /aaa/role-bindings/{binding-id} | Delete user/group&#x27;s roles assignment
[**get_all_role_bindings**](SystemAdministrationSettingsUserManagementRolesApi.md#get_all_role_bindings) | **GET** /aaa/role-bindings | Get all users and groups with their roles
[**get_all_roles_info**](SystemAdministrationSettingsUserManagementRolesApi.md#get_all_roles_info) | **GET** /aaa/roles | Get information about all roles
[**get_role_binding**](SystemAdministrationSettingsUserManagementRolesApi.md#get_role_binding) | **GET** /aaa/role-bindings/{binding-id} | Get user/group&#x27;s role information
[**get_role_info**](SystemAdministrationSettingsUserManagementRolesApi.md#get_role_info) | **GET** /aaa/roles/{role} | Get role information
[**list_features**](SystemAdministrationSettingsUserManagementRolesApi.md#list_features) | **GET** /aaa/features-with-properties | List feature permissions
[**list_roles_info**](SystemAdministrationSettingsUserManagementRolesApi.md#list_roles_info) | **GET** /aaa/roles-with-feature-permissions | Get information about all roles with features and their permissions
[**update_role_binding**](SystemAdministrationSettingsUserManagementRolesApi.md#update_role_binding) | **PUT** /aaa/role-bindings/{binding-id} | Update User or Group&#x27;s roles
[**validate_and_recommend_permissions_validate**](SystemAdministrationSettingsUserManagementRolesApi.md#validate_and_recommend_permissions_validate) | **POST** /aaa/roles?action&#x3D;validate | Validate a new feature permission set

# **clone_role_clone**
> NewRole clone_role_clone(body, role)

Clone an already present role

The role with id <role> is cloned and the new id, name and description are the ones provided in the request body. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.NewRole() # NewRole | 
role = 'role_example' # str | Role id

try:
    # Clone an already present role
    api_response = api_instance.clone_role_clone(body, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->clone_role_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewRole**](NewRole.md)|  | 
 **role** | **str**| Role id | 

### Return type

[**NewRole**](NewRole.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_role**
> RoleWithFeatures create_or_update_role(body, role)

Update custom role

Creates a new role with id as <role> if there does not exist any role with id <role>, else updates the existing role. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoleWithFeatures() # RoleWithFeatures | 
role = 'role_example' # str | Custom role id

try:
    # Update custom role
    api_response = api_instance.create_or_update_role(body, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->create_or_update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleWithFeatures**](RoleWithFeatures.md)|  | 
 **role** | **str**| Custom role id | 

### Return type

[**RoleWithFeatures**](RoleWithFeatures.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role_binding**
> RoleBinding create_role_binding(body)

Assign roles to User or Group

When assigning a user role, specify the user name with the same case as it appears in vIDM to access the NSX-T user interface. For example, if vIDM has the user name User1@example.com then the name attribute in the API call must be be User1@example.com and cannot be user1@example.com. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoleBinding() # RoleBinding | 

try:
    # Assign roles to User or Group
    api_response = api_instance.create_role_binding(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->create_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleBinding**](RoleBinding.md)|  | 

### Return type

[**RoleBinding**](RoleBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_stale_role_bindings_delete_stale_bindings**
> delete_all_stale_role_bindings_delete_stale_bindings()

Delete all stale role assignments

Delete all stale role assignments

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))

try:
    # Delete all stale role assignments
    api_instance.delete_all_stale_role_bindings_delete_stale_bindings()
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->delete_all_stale_role_bindings_delete_stale_bindings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(role)

Delete custom role

If a role is assigned to a role binding then the deletion of the role is not allowed. Precanned roles cannot be deleted. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))
role = 'role_example' # str | Custom role id

try:
    # Delete custom role
    api_instance.delete_role(role)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Custom role id | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_binding**
> delete_role_binding(binding_id)

Delete user/group's roles assignment

Delete user/group's roles assignment

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))
binding_id = 'binding_id_example' # str | User/Group's id

try:
    # Delete user/group's roles assignment
    api_instance.delete_role_binding(binding_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->delete_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binding_id** | **str**| User/Group&#x27;s id | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_role_bindings**
> RoleBindingListResult get_all_role_bindings(cursor=cursor, identity_source_id=identity_source_id, identity_source_type=identity_source_type, included_fields=included_fields, name=name, page_size=page_size, role=role, sort_ascending=sort_ascending, sort_by=sort_by, type=type)

Get all users and groups with their roles

Get all users and groups with their roles

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
identity_source_id = 'identity_source_id_example' # str | Identity source ID (optional)
identity_source_type = 'identity_source_type_example' # str | Identity source type (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
name = 'name_example' # str | User/Group name (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
role = 'role_example' # str | Role ID (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
type = 'type_example' # str | Type (optional)

try:
    # Get all users and groups with their roles
    api_response = api_instance.get_all_role_bindings(cursor=cursor, identity_source_id=identity_source_id, identity_source_type=identity_source_type, included_fields=included_fields, name=name, page_size=page_size, role=role, sort_ascending=sort_ascending, sort_by=sort_by, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->get_all_role_bindings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **identity_source_id** | **str**| Identity source ID | [optional] 
 **identity_source_type** | **str**| Identity source type | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **name** | **str**| User/Group name | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **role** | **str**| Role ID | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **type** | **str**| Type | [optional] 

### Return type

[**RoleBindingListResult**](RoleBindingListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles_info**
> RoleListResult get_all_roles_info()

Get information about all roles

Get information about all roles

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))

try:
    # Get information about all roles
    api_response = api_instance.get_all_roles_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->get_all_roles_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RoleListResult**](RoleListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_binding**
> RoleBinding get_role_binding(binding_id)

Get user/group's role information

Get user/group's role information

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))
binding_id = 'binding_id_example' # str | User/Group's id

try:
    # Get user/group's role information
    api_response = api_instance.get_role_binding(binding_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->get_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **binding_id** | **str**| User/Group&#x27;s id | 

### Return type

[**RoleBinding**](RoleBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_info**
> RoleWithFeatures get_role_info(role)

Get role information

Get role information

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))
role = 'role_example' # str | Role id

try:
    # Get role information
    api_response = api_instance.get_role_info(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->get_role_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| Role id | 

### Return type

[**RoleWithFeatures**](RoleWithFeatures.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_features**
> FeaturePermissionListResult list_features()

List feature permissions

List features 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))

try:
    # List feature permissions
    api_response = api_instance.list_features()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->list_features: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FeaturePermissionListResult**](FeaturePermissionListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles_info**
> RoleWithFeaturesListResult list_roles_info(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get information about all roles with features and their permissions

Get information about all roles with features and their permissions

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get information about all roles with features and their permissions
    api_response = api_instance.list_roles_info(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->list_roles_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**RoleWithFeaturesListResult**](RoleWithFeaturesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_binding**
> RoleBinding update_role_binding(body, binding_id)

Update User or Group's roles

Update User or Group's roles

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoleBinding() # RoleBinding | 
binding_id = 'binding_id_example' # str | User/Group's id

try:
    # Update User or Group's roles
    api_response = api_instance.update_role_binding(body, binding_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->update_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleBinding**](RoleBinding.md)|  | 
 **binding_id** | **str**| User/Group&#x27;s id | 

### Return type

[**RoleBinding**](RoleBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_and_recommend_permissions_validate**
> RecommendedFeaturePermissionListResult validate_and_recommend_permissions_validate(body)

Validate a new feature permission set

Validate the permissions of an incoming role. Also, recommend the permissions which need to be corrected. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementRolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.FeaturePermissionArray() # FeaturePermissionArray | 

try:
    # Validate a new feature permission set
    api_response = api_instance.validate_and_recommend_permissions_validate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementRolesApi->validate_and_recommend_permissions_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeaturePermissionArray**](FeaturePermissionArray.md)|  | 

### Return type

[**RecommendedFeaturePermissionListResult**](RecommendedFeaturePermissionListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

