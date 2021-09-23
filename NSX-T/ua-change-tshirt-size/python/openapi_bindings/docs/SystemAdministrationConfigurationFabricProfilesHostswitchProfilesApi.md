# swagger_client.SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_host_switch_profile**](SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi.md#create_host_switch_profile) | **POST** /host-switch-profiles | Create a Hostswitch Profile
[**delete_host_switch_profile**](SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi.md#delete_host_switch_profile) | **DELETE** /host-switch-profiles/{host-switch-profile-id} | Delete a Hostswitch Profile
[**get_host_switch_profile**](SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi.md#get_host_switch_profile) | **GET** /host-switch-profiles/{host-switch-profile-id} | Get a Hostswitch Profile by ID
[**list_host_switch_profiles**](SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi.md#list_host_switch_profiles) | **GET** /host-switch-profiles | List Hostswitch Profiles
[**update_host_switch_profile**](SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi.md#update_host_switch_profile) | **PUT** /host-switch-profiles/{host-switch-profile-id} | Update a Hostswitch Profile

# **create_host_switch_profile**
> BaseHostSwitchProfile create_host_switch_profile(body)

Create a Hostswitch Profile

Creates a hostswitch profile. The resource_type is required. For uplink profiles, the teaming and policy parameters are required. By default, the mtu is 1600 and the transport_vlan is 0. The supported MTU range is 1280 through (uplink_mtu_threshold). (uplink_mtu_threshold) is 9000 by default. Range can be extended by modifying (uplink_mtu_threshold) in SwitchingGlobalConfig to the required upper threshold. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.BaseHostSwitchProfile() # BaseHostSwitchProfile | 

try:
    # Create a Hostswitch Profile
    api_response = api_instance.create_host_switch_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi->create_host_switch_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseHostSwitchProfile**](BaseHostSwitchProfile.md)|  | 

### Return type

[**BaseHostSwitchProfile**](BaseHostSwitchProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_host_switch_profile**
> delete_host_switch_profile(host_switch_profile_id)

Delete a Hostswitch Profile

Deletes a specified hostswitch profile.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi(swagger_client.ApiClient(configuration))
host_switch_profile_id = 'host_switch_profile_id_example' # str | 

try:
    # Delete a Hostswitch Profile
    api_instance.delete_host_switch_profile(host_switch_profile_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi->delete_host_switch_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_switch_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_switch_profile**
> BaseHostSwitchProfile get_host_switch_profile(host_switch_profile_id)

Get a Hostswitch Profile by ID

Returns information about a specified hostswitch profile.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi(swagger_client.ApiClient(configuration))
host_switch_profile_id = 'host_switch_profile_id_example' # str | 

try:
    # Get a Hostswitch Profile by ID
    api_response = api_instance.get_host_switch_profile(host_switch_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi->get_host_switch_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_switch_profile_id** | **str**|  | 

### Return type

[**BaseHostSwitchProfile**](BaseHostSwitchProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_host_switch_profiles**
> HostSwitchProfilesListResult list_host_switch_profiles(cursor=cursor, deployment_type=deployment_type, hostswitch_profile_type=hostswitch_profile_type, include_system_owned=include_system_owned, included_fields=included_fields, node_type=node_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, uplink_teaming_policy_name=uplink_teaming_policy_name)

List Hostswitch Profiles

Returns information about the configured hostswitch profiles. Hostswitch profiles define networking policies for hostswitches (sometimes referred to as bridges in OVS). Currently, only uplink teaming is supported. Uplink teaming allows NSX to load balance traffic across different physical NICs (PNICs) on the hypervisor hosts. Multiple teaming policies are supported, including LACP active, LACP passive, load balancing based on source ID, and failover order. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
deployment_type = 'deployment_type_example' # str | Supported edge deployment type. (optional)
hostswitch_profile_type = 'hostswitch_profile_type_example' # str | Supported HostSwitch profiles. (optional)
include_system_owned = false # bool | Whether the list result contains system resources (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
node_type = 'node_type_example' # str | Fabric node type for which uplink profiles are to be listed (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
uplink_teaming_policy_name = 'uplink_teaming_policy_name_example' # str | The host switch profile's uplink teaming policy name (optional)

try:
    # List Hostswitch Profiles
    api_response = api_instance.list_host_switch_profiles(cursor=cursor, deployment_type=deployment_type, hostswitch_profile_type=hostswitch_profile_type, include_system_owned=include_system_owned, included_fields=included_fields, node_type=node_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, uplink_teaming_policy_name=uplink_teaming_policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi->list_host_switch_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **deployment_type** | **str**| Supported edge deployment type. | [optional] 
 **hostswitch_profile_type** | **str**| Supported HostSwitch profiles. | [optional] 
 **include_system_owned** | **bool**| Whether the list result contains system resources | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **node_type** | **str**| Fabric node type for which uplink profiles are to be listed | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **uplink_teaming_policy_name** | **str**| The host switch profile&#x27;s uplink teaming policy name | [optional] 

### Return type

[**HostSwitchProfilesListResult**](HostSwitchProfilesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_host_switch_profile**
> BaseHostSwitchProfile update_host_switch_profile(body, host_switch_profile_id)

Update a Hostswitch Profile

Modifies a specified hostswitch profile. The body of the PUT request must include the resource_type. For uplink profiles, the put request must also include teaming parameters. Modifiable attributes include display_name, mtu, and transport_vlan. For uplink teaming policies, uplink_name and policy are also modifiable. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.BaseHostSwitchProfile() # BaseHostSwitchProfile | 
host_switch_profile_id = 'host_switch_profile_id_example' # str | 

try:
    # Update a Hostswitch Profile
    api_response = api_instance.update_host_switch_profile(body, host_switch_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricProfilesHostswitchProfilesApi->update_host_switch_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseHostSwitchProfile**](BaseHostSwitchProfile.md)|  | 
 **host_switch_profile_id** | **str**|  | 

### Return type

[**BaseHostSwitchProfile**](BaseHostSwitchProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

