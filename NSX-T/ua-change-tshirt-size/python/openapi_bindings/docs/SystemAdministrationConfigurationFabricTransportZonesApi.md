# swagger_client.SystemAdministrationConfigurationFabricTransportZonesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transport_zone**](SystemAdministrationConfigurationFabricTransportZonesApi.md#create_transport_zone) | **POST** /transport-zones | Create a Transport Zone
[**delete_transport_zone**](SystemAdministrationConfigurationFabricTransportZonesApi.md#delete_transport_zone) | **DELETE** /transport-zones/{zone-id} | Delete a Transport Zone
[**get_all_transport_zone_status**](SystemAdministrationConfigurationFabricTransportZonesApi.md#get_all_transport_zone_status) | **GET** /transport-zones/status | Get high-level summary of a transport zone. The service layer does not support source &#x3D; realtime or cached.
[**get_heatmap_transport_zone_status**](SystemAdministrationConfigurationFabricTransportZonesApi.md#get_heatmap_transport_zone_status) | **GET** /transport-zones/{zone-id}/status | Get high-level summary of a transport zone
[**get_transport_zone**](SystemAdministrationConfigurationFabricTransportZonesApi.md#get_transport_zone) | **GET** /transport-zones/{zone-id} | Get a Transport Zone
[**get_transport_zone_status**](SystemAdministrationConfigurationFabricTransportZonesApi.md#get_transport_zone_status) | **GET** /transport-zones/{zone-id}/summary | Get a Transport Zone&#x27;s Current Runtime Status Information
[**list_transport_zones**](SystemAdministrationConfigurationFabricTransportZonesApi.md#list_transport_zones) | **GET** /transport-zones | List Transport Zones
[**update_transport_zone**](SystemAdministrationConfigurationFabricTransportZonesApi.md#update_transport_zone) | **PUT** /transport-zones/{zone-id} | Update a Transport Zone

# **create_transport_zone**
> TransportZone create_transport_zone(body)

Create a Transport Zone

Creates a new transport zone. The required parameters are host_switch_name and transport_type (OVERLAY or VLAN). The optional parameters are description and display_name. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricTransportZonesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportZone() # TransportZone | 

try:
    # Create a Transport Zone
    api_response = api_instance.create_transport_zone(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricTransportZonesApi->create_transport_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportZone**](TransportZone.md)|  | 

### Return type

[**TransportZone**](TransportZone.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transport_zone**
> delete_transport_zone(zone_id)

Delete a Transport Zone

Deletes an existing transport zone.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricTransportZonesApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | 

try:
    # Delete a Transport Zone
    api_instance.delete_transport_zone(zone_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricTransportZonesApi->delete_transport_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_transport_zone_status**
> HeatMapTransportNodesAggregateStatus get_all_transport_zone_status()

Get high-level summary of a transport zone. The service layer does not support source = realtime or cached.

Get high-level summary of a transport zone. The service layer does not support source = realtime or cached.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricTransportZonesApi(swagger_client.ApiClient(configuration))

try:
    # Get high-level summary of a transport zone. The service layer does not support source = realtime or cached.
    api_response = api_instance.get_all_transport_zone_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricTransportZonesApi->get_all_transport_zone_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HeatMapTransportNodesAggregateStatus**](HeatMapTransportNodesAggregateStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heatmap_transport_zone_status**
> HeatMapTransportZoneStatus get_heatmap_transport_zone_status(zone_id, source=source)

Get high-level summary of a transport zone

Get high-level summary of a transport zone

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricTransportZonesApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | ID of transport zone
source = 'source_example' # str | Data source type. (optional)

try:
    # Get high-level summary of a transport zone
    api_response = api_instance.get_heatmap_transport_zone_status(zone_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricTransportZonesApi->get_heatmap_transport_zone_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| ID of transport zone | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**HeatMapTransportZoneStatus**](HeatMapTransportZoneStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_zone**
> TransportZone get_transport_zone(zone_id)

Get a Transport Zone

Returns information about a single transport zone.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricTransportZonesApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | 

try:
    # Get a Transport Zone
    api_response = api_instance.get_transport_zone(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricTransportZonesApi->get_transport_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

[**TransportZone**](TransportZone.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_zone_status**
> TransportZoneStatus get_transport_zone_status(zone_id)

Get a Transport Zone's Current Runtime Status Information

Returns information about a specified transport zone, including the number of logical switches in the transport zone, number of logical spitch ports assigned to the transport zone, and number of transport nodes in the transport zone. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricTransportZonesApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | 

try:
    # Get a Transport Zone's Current Runtime Status Information
    api_response = api_instance.get_transport_zone_status(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricTransportZonesApi->get_transport_zone_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

[**TransportZoneStatus**](TransportZoneStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_zones**
> TransportZoneListResult list_transport_zones(cursor=cursor, include_system_owned=include_system_owned, included_fields=included_fields, is_default=is_default, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, transport_type=transport_type, uplink_teaming_policy_name=uplink_teaming_policy_name)

List Transport Zones

Returns information about configured transport zones. NSX requires at least one transport zone. NSX uses transport zones to provide connectivity based on the topology of the underlying network, trust zones, or organizational separations. For example, you might have hypervisors that use one network for management traffic and a different network for VM traffic. This architecture would require two transport zones. The combination of transport zones plus transport connectors enables NSX to form tunnels between hypervisors. Transport zones define which interfaces on the hypervisors can communicate with which other interfaces on other hypervisors to establish overlay tunnels or provide connectivity to a VLAN. A logical switch can be in one (and only one) transport zone. This means that all of a switch's interfaces must be in the same transport zone. However, each hypervisor virtual switch (OVS or VDS) has multiple interfaces (connectors), and each connector can be attached to a different logical switch. For example, on a single hypervisor with two connectors, connector A can be attached to logical switch 1 in transport zone A, while connector B is attached to logical switch 2 in transport zone B. In this way, a single hypervisor can participate in multiple transport zones. The API for creating a transport zone requires that a single host switch be specified for each transport zone, and multiple transport zones can share the same host switch. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricTransportZonesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
include_system_owned = false # bool | Filter to indicate whether to include system owned Transport Zones. (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
is_default = true # bool | Filter to choose if default transport zones will be returned (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
transport_type = 'transport_type_example' # str | Filter to choose the type of transport zones to return (optional)
uplink_teaming_policy_name = 'uplink_teaming_policy_name_example' # str | The transport zone's uplink teaming policy name (optional)

try:
    # List Transport Zones
    api_response = api_instance.list_transport_zones(cursor=cursor, include_system_owned=include_system_owned, included_fields=included_fields, is_default=is_default, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, transport_type=transport_type, uplink_teaming_policy_name=uplink_teaming_policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricTransportZonesApi->list_transport_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **include_system_owned** | **bool**| Filter to indicate whether to include system owned Transport Zones. | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **is_default** | **bool**| Filter to choose if default transport zones will be returned | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **transport_type** | **str**| Filter to choose the type of transport zones to return | [optional] 
 **uplink_teaming_policy_name** | **str**| The transport zone&#x27;s uplink teaming policy name | [optional] 

### Return type

[**TransportZoneListResult**](TransportZoneListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transport_zone**
> TransportZone update_transport_zone(body, zone_id)

Update a Transport Zone

Updates an existing transport zone. Modifiable parameters are is_default, description, and display_name. The request must include the existing host_switch_name. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricTransportZonesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportZone() # TransportZone | 
zone_id = 'zone_id_example' # str | 

try:
    # Update a Transport Zone
    api_response = api_instance.update_transport_zone(body, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricTransportZonesApi->update_transport_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportZone**](TransportZone.md)|  | 
 **zone_id** | **str**|  | 

### Return type

[**TransportZone**](TransportZone.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

