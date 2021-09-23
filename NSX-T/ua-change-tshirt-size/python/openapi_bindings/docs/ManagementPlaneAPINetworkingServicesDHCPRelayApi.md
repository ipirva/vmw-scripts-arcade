# swagger_client.ManagementPlaneAPINetworkingServicesDHCPRelayApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dhcp_relay**](ManagementPlaneAPINetworkingServicesDHCPRelayApi.md#create_dhcp_relay) | **POST** /dhcp/relays | Create a DHCP Relay Service
[**delete_dhcp_relay**](ManagementPlaneAPINetworkingServicesDHCPRelayApi.md#delete_dhcp_relay) | **DELETE** /dhcp/relays/{relay-id} | Delete a DHCP Relay Service
[**list_dhcp_relays**](ManagementPlaneAPINetworkingServicesDHCPRelayApi.md#list_dhcp_relays) | **GET** /dhcp/relays | List all DHCP Relay Services
[**read_dhcp_relay**](ManagementPlaneAPINetworkingServicesDHCPRelayApi.md#read_dhcp_relay) | **GET** /dhcp/relays/{relay-id} | Read a DHCP Relay Service
[**update_dhcp_relay**](ManagementPlaneAPINetworkingServicesDHCPRelayApi.md#update_dhcp_relay) | **PUT** /dhcp/relays/{relay-id} | Update a DHCP Relay Service

# **create_dhcp_relay**
> DhcpRelayService create_dhcp_relay(body)

Create a DHCP Relay Service

Creates a dhcp relay service. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPRelayApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpRelayService() # DhcpRelayService | 

try:
    # Create a DHCP Relay Service
    api_response = api_instance.create_dhcp_relay(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPRelayApi->create_dhcp_relay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpRelayService**](DhcpRelayService.md)|  | 

### Return type

[**DhcpRelayService**](DhcpRelayService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dhcp_relay**
> delete_dhcp_relay(relay_id)

Delete a DHCP Relay Service

Deletes the specified dhcp relay service.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPRelayApi(swagger_client.ApiClient(configuration))
relay_id = 'relay_id_example' # str | 

try:
    # Delete a DHCP Relay Service
    api_instance.delete_dhcp_relay(relay_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPRelayApi->delete_dhcp_relay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relay_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dhcp_relays**
> DhcpRelayServiceListResult list_dhcp_relays(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List all DHCP Relay Services

Returns information about all configured dhcp relay services. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPRelayApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List all DHCP Relay Services
    api_response = api_instance.list_dhcp_relays(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPRelayApi->list_dhcp_relays: %s\n" % e)
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

[**DhcpRelayServiceListResult**](DhcpRelayServiceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_dhcp_relay**
> DhcpRelayService read_dhcp_relay(relay_id)

Read a DHCP Relay Service

Returns the dhcp relay service information.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPRelayApi(swagger_client.ApiClient(configuration))
relay_id = 'relay_id_example' # str | 

try:
    # Read a DHCP Relay Service
    api_response = api_instance.read_dhcp_relay(relay_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPRelayApi->read_dhcp_relay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relay_id** | **str**|  | 

### Return type

[**DhcpRelayService**](DhcpRelayService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dhcp_relay**
> DhcpRelayService update_dhcp_relay(body, relay_id)

Update a DHCP Relay Service

Modifies the specified dhcp relay service. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPRelayApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpRelayService() # DhcpRelayService | 
relay_id = 'relay_id_example' # str | 

try:
    # Update a DHCP Relay Service
    api_response = api_instance.update_dhcp_relay(body, relay_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPRelayApi->update_dhcp_relay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpRelayService**](DhcpRelayService.md)|  | 
 **relay_id** | **str**|  | 

### Return type

[**DhcpRelayService**](DhcpRelayService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

