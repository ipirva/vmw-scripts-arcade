# swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPortConnectionApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_forwarding_path**](ManagementPlaneAPITroubleshootingAndMonitoringPortConnectionApi.md#get_forwarding_path) | **GET** /logical-ports/{lport-id}/forwarding-path | Get networking entities between two logical ports with VIF attachment

# **get_forwarding_path**
> PortConnectionEntities get_forwarding_path(lport_id, peer_port_id)

Get networking entities between two logical ports with VIF attachment

Get networking entities between two logical ports with VIF attachment

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPortConnectionApi(swagger_client.ApiClient(configuration))
lport_id = 'lport_id_example' # str | ID of source port
peer_port_id = 'peer_port_id_example' # str | ID of peer port

try:
    # Get networking entities between two logical ports with VIF attachment
    api_response = api_instance.get_forwarding_path(lport_id, peer_port_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPortConnectionApi->get_forwarding_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lport_id** | **str**| ID of source port | 
 **peer_port_id** | **str**| ID of peer port | 

### Return type

[**PortConnectionEntities**](PortConnectionEntities.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

