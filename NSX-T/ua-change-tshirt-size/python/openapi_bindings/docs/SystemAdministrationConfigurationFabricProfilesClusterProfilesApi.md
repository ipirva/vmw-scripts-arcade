# swagger_client.SystemAdministrationConfigurationFabricProfilesClusterProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_profile**](SystemAdministrationConfigurationFabricProfilesClusterProfilesApi.md#create_cluster_profile) | **POST** /cluster-profiles | Create a Cluster Profile
[**delete_cluster_profile**](SystemAdministrationConfigurationFabricProfilesClusterProfilesApi.md#delete_cluster_profile) | **DELETE** /cluster-profiles/{cluster-profile-id} | Delete a cluster profile
[**get_cluster_profile**](SystemAdministrationConfigurationFabricProfilesClusterProfilesApi.md#get_cluster_profile) | **GET** /cluster-profiles/{cluster-profile-id} | Get cluster profile by Id
[**list_cluster_profiles**](SystemAdministrationConfigurationFabricProfilesClusterProfilesApi.md#list_cluster_profiles) | **GET** /cluster-profiles | List Cluster Profiles
[**update_cluster_profile**](SystemAdministrationConfigurationFabricProfilesClusterProfilesApi.md#update_cluster_profile) | **PUT** /cluster-profiles/{cluster-profile-id} | Update a cluster profile

# **create_cluster_profile**
> ClusterProfile create_cluster_profile(body)

Create a Cluster Profile

Create a cluster profile. The resource_type is required. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesClusterProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClusterProfile() # ClusterProfile | 

try:
    # Create a Cluster Profile
    api_response = api_instance.create_cluster_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesClusterProfilesApi->create_cluster_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterProfile**](ClusterProfile.md)|  | 

### Return type

[**ClusterProfile**](ClusterProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_profile**
> delete_cluster_profile(cluster_profile_id)

Delete a cluster profile

Delete a specified cluster profile.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesClusterProfilesApi(swagger_client.ApiClient(configuration))
cluster_profile_id = 'cluster_profile_id_example' # str | 

try:
    # Delete a cluster profile
    api_instance.delete_cluster_profile(cluster_profile_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesClusterProfilesApi->delete_cluster_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_profile**
> ClusterProfile get_cluster_profile(cluster_profile_id)

Get cluster profile by Id

Returns information about a specified cluster profile.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesClusterProfilesApi(swagger_client.ApiClient(configuration))
cluster_profile_id = 'cluster_profile_id_example' # str | 

try:
    # Get cluster profile by Id
    api_response = api_instance.get_cluster_profile(cluster_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesClusterProfilesApi->get_cluster_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_profile_id** | **str**|  | 

### Return type

[**ClusterProfile**](ClusterProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_profiles**
> ClusterProfileListResult list_cluster_profiles(cursor=cursor, include_system_owned=include_system_owned, included_fields=included_fields, page_size=page_size, resource_type=resource_type, sort_ascending=sort_ascending, sort_by=sort_by)

List Cluster Profiles

Returns paginated list of cluster profiles Cluster profiles define policies for edge cluster and bridge cluster. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesClusterProfilesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
include_system_owned = true # bool | Whether the list result contains system resources (optional) (default to true)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
resource_type = 'resource_type_example' # str | Supported cluster profiles. (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List Cluster Profiles
    api_response = api_instance.list_cluster_profiles(cursor=cursor, include_system_owned=include_system_owned, included_fields=included_fields, page_size=page_size, resource_type=resource_type, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesClusterProfilesApi->list_cluster_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **include_system_owned** | **bool**| Whether the list result contains system resources | [optional] [default to true]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **resource_type** | **str**| Supported cluster profiles. | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ClusterProfileListResult**](ClusterProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_profile**
> ClusterProfile update_cluster_profile(body, cluster_profile_id)

Update a cluster profile

Modifie a specified cluster profile. The body of the PUT request must include the resource_type. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesClusterProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClusterProfile() # ClusterProfile | 
cluster_profile_id = 'cluster_profile_id_example' # str | 

try:
    # Update a cluster profile
    api_response = api_instance.update_cluster_profile(body, cluster_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesClusterProfilesApi->update_cluster_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterProfile**](ClusterProfile.md)|  | 
 **cluster_profile_id** | **str**|  | 

### Return type

[**ClusterProfile**](ClusterProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

