# swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingBFDConfigurationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_routing_bfd_config**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingBFDConfigurationApi.md#read_routing_bfd_config) | **GET** /logical-routers/{logical-router-id}/routing/bfd-config | Read the Routing BFD Configuration
[**update_routing_bfd_config**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingBFDConfigurationApi.md#update_routing_bfd_config) | **PUT** /logical-routers/{logical-router-id}/routing/bfd-config | Update the BFD Configuration for BFD peers for routing

# **read_routing_bfd_config**
> BfdConfig read_routing_bfd_config(logical_router_id)

Read the Routing BFD Configuration

Returns the BFD configuration for all routing BFD peers. This will be inherited |   by all BFD peers for LogicalRouter unless overriden while configuring the Peer. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingBFDConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Read the Routing BFD Configuration
    api_response = api_instance.read_routing_bfd_config(logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingBFDConfigurationApi->read_routing_bfd_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 

### Return type

[**BfdConfig**](BfdConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_routing_bfd_config**
> BfdConfig update_routing_bfd_config(body, logical_router_id)

Update the BFD Configuration for BFD peers for routing

Modifies the BFD configuration for routing BFD peers. Note - the configuration |   changes apply only to those routing BFD peers for which the BFD configuration has |   not been overridden at Peer level. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingBFDConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.BfdConfig() # BfdConfig | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Update the BFD Configuration for BFD peers for routing
    api_response = api_instance.update_routing_bfd_config(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingBFDConfigurationApi->update_routing_bfd_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BfdConfig**](BfdConfig.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**BfdConfig**](BfdConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

