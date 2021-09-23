# swagger_client.SystemAdministrationConfigurationDirectoryServiceGroupsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_directory_group_member_groups**](SystemAdministrationConfigurationDirectoryServiceGroupsApi.md#list_directory_group_member_groups) | **GET** /directory/domains/{domain-id}/groups/{group-id}/member-groups | List members of a directory group
[**search_directory_groups**](SystemAdministrationConfigurationDirectoryServiceGroupsApi.md#search_directory_groups) | **GET** /directory/domains/{domain-id}/groups | Search for directory groups within a domain based on the substring of a distinguished name. (e.g. CN&#x3D;User,DC&#x3D;acme,DC&#x3D;com) The search filter pattern can optionally support multiple (up to 100 maximum) search pattern separated by &#x27;|&#x27; (url encoded %7C). In this case, the search results will be returned as the union of all matching criteria. (e.g. CN&#x3D;Ann,CN&#x3D;Users,DC&#x3D;acme,DC&#x3D;com|CN&#x3D;Bob,CN&#x3D;Users,DC&#x3D;acme,DC&#x3D;com)

# **list_directory_group_member_groups**
> DirectoryGroupMemberListResults list_directory_group_member_groups(domain_id, group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List members of a directory group

A member group could be either direct member of the group specified by group_id or nested member of it. Both direct member groups and nested member groups are returned.

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceGroupsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
group_id = 'group_id_example' # str | Directory group identifier
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List members of a directory group
    api_response = api_instance.list_directory_group_member_groups(domain_id, group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceGroupsApi->list_directory_group_member_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **group_id** | **str**| Directory group identifier | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**DirectoryGroupMemberListResults**](DirectoryGroupMemberListResults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_directory_groups**
> DirectoryGroupListResults search_directory_groups(domain_id, filter_value, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Search for directory groups within a domain based on the substring of a distinguished name. (e.g. CN=User,DC=acme,DC=com) The search filter pattern can optionally support multiple (up to 100 maximum) search pattern separated by '|' (url encoded %7C). In this case, the search results will be returned as the union of all matching criteria. (e.g. CN=Ann,CN=Users,DC=acme,DC=com|CN=Bob,CN=Users,DC=acme,DC=com)

Search for directory groups within a domain based on the substring of a distinguished name. (e.g. CN=User,DC=acme,DC=com) The search filter pattern can optionally support multiple (up to 100 maximum) search pattern separated by '|' (url encoded %7C). In this case, the search results will be returned as the union of all matching criteria. (e.g. CN=Ann,CN=Users,DC=acme,DC=com|CN=Bob,CN=Users,DC=acme,DC=com)

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceGroupsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
filter_value = 'filter_value_example' # str | Name search filter value
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Search for directory groups within a domain based on the substring of a distinguished name. (e.g. CN=User,DC=acme,DC=com) The search filter pattern can optionally support multiple (up to 100 maximum) search pattern separated by '|' (url encoded %7C). In this case, the search results will be returned as the union of all matching criteria. (e.g. CN=Ann,CN=Users,DC=acme,DC=com|CN=Bob,CN=Users,DC=acme,DC=com)
    api_response = api_instance.search_directory_groups(domain_id, filter_value, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceGroupsApi->search_directory_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **filter_value** | **str**| Name search filter value | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**DirectoryGroupListResults**](DirectoryGroupListResults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

