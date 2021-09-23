# swagger_client.SystemAdministrationConfigurationFabricInventoryVirtualSwitchesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_virtual_switches**](SystemAdministrationConfigurationFabricInventoryVirtualSwitchesApi.md#list_virtual_switches) | **GET** /fabric/virtual-switches | Return the List of Virtual Switches

# **list_virtual_switches**
> VirtualSwitchListResult list_virtual_switches(cm_local_id=cm_local_id, cursor=cursor, discovered_node_id=discovered_node_id, display_name=display_name, external_id=external_id, included_fields=included_fields, origin_id=origin_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, uuid=uuid)

Return the List of Virtual Switches

Returns information about all virtual switches based on the request parameters. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricInventoryVirtualSwitchesApi(swagger_client.ApiClient(configuration))
cm_local_id = 'cm_local_id_example' # str | Local Id of the virtual switch (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
discovered_node_id = 'discovered_node_id_example' # str | Discovered node ID (optional)
display_name = 'display_name_example' # str | Display name of the virtual switch (optional)
external_id = 'external_id_example' # str | External id of the virtual switch (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
origin_id = 'origin_id_example' # str | ID of the compute manager (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
uuid = 'uuid_example' # str | UUID of the switch (optional)

try:
    # Return the List of Virtual Switches
    api_response = api_instance.list_virtual_switches(cm_local_id=cm_local_id, cursor=cursor, discovered_node_id=discovered_node_id, display_name=display_name, external_id=external_id, included_fields=included_fields, origin_id=origin_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, uuid=uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricInventoryVirtualSwitchesApi->list_virtual_switches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cm_local_id** | **str**| Local Id of the virtual switch | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **discovered_node_id** | **str**| Discovered node ID | [optional] 
 **display_name** | **str**| Display name of the virtual switch | [optional] 
 **external_id** | **str**| External id of the virtual switch | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **origin_id** | **str**| ID of the compute manager | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **uuid** | **str**| UUID of the switch | [optional] 

### Return type

[**VirtualSwitchListResult**](VirtualSwitchListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

