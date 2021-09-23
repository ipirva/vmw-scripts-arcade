# swagger_client.SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transport_node_profile**](SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi.md#create_transport_node_profile) | **POST** /transport-node-profiles | Create a Transport Node Profile
[**delete_transport_node_profile**](SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi.md#delete_transport_node_profile) | **DELETE** /transport-node-profiles/{transport-node-profile-id} | Delete a Transport Node Profile
[**get_transport_node_profile**](SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi.md#get_transport_node_profile) | **GET** /transport-node-profiles/{transport-node-profile-id} | Get a Transport Node
[**list_transport_node_profiles**](SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi.md#list_transport_node_profiles) | **GET** /transport-node-profiles | List Transport Nodes
[**update_transport_node_profile**](SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi.md#update_transport_node_profile) | **PUT** /transport-node-profiles/{transport-node-profile-id} | Update a Transport Node Profile

# **create_transport_node_profile**
> TransportNodeProfile create_transport_node_profile(body)

Create a Transport Node Profile

Transport node profile captures the configuration needed to create a transport node. A transport node profile can be attached to compute collections for automatic TN creation of member hosts. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportNodeProfile() # TransportNodeProfile | 

try:
    # Create a Transport Node Profile
    api_response = api_instance.create_transport_node_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi->create_transport_node_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportNodeProfile**](TransportNodeProfile.md)|  | 

### Return type

[**TransportNodeProfile**](TransportNodeProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transport_node_profile**
> delete_transport_node_profile(transport_node_profile_id)

Delete a Transport Node Profile

Deletes the specified transport node profile. A transport node profile can be deleted only when it is not attached to any compute collection. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi(swagger_client.ApiClient(configuration))
transport_node_profile_id = 'transport_node_profile_id_example' # str | 

try:
    # Delete a Transport Node Profile
    api_instance.delete_transport_node_profile(transport_node_profile_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi->delete_transport_node_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_profile**
> TransportNodeProfile get_transport_node_profile(transport_node_profile_id)

Get a Transport Node

Returns information about a specified transport node profile.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi(swagger_client.ApiClient(configuration))
transport_node_profile_id = 'transport_node_profile_id_example' # str | 

try:
    # Get a Transport Node
    api_response = api_instance.get_transport_node_profile(transport_node_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi->get_transport_node_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_profile_id** | **str**|  | 

### Return type

[**TransportNodeProfile**](TransportNodeProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_node_profiles**
> TransportNodeProfileListResult list_transport_node_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List Transport Nodes

Returns information about all transport node profiles. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List Transport Nodes
    api_response = api_instance.list_transport_node_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi->list_transport_node_profiles: %s\n" % e)
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

[**TransportNodeProfileListResult**](TransportNodeProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transport_node_profile**
> TransportNodeProfile update_transport_node_profile(body, transport_node_profile_id, esx_mgmt_if_migration_dest=esx_mgmt_if_migration_dest, if_id=if_id, ping_ip=ping_ip, skip_validation=skip_validation, vnic=vnic, vnic_migration_dest=vnic_migration_dest)

Update a Transport Node Profile

When configurations of a transport node profile(TNP) is updated, all the transport nodes in all the compute collections to which this TNP is attached are updated to reflect the updated configuration. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportNodeProfile() # TransportNodeProfile | 
transport_node_profile_id = 'transport_node_profile_id_example' # str | 
esx_mgmt_if_migration_dest = 'esx_mgmt_if_migration_dest_example' # str | The network ids to which the ESX vmk interfaces will be migrated (optional)
if_id = 'if_id_example' # str | The ESX vmk interfaces to migrate (optional)
ping_ip = 'ping_ip_example' # str | IP Addresses to ping right after ESX vmk interfaces were migrated. (optional)
skip_validation = false # bool | Whether to skip front-end validation for vmk/vnic/pnic migration (optional) (default to false)
vnic = 'vnic_example' # str | The ESX vmk interfaces and/or VM NIC to migrate (optional)
vnic_migration_dest = 'vnic_migration_dest_example' # str | The migration destinations of ESX vmk interfaces and/or VM NIC (optional)

try:
    # Update a Transport Node Profile
    api_response = api_instance.update_transport_node_profile(body, transport_node_profile_id, esx_mgmt_if_migration_dest=esx_mgmt_if_migration_dest, if_id=if_id, ping_ip=ping_ip, skip_validation=skip_validation, vnic=vnic, vnic_migration_dest=vnic_migration_dest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesTransportNodeProfilesApi->update_transport_node_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportNodeProfile**](TransportNodeProfile.md)|  | 
 **transport_node_profile_id** | **str**|  | 
 **esx_mgmt_if_migration_dest** | **str**| The network ids to which the ESX vmk interfaces will be migrated | [optional] 
 **if_id** | **str**| The ESX vmk interfaces to migrate | [optional] 
 **ping_ip** | **str**| IP Addresses to ping right after ESX vmk interfaces were migrated. | [optional] 
 **skip_validation** | **bool**| Whether to skip front-end validation for vmk/vnic/pnic migration | [optional] [default to false]
 **vnic** | **str**| The ESX vmk interfaces and/or VM NIC to migrate | [optional] 
 **vnic_migration_dest** | **str**| The migration destinations of ESX vmk interfaces and/or VM NIC | [optional] 

### Return type

[**TransportNodeProfile**](TransportNodeProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

