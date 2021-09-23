# swagger_client.ManagementPlaneAPINetworkingVPNIPSECServicesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ip_sec_vpn_service**](ManagementPlaneAPINetworkingVPNIPSECServicesApi.md#create_ip_sec_vpn_service) | **POST** /vpn/ipsec/services | Create VPN service
[**delete_ip_sec_vpn_service**](ManagementPlaneAPINetworkingVPNIPSECServicesApi.md#delete_ip_sec_vpn_service) | **DELETE** /vpn/ipsec/services/{ipsec-vpn-service-id} | Delete IPSec VPN service
[**get_ip_sec_vpn_service**](ManagementPlaneAPINetworkingVPNIPSECServicesApi.md#get_ip_sec_vpn_service) | **GET** /vpn/ipsec/services/{ipsec-vpn-service-id} | Get IPSec VPN service
[**list_ip_sec_vpn_services**](ManagementPlaneAPINetworkingVPNIPSECServicesApi.md#list_ip_sec_vpn_services) | **GET** /vpn/ipsec/services | Get IPSec VPN service list result
[**update_ip_sec_vpn_service**](ManagementPlaneAPINetworkingVPNIPSECServicesApi.md#update_ip_sec_vpn_service) | **PUT** /vpn/ipsec/services/{ipsec-vpn-service-id} | Edit IPSec VPN service

# **create_ip_sec_vpn_service**
> IPSecVPNService create_ip_sec_vpn_service(body)

Create VPN service

Create VPN service for given logical router.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNService() # IPSecVPNService | 

try:
    # Create VPN service
    api_response = api_instance.create_ip_sec_vpn_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECServicesApi->create_ip_sec_vpn_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNService**](IPSecVPNService.md)|  | 

### Return type

[**IPSecVPNService**](IPSecVPNService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_sec_vpn_service**
> delete_ip_sec_vpn_service(ipsec_vpn_service_id, force=force)

Delete IPSec VPN service

Delete IPSec VPN service for given router.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECServicesApi(swagger_client.ApiClient(configuration))
ipsec_vpn_service_id = 'ipsec_vpn_service_id_example' # str | 
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete IPSec VPN service
    api_instance.delete_ip_sec_vpn_service(ipsec_vpn_service_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECServicesApi->delete_ip_sec_vpn_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_service_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_sec_vpn_service**
> IPSecVPNService get_ip_sec_vpn_service(ipsec_vpn_service_id)

Get IPSec VPN service

Get IPSec VPN service for given logical router.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECServicesApi(swagger_client.ApiClient(configuration))
ipsec_vpn_service_id = 'ipsec_vpn_service_id_example' # str | 

try:
    # Get IPSec VPN service
    api_response = api_instance.get_ip_sec_vpn_service(ipsec_vpn_service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECServicesApi->get_ip_sec_vpn_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_service_id** | **str**|  | 

### Return type

[**IPSecVPNService**](IPSecVPNService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_sec_vpn_services**
> IPSecVPNServiceListResult list_ip_sec_vpn_services(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get IPSec VPN service list result

Get paginated list of all IPSec VPN services.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECServicesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get IPSec VPN service list result
    api_response = api_instance.list_ip_sec_vpn_services(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECServicesApi->list_ip_sec_vpn_services: %s\n" % e)
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

[**IPSecVPNServiceListResult**](IPSecVPNServiceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_sec_vpn_service**
> IPSecVPNService update_ip_sec_vpn_service(body, ipsec_vpn_service_id)

Edit IPSec VPN service

Edit IPSec VPN service for given logical router.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNService() # IPSecVPNService | 
ipsec_vpn_service_id = 'ipsec_vpn_service_id_example' # str | 

try:
    # Edit IPSec VPN service
    api_response = api_instance.update_ip_sec_vpn_service(body, ipsec_vpn_service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECServicesApi->update_ip_sec_vpn_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNService**](IPSecVPNService.md)|  | 
 **ipsec_vpn_service_id** | **str**|  | 

### Return type

[**IPSecVPNService**](IPSecVPNService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

