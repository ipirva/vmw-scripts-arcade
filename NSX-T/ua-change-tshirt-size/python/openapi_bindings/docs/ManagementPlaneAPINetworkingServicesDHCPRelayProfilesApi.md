# swagger_client.ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dhcp_relay_profile**](ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi.md#create_dhcp_relay_profile) | **POST** /dhcp/relay-profiles | Create a DHCP Relay Profile
[**delete_dhcp_relay_profile**](ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi.md#delete_dhcp_relay_profile) | **DELETE** /dhcp/relay-profiles/{relay-profile-id} | Delete a DHCP Relay Profile
[**list_dhcp_relay_profiles**](ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi.md#list_dhcp_relay_profiles) | **GET** /dhcp/relay-profiles | List All DHCP Relay Profiles
[**read_dhcp_relay_profile**](ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi.md#read_dhcp_relay_profile) | **GET** /dhcp/relay-profiles/{relay-profile-id} | Read a DHCP Relay Profile
[**update_dhcp_relay_profile**](ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi.md#update_dhcp_relay_profile) | **PUT** /dhcp/relay-profiles/{relay-profile-id} | Update a DHCP Relay Profile

# **create_dhcp_relay_profile**
> DhcpRelayProfile create_dhcp_relay_profile(body)

Create a DHCP Relay Profile

Creates a dhcp relay profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpRelayProfile() # DhcpRelayProfile | 

try:
    # Create a DHCP Relay Profile
    api_response = api_instance.create_dhcp_relay_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi->create_dhcp_relay_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpRelayProfile**](DhcpRelayProfile.md)|  | 

### Return type

[**DhcpRelayProfile**](DhcpRelayProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dhcp_relay_profile**
> delete_dhcp_relay_profile(relay_profile_id)

Delete a DHCP Relay Profile

Deletes the specified dhcp relay profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi(swagger_client.ApiClient(configuration))
relay_profile_id = 'relay_profile_id_example' # str | 

try:
    # Delete a DHCP Relay Profile
    api_instance.delete_dhcp_relay_profile(relay_profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi->delete_dhcp_relay_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relay_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dhcp_relay_profiles**
> DhcpRelayProfileListResult list_dhcp_relay_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List All DHCP Relay Profiles

Returns information about all dhcp relay profiles. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List All DHCP Relay Profiles
    api_response = api_instance.list_dhcp_relay_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi->list_dhcp_relay_profiles: %s\n" % e)
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

[**DhcpRelayProfileListResult**](DhcpRelayProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_dhcp_relay_profile**
> DhcpRelayProfile read_dhcp_relay_profile(relay_profile_id)

Read a DHCP Relay Profile

Returns information about the specified dhcp relay profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi(swagger_client.ApiClient(configuration))
relay_profile_id = 'relay_profile_id_example' # str | 

try:
    # Read a DHCP Relay Profile
    api_response = api_instance.read_dhcp_relay_profile(relay_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi->read_dhcp_relay_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relay_profile_id** | **str**|  | 

### Return type

[**DhcpRelayProfile**](DhcpRelayProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dhcp_relay_profile**
> DhcpRelayProfile update_dhcp_relay_profile(body, relay_profile_id)

Update a DHCP Relay Profile

Modifies the specified dhcp relay profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpRelayProfile() # DhcpRelayProfile | 
relay_profile_id = 'relay_profile_id_example' # str | 

try:
    # Update a DHCP Relay Profile
    api_response = api_instance.update_dhcp_relay_profile(body, relay_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPRelayProfilesApi->update_dhcp_relay_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpRelayProfile**](DhcpRelayProfile.md)|  | 
 **relay_profile_id** | **str**|  | 

### Return type

[**DhcpRelayProfile**](DhcpRelayProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

