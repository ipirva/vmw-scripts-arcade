# swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pbr_rule_in_section**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#add_pbr_rule_in_section) | **POST** /pbr/sections/{section-id}/rules | Add a Single Rule in a Section
[**add_pbr_rules_in_section_create_multiple**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#add_pbr_rules_in_section_create_multiple) | **POST** /pbr/sections/{section-id}/rules?action&#x3D;create_multiple | Add Multiple Rules in a Section
[**add_pbr_section**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#add_pbr_section) | **POST** /pbr/sections | Create a New Empty Section
[**add_pbr_section_with_rules_create_with_rules**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#add_pbr_section_with_rules_create_with_rules) | **POST** /pbr/sections?action&#x3D;create_with_rules | Create a Section with Rules
[**delete_pbr_rule**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#delete_pbr_rule) | **DELETE** /pbr/sections/{section-id}/rules/{rule-id} | Delete an Existing Rule
[**delete_pbr_section**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#delete_pbr_section) | **DELETE** /pbr/sections/{section-id} | Delete an Existing Section and Its Associated Rules
[**get_pbr_rule**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#get_pbr_rule) | **GET** /pbr/sections/{section-id}/rules/{rule-id} | Read an Existing Rule
[**get_pbr_rule_stats**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#get_pbr_rule_stats) | **GET** /pbr/sections/{section-id}/rules/{rule-id}/stats | Get PBR rule level statistics.
[**get_pbr_rules**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#get_pbr_rules) | **GET** /pbr/sections/{section-id}/rules | Get All the Rules for a Section
[**get_pbr_section**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#get_pbr_section) | **GET** /pbr/sections/{section-id} | Get an Existing Section
[**get_pbr_section_stats**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#get_pbr_section_stats) | **GET** /pbr/sections/{section-id}/rules/stats | Get PBR section level statistics.
[**get_pbr_section_with_rules_list_with_rules**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#get_pbr_section_with_rules_list_with_rules) | **POST** /pbr/sections/{section-id}?action&#x3D;list_with_rules | Get an Existing Section, Including Rules
[**list_pbr_sections**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#list_pbr_sections) | **GET** /pbr/sections | List All PBR Sections
[**revise_pbr_rule_revise**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#revise_pbr_rule_revise) | **POST** /pbr/sections/{section-id}/rules/{rule-id}?action&#x3D;revise | Update an Existing Rule and Reorder the Rule
[**revise_pbr_section_revise**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#revise_pbr_section_revise) | **POST** /pbr/sections/{section-id}?action&#x3D;revise | Update an Existing Section, including Its Position
[**revise_pbr_section_with_rules_revise_with_rules**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#revise_pbr_section_with_rules_revise_with_rules) | **POST** /pbr/sections/{section-id}?action&#x3D;revise_with_rules | Update an Existing Section with Rules
[**update_pbr_rule**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#update_pbr_rule) | **PUT** /pbr/sections/{section-id}/rules/{rule-id} | Update an Existing Rule
[**update_pbr_section**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#update_pbr_section) | **PUT** /pbr/sections/{section-id} | Update an Existing Section
[**update_pbr_section_with_rules_update_with_rules**](ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi.md#update_pbr_section_with_rules_update_with_rules) | **POST** /pbr/sections/{section-id}?action&#x3D;update_with_rules | Update an Existing Section, Including Its Rules

# **add_pbr_rule_in_section**
> PBRRule add_pbr_rule_in_section(body, section_id, id=id, operation=operation)

Add a Single Rule in a Section

Adds a new PBR rule in existing PBR section. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
body = swagger_client.PBRRule() # PBRRule | 
section_id = 'section_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Add a Single Rule in a Section
    api_response = api_instance.add_pbr_rule_in_section(body, section_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->add_pbr_rule_in_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PBRRule**](PBRRule.md)|  | 
 **section_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**PBRRule**](PBRRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pbr_rules_in_section_create_multiple**
> PBRRuleList add_pbr_rules_in_section_create_multiple(body, section_id, id=id, operation=operation)

Add Multiple Rules in a Section

Create multiple PBR rules in existing PBR section bounded by limit of 1000 PBR rules per section. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
body = swagger_client.PBRRuleList() # PBRRuleList | 
section_id = 'section_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Add Multiple Rules in a Section
    api_response = api_instance.add_pbr_rules_in_section_create_multiple(body, section_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->add_pbr_rules_in_section_create_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PBRRuleList**](PBRRuleList.md)|  | 
 **section_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**PBRRuleList**](PBRRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pbr_section**
> PBRSection add_pbr_section(body, id=id, operation=operation)

Create a New Empty Section

Creates new empty PBR section in the system. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
body = swagger_client.PBRSection() # PBRSection | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Create a New Empty Section
    api_response = api_instance.add_pbr_section(body, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->add_pbr_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PBRSection**](PBRSection.md)|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**PBRSection**](PBRSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pbr_section_with_rules_create_with_rules**
> PBRSectionRuleList add_pbr_section_with_rules_create_with_rules(body, id=id, operation=operation)

Create a Section with Rules

Creates a new PBR section with rules. The limit on the number of rules is defined by maxItems in collection types for PBRRule (PBRRuleXXXList types). When invoked on a section with a large number of rules, this API is supported only at low rates of invocation (not more than 4-5 times per minute). The typical latency of this API with about 1024 rules is about 4-5 seconds. This API should not be invoked with large payloads at automation speeds. More than 50 rules with a large number of rule references is not supported.  Instead, to create sections, use: POST /api/v1/pbr/sections  To create rules, use: POST /api/v1/pbr/sections/&lt;section-id&gt;/rules 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
body = swagger_client.PBRSectionRuleList() # PBRSectionRuleList | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Create a Section with Rules
    api_response = api_instance.add_pbr_section_with_rules_create_with_rules(body, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->add_pbr_section_with_rules_create_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PBRSectionRuleList**](PBRSectionRuleList.md)|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**PBRSectionRuleList**](PBRSectionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbr_rule**
> delete_pbr_rule(section_id, rule_id)

Delete an Existing Rule

Delete existing PBR rule in a PBR section. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Delete an Existing Rule
    api_instance.delete_pbr_rule(section_id, rule_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->delete_pbr_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pbr_section**
> delete_pbr_section(section_id, cascade=cascade)

Delete an Existing Section and Its Associated Rules

Removes PBR section from the system. PBR section with rules can only be deleted by passing \"cascade=true\" parameter. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
cascade = false # bool | Flag to cascade delete of this object to all it's child objects. (optional) (default to false)

try:
    # Delete an Existing Section and Its Associated Rules
    api_instance.delete_pbr_section(section_id, cascade=cascade)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->delete_pbr_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 
 **cascade** | **bool**| Flag to cascade delete of this object to all it&#x27;s child objects. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbr_rule**
> PBRRule get_pbr_rule(section_id, rule_id)

Read an Existing Rule

Return existing PBR rule information in a PBR section. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Read an Existing Rule
    api_response = api_instance.get_pbr_rule(section_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->get_pbr_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**PBRRule**](PBRRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbr_rule_stats**
> PBRStats get_pbr_rule_stats(section_id, rule_id)

Get PBR rule level statistics.

Get aggregated statistics for a rule for given PBR rule. Stats include total number of packets and total number of bytes for the PBR rule. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Get PBR rule level statistics.
    api_response = api_instance.get_pbr_rule_stats(section_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->get_pbr_rule_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**PBRStats**](PBRStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbr_rules**
> PBRRuleListResult get_pbr_rules(section_id, applied_tos=applied_tos, cursor=cursor, destinations=destinations, filter_type=filter_type, included_fields=included_fields, page_size=page_size, services=services, sort_ascending=sort_ascending, sort_by=sort_by, sources=sources)

Get All the Rules for a Section

Return all PBR rule(s) information for a given PBR section. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
applied_tos = 'applied_tos_example' # str | AppliedTo's referenced by this section or section's Distributed Service Rules . (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
destinations = 'destinations_example' # str | Destinations referenced by this section's Distributed Service Rules . (optional)
filter_type = 'FILTER' # str | Filter type (optional) (default to FILTER)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
services = 'services_example' # str | NSService referenced by this section's Distributed Service Rules . (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
sources = 'sources_example' # str | Sources referenced by this section's Distributed Service Rules . (optional)

try:
    # Get All the Rules for a Section
    api_response = api_instance.get_pbr_rules(section_id, applied_tos=applied_tos, cursor=cursor, destinations=destinations, filter_type=filter_type, included_fields=included_fields, page_size=page_size, services=services, sort_ascending=sort_ascending, sort_by=sort_by, sources=sources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->get_pbr_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 
 **applied_tos** | **str**| AppliedTo&#x27;s referenced by this section or section&#x27;s Distributed Service Rules . | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **destinations** | **str**| Destinations referenced by this section&#x27;s Distributed Service Rules . | [optional] 
 **filter_type** | **str**| Filter type | [optional] [default to FILTER]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **services** | **str**| NSService referenced by this section&#x27;s Distributed Service Rules . | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **sources** | **str**| Sources referenced by this section&#x27;s Distributed Service Rules . | [optional] 

### Return type

[**PBRRuleListResult**](PBRRuleListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbr_section**
> PBRSection get_pbr_section(section_id)

Get an Existing Section

Returns information about PBR section for the identifier. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 

try:
    # Get an Existing Section
    api_response = api_instance.get_pbr_section(section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->get_pbr_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 

### Return type

[**PBRSection**](PBRSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbr_section_stats**
> PBRStatsList get_pbr_section_stats(section_id)

Get PBR section level statistics.

Get aggregated statistics for all rules for a given pbr section. Data includes total number of packets, and total number of bytes for all PBR rules in the given section. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 

try:
    # Get PBR section level statistics.
    api_response = api_instance.get_pbr_section_stats(section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->get_pbr_section_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 

### Return type

[**PBRStatsList**](PBRStatsList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbr_section_with_rules_list_with_rules**
> PBRSectionRuleList get_pbr_section_with_rules_list_with_rules(section_id)

Get an Existing Section, Including Rules

Returns PBR section information with rules for a section identifier. When invoked on a section with a large number of rules, this API is supported only at low rates of invocation (not more than 4-5 times per minute). The typical latency of this API with about 1024 rules is about 4-5 seconds. This API should not be invoked with large payloads at automation speeds. More than 50 rules with a large number rule references is not supported.  Instead, to read PBR rules, use: GET /api/v1/pbr/sections/&lt;section-id&gt;/rules with the appropriate page_size. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 

try:
    # Get an Existing Section, Including Rules
    api_response = api_instance.get_pbr_section_with_rules_list_with_rules(section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->get_pbr_section_with_rules_list_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 

### Return type

[**PBRSectionRuleList**](PBRSectionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pbr_sections**
> PBRSectionListResult list_pbr_sections(applied_tos=applied_tos, cursor=cursor, destinations=destinations, exclude_applied_to_type=exclude_applied_to_type, filter_type=filter_type, include_applied_to_type=include_applied_to_type, included_fields=included_fields, page_size=page_size, services=services, sort_ascending=sort_ascending, sort_by=sort_by, sources=sources)

List All PBR Sections

List all PBR section in paginated form. A default page size is limited to 1000 PBR sections. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
applied_tos = 'applied_tos_example' # str | AppliedTo's referenced by this section or section's Distributed Service Rules . (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
destinations = 'destinations_example' # str | Destinations referenced by this section's Distributed Service Rules . (optional)
exclude_applied_to_type = 'exclude_applied_to_type_example' # str | Resource type valid for use as AppliedTo filter in section API (optional)
filter_type = 'FILTER' # str | Filter type (optional) (default to FILTER)
include_applied_to_type = 'include_applied_to_type_example' # str | Resource type valid for use as AppliedTo filter in section API (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
services = 'services_example' # str | NSService referenced by this section's Distributed Service Rules . (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
sources = 'sources_example' # str | Sources referenced by this section's Distributed Service Rules . (optional)

try:
    # List All PBR Sections
    api_response = api_instance.list_pbr_sections(applied_tos=applied_tos, cursor=cursor, destinations=destinations, exclude_applied_to_type=exclude_applied_to_type, filter_type=filter_type, include_applied_to_type=include_applied_to_type, included_fields=included_fields, page_size=page_size, services=services, sort_ascending=sort_ascending, sort_by=sort_by, sources=sources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->list_pbr_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applied_tos** | **str**| AppliedTo&#x27;s referenced by this section or section&#x27;s Distributed Service Rules . | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **destinations** | **str**| Destinations referenced by this section&#x27;s Distributed Service Rules . | [optional] 
 **exclude_applied_to_type** | **str**| Resource type valid for use as AppliedTo filter in section API | [optional] 
 **filter_type** | **str**| Filter type | [optional] [default to FILTER]
 **include_applied_to_type** | **str**| Resource type valid for use as AppliedTo filter in section API | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **services** | **str**| NSService referenced by this section&#x27;s Distributed Service Rules . | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **sources** | **str**| Sources referenced by this section&#x27;s Distributed Service Rules . | [optional] 

### Return type

[**PBRSectionListResult**](PBRSectionListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revise_pbr_rule_revise**
> PBRRule revise_pbr_rule_revise(body, section_id, rule_id, id=id, operation=operation)

Update an Existing Rule and Reorder the Rule

Modifies existing PBR rule along with relative position among other PBR rules inside a PBR section. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
body = swagger_client.PBRRule() # PBRRule | 
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Update an Existing Rule and Reorder the Rule
    api_response = api_instance.revise_pbr_rule_revise(body, section_id, rule_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->revise_pbr_rule_revise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PBRRule**](PBRRule.md)|  | 
 **section_id** | **str**|  | 
 **rule_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**PBRRule**](PBRRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revise_pbr_section_revise**
> PBRSection revise_pbr_section_revise(body, section_id, id=id, operation=operation)

Update an Existing Section, including Its Position

Modifies an existing PBR section along with its relative position among other PBR sections in the system. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
body = swagger_client.PBRSection() # PBRSection | 
section_id = 'section_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Update an Existing Section, including Its Position
    api_response = api_instance.revise_pbr_section_revise(body, section_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->revise_pbr_section_revise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PBRSection**](PBRSection.md)|  | 
 **section_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**PBRSection**](PBRSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revise_pbr_section_with_rules_revise_with_rules**
> PBRSectionRuleList revise_pbr_section_with_rules_revise_with_rules(body, section_id, id=id, operation=operation)

Update an Existing Section with Rules

Modifies an existing PBR section along with its relative position among other PBR sections with rules. When invoked on a large number of rules, this API is supported only at low rates of invocation (not more than 2 times per minute). The typical latency of this API with about 1024 rules is about 15 seconds in a cluster setup. This API should not be invoked with large payloads at automation speeds.  Instead, to move a section above or below another section, use: POST /api/v1/pbr/sections/&lt;section-id&gt;?action=revise  To modify rules, use: PUT /api/v1/pbr/sections/&lt;section-id&gt;/rules/&lt;rule-id&gt; 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
body = swagger_client.PBRSectionRuleList() # PBRSectionRuleList | 
section_id = 'section_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Update an Existing Section with Rules
    api_response = api_instance.revise_pbr_section_with_rules_revise_with_rules(body, section_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->revise_pbr_section_with_rules_revise_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PBRSectionRuleList**](PBRSectionRuleList.md)|  | 
 **section_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**PBRSectionRuleList**](PBRSectionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbr_rule**
> PBRRule update_pbr_rule(body, section_id, rule_id)

Update an Existing Rule

Modifies existing rule in a PBR section. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
body = swagger_client.PBRRule() # PBRRule | 
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Update an Existing Rule
    api_response = api_instance.update_pbr_rule(body, section_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->update_pbr_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PBRRule**](PBRRule.md)|  | 
 **section_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**PBRRule**](PBRRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbr_section**
> PBRSection update_pbr_section(body, section_id)

Update an Existing Section

Modifies the specified section, but does not modify the section's associated rules. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
body = swagger_client.PBRSection() # PBRSection | 
section_id = 'section_id_example' # str | 

try:
    # Update an Existing Section
    api_response = api_instance.update_pbr_section(body, section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->update_pbr_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PBRSection**](PBRSection.md)|  | 
 **section_id** | **str**|  | 

### Return type

[**PBRSection**](PBRSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pbr_section_with_rules_update_with_rules**
> PBRSectionRuleList update_pbr_section_with_rules_update_with_rules(body, section_id)

Update an Existing Section, Including Its Rules

Modifies existing PBR section along with its association with rules. When invoked on a large number of rules, this API is supported only at low rates of invocation (not more than 2 times per minute). The typical latency of this API with about 1024 rules is about 15 seconds in a cluster setup. This API should not be invoked with large payloads at automation speeds.  Instead, to update rule content, use: PUT /api/v1/pbr/sections/&lt;section-id&gt;/rules/&lt;rule-id&gt; 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi(swagger_client.ApiClient(configuration))
body = swagger_client.PBRSectionRuleList() # PBRSectionRuleList | 
section_id = 'section_id_example' # str | 

try:
    # Update an Existing Section, Including Its Rules
    api_response = api_instance.update_pbr_section_with_rules_update_with_rules(body, section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesPolicyBasedRoutingApi->update_pbr_section_with_rules_update_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PBRSectionRuleList**](PBRSectionRuleList.md)|  | 
 **section_id** | **str**|  | 

### Return type

[**PBRSectionRuleList**](PBRSectionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

