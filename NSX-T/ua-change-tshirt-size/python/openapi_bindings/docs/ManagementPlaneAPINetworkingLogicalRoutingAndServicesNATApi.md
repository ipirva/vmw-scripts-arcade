# swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_nat_rule**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi.md#add_nat_rule) | **POST** /logical-routers/{logical-router-id}/nat/rules | Add a NAT rule in a specific logical router
[**add_nat_rules_create_multiple**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi.md#add_nat_rules_create_multiple) | **POST** /logical-routers/{logical-router-id}/nat/rules?action&#x3D;create_multiple | Add multiple NAT rules in a specific logical router
[**delete_nat_rule**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi.md#delete_nat_rule) | **DELETE** /logical-routers/{logical-router-id}/nat/rules/{rule-id} | Delete a specific NAT rule from a logical router
[**get_nat_rule**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi.md#get_nat_rule) | **GET** /logical-routers/{logical-router-id}/nat/rules/{rule-id} | Get a specific NAT rule from a given logical router
[**get_nat_statistics_per_logical_router**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi.md#get_nat_statistics_per_logical_router) | **GET** /logical-routers/{logical-router-id}/nat/rules/statistics | Get the statistics of all rules of the logical router
[**get_nat_statistics_per_rule**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi.md#get_nat_statistics_per_rule) | **GET** /logical-routers/{logical-router-id}/nat/rules/{rule-id}/statistics | Get the statistics of a specified logical router NAT Rule
[**get_nat_statistics_per_transport_node**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi.md#get_nat_statistics_per_transport_node) | **GET** /transport-nodes/{node-id}/statistics/nat-rules | Get statistics for all logical router NAT rules on a transport node
[**list_nat_rules**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi.md#list_nat_rules) | **GET** /logical-routers/{logical-router-id}/nat/rules | List NAT rules of the logical router
[**update_nat_rule**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi.md#update_nat_rule) | **PUT** /logical-routers/{logical-router-id}/nat/rules/{rule-id} | Update a specific NAT rule from a given logical router

# **add_nat_rule**
> NatRule add_nat_rule(body, logical_router_id)

Add a NAT rule in a specific logical router

Add a NAT rule in a specific logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi(swagger_client.ApiClient(configuration))
body = swagger_client.NatRule() # NatRule | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Add a NAT rule in a specific logical router
    api_response = api_instance.add_nat_rule(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi->add_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NatRule**](NatRule.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**NatRule**](NatRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_nat_rules_create_multiple**
> NatRuleList add_nat_rules_create_multiple(body, logical_router_id)

Add multiple NAT rules in a specific logical router

Create multiple NAT rules in a specific logical router. The API succeeds only when all rules are accepted and created successfully. Any one validation voilation will fail the API, no rule will be created. The ruleIds of each rules can be found from the responsed message. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi(swagger_client.ApiClient(configuration))
body = swagger_client.NatRuleList() # NatRuleList | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Add multiple NAT rules in a specific logical router
    api_response = api_instance.add_nat_rules_create_multiple(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi->add_nat_rules_create_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NatRuleList**](NatRuleList.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**NatRuleList**](NatRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nat_rule**
> delete_nat_rule(logical_router_id, rule_id)

Delete a specific NAT rule from a logical router

Delete a specific NAT rule from a logical router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Delete a specific NAT rule from a logical router
    api_instance.delete_nat_rule(logical_router_id, rule_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi->delete_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nat_rule**
> NatRule get_nat_rule(logical_router_id, rule_id)

Get a specific NAT rule from a given logical router

Get a specific NAT rule from a given logical router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Get a specific NAT rule from a given logical router
    api_response = api_instance.get_nat_rule(logical_router_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi->get_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**NatRule**](NatRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nat_statistics_per_logical_router**
> NatStatisticsPerLogicalRouter get_nat_statistics_per_logical_router(logical_router_id, source=source)

Get the statistics of all rules of the logical router

Returns the summation of statistics for all rules from all nodes for the Specified Logical Router. Also gives the per transport node statistics for provided logical router. The query parameter \"source=realtime\" is not supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the statistics of all rules of the logical router
    api_response = api_instance.get_nat_statistics_per_logical_router(logical_router_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi->get_nat_statistics_per_logical_router: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NatStatisticsPerLogicalRouter**](NatStatisticsPerLogicalRouter.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nat_statistics_per_rule**
> NatStatisticsPerRule get_nat_statistics_per_rule(logical_router_id, rule_id, source=source)

Get the statistics of a specified logical router NAT Rule

Returns the summation of statistics from all nodes for the Specified Logical Router NAT Rule. Query parameter \"source=realtime\" is the only supported source. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
rule_id = 'rule_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the statistics of a specified logical router NAT Rule
    api_response = api_instance.get_nat_statistics_per_rule(logical_router_id, rule_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi->get_nat_statistics_per_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **rule_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NatStatisticsPerRule**](NatStatisticsPerRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nat_statistics_per_transport_node**
> NatStatisticsPerTransportNode get_nat_statistics_per_transport_node(node_id, source=source)

Get statistics for all logical router NAT rules on a transport node

Returns the summation of statistics for all rules from all logical routers which are present on given transport node. Only cached statistics are supported. The query parameter \"source=realtime\" is not supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get statistics for all logical router NAT rules on a transport node
    api_response = api_instance.get_nat_statistics_per_transport_node(node_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi->get_nat_statistics_per_transport_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NatStatisticsPerTransportNode**](NatStatisticsPerTransportNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nat_rules**
> NatRuleListResult list_nat_rules(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, rule_type=rule_type, sort_ascending=sort_ascending, sort_by=sort_by)

List NAT rules of the logical router

Returns paginated list of all user defined NAT rules of the specific logical router. If a rule_type is provided, only the given type of rules will be returned. If no rule_type is specified, the rule_type will be defaulted to NATv4, i.e. only the NATv4 rules will be listed. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
rule_type = 'rule_type_example' # str | Action type for getting NAT rules (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List NAT rules of the logical router
    api_response = api_instance.list_nat_rules(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, rule_type=rule_type, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi->list_nat_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **rule_type** | **str**| Action type for getting NAT rules | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**NatRuleListResult**](NatRuleListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nat_rule**
> NatRule update_nat_rule(body, logical_router_id, rule_id)

Update a specific NAT rule from a given logical router

Update a specific NAT rule from a given logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi(swagger_client.ApiClient(configuration))
body = swagger_client.NatRule() # NatRule | 
logical_router_id = 'logical_router_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Update a specific NAT rule from a given logical router
    api_response = api_instance.update_nat_rule(body, logical_router_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesNATApi->update_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NatRule**](NatRule.md)|  | 
 **logical_router_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**NatRule**](NatRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

