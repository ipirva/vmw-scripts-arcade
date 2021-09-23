# swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_or_remove_ns_group_expression**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#add_or_remove_ns_group_expression) | **POST** /ns-groups/{ns-group-id} | Add NSGroup expression
[**create_ns_group**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#create_ns_group) | **POST** /ns-groups | Create NSGroup
[**create_ns_profile**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#create_ns_profile) | **POST** /ns-profiles | Create NSProfile
[**delete_ns_group**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#delete_ns_group) | **DELETE** /ns-groups/{ns-group-id} | Delete NSGroup
[**get_consolidated_effective_ip_address_members**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_consolidated_effective_ip_address_members) | **GET** /ns-groups/{ns-group-id}/consolidated-effective-ip-address-members | Get consolidated Effective IPAddress translated from the NSGroup
[**get_effective_active_directory_groups**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_effective_active_directory_groups) | **GET** /ns-groups/{ns-group-id}/effective-directory-group-members | Get Effective Directory Groups of the specified NSGroup.
[**get_effective_cloud_native_service_instances**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_effective_cloud_native_service_instances) | **GET** /ns-groups/{ns-group-id}/effective-cloud-native-service-instance-members | Get Effective Cloud Native Service Instances of the specified NSGroup.
[**get_effective_ip_address_members**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_effective_ip_address_members) | **GET** /ns-groups/{ns-group-id}/effective-ip-address-members | Get Effective IPAddress translated from the NSGroup
[**get_effective_ip_set_members**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_effective_ip_set_members) | **GET** /ns-groups/{ns-group-id}/effective-ipset-members | Get Effective IPSets of the specified NSGroup.
[**get_effective_logical_port_members**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_effective_logical_port_members) | **GET** /ns-groups/{ns-group-id}/effective-logical-port-members | Get Effective Logical Ports translated from the NSgroup
[**get_effective_logical_switch_members**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_effective_logical_switch_members) | **GET** /ns-groups/{ns-group-id}/effective-logical-switch-members | Get Effective switch members translated from the NSGroup
[**get_effective_physical_server_members**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_effective_physical_server_members) | **GET** /ns-groups/{ns-group-id}/effective-physical-server-members | Get Effective Physical Server Memebers of the specified NSGroup.
[**get_effective_transport_node_members**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_effective_transport_node_members) | **GET** /ns-groups/{ns-group-id}/effective-transport-node-members | Get effective transport node members translated from the NSGroup
[**get_effective_vif_members**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_effective_vif_members) | **GET** /ns-groups/{ns-group-id}/effective-vif-members | Get effective VIF members translated from the NSGroup
[**get_effective_virtual_machine_members**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_effective_virtual_machine_members) | **GET** /ns-groups/{ns-group-id}/effective-virtual-machine-members | Get Effective Virtual Machine members of the specified NSGroup.
[**get_member_types**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_member_types) | **GET** /ns-groups/{ns-group-id}/member-types | Get member types from NSGroup
[**get_service_associations**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_service_associations) | **GET** /ns-groups/{nsgroup-id}/service-associations | Get services to which the given nsgroup belongs to 
[**get_unassociated_virtual_machines**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#get_unassociated_virtual_machines) | **GET** /ns-groups/unassociated-virtual-machines | Get the list of all the virtual machines that are not a part of any existing NSGroup.
[**list_ns_groups**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#list_ns_groups) | **GET** /ns-groups | List NSGroups
[**read_ns_group**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#read_ns_group) | **GET** /ns-groups/{ns-group-id} | Read NSGroup
[**update_ns_group**](ManagementPlaneAPIGroupingObjectsNSGroupsApi.md#update_ns_group) | **PUT** /ns-groups/{ns-group-id} | Update NSGroup

# **add_or_remove_ns_group_expression**
> NSGroup add_or_remove_ns_group_expression(body, action, ns_group_id)

Add NSGroup expression

Add/remove the expressions passed in the request body to/from the NSGroup 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.NSGroupExpressionList() # NSGroupExpressionList | 
action = 'action_example' # str | Specifies addition or removal action
ns_group_id = 'ns_group_id_example' # str | NSGroup Id

try:
    # Add NSGroup expression
    api_response = api_instance.add_or_remove_ns_group_expression(body, action, ns_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->add_or_remove_ns_group_expression: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NSGroupExpressionList**](NSGroupExpressionList.md)|  | 
 **action** | **str**| Specifies addition or removal action | 
 **ns_group_id** | **str**| NSGroup Id | 

### Return type

[**NSGroup**](NSGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ns_group**
> NSGroup create_ns_group(body)

Create NSGroup

Creates a new NSGroup that can group NSX resources - VIFs, Lports and LSwitches as well as the grouping objects - IPSet, MACSet and other NSGroups. For NSGroups containing VM criteria(both static and dynamic), system VMs will not be included as members. This filter applies at VM level only. Exceptions are as follows: 1. LogicalPorts and VNI of System VMs will be included in NSGroup if the criteria  is based on LogicalPort, LogicalSwitch or VNI directly. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.NSGroup() # NSGroup | 

try:
    # Create NSGroup
    api_response = api_instance.create_ns_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->create_ns_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NSGroup**](NSGroup.md)|  | 

### Return type

[**NSGroup**](NSGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ns_profile**
> NSProfile create_ns_profile(body)

Create NSProfile

Creates a new NSProfile which allows users to encapsulate attribute and sub-attributes of network services. Rules for using attributes and sub-attributes in single NSProfile 1. One type of attribute can't have multiple occurrences. ( Example -  Attribute type APP_ID can be used only once per NSProfile.) 2. Values for an attribute are mentioned as array of strings.  ( Example - For type APP_ID , values can be mentioned as [\"SSL\",\"FTP\"].) 3. If sub-attribtes are mentioned for an attribute, then only single  value is allowed for that attribute. 4. To get a list of supported  attributes and sub-attributes fire the following REST API  GET https://&lt;nsx-mgr&gt;/api/v1/ns-profiles/attributes 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.NSProfile() # NSProfile | 

try:
    # Create NSProfile
    api_response = api_instance.create_ns_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->create_ns_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NSProfile**](NSProfile.md)|  | 

### Return type

[**NSProfile**](NSProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ns_group**
> delete_ns_group(ns_group_id, force=force)

Delete NSGroup

Deletes the specified NSGroup. By default, if the NSGroup is added to another NSGroup, it won't be deleted. In such situations, pass \"force=true\" as query param to force delete the NSGroup. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete NSGroup
    api_instance.delete_ns_group(ns_group_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->delete_ns_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consolidated_effective_ip_address_members**
> ConsolidatedEffectiveIPAddressMemberListResult get_consolidated_effective_ip_address_members(ns_group_id, cursor=cursor, included_fields=included_fields, ip_filter=ip_filter, page_size=page_size, site_id=site_id, sort_ascending=sort_ascending, sort_by=sort_by)

Get consolidated Effective IPAddress translated from the NSGroup

Returns consolidated effective ip address members of the specified NSGroup. Applicable in case of federated environment. The response contains site-wise list of consolidated effective IP address members. In the response, for the local-site, the list will contain static and dynamicaly translated IPs. For the remote sites, the list will contain only the dynamically translated IPs. The static IPs will not be seen in the response of this API. Hence, user can refer to the local-site Ip response in the API results or the group definition to see the static IP membership of the Group. This API is applicable only for NSGroups containing either VirtualMachine, VIF, LogicalSwitch, LogicalPort or IPSet member type. For NSGroups containing other member types,it returns an empty list. Use the cursor value in the response to fetch the next page. If there is no cursor value for a response, it implies the last page in the results for the query. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
ip_filter = 'ip_filter_example' # str | IP address, range, or subnet (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
site_id = 'site_id_example' # str | UUID of the site from which the effective IP addresses are to be fetched  (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get consolidated Effective IPAddress translated from the NSGroup
    api_response = api_instance.get_consolidated_effective_ip_address_members(ns_group_id, cursor=cursor, included_fields=included_fields, ip_filter=ip_filter, page_size=page_size, site_id=site_id, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_consolidated_effective_ip_address_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **ip_filter** | **str**| IP address, range, or subnet | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **site_id** | **str**| UUID of the site from which the effective IP addresses are to be fetched  | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ConsolidatedEffectiveIPAddressMemberListResult**](ConsolidatedEffectiveIPAddressMemberListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_active_directory_groups**
> EffectiveMemberResourceListResult get_effective_active_directory_groups(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get Effective Directory Groups of the specified NSGroup.

Returns effective directory groups which are members of the specified NSGroup. This API is applicable only for NSGroups containing DirectoryGroup member type. For NSGroups containing other member types,it returns an empty list. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get Effective Directory Groups of the specified NSGroup.
    api_response = api_instance.get_effective_active_directory_groups(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_effective_active_directory_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**EffectiveMemberResourceListResult**](EffectiveMemberResourceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_cloud_native_service_instances**
> EffectiveMemberResourceListResult get_effective_cloud_native_service_instances(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get Effective Cloud Native Service Instances of the specified NSGroup.

Returns effective cloud native service instances of the specified NSGroup. This API is applicable only for NSGroups containing CloudNativeServiceInstance member type. For NSGroups containing other member types,it returns an empty list. target_id in response is external_id of CloudNativeServiceInstance 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get Effective Cloud Native Service Instances of the specified NSGroup.
    api_response = api_instance.get_effective_cloud_native_service_instances(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_effective_cloud_native_service_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**EffectiveMemberResourceListResult**](EffectiveMemberResourceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_ip_address_members**
> EffectiveIPAddressMemberListResult get_effective_ip_address_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get Effective IPAddress translated from the NSGroup

Returns effective ip address members of the specified NSGroup. This API is applicable only for NSGroups containing either VirtualMachine, VIF, LogicalSwitch, LogicalPort or IPSet member type. For NSGroups containing other member types,it returns an empty list. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get Effective IPAddress translated from the NSGroup
    api_response = api_instance.get_effective_ip_address_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_effective_ip_address_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**EffectiveIPAddressMemberListResult**](EffectiveIPAddressMemberListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_ip_set_members**
> EffectiveMemberResourceListResult get_effective_ip_set_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get Effective IPSets of the specified NSGroup.

Returns effective IPSets which are members of the specified NSGroup. This API is applicable only for NSGroups containing IPSet member type. For NSGroups containing other member types,it returns an empty list. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get Effective IPSets of the specified NSGroup.
    api_response = api_instance.get_effective_ip_set_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_effective_ip_set_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**EffectiveMemberResourceListResult**](EffectiveMemberResourceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_logical_port_members**
> EffectiveMemberResourceListResult get_effective_logical_port_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get Effective Logical Ports translated from the NSgroup

Returns effective logical port members of the specified NSGroup. This API is applicable only for NSGroups containing either VirtualMachines, LogicalSwitch or LogicalPort member types.For NSGroups containing other member types,it returns an empty list. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get Effective Logical Ports translated from the NSgroup
    api_response = api_instance.get_effective_logical_port_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_effective_logical_port_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**EffectiveMemberResourceListResult**](EffectiveMemberResourceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_logical_switch_members**
> EffectiveMemberResourceListResult get_effective_logical_switch_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get Effective switch members translated from the NSGroup

Returns effective logical switch members of the specified NSGroup. This API is applicable for NSGroups containing LogicalSwitch members. For NSGroups containing other member types,it returns an empty list. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get Effective switch members translated from the NSGroup
    api_response = api_instance.get_effective_logical_switch_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_effective_logical_switch_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**EffectiveMemberResourceListResult**](EffectiveMemberResourceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_physical_server_members**
> EffectiveMemberResourceListResult get_effective_physical_server_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get Effective Physical Server Memebers of the specified NSGroup.

Returns effective physical server members of the specified NSGroup. This API is applicable only for NSGroups containing Physical Server member type. For NSGroups containing other member types,it returns an empty list. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get Effective Physical Server Memebers of the specified NSGroup.
    api_response = api_instance.get_effective_physical_server_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_effective_physical_server_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**EffectiveMemberResourceListResult**](EffectiveMemberResourceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_transport_node_members**
> EffectiveMemberResourceListResult get_effective_transport_node_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get effective transport node members translated from the NSGroup

Returns effective transport node members of the specified NSGroup. This API is applicable only for NSGroups containing TransportNode member type. For NSGroups containing other member types,it returns an empty list. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get effective transport node members translated from the NSGroup
    api_response = api_instance.get_effective_transport_node_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_effective_transport_node_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**EffectiveMemberResourceListResult**](EffectiveMemberResourceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_vif_members**
> VirtualNetworkInterfaceListResult get_effective_vif_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get effective VIF members translated from the NSGroup

Returns effective VIF members of the specified NSGroup. This API is applicable only for NSGroups containing either VirtualMachines or VIF member type. For NSGroups containing other member types,it returns an empty list. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get effective VIF members translated from the NSGroup
    api_response = api_instance.get_effective_vif_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_effective_vif_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**VirtualNetworkInterfaceListResult**](VirtualNetworkInterfaceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_effective_virtual_machine_members**
> VirtualMachineListResult get_effective_virtual_machine_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get Effective Virtual Machine members of the specified NSGroup.

Returns effective virtual machine members of the specified NSGroup. This API is applicable only for NSGroups containing VirtualMachine member type. For NSGroups containing other member types,it returns an empty list. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get Effective Virtual Machine members of the specified NSGroup.
    api_response = api_instance.get_effective_virtual_machine_members(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_effective_virtual_machine_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**VirtualMachineListResult**](VirtualMachineListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_types**
> EffectiveMemberTypeListResult get_member_types(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get member types from NSGroup

Returns member types for a specified NSGroup including child NSGroups. This considers static members and members added via membership criteria only 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get member types from NSGroup
    api_response = api_instance.get_member_types(ns_group_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_member_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**EffectiveMemberTypeListResult**](EffectiveMemberTypeListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_associations**
> ServiceAssociationListResult get_service_associations(nsgroup_id, service_type, cursor=cursor, fetch_parentgroup_associations=fetch_parentgroup_associations, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get services to which the given nsgroup belongs to 

Returns information about services that are associated with the given NSGroup. The service name is passed by service_type parameter 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
nsgroup_id = 'nsgroup_id_example' # str | 
service_type = 'service_type_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
fetch_parentgroup_associations = false # bool | Fetch complete list of associated resources considering nesting  (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get services to which the given nsgroup belongs to 
    api_response = api_instance.get_service_associations(nsgroup_id, service_type, cursor=cursor, fetch_parentgroup_associations=fetch_parentgroup_associations, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_service_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nsgroup_id** | **str**|  | 
 **service_type** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **fetch_parentgroup_associations** | **bool**| Fetch complete list of associated resources considering nesting  | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ServiceAssociationListResult**](ServiceAssociationListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unassociated_virtual_machines**
> UnassociatedVMListResult get_unassociated_virtual_machines(cursor=cursor, display_name=display_name, external_id=external_id, host_id=host_id, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get the list of all the virtual machines that are not a part of any existing NSGroup.

Get the list of all the virtual machines that are not a part of any existing NSGroup. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
display_name = 'display_name_example' # str | Display Name of the virtual machine (optional)
external_id = 'external_id_example' # str | External id of the virtual machine (optional)
host_id = 'host_id_example' # str | Id of the host where this vif is located (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get the list of all the virtual machines that are not a part of any existing NSGroup.
    api_response = api_instance.get_unassociated_virtual_machines(cursor=cursor, display_name=display_name, external_id=external_id, host_id=host_id, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->get_unassociated_virtual_machines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **display_name** | **str**| Display Name of the virtual machine | [optional] 
 **external_id** | **str**| External id of the virtual machine | [optional] 
 **host_id** | **str**| Id of the host where this vif is located | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**UnassociatedVMListResult**](UnassociatedVMListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ns_groups**
> NSGroupListResult list_ns_groups(cursor=cursor, included_fields=included_fields, member_types=member_types, page_size=page_size, populate_references=populate_references, sort_ascending=sort_ascending, sort_by=sort_by)

List NSGroups

List the NSGroups in a paginated format. The page size is restricted to 50 NSGroups so that the size of the response remains small even in the worst case. Optionally, specify valid member types as request parameter to filter NSGroups. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
member_types = 'member_types_example' # str | Specify member types to filter corresponding NSGroups  (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
populate_references = false # bool | Populate metadata of resource referenced by NSGroupExpressions  (optional) (default to false)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List NSGroups
    api_response = api_instance.list_ns_groups(cursor=cursor, included_fields=included_fields, member_types=member_types, page_size=page_size, populate_references=populate_references, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->list_ns_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **member_types** | **str**| Specify member types to filter corresponding NSGroups  | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **populate_references** | **bool**| Populate metadata of resource referenced by NSGroupExpressions  | [optional] [default to false]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**NSGroupListResult**](NSGroupListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ns_group**
> NSGroup read_ns_group(ns_group_id, populate_references=populate_references)

Read NSGroup

Returns information about the specified NSGroup. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
ns_group_id = 'ns_group_id_example' # str | NSGroup Id
populate_references = false # bool | Populate metadata of resource referenced by NSGroupExpressions  (optional) (default to false)

try:
    # Read NSGroup
    api_response = api_instance.read_ns_group(ns_group_id, populate_references=populate_references)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->read_ns_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_group_id** | **str**| NSGroup Id | 
 **populate_references** | **bool**| Populate metadata of resource referenced by NSGroupExpressions  | [optional] [default to false]

### Return type

[**NSGroup**](NSGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ns_group**
> NSGroup update_ns_group(body, ns_group_id)

Update NSGroup

Updates the specified NSGroup. Modifiable parameters include the description, display_name and members. For NSGroups containing VM criteria(both static and dynamic), system VMs will not be included as members. This filter applies at VM level only. Exceptions are as follows. 1. LogicalPorts and VNI of system VMs will be included in NSGroup if the criteria  is based on LogicalPort, LogicalSwitch or VNI directly. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.NSGroup() # NSGroup | 
ns_group_id = 'ns_group_id_example' # str | NSGroup Id

try:
    # Update NSGroup
    api_response = api_instance.update_ns_group(body, ns_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSGroupsApi->update_ns_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NSGroup**](NSGroup.md)|  | 
 **ns_group_id** | **str**| NSGroup Id | 

### Return type

[**NSGroup**](NSGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

