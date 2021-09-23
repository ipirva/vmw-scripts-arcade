# swagger_client.SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transport_zone_profile**](SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi.md#create_transport_zone_profile) | **POST** /transportzone-profiles | Create a transport zone Profile
[**delete_transport_zone_profile**](SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi.md#delete_transport_zone_profile) | **DELETE** /transportzone-profiles/{transportzone-profile-id} | Delete a transport zone Profile
[**get_transport_zone_profile**](SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi.md#get_transport_zone_profile) | **GET** /transportzone-profiles/{transportzone-profile-id} | Get transport zone profile by identifier
[**list_transport_zone_profiles**](SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi.md#list_transport_zone_profiles) | **GET** /transportzone-profiles | List transport zone profiles
[**update_transport_zone_profile**](SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi.md#update_transport_zone_profile) | **PUT** /transportzone-profiles/{transportzone-profile-id} | Update a transport zone profile

# **create_transport_zone_profile**
> TransportZoneProfile create_transport_zone_profile(body)

Create a transport zone Profile

Creates a transport zone profile. The resource_type is required. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportZoneProfile() # TransportZoneProfile | 

try:
    # Create a transport zone Profile
    api_response = api_instance.create_transport_zone_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi->create_transport_zone_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportZoneProfile**](TransportZoneProfile.md)|  | 

### Return type

[**TransportZoneProfile**](TransportZoneProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transport_zone_profile**
> delete_transport_zone_profile(transportzone_profile_id)

Delete a transport zone Profile

Deletes a specified transport zone profile.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi(swagger_client.ApiClient(configuration))
transportzone_profile_id = 'transportzone_profile_id_example' # str | 

try:
    # Delete a transport zone Profile
    api_instance.delete_transport_zone_profile(transportzone_profile_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi->delete_transport_zone_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transportzone_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_zone_profile**
> TransportZoneProfile get_transport_zone_profile(transportzone_profile_id)

Get transport zone profile by identifier

Returns information about a specified transport zone profile.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi(swagger_client.ApiClient(configuration))
transportzone_profile_id = 'transportzone_profile_id_example' # str | 

try:
    # Get transport zone profile by identifier
    api_response = api_instance.get_transport_zone_profile(transportzone_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi->get_transport_zone_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transportzone_profile_id** | **str**|  | 

### Return type

[**TransportZoneProfile**](TransportZoneProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_zone_profiles**
> TransportZoneProfileListResult list_transport_zone_profiles(cursor=cursor, include_system_owned=include_system_owned, included_fields=included_fields, page_size=page_size, resource_type=resource_type, sort_ascending=sort_ascending, sort_by=sort_by)

List transport zone profiles

Returns information about the configured transport zone profiles. Transport zone profiles define networking policies for transport zones and transport zone endpoints. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
include_system_owned = false # bool | Whether the list result contains system resources (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
resource_type = 'resource_type_example' # str | comma-separated list of transport zone profile types, e.g. ?resource_type=BfdHealthMonitoringProfile (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List transport zone profiles
    api_response = api_instance.list_transport_zone_profiles(cursor=cursor, include_system_owned=include_system_owned, included_fields=included_fields, page_size=page_size, resource_type=resource_type, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi->list_transport_zone_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **include_system_owned** | **bool**| Whether the list result contains system resources | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **resource_type** | **str**| comma-separated list of transport zone profile types, e.g. ?resource_type&#x3D;BfdHealthMonitoringProfile | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**TransportZoneProfileListResult**](TransportZoneProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transport_zone_profile**
> TransportZoneProfile update_transport_zone_profile(body, transportzone_profile_id)

Update a transport zone profile

Modifies a specified transport zone profile. The body of the PUT request must include the resource_type. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportZoneProfile() # TransportZoneProfile | 
transportzone_profile_id = 'transportzone_profile_id_example' # str | 

try:
    # Update a transport zone profile
    api_response = api_instance.update_transport_zone_profile(body, transportzone_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesTransportZoneProfilesApi->update_transport_zone_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportZoneProfile**](TransportZoneProfile.md)|  | 
 **transportzone_profile_id** | **str**|  | 

### Return type

[**TransportZoneProfile**](TransportZoneProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

