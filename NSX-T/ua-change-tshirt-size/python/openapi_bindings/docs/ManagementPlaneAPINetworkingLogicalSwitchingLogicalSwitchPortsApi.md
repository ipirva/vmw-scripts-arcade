# swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_logical_port**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#create_logical_port) | **POST** /logical-ports | Create a Logical Port
[**create_switching_profile**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#create_switching_profile) | **POST** /switching-profiles | Create a Switching Profile
[**delete_logical_port**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#delete_logical_port) | **DELETE** /logical-ports/{lport-id} | Delete a Logical Port
[**delete_switching_profile**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#delete_switching_profile) | **DELETE** /switching-profiles/{switching-profile-id} | Delete a Switching Profile
[**get_logical_port**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#get_logical_port) | **GET** /logical-ports/{lport-id} | Get Information About a Logical Port
[**get_logical_port_mac_table**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#get_logical_port_mac_table) | **GET** /logical-ports/{lport-id}/mac-table | Get MAC table of a logical port with a given port id (lport-id)
[**get_logical_port_mac_table_in_csv_format_csv**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#get_logical_port_mac_table_in_csv_format_csv) | **GET** /logical-ports/{lport-id}/mac-table?format&#x3D;csv | Get MAC table of a logical port with a given port id (lport-id)
[**get_logical_port_operational_status**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#get_logical_port_operational_status) | **GET** /logical-ports/{lport-id}/status | Get Operational Status for Logical Port of a Given Port ID (lport-id)
[**get_logical_port_state**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#get_logical_port_state) | **GET** /logical-ports/{lport-id}/state | Get realized state &amp; location of a logical port
[**get_logical_port_statistics**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#get_logical_port_statistics) | **GET** /logical-ports/{lport-id}/statistics | Get Statistics for Logical Port of a Given Port ID (lport-id)
[**get_logical_port_status_summary**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#get_logical_port_status_summary) | **GET** /logical-ports/status | Get Operational Status Summary of All Logical Ports in the System
[**get_switching_profile**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#get_switching_profile) | **GET** /switching-profiles/{switching-profile-id} | Get Switching Profile by ID
[**get_switching_profile_status**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#get_switching_profile_status) | **GET** /switching-profiles/{switching-profile-id}/summary | Get Counts of Ports and Switches Using This Switching Profile
[**list_logical_ports**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#list_logical_ports) | **GET** /logical-ports | List All Logical Ports
[**list_switching_profiles**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#list_switching_profiles) | **GET** /switching-profiles | List Switching Profiles
[**update_logical_port**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#update_logical_port) | **PUT** /logical-ports/{lport-id} | Update a Logical Port
[**update_switching_profile**](ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi.md#update_switching_profile) | **PUT** /switching-profiles/{switching-profile-id} | Update a Switching Profile

# **create_logical_port**
> LogicalPort create_logical_port(body)

Create a Logical Port

Creates a new logical switch port. The required parameters are the associated logical_switch_id and admin_state (UP or DOWN). Optional parameters are the attachment and switching_profile_ids. If you don't specify switching_profile_ids, default switching profiles are assigned to the port. If you don't specify an attachment, the switch port remains empty. To configure an attachment, you must specify an id, and optionally you can specify an attachment_type (VIF or LOGICALROUTER). The attachment_type is VIF by default. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LogicalPort() # LogicalPort | 

try:
    # Create a Logical Port
    api_response = api_instance.create_logical_port(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->create_logical_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogicalPort**](LogicalPort.md)|  | 

### Return type

[**LogicalPort**](LogicalPort.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_switching_profile**
> BaseSwitchingProfile create_switching_profile(body)

Create a Switching Profile

Creates a new, custom qos, port-mirroring, spoof-guard or port-security switching profile. You can override their default switching profile assignments by creating a new switching profile and assigning it to one or more logical switches. You cannot override the default ipfix or ip_discovery switching profiles. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BaseSwitchingProfile() # BaseSwitchingProfile | 

try:
    # Create a Switching Profile
    api_response = api_instance.create_switching_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->create_switching_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseSwitchingProfile**](BaseSwitchingProfile.md)|  | 

### Return type

[**BaseSwitchingProfile**](BaseSwitchingProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_logical_port**
> delete_logical_port(lport_id, detach=detach)

Delete a Logical Port

Deletes the specified logical switch port. By default, if logical port has attachments, or it is added to any NSGroup, the deletion will be failed. Option detach could be used for deleting logical port forcibly. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
lport_id = 'lport_id_example' # str | 
detach = false # bool | force delete even if attached or referenced by a group (optional) (default to false)

try:
    # Delete a Logical Port
    api_instance.delete_logical_port(lport_id, detach=detach)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->delete_logical_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lport_id** | **str**|  | 
 **detach** | **bool**| force delete even if attached or referenced by a group | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_switching_profile**
> delete_switching_profile(switching_profile_id, unbind=unbind)

Delete a Switching Profile

Deletes the specified switching profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
switching_profile_id = 'switching_profile_id_example' # str | 
unbind = false # bool | force unbinding of logical switches and ports from a switching profile (optional) (default to false)

try:
    # Delete a Switching Profile
    api_instance.delete_switching_profile(switching_profile_id, unbind=unbind)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->delete_switching_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switching_profile_id** | **str**|  | 
 **unbind** | **bool**| force unbinding of logical switches and ports from a switching profile | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_port**
> LogicalPort get_logical_port(lport_id)

Get Information About a Logical Port

Returns information about a specified logical port.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
lport_id = 'lport_id_example' # str | 

try:
    # Get Information About a Logical Port
    api_response = api_instance.get_logical_port(lport_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->get_logical_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lport_id** | **str**|  | 

### Return type

[**LogicalPort**](LogicalPort.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_port_mac_table**
> LogicalPortMacAddressListResult get_logical_port_mac_table(lport_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, transport_node_id=transport_node_id)

Get MAC table of a logical port with a given port id (lport-id)

Returns MAC table of a specified logical port. If the target transport node id is not provided, the NSX manager will ask the controller for the transport node where the logical port is located. The query parameter \"source=cached\" is not supported. MAC table retrieval is not supported on logical ports that are attached to a logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
lport_id = 'lport_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
transport_node_id = 'transport_node_id_example' # str | TransportNode Id (optional)

try:
    # Get MAC table of a logical port with a given port id (lport-id)
    api_response = api_instance.get_logical_port_mac_table(lport_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, transport_node_id=transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->get_logical_port_mac_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lport_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **transport_node_id** | **str**| TransportNode Id | [optional] 

### Return type

[**LogicalPortMacAddressListResult**](LogicalPortMacAddressListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_port_mac_table_in_csv_format_csv**
> LogicalPortMacAddressCsvListResult get_logical_port_mac_table_in_csv_format_csv(lport_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, transport_node_id=transport_node_id)

Get MAC table of a logical port with a given port id (lport-id)

Returns MAC table in CSV format of a specified logical port. If the target transport node id is not provided, the NSX manager will ask the controller for the transport node where the logical port is located. The query parameter \"source=cached\" is not supported. MAC table retrieval is not supported on logical ports that are attached to a logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
lport_id = 'lport_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
transport_node_id = 'transport_node_id_example' # str | TransportNode Id (optional)

try:
    # Get MAC table of a logical port with a given port id (lport-id)
    api_response = api_instance.get_logical_port_mac_table_in_csv_format_csv(lport_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, transport_node_id=transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->get_logical_port_mac_table_in_csv_format_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lport_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **transport_node_id** | **str**| TransportNode Id | [optional] 

### Return type

[**LogicalPortMacAddressCsvListResult**](LogicalPortMacAddressCsvListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_port_operational_status**
> LogicalPortOperationalStatus get_logical_port_operational_status(lport_id, source=source)

Get Operational Status for Logical Port of a Given Port ID (lport-id)

Returns operational status of a specified logical port.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
lport_id = 'lport_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get Operational Status for Logical Port of a Given Port ID (lport-id)
    api_response = api_instance.get_logical_port_operational_status(lport_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->get_logical_port_operational_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lport_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LogicalPortOperationalStatus**](LogicalPortOperationalStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_port_state**
> LogicalPortState get_logical_port_state(lport_id)

Get realized state & location of a logical port

Returns transport node id for a specified logical port. Also returns information about all address bindings of the specified logical port. This includes address bindings discovered via various snooping methods like ARP snooping, DHCP snooping etc. and addressing bindings that are realized based on user configuration. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
lport_id = 'lport_id_example' # str | 

try:
    # Get realized state & location of a logical port
    api_response = api_instance.get_logical_port_state(lport_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->get_logical_port_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lport_id** | **str**|  | 

### Return type

[**LogicalPortState**](LogicalPortState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_port_statistics**
> LogicalPortStatistics get_logical_port_statistics(lport_id, source=source)

Get Statistics for Logical Port of a Given Port ID (lport-id)

Returns statistics of a specified logical port. If the logical port is attached to a logical router port, query parameter \"source=realtime\" is not supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
lport_id = 'lport_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get Statistics for Logical Port of a Given Port ID (lport-id)
    api_response = api_instance.get_logical_port_statistics(lport_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->get_logical_port_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lport_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LogicalPortStatistics**](LogicalPortStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_port_status_summary**
> LogicalPortStatusSummary get_logical_port_status_summary(attachment_id=attachment_id, attachment_type=attachment_type, bridge_cluster_id=bridge_cluster_id, container_ports_only=container_ports_only, cursor=cursor, diagnostic=diagnostic, included_fields=included_fields, logical_switch_id=logical_switch_id, page_size=page_size, parent_vif_id=parent_vif_id, sort_ascending=sort_ascending, sort_by=sort_by, source=source, switching_profile_id=switching_profile_id, transport_node_id=transport_node_id, transport_zone_id=transport_zone_id)

Get Operational Status Summary of All Logical Ports in the System

Returns operational status of all logical ports. The query parameter \"source=realtime\" is not supported. Pagination is not supported for this API. The query parameters \"cursor\", \"sort_ascending\", \"sort_by\", \"page_size\" and \"included_fields\" will be ignored. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
attachment_id = 'attachment_id_example' # str | Logical Port attachment Id (optional)
attachment_type = 'attachment_type_example' # str | Type of attachment for logical port; for query only. (optional)
bridge_cluster_id = 'bridge_cluster_id_example' # str | Bridge Cluster identifier (optional)
container_ports_only = false # bool | Only container VIF logical ports will be returned if true (optional) (default to false)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
diagnostic = false # bool | Flag to enable showing of transit logical port. (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
logical_switch_id = 'logical_switch_id_example' # str | Logical Switch identifier (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
parent_vif_id = 'parent_vif_id_example' # str | ID of the VIF of type PARENT (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
switching_profile_id = 'switching_profile_id_example' # str | Network Profile identifier (optional)
transport_node_id = 'transport_node_id_example' # str | Transport node identifier (optional)
transport_zone_id = 'transport_zone_id_example' # str | Transport zone identifier (optional)

try:
    # Get Operational Status Summary of All Logical Ports in the System
    api_response = api_instance.get_logical_port_status_summary(attachment_id=attachment_id, attachment_type=attachment_type, bridge_cluster_id=bridge_cluster_id, container_ports_only=container_ports_only, cursor=cursor, diagnostic=diagnostic, included_fields=included_fields, logical_switch_id=logical_switch_id, page_size=page_size, parent_vif_id=parent_vif_id, sort_ascending=sort_ascending, sort_by=sort_by, source=source, switching_profile_id=switching_profile_id, transport_node_id=transport_node_id, transport_zone_id=transport_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->get_logical_port_status_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Logical Port attachment Id | [optional] 
 **attachment_type** | **str**| Type of attachment for logical port; for query only. | [optional] 
 **bridge_cluster_id** | **str**| Bridge Cluster identifier | [optional] 
 **container_ports_only** | **bool**| Only container VIF logical ports will be returned if true | [optional] [default to false]
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **diagnostic** | **bool**| Flag to enable showing of transit logical port. | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **logical_switch_id** | **str**| Logical Switch identifier | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **parent_vif_id** | **str**| ID of the VIF of type PARENT | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **switching_profile_id** | **str**| Network Profile identifier | [optional] 
 **transport_node_id** | **str**| Transport node identifier | [optional] 
 **transport_zone_id** | **str**| Transport zone identifier | [optional] 

### Return type

[**LogicalPortStatusSummary**](LogicalPortStatusSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_switching_profile**
> BaseSwitchingProfile get_switching_profile(switching_profile_id)

Get Switching Profile by ID

Returns information about a specified switching profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
switching_profile_id = 'switching_profile_id_example' # str | 

try:
    # Get Switching Profile by ID
    api_response = api_instance.get_switching_profile(switching_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->get_switching_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switching_profile_id** | **str**|  | 

### Return type

[**BaseSwitchingProfile**](BaseSwitchingProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_switching_profile_status**
> SwitchingProfileStatus get_switching_profile_status(switching_profile_id)

Get Counts of Ports and Switches Using This Switching Profile

Get Counts of Ports and Switches Using This Switching Profile

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
switching_profile_id = 'switching_profile_id_example' # str | 

try:
    # Get Counts of Ports and Switches Using This Switching Profile
    api_response = api_instance.get_switching_profile_status(switching_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->get_switching_profile_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switching_profile_id** | **str**|  | 

### Return type

[**SwitchingProfileStatus**](SwitchingProfileStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_logical_ports**
> LogicalPortListResult list_logical_ports(attachment_id=attachment_id, attachment_type=attachment_type, bridge_cluster_id=bridge_cluster_id, container_ports_only=container_ports_only, cursor=cursor, diagnostic=diagnostic, included_fields=included_fields, logical_switch_id=logical_switch_id, page_size=page_size, parent_vif_id=parent_vif_id, sort_ascending=sort_ascending, sort_by=sort_by, switching_profile_id=switching_profile_id, transport_node_id=transport_node_id, transport_zone_id=transport_zone_id)

List All Logical Ports

Returns information about all configured logical switch ports. Logical switch ports connect to VM virtual network interface cards (NICs). Each logical port is associated with one logical switch. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
attachment_id = 'attachment_id_example' # str | Logical Port attachment Id (optional)
attachment_type = 'attachment_type_example' # str | Type of attachment for logical port; for query only. (optional)
bridge_cluster_id = 'bridge_cluster_id_example' # str | Bridge Cluster identifier (optional)
container_ports_only = false # bool | Only container VIF logical ports will be returned if true (optional) (default to false)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
diagnostic = false # bool | Flag to enable showing of transit logical port. (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
logical_switch_id = 'logical_switch_id_example' # str | Logical Switch identifier (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
parent_vif_id = 'parent_vif_id_example' # str | ID of the VIF of type PARENT (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
switching_profile_id = 'switching_profile_id_example' # str | Network Profile identifier (optional)
transport_node_id = 'transport_node_id_example' # str | Transport node identifier (optional)
transport_zone_id = 'transport_zone_id_example' # str | Transport zone identifier (optional)

try:
    # List All Logical Ports
    api_response = api_instance.list_logical_ports(attachment_id=attachment_id, attachment_type=attachment_type, bridge_cluster_id=bridge_cluster_id, container_ports_only=container_ports_only, cursor=cursor, diagnostic=diagnostic, included_fields=included_fields, logical_switch_id=logical_switch_id, page_size=page_size, parent_vif_id=parent_vif_id, sort_ascending=sort_ascending, sort_by=sort_by, switching_profile_id=switching_profile_id, transport_node_id=transport_node_id, transport_zone_id=transport_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->list_logical_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Logical Port attachment Id | [optional] 
 **attachment_type** | **str**| Type of attachment for logical port; for query only. | [optional] 
 **bridge_cluster_id** | **str**| Bridge Cluster identifier | [optional] 
 **container_ports_only** | **bool**| Only container VIF logical ports will be returned if true | [optional] [default to false]
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **diagnostic** | **bool**| Flag to enable showing of transit logical port. | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **logical_switch_id** | **str**| Logical Switch identifier | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **parent_vif_id** | **str**| ID of the VIF of type PARENT | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **switching_profile_id** | **str**| Network Profile identifier | [optional] 
 **transport_node_id** | **str**| Transport node identifier | [optional] 
 **transport_zone_id** | **str**| Transport zone identifier | [optional] 

### Return type

[**LogicalPortListResult**](LogicalPortListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_switching_profiles**
> SwitchingProfilesListResult list_switching_profiles(cursor=cursor, include_system_owned=include_system_owned, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, switching_profile_type=switching_profile_type)

List Switching Profiles

Returns information about the system-default and user-configured switching profiles. Each switching profile has a unique ID, a display name, and various other read-only and configurable properties. The default switching profiles are assigned automatically to each switch. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
include_system_owned = false # bool | Whether the list result contains system resources (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
switching_profile_type = 'switching_profile_type_example' # str | comma-separated list of switching profile types, e.g. ?switching_profile_type=QosSwitchingProfile,IpDiscoverySwitchingProfile (optional)

try:
    # List Switching Profiles
    api_response = api_instance.list_switching_profiles(cursor=cursor, include_system_owned=include_system_owned, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, switching_profile_type=switching_profile_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->list_switching_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **include_system_owned** | **bool**| Whether the list result contains system resources | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **switching_profile_type** | **str**| comma-separated list of switching profile types, e.g. ?switching_profile_type&#x3D;QosSwitchingProfile,IpDiscoverySwitchingProfile | [optional] 

### Return type

[**SwitchingProfilesListResult**](SwitchingProfilesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_logical_port**
> LogicalPort update_logical_port(body, lport_id)

Update a Logical Port

Modifies an existing logical switch port. Parameters that can be modified include attachment_type (LOGICALROUTER, VIF), admin_state (UP or DOWN), attachment id and switching_profile_ids. You cannot modify the logical_switch_id. In other words, you cannot move an existing port from one switch to another switch. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LogicalPort() # LogicalPort | 
lport_id = 'lport_id_example' # str | 

try:
    # Update a Logical Port
    api_response = api_instance.update_logical_port(body, lport_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->update_logical_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogicalPort**](LogicalPort.md)|  | 
 **lport_id** | **str**|  | 

### Return type

[**LogicalPort**](LogicalPort.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_switching_profile**
> BaseSwitchingProfile update_switching_profile(body, switching_profile_id)

Update a Switching Profile

Updates the user-configurable parameters of a switching profile. Only the qos, port-mirroring, spoof-guard and port-security switching profiles can be modified. You cannot modify the ipfix or ip-discovery switching profiles. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BaseSwitchingProfile() # BaseSwitchingProfile | 
switching_profile_id = 'switching_profile_id_example' # str | 

try:
    # Update a Switching Profile
    api_response = api_instance.update_switching_profile(body, switching_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi->update_switching_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseSwitchingProfile**](BaseSwitchingProfile.md)|  | 
 **switching_profile_id** | **str**|  | 

### Return type

[**BaseSwitchingProfile**](BaseSwitchingProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

