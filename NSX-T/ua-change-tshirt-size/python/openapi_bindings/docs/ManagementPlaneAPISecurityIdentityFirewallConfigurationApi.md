# swagger_client.ManagementPlaneAPISecurityIdentityFirewallConfigurationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_enabled_compute_collection**](ManagementPlaneAPISecurityIdentityFirewallConfigurationApi.md#delete_enabled_compute_collection) | **DELETE** /idfw/idfw-compute-collections/{cc-ext-id} | Delete IDFW compute collection.
[**get_enabled_compute_collection**](ManagementPlaneAPISecurityIdentityFirewallConfigurationApi.md#get_enabled_compute_collection) | **GET** /idfw/idfw-compute-collections/{cc-ext-id} | Get IDFW compute collection.
[**get_master_switch_setting**](ManagementPlaneAPISecurityIdentityFirewallConfigurationApi.md#get_master_switch_setting) | **GET** /idfw/master-switch-setting | Get Identity Firewall master switch enabled/disabled
[**get_standalone_hosts_switch_setting**](ManagementPlaneAPISecurityIdentityFirewallConfigurationApi.md#get_standalone_hosts_switch_setting) | **GET** /idfw/standalone-host-switch-setting | Get Standalone hosts switch enabled/disabled
[**list_enabled_compute_collections**](ManagementPlaneAPISecurityIdentityFirewallConfigurationApi.md#list_enabled_compute_collections) | **GET** /idfw/idfw-compute-collections | List all Identity firewall compute collections
[**update_enabled_compute_collection**](ManagementPlaneAPISecurityIdentityFirewallConfigurationApi.md#update_enabled_compute_collection) | **PUT** /idfw/idfw-compute-collections/{cc-ext-id} | Update IDFW compute collection
[**update_master_switch_setting**](ManagementPlaneAPISecurityIdentityFirewallConfigurationApi.md#update_master_switch_setting) | **PUT** /idfw/master-switch-setting | Update IDFW master switch setting enabled/disabled
[**update_standalone_hosts_switch_setting**](ManagementPlaneAPISecurityIdentityFirewallConfigurationApi.md#update_standalone_hosts_switch_setting) | **PUT** /idfw/standalone-host-switch-setting | Update IDFW master switch setting enabled/disabled

# **delete_enabled_compute_collection**
> delete_enabled_compute_collection(cc_ext_id)

Delete IDFW compute collection.

Delete individual compute collections for IDFW. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallConfigurationApi(swagger_client.ApiClient(configuration))
cc_ext_id = 'cc_ext_id_example' # str | 

try:
    # Delete IDFW compute collection.
    api_instance.delete_enabled_compute_collection(cc_ext_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallConfigurationApi->delete_enabled_compute_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cc_ext_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enabled_compute_collection**
> IdfwEnabledComputeCollection get_enabled_compute_collection(cc_ext_id)

Get IDFW compute collection.

Get enable/disable status of individual compute collections for IDFW. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallConfigurationApi(swagger_client.ApiClient(configuration))
cc_ext_id = 'cc_ext_id_example' # str | 

try:
    # Get IDFW compute collection.
    api_response = api_instance.get_enabled_compute_collection(cc_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallConfigurationApi->get_enabled_compute_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cc_ext_id** | **str**|  | 

### Return type

[**IdfwEnabledComputeCollection**](IdfwEnabledComputeCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_master_switch_setting**
> IdfwMasterSwitchSetting get_master_switch_setting()

Get Identity Firewall master switch enabled/disabled

Fetches IDFW master switch setting to check whether master switch is enabled or disabled 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Get Identity Firewall master switch enabled/disabled
    api_response = api_instance.get_master_switch_setting()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallConfigurationApi->get_master_switch_setting: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdfwMasterSwitchSetting**](IdfwMasterSwitchSetting.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standalone_hosts_switch_setting**
> IdfwStandaloneHostsSwitchSetting get_standalone_hosts_switch_setting()

Get Standalone hosts switch enabled/disabled

Fetches IDFW standalone hosts switch setting to check whether standalone hosts is enabled or disabled 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Get Standalone hosts switch enabled/disabled
    api_response = api_instance.get_standalone_hosts_switch_setting()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallConfigurationApi->get_standalone_hosts_switch_setting: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdfwStandaloneHostsSwitchSetting**](IdfwStandaloneHostsSwitchSetting.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_enabled_compute_collections**
> IdfwEnabledComputeCollectionListResult list_enabled_compute_collections(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List all Identity firewall compute collections

List all Identity firewall compute collections. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallConfigurationApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List all Identity firewall compute collections
    api_response = api_instance.list_enabled_compute_collections(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallConfigurationApi->list_enabled_compute_collections: %s\n" % e)
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

[**IdfwEnabledComputeCollectionListResult**](IdfwEnabledComputeCollectionListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_enabled_compute_collection**
> IdfwEnabledComputeCollection update_enabled_compute_collection(body, cc_ext_id)

Update IDFW compute collection

Enable/disable individual compute collections for IDFW. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.IdfwEnabledComputeCollection() # IdfwEnabledComputeCollection | 
cc_ext_id = 'cc_ext_id_example' # str | 

try:
    # Update IDFW compute collection
    api_response = api_instance.update_enabled_compute_collection(body, cc_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallConfigurationApi->update_enabled_compute_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdfwEnabledComputeCollection**](IdfwEnabledComputeCollection.md)|  | 
 **cc_ext_id** | **str**|  | 

### Return type

[**IdfwEnabledComputeCollection**](IdfwEnabledComputeCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_master_switch_setting**
> IdfwMasterSwitchSetting update_master_switch_setting(body)

Update IDFW master switch setting enabled/disabled

Update Identity Firewall master switch setting (true=enabled / false=disabled). Identity Firewall master switch setting enables or disables Identity Firewall feature across the system.  It affects compute collections, hypervisor and virtual machines.  This operation is expensive and also has big impact and implication on system perforamce. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.IdfwMasterSwitchSetting() # IdfwMasterSwitchSetting | 

try:
    # Update IDFW master switch setting enabled/disabled
    api_response = api_instance.update_master_switch_setting(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallConfigurationApi->update_master_switch_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdfwMasterSwitchSetting**](IdfwMasterSwitchSetting.md)|  | 

### Return type

[**IdfwMasterSwitchSetting**](IdfwMasterSwitchSetting.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_standalone_hosts_switch_setting**
> IdfwStandaloneHostsSwitchSetting update_standalone_hosts_switch_setting(body)

Update IDFW master switch setting enabled/disabled

Update Identity Firewall standalone hosts switch setting (true=enabled / false=disabled). 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.IdfwStandaloneHostsSwitchSetting() # IdfwStandaloneHostsSwitchSetting | 

try:
    # Update IDFW master switch setting enabled/disabled
    api_response = api_instance.update_standalone_hosts_switch_setting(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallConfigurationApi->update_standalone_hosts_switch_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdfwStandaloneHostsSwitchSetting**](IdfwStandaloneHostsSwitchSetting.md)|  | 

### Return type

[**IdfwStandaloneHostsSwitchSetting**](IdfwStandaloneHostsSwitchSetting.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

