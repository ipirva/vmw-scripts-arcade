# swagger_client.ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ip_sec_vpn_local_endpoint**](ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi.md#create_ip_sec_vpn_local_endpoint) | **POST** /vpn/ipsec/local-endpoints | Create custom local endpoint
[**create_ip_sec_vpn_peer_end_point**](ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi.md#create_ip_sec_vpn_peer_end_point) | **POST** /vpn/ipsec/peer-endpoints | Create custom peer endpoint
[**delete_ip_sec_vpn_local_endpoint**](ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi.md#delete_ip_sec_vpn_local_endpoint) | **DELETE** /vpn/ipsec/local-endpoints/{ipsec-vpn-local-endpoint-id} | Delete custom IPSec local endpoint
[**delete_ip_sec_vpn_peer_endpoint**](ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi.md#delete_ip_sec_vpn_peer_endpoint) | **DELETE** /vpn/ipsec/peer-endpoints/{ipsec-vpn-peer-endpoint-id} | Delete custom IPSec VPN peer endpoint
[**get_ip_sec_vpn_local_endpoint**](ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi.md#get_ip_sec_vpn_local_endpoint) | **GET** /vpn/ipsec/local-endpoints/{ipsec-vpn-local-endpoint-id} | Get custom IPSec local endpoint
[**get_ip_sec_vpn_peer_endpoint**](ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi.md#get_ip_sec_vpn_peer_endpoint) | **GET** /vpn/ipsec/peer-endpoints/{ipsec-vpn-peer-endpoint-id} | Get IPSec VPN peer endpoint
[**get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data**](ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi.md#get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data) | **GET** /vpn/ipsec/peer-endpoints/{ipsec-vpn-peer-endpoint-id}?action&#x3D;show-sensitive-data | Get IPSec VPN peer endpoint with PSK
[**list_ip_sec_vpn_local_endpoints**](ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi.md#list_ip_sec_vpn_local_endpoints) | **GET** /vpn/ipsec/local-endpoints | Get IPSec local endpoint list result
[**list_ip_sec_vpn_peer_endpoints**](ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi.md#list_ip_sec_vpn_peer_endpoints) | **GET** /vpn/ipsec/peer-endpoints | Get IPSecVPNPeerEndpoint List Result
[**update_ip_sec_vpn_local_endpoint**](ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi.md#update_ip_sec_vpn_local_endpoint) | **PUT** /vpn/ipsec/local-endpoints/{ipsec-vpn-local-endpoint-id} | Edit custom IPSec local endpoint
[**update_ip_sec_vpn_peer_endpoint**](ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi.md#update_ip_sec_vpn_peer_endpoint) | **PUT** /vpn/ipsec/peer-endpoints/{ipsec-vpn-peer-endpoint-id} | Edit custom IPSecPeerEndpoint

# **create_ip_sec_vpn_local_endpoint**
> IPSecVPNLocalEndpoint create_ip_sec_vpn_local_endpoint(body)

Create custom local endpoint

Create custom IPSec local endpoint.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNLocalEndpoint() # IPSecVPNLocalEndpoint | 

try:
    # Create custom local endpoint
    api_response = api_instance.create_ip_sec_vpn_local_endpoint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi->create_ip_sec_vpn_local_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNLocalEndpoint**](IPSecVPNLocalEndpoint.md)|  | 

### Return type

[**IPSecVPNLocalEndpoint**](IPSecVPNLocalEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ip_sec_vpn_peer_end_point**
> IPSecVPNPeerEndpoint create_ip_sec_vpn_peer_end_point(body)

Create custom peer endpoint

Create custom IPSec peer endpoint.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNPeerEndpoint() # IPSecVPNPeerEndpoint | 

try:
    # Create custom peer endpoint
    api_response = api_instance.create_ip_sec_vpn_peer_end_point(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi->create_ip_sec_vpn_peer_end_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNPeerEndpoint**](IPSecVPNPeerEndpoint.md)|  | 

### Return type

[**IPSecVPNPeerEndpoint**](IPSecVPNPeerEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_sec_vpn_local_endpoint**
> delete_ip_sec_vpn_local_endpoint(ipsec_vpn_local_endpoint_id, force=force)

Delete custom IPSec local endpoint

Delete custom IPSec local endpoint.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi(swagger_client.ApiClient(configuration))
ipsec_vpn_local_endpoint_id = 'ipsec_vpn_local_endpoint_id_example' # str | 
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete custom IPSec local endpoint
    api_instance.delete_ip_sec_vpn_local_endpoint(ipsec_vpn_local_endpoint_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi->delete_ip_sec_vpn_local_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_local_endpoint_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_sec_vpn_peer_endpoint**
> delete_ip_sec_vpn_peer_endpoint(ipsec_vpn_peer_endpoint_id, force=force)

Delete custom IPSec VPN peer endpoint

Delete custom IPSec VPN peer endpoint. All references are strong references and dependent peer endpoints can not be deleted if being referenced.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi(swagger_client.ApiClient(configuration))
ipsec_vpn_peer_endpoint_id = 'ipsec_vpn_peer_endpoint_id_example' # str | 
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete custom IPSec VPN peer endpoint
    api_instance.delete_ip_sec_vpn_peer_endpoint(ipsec_vpn_peer_endpoint_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi->delete_ip_sec_vpn_peer_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_peer_endpoint_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_sec_vpn_local_endpoint**
> IPSecVPNLocalEndpoint get_ip_sec_vpn_local_endpoint(ipsec_vpn_local_endpoint_id)

Get custom IPSec local endpoint

Get custom IPSec local endpoint.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi(swagger_client.ApiClient(configuration))
ipsec_vpn_local_endpoint_id = 'ipsec_vpn_local_endpoint_id_example' # str | 

try:
    # Get custom IPSec local endpoint
    api_response = api_instance.get_ip_sec_vpn_local_endpoint(ipsec_vpn_local_endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi->get_ip_sec_vpn_local_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_local_endpoint_id** | **str**|  | 

### Return type

[**IPSecVPNLocalEndpoint**](IPSecVPNLocalEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_sec_vpn_peer_endpoint**
> IPSecVPNPeerEndpoint get_ip_sec_vpn_peer_endpoint(ipsec_vpn_peer_endpoint_id)

Get IPSec VPN peer endpoint

Get custom IPSec VPN peer endpoint.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi(swagger_client.ApiClient(configuration))
ipsec_vpn_peer_endpoint_id = 'ipsec_vpn_peer_endpoint_id_example' # str | 

try:
    # Get IPSec VPN peer endpoint
    api_response = api_instance.get_ip_sec_vpn_peer_endpoint(ipsec_vpn_peer_endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi->get_ip_sec_vpn_peer_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_peer_endpoint_id** | **str**|  | 

### Return type

[**IPSecVPNPeerEndpoint**](IPSecVPNPeerEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data**
> IPSecVPNPeerEndpoint get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data(ipsec_vpn_peer_endpoint_id)

Get IPSec VPN peer endpoint with PSK

Get custom IPSec VPN peer endpoint with PSK.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi(swagger_client.ApiClient(configuration))
ipsec_vpn_peer_endpoint_id = 'ipsec_vpn_peer_endpoint_id_example' # str | 

try:
    # Get IPSec VPN peer endpoint with PSK
    api_response = api_instance.get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data(ipsec_vpn_peer_endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi->get_ip_sec_vpn_peer_endpoint_with_psk_show_sensitive_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_peer_endpoint_id** | **str**|  | 

### Return type

[**IPSecVPNPeerEndpoint**](IPSecVPNPeerEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_sec_vpn_local_endpoints**
> IPSecVPNLocalEndpointListResult list_ip_sec_vpn_local_endpoints(cursor=cursor, included_fields=included_fields, ipsec_vpn_service_id=ipsec_vpn_service_id, logical_router_id=logical_router_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get IPSec local endpoint list result

Get paginated list of all local endpoints.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
ipsec_vpn_service_id = 'ipsec_vpn_service_id_example' # str | Id of the IPSec VPN service (optional)
logical_router_id = 'logical_router_id_example' # str | Id of logical router (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get IPSec local endpoint list result
    api_response = api_instance.list_ip_sec_vpn_local_endpoints(cursor=cursor, included_fields=included_fields, ipsec_vpn_service_id=ipsec_vpn_service_id, logical_router_id=logical_router_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi->list_ip_sec_vpn_local_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **ipsec_vpn_service_id** | **str**| Id of the IPSec VPN service | [optional] 
 **logical_router_id** | **str**| Id of logical router | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IPSecVPNLocalEndpointListResult**](IPSecVPNLocalEndpointListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_sec_vpn_peer_endpoints**
> IPSecVPNPeerEndpointListResult list_ip_sec_vpn_peer_endpoints(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get IPSecVPNPeerEndpoint List Result

Get paginated list of all peer endpoint.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get IPSecVPNPeerEndpoint List Result
    api_response = api_instance.list_ip_sec_vpn_peer_endpoints(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi->list_ip_sec_vpn_peer_endpoints: %s\n" % e)
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

[**IPSecVPNPeerEndpointListResult**](IPSecVPNPeerEndpointListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_sec_vpn_local_endpoint**
> IPSecVPNLocalEndpoint update_ip_sec_vpn_local_endpoint(body, ipsec_vpn_local_endpoint_id)

Edit custom IPSec local endpoint

Edit custom IPSec local endpoint.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNLocalEndpoint() # IPSecVPNLocalEndpoint | 
ipsec_vpn_local_endpoint_id = 'ipsec_vpn_local_endpoint_id_example' # str | 

try:
    # Edit custom IPSec local endpoint
    api_response = api_instance.update_ip_sec_vpn_local_endpoint(body, ipsec_vpn_local_endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi->update_ip_sec_vpn_local_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNLocalEndpoint**](IPSecVPNLocalEndpoint.md)|  | 
 **ipsec_vpn_local_endpoint_id** | **str**|  | 

### Return type

[**IPSecVPNLocalEndpoint**](IPSecVPNLocalEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_sec_vpn_peer_endpoint**
> IPSecVPNPeerEndpoint update_ip_sec_vpn_peer_endpoint(body, ipsec_vpn_peer_endpoint_id)

Edit custom IPSecPeerEndpoint

Edit custom IPSec peer endpoint. System owned endpoints are non editable.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNPeerEndpoint() # IPSecVPNPeerEndpoint | 
ipsec_vpn_peer_endpoint_id = 'ipsec_vpn_peer_endpoint_id_example' # str | 

try:
    # Edit custom IPSecPeerEndpoint
    api_response = api_instance.update_ip_sec_vpn_peer_endpoint(body, ipsec_vpn_peer_endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECPeerEndpointsApi->update_ip_sec_vpn_peer_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNPeerEndpoint**](IPSecVPNPeerEndpoint.md)|  | 
 **ipsec_vpn_peer_endpoint_id** | **str**|  | 

### Return type

[**IPSecVPNPeerEndpoint**](IPSecVPNPeerEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

