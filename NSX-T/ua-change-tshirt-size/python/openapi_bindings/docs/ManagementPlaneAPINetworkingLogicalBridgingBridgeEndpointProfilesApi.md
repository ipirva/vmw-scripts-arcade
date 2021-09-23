# swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bridge_endpoint_profile**](ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi.md#create_bridge_endpoint_profile) | **POST** /bridge-endpoint-profiles | Create a Bridge Endpoint Profile
[**delete_bridge_endpoint_profile**](ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi.md#delete_bridge_endpoint_profile) | **DELETE** /bridge-endpoint-profiles/{bridgeendpointprofile-id} | Delete a Bridge Endpoint Profile
[**get_bridge_endpoint_profile**](ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi.md#get_bridge_endpoint_profile) | **GET** /bridge-endpoint-profiles/{bridgeendpointprofile-id} | Get Information about a bridge endpoint Profile
[**list_bridge_endpoint_profiles**](ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi.md#list_bridge_endpoint_profiles) | **GET** /bridge-endpoint-profiles | List All Bridge Endpoint Profiles
[**update_bridge_endpoint_profile**](ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi.md#update_bridge_endpoint_profile) | **PUT** /bridge-endpoint-profiles/{bridgeendpointprofile-id} | Update a Bridge Endpoint Profile

# **create_bridge_endpoint_profile**
> BridgeEndpointProfile create_bridge_endpoint_profile(body)

Create a Bridge Endpoint Profile

Creates a Bridge Endpoint Profile. Profile contains edge cluster id, indexes of the member nodes, fialover mode and high availability mode for a Bridge EndPoint 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.BridgeEndpointProfile() # BridgeEndpointProfile | 

try:
    # Create a Bridge Endpoint Profile
    api_response = api_instance.create_bridge_endpoint_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi->create_bridge_endpoint_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BridgeEndpointProfile**](BridgeEndpointProfile.md)|  | 

### Return type

[**BridgeEndpointProfile**](BridgeEndpointProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bridge_endpoint_profile**
> delete_bridge_endpoint_profile(bridgeendpointprofile_id)

Delete a Bridge Endpoint Profile

Deletes the specified Bridge Endpoint Profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi(swagger_client.ApiClient(configuration))
bridgeendpointprofile_id = 'bridgeendpointprofile_id_example' # str | 

try:
    # Delete a Bridge Endpoint Profile
    api_instance.delete_bridge_endpoint_profile(bridgeendpointprofile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi->delete_bridge_endpoint_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridgeendpointprofile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bridge_endpoint_profile**
> BridgeEndpointProfile get_bridge_endpoint_profile(bridgeendpointprofile_id)

Get Information about a bridge endpoint Profile

Returns information about a specified bridge endpoint profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi(swagger_client.ApiClient(configuration))
bridgeendpointprofile_id = 'bridgeendpointprofile_id_example' # str | 

try:
    # Get Information about a bridge endpoint Profile
    api_response = api_instance.get_bridge_endpoint_profile(bridgeendpointprofile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi->get_bridge_endpoint_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridgeendpointprofile_id** | **str**|  | 

### Return type

[**BridgeEndpointProfile**](BridgeEndpointProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bridge_endpoint_profiles**
> BridgeEndpointProfileListResult list_bridge_endpoint_profiles(cursor=cursor, edge_cluster_id=edge_cluster_id, failover_mode=failover_mode, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List All Bridge Endpoint Profiles

Returns information about all configured bridge endoint profiles 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
edge_cluster_id = 'edge_cluster_id_example' # str | Edge Cluster Identifier (optional)
failover_mode = 'failover_mode_example' # str |  (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List All Bridge Endpoint Profiles
    api_response = api_instance.list_bridge_endpoint_profiles(cursor=cursor, edge_cluster_id=edge_cluster_id, failover_mode=failover_mode, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi->list_bridge_endpoint_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **edge_cluster_id** | **str**| Edge Cluster Identifier | [optional] 
 **failover_mode** | **str**|  | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**BridgeEndpointProfileListResult**](BridgeEndpointProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bridge_endpoint_profile**
> BridgeEndpointProfile update_bridge_endpoint_profile(body, bridgeendpointprofile_id)

Update a Bridge Endpoint Profile

Modifies a existing bridge endpoint profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.BridgeEndpointProfile() # BridgeEndpointProfile | 
bridgeendpointprofile_id = 'bridgeendpointprofile_id_example' # str | 

try:
    # Update a Bridge Endpoint Profile
    api_response = api_instance.update_bridge_endpoint_profile(body, bridgeendpointprofile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointProfilesApi->update_bridge_endpoint_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BridgeEndpointProfile**](BridgeEndpointProfile.md)|  | 
 **bridgeendpointprofile_id** | **str**|  | 

### Return type

[**BridgeEndpointProfile**](BridgeEndpointProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

