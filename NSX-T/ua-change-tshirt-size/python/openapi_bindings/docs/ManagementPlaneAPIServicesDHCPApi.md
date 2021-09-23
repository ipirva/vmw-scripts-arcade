# swagger_client.ManagementPlaneAPIServicesDHCPApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dhcp_lease_info**](ManagementPlaneAPIServicesDHCPApi.md#get_dhcp_lease_info) | **GET** /dhcp/servers/{server-id}/leases | Get specific leases of a given dhcp server
[**get_dhcp_statistics**](ManagementPlaneAPIServicesDHCPApi.md#get_dhcp_statistics) | **GET** /dhcp/servers/{server-id}/statistics | Get DHCP statistics with given dhcp server id

# **get_dhcp_lease_info**
> DhcpLeases get_dhcp_lease_info(server_id, address=address, pool_id=pool_id, source=source)

Get specific leases of a given dhcp server

Get specific leases of a given dhcp server. As a dhcp server could manage millions of leases, the API has to limit the number of the returned leases via two mutually-excluded request parameters, i.e. \"pool_id\" and \"address\". Either a \"pool_id\" or an \"address\" can be provided, but not both in a same call.  If a \"pool_id\" is specified, the leases of the specific pool are returned. If an \"address\" is specified, only the lease(s) represented y this address is(are) returned. The \"address\" can be a single IP, an ip-range, or a mac address. 

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
api_instance = swagger_client.ManagementPlaneAPIServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
address = 'address_example' # str | can be an ip address, or an ip range, or a mac address (optional)
pool_id = 'pool_id_example' # str | The uuid of dhcp ip pool (optional)
source = 'source_example' # str | Data source type. (optional)

try:
    # Get specific leases of a given dhcp server
    api_response = api_instance.get_dhcp_lease_info(server_id, address=address, pool_id=pool_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIServicesDHCPApi->get_dhcp_lease_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **address** | **str**| can be an ip address, or an ip range, or a mac address | [optional] 
 **pool_id** | **str**| The uuid of dhcp ip pool | [optional] 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**DhcpLeases**](DhcpLeases.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dhcp_statistics**
> DhcpStatistics get_dhcp_statistics(server_id)

Get DHCP statistics with given dhcp server id

Returns the statistics of the given dhcp server. 

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
api_instance = swagger_client.ManagementPlaneAPIServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 

try:
    # Get DHCP statistics with given dhcp server id
    api_response = api_instance.get_dhcp_statistics(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIServicesDHCPApi->get_dhcp_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 

### Return type

[**DhcpStatistics**](DhcpStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

