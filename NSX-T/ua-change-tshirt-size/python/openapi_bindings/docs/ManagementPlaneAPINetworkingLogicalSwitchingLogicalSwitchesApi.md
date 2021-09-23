# swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_logical_switch**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#create_logical_switch) | **POST** /logical-switches | Create a Logical Switch
[**delete_logical_switch**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#delete_logical_switch) | **DELETE** /logical-switches/{lswitch-id} | Delete a Logical Switch
[**get_logical_switch**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#get_logical_switch) | **GET** /logical-switches/{lswitch-id} | Get Logical Switch associated with the provided id (lswitch-id)
[**get_logical_switch_mac_table**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#get_logical_switch_mac_table) | **GET** /logical-switches/{lswitch-id}/mac-table | Get MAC Table for Logical Switch of the Given ID (lswitch-id)
[**get_logical_switch_mac_table_in_csv_format_csv**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#get_logical_switch_mac_table_in_csv_format_csv) | **GET** /logical-switches/{lswitch-id}/mac-table?format&#x3D;csv | Get MAC Table for Logical Switch of the Given ID (lswitch-id)
[**get_logical_switch_state**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#get_logical_switch_state) | **GET** /logical-switches/{lswitch-id}/state | Get the realized state associated with provided logical switch id
[**get_logical_switch_statistics**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#get_logical_switch_statistics) | **GET** /logical-switches/{lswitch-id}/statistics | Get Statistics for Logical Switch of the Given ID (lswitch-id)
[**get_logical_switch_status**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#get_logical_switch_status) | **GET** /logical-switches/{lswitch-id}/summary | Get Logical Switch runtime status info for a given logical switch
[**get_logical_switch_status_summary**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#get_logical_switch_status_summary) | **GET** /logical-switches/status | Get Status Summary of All Logical Switches in the System
[**get_logical_switch_vtep_table**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#get_logical_switch_vtep_table) | **GET** /logical-switches/{lswitch-id}/vtep-table | Get virtual tunnel endpoint table for logical switch of the given ID (lswitch-id) 
[**get_logical_switch_vtep_table_in_csv_format_csv**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#get_logical_switch_vtep_table_in_csv_format_csv) | **GET** /logical-switches/{lswitch-id}/vtep-table?format&#x3D;csv | Get virtual tunnel endpoint table for logical switch of the given ID (lswitch-id) 
[**list_logical_switches**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#list_logical_switches) | **GET** /logical-switches | List all Logical Switches
[**list_logical_switches_by_state**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#list_logical_switches_by_state) | **GET** /logical-switches/state | List logical switches by realized state
[**update_logical_switch**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi.md#update_logical_switch) | **PUT** /logical-switches/{lswitch-id} | Update a Logical Switch

# **create_logical_switch**
> LogicalSwitch create_logical_switch(body)

Create a Logical Switch

Creates a new logical switch. The request must include the transport_zone_id, display_name, and admin_state (UP or DOWN). The replication_mode (MTEP or SOURCE) is required for overlay logical switches, but not for VLAN-based logical switches. A vlan needs to be provided for VLAN-based logical switches 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
body = swagger_client.LogicalSwitch() # LogicalSwitch | 

try:
    # Create a Logical Switch
    api_response = api_instance.create_logical_switch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->create_logical_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogicalSwitch**](LogicalSwitch.md)|  | 

### Return type

[**LogicalSwitch**](LogicalSwitch.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_logical_switch**
> delete_logical_switch(lswitch_id, cascade=cascade, detach=detach)

Delete a Logical Switch

Removes a logical switch from the associated overlay or VLAN transport zone. By default, a logical switch cannot be deleted if there are logical ports on the switch, or it is added to a NSGroup. Cascade option can be used to delete all ports and the logical switch. Detach option can be used to delete the logical switch forcibly. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
lswitch_id = 'lswitch_id_example' # str | 
cascade = false # bool | Delete a Logical Switch and all the logical ports in it, if none of the logical ports have any attachment.  (optional) (default to false)
detach = false # bool | Force delete a logical switch (optional) (default to false)

try:
    # Delete a Logical Switch
    api_instance.delete_logical_switch(lswitch_id, cascade=cascade, detach=detach)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->delete_logical_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lswitch_id** | **str**|  | 
 **cascade** | **bool**| Delete a Logical Switch and all the logical ports in it, if none of the logical ports have any attachment.  | [optional] [default to false]
 **detach** | **bool**| Force delete a logical switch | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_switch**
> LogicalSwitch get_logical_switch(lswitch_id)

Get Logical Switch associated with the provided id (lswitch-id)

Returns information about the specified logical switch Id.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
lswitch_id = 'lswitch_id_example' # str | 

try:
    # Get Logical Switch associated with the provided id (lswitch-id)
    api_response = api_instance.get_logical_switch(lswitch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->get_logical_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lswitch_id** | **str**|  | 

### Return type

[**LogicalSwitch**](LogicalSwitch.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_switch_mac_table**
> MacAddressListResult get_logical_switch_mac_table(lswitch_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, transport_node_id=transport_node_id)

Get MAC Table for Logical Switch of the Given ID (lswitch-id)

Returns MAC table of a specified logical switch from the given transport node if a transport node id is given in the query parameter from the Central Controller Plane. The query parameter \"source=cached\" is not supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
lswitch_id = 'lswitch_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
transport_node_id = 'transport_node_id_example' # str | TransportNode Id (optional)

try:
    # Get MAC Table for Logical Switch of the Given ID (lswitch-id)
    api_response = api_instance.get_logical_switch_mac_table(lswitch_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, transport_node_id=transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->get_logical_switch_mac_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lswitch_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **transport_node_id** | **str**| TransportNode Id | [optional] 

### Return type

[**MacAddressListResult**](MacAddressListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_switch_mac_table_in_csv_format_csv**
> MacAddressCsvListResult get_logical_switch_mac_table_in_csv_format_csv(lswitch_id, source=source, transport_node_id=transport_node_id)

Get MAC Table for Logical Switch of the Given ID (lswitch-id)

Returns MAC table of a specified logical switch in CSV format from the given transport node if a transport node id is given in the query parameter from the Central Controller Plane. The query parameter \"source=cached\" is not supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
lswitch_id = 'lswitch_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)
transport_node_id = 'transport_node_id_example' # str | TransportNode Id (optional)

try:
    # Get MAC Table for Logical Switch of the Given ID (lswitch-id)
    api_response = api_instance.get_logical_switch_mac_table_in_csv_format_csv(lswitch_id, source=source, transport_node_id=transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->get_logical_switch_mac_table_in_csv_format_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lswitch_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 
 **transport_node_id** | **str**| TransportNode Id | [optional] 

### Return type

[**MacAddressCsvListResult**](MacAddressCsvListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_switch_state**
> LogicalSwitchState get_logical_switch_state(lswitch_id)

Get the realized state associated with provided logical switch id

Returns current state of the logical switch configuration and details of only out-of-sync transport nodes. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
lswitch_id = 'lswitch_id_example' # str | 

try:
    # Get the realized state associated with provided logical switch id
    api_response = api_instance.get_logical_switch_state(lswitch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->get_logical_switch_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lswitch_id** | **str**|  | 

### Return type

[**LogicalSwitchState**](LogicalSwitchState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_switch_statistics**
> LogicalSwitchStatistics get_logical_switch_statistics(lswitch_id, source=source)

Get Statistics for Logical Switch of the Given ID (lswitch-id)

Returns statistics  of a specified logical switch. The query parameter \"source=realtime\" is not supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
lswitch_id = 'lswitch_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get Statistics for Logical Switch of the Given ID (lswitch-id)
    api_response = api_instance.get_logical_switch_statistics(lswitch_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->get_logical_switch_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lswitch_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LogicalSwitchStatistics**](LogicalSwitchStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_switch_status**
> LogicalSwitchStatus get_logical_switch_status(lswitch_id)

Get Logical Switch runtime status info for a given logical switch

Returns the number of ports assigned to a logical switch.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
lswitch_id = 'lswitch_id_example' # str | 

try:
    # Get Logical Switch runtime status info for a given logical switch
    api_response = api_instance.get_logical_switch_status(lswitch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->get_logical_switch_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lswitch_id** | **str**|  | 

### Return type

[**LogicalSwitchStatus**](LogicalSwitchStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_switch_status_summary**
> LogicalSwitchStatusSummary get_logical_switch_status_summary(cursor=cursor, diagnostic=diagnostic, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, switching_profile_id=switching_profile_id, transport_type=transport_type, transport_zone_id=transport_zone_id, uplink_teaming_policy_name=uplink_teaming_policy_name, vlan=vlan, vni=vni)

Get Status Summary of All Logical Switches in the System

Returns Operational status of all logical switches. The query parameter \"source=realtime\" is not supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
diagnostic = false # bool | Flag to enable showing of transit logical switch. (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
switching_profile_id = 'switching_profile_id_example' # str | Switching Profile identifier (optional)
transport_type = 'transport_type_example' # str | Mode of transport supported in the transport zone for this logical switch (optional)
transport_zone_id = 'transport_zone_id_example' # str | Transport zone identifier (optional)
uplink_teaming_policy_name = 'uplink_teaming_policy_name_example' # str | The logical switch's uplink teaming policy name (optional)
vlan = 789 # int | Virtual Local Area Network Identifier (optional)
vni = 56 # int | VNI of the OVERLAY LogicalSwitch(es) to return. (optional)

try:
    # Get Status Summary of All Logical Switches in the System
    api_response = api_instance.get_logical_switch_status_summary(cursor=cursor, diagnostic=diagnostic, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, switching_profile_id=switching_profile_id, transport_type=transport_type, transport_zone_id=transport_zone_id, uplink_teaming_policy_name=uplink_teaming_policy_name, vlan=vlan, vni=vni)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->get_logical_switch_status_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **diagnostic** | **bool**| Flag to enable showing of transit logical switch. | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **switching_profile_id** | **str**| Switching Profile identifier | [optional] 
 **transport_type** | **str**| Mode of transport supported in the transport zone for this logical switch | [optional] 
 **transport_zone_id** | **str**| Transport zone identifier | [optional] 
 **uplink_teaming_policy_name** | **str**| The logical switch&#x27;s uplink teaming policy name | [optional] 
 **vlan** | **int**| Virtual Local Area Network Identifier | [optional] 
 **vni** | **int**| VNI of the OVERLAY LogicalSwitch(es) to return. | [optional] 

### Return type

[**LogicalSwitchStatusSummary**](LogicalSwitchStatusSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_switch_vtep_table**
> VtepListResult get_logical_switch_vtep_table(lswitch_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, transport_node_id=transport_node_id)

Get virtual tunnel endpoint table for logical switch of the given ID (lswitch-id) 

Returns the virtual tunnel endpoint table of a specified logical switch from the given transport node if a transport node id is given in the query parameter, from the Central Controller Plane. The query parameter \"source=cached\" is not supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
lswitch_id = 'lswitch_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
transport_node_id = 'transport_node_id_example' # str | TransportNode Id (optional)

try:
    # Get virtual tunnel endpoint table for logical switch of the given ID (lswitch-id) 
    api_response = api_instance.get_logical_switch_vtep_table(lswitch_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, transport_node_id=transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->get_logical_switch_vtep_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lswitch_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **transport_node_id** | **str**| TransportNode Id | [optional] 

### Return type

[**VtepListResult**](VtepListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_switch_vtep_table_in_csv_format_csv**
> VtepCsvListResult get_logical_switch_vtep_table_in_csv_format_csv(lswitch_id, source=source, transport_node_id=transport_node_id)

Get virtual tunnel endpoint table for logical switch of the given ID (lswitch-id) 

Returns virtual tunnel endpoint table of a specified logical switch in CSV format from the given transport node if a transport node id is given in the query parameter from the Central Controller Plane. The query parameter \"source=cached\" is not supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
lswitch_id = 'lswitch_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)
transport_node_id = 'transport_node_id_example' # str | TransportNode Id (optional)

try:
    # Get virtual tunnel endpoint table for logical switch of the given ID (lswitch-id) 
    api_response = api_instance.get_logical_switch_vtep_table_in_csv_format_csv(lswitch_id, source=source, transport_node_id=transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->get_logical_switch_vtep_table_in_csv_format_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lswitch_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 
 **transport_node_id** | **str**| TransportNode Id | [optional] 

### Return type

[**VtepCsvListResult**](VtepCsvListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_logical_switches**
> LogicalSwitchListResult list_logical_switches(cursor=cursor, diagnostic=diagnostic, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, switching_profile_id=switching_profile_id, transport_type=transport_type, transport_zone_id=transport_zone_id, uplink_teaming_policy_name=uplink_teaming_policy_name, vlan=vlan, vni=vni)

List all Logical Switches

Returns information about all configured logical switches.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
diagnostic = false # bool | Flag to enable showing of transit logical switch. (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
switching_profile_id = 'switching_profile_id_example' # str | Switching Profile identifier (optional)
transport_type = 'transport_type_example' # str | Mode of transport supported in the transport zone for this logical switch (optional)
transport_zone_id = 'transport_zone_id_example' # str | Transport zone identifier (optional)
uplink_teaming_policy_name = 'uplink_teaming_policy_name_example' # str | The logical switch's uplink teaming policy name (optional)
vlan = 789 # int | Virtual Local Area Network Identifier (optional)
vni = 56 # int | VNI of the OVERLAY LogicalSwitch(es) to return. (optional)

try:
    # List all Logical Switches
    api_response = api_instance.list_logical_switches(cursor=cursor, diagnostic=diagnostic, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, switching_profile_id=switching_profile_id, transport_type=transport_type, transport_zone_id=transport_zone_id, uplink_teaming_policy_name=uplink_teaming_policy_name, vlan=vlan, vni=vni)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->list_logical_switches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **diagnostic** | **bool**| Flag to enable showing of transit logical switch. | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **switching_profile_id** | **str**| Switching Profile identifier | [optional] 
 **transport_type** | **str**| Mode of transport supported in the transport zone for this logical switch | [optional] 
 **transport_zone_id** | **str**| Transport zone identifier | [optional] 
 **uplink_teaming_policy_name** | **str**| The logical switch&#x27;s uplink teaming policy name | [optional] 
 **vlan** | **int**| Virtual Local Area Network Identifier | [optional] 
 **vni** | **int**| VNI of the OVERLAY LogicalSwitch(es) to return. | [optional] 

### Return type

[**LogicalSwitchListResult**](LogicalSwitchListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_logical_switches_by_state**
> LogicalSwitchStateListResult list_logical_switches_by_state(status=status)

List logical switches by realized state

Returns a list of logical switches states that have realized state as provided as query parameter. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
status = 'status_example' # str | Realized state of logical switches (optional)

try:
    # List logical switches by realized state
    api_response = api_instance.list_logical_switches_by_state(status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->list_logical_switches_by_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Realized state of logical switches | [optional] 

### Return type

[**LogicalSwitchStateListResult**](LogicalSwitchStateListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_logical_switch**
> LogicalSwitch update_logical_switch(body, lswitch_id)

Update a Logical Switch

Modifies attributes of an existing logical switch. Modifiable attributes include admin_state, replication_mode, switching_profile_ids and VLAN spec. You cannot modify the original transport_zone_id. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi(swagger_client.ApiClient(configuration))
body = swagger_client.LogicalSwitch() # LogicalSwitch | 
lswitch_id = 'lswitch_id_example' # str | 

try:
    # Update a Logical Switch
    api_response = api_instance.update_logical_switch(body, lswitch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchesApi->update_logical_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogicalSwitch**](LogicalSwitch.md)|  | 
 **lswitch_id** | **str**|  | 

### Return type

[**LogicalSwitch**](LogicalSwitch.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

