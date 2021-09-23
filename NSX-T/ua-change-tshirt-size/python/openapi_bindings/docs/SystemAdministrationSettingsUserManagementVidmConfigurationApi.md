# swagger_client.SystemAdministrationSettingsUserManagementVidmConfigurationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_group_vidm_search_result**](SystemAdministrationSettingsUserManagementVidmConfigurationApi.md#get_group_vidm_search_result) | **GET** /aaa/vidm/groups | Get all the User Groups where vIDM display name matches the search key case insensitively. The search key is checked to be a substring of display name. This is a non paginated API.
[**get_user_vidm_search_result**](SystemAdministrationSettingsUserManagementVidmConfigurationApi.md#get_user_vidm_search_result) | **GET** /aaa/vidm/users | Get all the users from vIDM whose userName, givenName or familyName matches the search key case insensitively. The search key is checked to be a substring of name or given name or family name. This is a non paginated API.
[**get_vidm_search_result**](SystemAdministrationSettingsUserManagementVidmConfigurationApi.md#get_vidm_search_result) | **POST** /aaa/vidm/search | Get all the users and groups from vIDM matching the search key case insensitively. The search key is checked to be a substring of name or given name or family name of user and display name of group. This is a non paginated API.
[**read_auth_provider_vidm**](SystemAdministrationSettingsUserManagementVidmConfigurationApi.md#read_auth_provider_vidm) | **GET** /node/aaa/providers/vidm | Read AAA provider vIDM properties
[**read_auth_provider_vidm_status**](SystemAdministrationSettingsUserManagementVidmConfigurationApi.md#read_auth_provider_vidm_status) | **GET** /node/aaa/providers/vidm/status | Read AAA provider vIDM status
[**update_auth_provider_vidm**](SystemAdministrationSettingsUserManagementVidmConfigurationApi.md#update_auth_provider_vidm) | **PUT** /node/aaa/providers/vidm | Update AAA provider vIDM properties

# **get_group_vidm_search_result**
> VidmInfoListResult get_group_vidm_search_result(search_string, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get all the User Groups where vIDM display name matches the search key case insensitively. The search key is checked to be a substring of display name. This is a non paginated API.

Get all the User Groups where vIDM display name matches the search key case insensitively. The search key is checked to be a substring of display name. This is a non paginated API.

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementVidmConfigurationApi(swagger_client.ApiClient(configuration))
search_string = 'search_string_example' # str | Search string to search for. 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get all the User Groups where vIDM display name matches the search key case insensitively. The search key is checked to be a substring of display name. This is a non paginated API.
    api_response = api_instance.get_group_vidm_search_result(search_string, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementVidmConfigurationApi->get_group_vidm_search_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| Search string to search for.  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**VidmInfoListResult**](VidmInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_vidm_search_result**
> VidmInfoListResult get_user_vidm_search_result(search_string, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get all the users from vIDM whose userName, givenName or familyName matches the search key case insensitively. The search key is checked to be a substring of name or given name or family name. This is a non paginated API.

Get all the users from vIDM whose userName, givenName or familyName matches the search key case insensitively. The search key is checked to be a substring of name or given name or family name. This is a non paginated API.

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementVidmConfigurationApi(swagger_client.ApiClient(configuration))
search_string = 'search_string_example' # str | Search string to search for. 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get all the users from vIDM whose userName, givenName or familyName matches the search key case insensitively. The search key is checked to be a substring of name or given name or family name. This is a non paginated API.
    api_response = api_instance.get_user_vidm_search_result(search_string, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementVidmConfigurationApi->get_user_vidm_search_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| Search string to search for.  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**VidmInfoListResult**](VidmInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vidm_search_result**
> VidmInfoListResult get_vidm_search_result(search_string, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get all the users and groups from vIDM matching the search key case insensitively. The search key is checked to be a substring of name or given name or family name of user and display name of group. This is a non paginated API.

Get all the users and groups from vIDM matching the search key case insensitively. The search key is checked to be a substring of name or given name or family name of user and display name of group. This is a non paginated API.

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementVidmConfigurationApi(swagger_client.ApiClient(configuration))
search_string = 'search_string_example' # str | Search string to search for. 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get all the users and groups from vIDM matching the search key case insensitively. The search key is checked to be a substring of name or given name or family name of user and display name of group. This is a non paginated API.
    api_response = api_instance.get_vidm_search_result(search_string, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementVidmConfigurationApi->get_vidm_search_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| Search string to search for.  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**VidmInfoListResult**](VidmInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_auth_provider_vidm**
> NodeAuthProviderVidmProperties read_auth_provider_vidm()

Read AAA provider vIDM properties

Read AAA provider vIDM properties

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementVidmConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Read AAA provider vIDM properties
    api_response = api_instance.read_auth_provider_vidm()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementVidmConfigurationApi->read_auth_provider_vidm: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeAuthProviderVidmProperties**](NodeAuthProviderVidmProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_auth_provider_vidm_status**
> NodeAuthProviderVidmStatus read_auth_provider_vidm_status()

Read AAA provider vIDM status

Read AAA provider vIDM status

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementVidmConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Read AAA provider vIDM status
    api_response = api_instance.read_auth_provider_vidm_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementVidmConfigurationApi->read_auth_provider_vidm_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeAuthProviderVidmStatus**](NodeAuthProviderVidmStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auth_provider_vidm**
> NodeAuthProviderVidmProperties update_auth_provider_vidm(body)

Update AAA provider vIDM properties

Update AAA provider vIDM properties

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementVidmConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeAuthProviderVidmProperties() # NodeAuthProviderVidmProperties | 

try:
    # Update AAA provider vIDM properties
    api_response = api_instance.update_auth_provider_vidm(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementVidmConfigurationApi->update_auth_provider_vidm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeAuthProviderVidmProperties**](NodeAuthProviderVidmProperties.md)|  | 

### Return type

[**NodeAuthProviderVidmProperties**](NodeAuthProviderVidmProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

