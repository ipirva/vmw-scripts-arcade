# swagger_client.SystemAdministrationConfigurationFabricInventoryVirtualInterfacesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_vifs**](SystemAdministrationConfigurationFabricInventoryVirtualInterfacesApi.md#list_vifs) | **GET** /fabric/vifs | Return the List of Virtual Network Interfaces (VIFs)

# **list_vifs**
> VirtualNetworkInterfaceListResult list_vifs(cursor=cursor, host_id=host_id, included_fields=included_fields, lport_attachment_id=lport_attachment_id, owner_vm_id=owner_vm_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, vm_id=vm_id)

Return the List of Virtual Network Interfaces (VIFs)

Returns information about all VIFs. A virtual network interface aggregates network interfaces into a logical interface unit that is indistinuishable from a physical network interface. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricInventoryVirtualInterfacesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
host_id = 'host_id_example' # str | Id of the host where this vif is located. (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
lport_attachment_id = 'lport_attachment_id_example' # str | LPort Attachment Id of the virtual network interface. (optional)
owner_vm_id = 'owner_vm_id_example' # str | External id of the virtual machine. (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
vm_id = 'vm_id_example' # str | External id of the virtual machine. (optional)

try:
    # Return the List of Virtual Network Interfaces (VIFs)
    api_response = api_instance.list_vifs(cursor=cursor, host_id=host_id, included_fields=included_fields, lport_attachment_id=lport_attachment_id, owner_vm_id=owner_vm_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, vm_id=vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricInventoryVirtualInterfacesApi->list_vifs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **host_id** | **str**| Id of the host where this vif is located. | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **lport_attachment_id** | **str**| LPort Attachment Id of the virtual network interface. | [optional] 
 **owner_vm_id** | **str**| External id of the virtual machine. | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **vm_id** | **str**| External id of the virtual machine. | [optional] 

### Return type

[**VirtualNetworkInterfaceListResult**](VirtualNetworkInterfaceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

