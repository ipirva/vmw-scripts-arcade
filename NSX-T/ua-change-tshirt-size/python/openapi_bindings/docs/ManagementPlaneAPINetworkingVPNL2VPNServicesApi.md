# swagger_client.ManagementPlaneAPINetworkingVPNL2VPNServicesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_l2_vpn_service**](ManagementPlaneAPINetworkingVPNL2VPNServicesApi.md#create_l2_vpn_service) | **POST** /vpn/l2vpn/services | Create L2VPN service
[**delete_l2_vpn_service**](ManagementPlaneAPINetworkingVPNL2VPNServicesApi.md#delete_l2_vpn_service) | **DELETE** /vpn/l2vpn/services/{l2vpn-service-id} | Delete a L2VPN service
[**get_l2_vpn_service**](ManagementPlaneAPINetworkingVPNL2VPNServicesApi.md#get_l2_vpn_service) | **GET** /vpn/l2vpn/services/{l2vpn-service-id} | Get L2VPN service
[**list_l2_vpn_services**](ManagementPlaneAPINetworkingVPNL2VPNServicesApi.md#list_l2_vpn_services) | **GET** /vpn/l2vpn/services | Get all L2VPN services
[**update_l2_vpn_service**](ManagementPlaneAPINetworkingVPNL2VPNServicesApi.md#update_l2_vpn_service) | **PUT** /vpn/l2vpn/services/{l2vpn-service-id} | Edit a L2VPN service

# **create_l2_vpn_service**
> L2VpnService create_l2_vpn_service(body)

Create L2VPN service

Create L2VPN service for a given logical router

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNL2VPNServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.L2VpnService() # L2VpnService | 

try:
    # Create L2VPN service
    api_response = api_instance.create_l2_vpn_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNL2VPNServicesApi->create_l2_vpn_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**L2VpnService**](L2VpnService.md)|  | 

### Return type

[**L2VpnService**](L2VpnService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_l2_vpn_service**
> delete_l2_vpn_service(l2vpn_service_id, force=force)

Delete a L2VPN service

Delete a specific L2VPN service. If there are any L2VpnSessions on this L2VpnService, those needs to be deleted first.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNL2VPNServicesApi(swagger_client.ApiClient(configuration))
l2vpn_service_id = 'l2vpn_service_id_example' # str | 
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete a L2VPN service
    api_instance.delete_l2_vpn_service(l2vpn_service_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNL2VPNServicesApi->delete_l2_vpn_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **l2vpn_service_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l2_vpn_service**
> L2VpnService get_l2_vpn_service(l2vpn_service_id)

Get L2VPN service

Get a specific L2VPN service

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNL2VPNServicesApi(swagger_client.ApiClient(configuration))
l2vpn_service_id = 'l2vpn_service_id_example' # str | 

try:
    # Get L2VPN service
    api_response = api_instance.get_l2_vpn_service(l2vpn_service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNL2VPNServicesApi->get_l2_vpn_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **l2vpn_service_id** | **str**|  | 

### Return type

[**L2VpnService**](L2VpnService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_l2_vpn_services**
> L2VpnServiceListResult list_l2_vpn_services(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get all L2VPN services

Get paginated list of all L2VPN services

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNL2VPNServicesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get all L2VPN services
    api_response = api_instance.list_l2_vpn_services(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNL2VPNServicesApi->list_l2_vpn_services: %s\n" % e)
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

[**L2VpnServiceListResult**](L2VpnServiceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_l2_vpn_service**
> L2VpnService update_l2_vpn_service(body, l2vpn_service_id)

Edit a L2VPN service

Edit a specific L2VPN service

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNL2VPNServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.L2VpnService() # L2VpnService | 
l2vpn_service_id = 'l2vpn_service_id_example' # str | 

try:
    # Edit a L2VPN service
    api_response = api_instance.update_l2_vpn_service(body, l2vpn_service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNL2VPNServicesApi->update_l2_vpn_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**L2VpnService**](L2VpnService.md)|  | 
 **l2vpn_service_id** | **str**|  | 

### Return type

[**L2VpnService**](L2VpnService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

