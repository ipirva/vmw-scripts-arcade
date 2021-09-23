# swagger_client.ManagementPlaneAPISecurityServicesFirewallApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member_add_member**](ManagementPlaneAPISecurityServicesFirewallApi.md#add_member_add_member) | **POST** /firewall/excludelist?action&#x3D;add_member | Add a new object in the exclude list
[**add_rule_in_section**](ManagementPlaneAPISecurityServicesFirewallApi.md#add_rule_in_section) | **POST** /firewall/sections/{section-id}/rules | Add a Single Rule in a Section
[**add_rules_in_section_create_multiple**](ManagementPlaneAPISecurityServicesFirewallApi.md#add_rules_in_section_create_multiple) | **POST** /firewall/sections/{section-id}/rules?action&#x3D;create_multiple | Add Multiple Rules in a Section
[**add_section**](ManagementPlaneAPISecurityServicesFirewallApi.md#add_section) | **POST** /firewall/sections | Create a New Empty Section
[**add_section_with_rules_create_with_rules**](ManagementPlaneAPISecurityServicesFirewallApi.md#add_section_with_rules_create_with_rules) | **POST** /firewall/sections?action&#x3D;create_with_rules | Create a Section with Rules
[**check_member_if_exists_check_if_exists**](ManagementPlaneAPISecurityServicesFirewallApi.md#check_member_if_exists_check_if_exists) | **POST** /firewall/excludelist?action&#x3D;check_if_exists | Check if the object a member of the exclude list
[**create_firewall_profile**](ManagementPlaneAPISecurityServicesFirewallApi.md#create_firewall_profile) | **POST** /firewall/profiles | Create a firewall profile.
[**delete_firewall_profile**](ManagementPlaneAPISecurityServicesFirewallApi.md#delete_firewall_profile) | **DELETE** /firewall/profiles/{profile-id} | Delete a firewall profile.
[**delete_rule**](ManagementPlaneAPISecurityServicesFirewallApi.md#delete_rule) | **DELETE** /firewall/sections/{section-id}/rules/{rule-id} | Delete an Existing Rule
[**delete_section**](ManagementPlaneAPISecurityServicesFirewallApi.md#delete_section) | **DELETE** /firewall/sections/{section-id} | Delete an Existing Section and Its Associated Rules
[**disable_firewall_on_target_resource_disable_firewall**](ManagementPlaneAPISecurityServicesFirewallApi.md#disable_firewall_on_target_resource_disable_firewall) | **POST** /firewall/status/{context-type}/{id}?action&#x3D;disable_firewall | Disable firewall on target resource in dfw context
[**enable_firewall_on_target_resource_enable_firewall**](ManagementPlaneAPISecurityServicesFirewallApi.md#enable_firewall_on_target_resource_enable_firewall) | **POST** /firewall/status/{context-type}/{id}?action&#x3D;enable_firewall | Enable firewall on target resource in dfw context
[**get_exclude_list**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_exclude_list) | **GET** /firewall/excludelist | Get list of entities in exclude list
[**get_firewall_profile**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_firewall_profile) | **GET** /firewall/profiles/{profile-id} | Get all firewall session timer profiles.
[**get_firewall_section_stats**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_firewall_section_stats) | **GET** /firewall/sections/{section-id}/rules/stats | Get Firewall section level statistics section
[**get_firewall_stats**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_firewall_stats) | **GET** /firewall/sections/{section-id}/rules/{rule-id}/stats | Get Firewall rule level statistics
[**get_firewall_status**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_firewall_status) | **GET** /firewall/status/{context-type} | Get firewall global status for dfw context
[**get_firewall_status_on_target_resource**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_firewall_status_on_target_resource) | **GET** /firewall/status/{context-type}/{id} | Get firewall status for target resource in dfw context
[**get_rule**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_rule) | **GET** /firewall/sections/{section-id}/rules/{rule-id} | Read an Existing Rule
[**get_rule_state**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_rule_state) | **GET** /firewall/rules/{rule-id}/state | Get the Realized State of a Firewall Rule
[**get_rules**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_rules) | **GET** /firewall/sections/{section-id}/rules | Get All the Rules for a Section
[**get_section**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_section) | **GET** /firewall/sections/{section-id} | Get an Existing Section
[**get_section_state**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_section_state) | **GET** /firewall/sections/{section-id}/state | Get the Realized State of a Firewall Section
[**get_section_with_rules_list_with_rules**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_section_with_rules_list_with_rules) | **POST** /firewall/sections/{section-id}?action&#x3D;list_with_rules | Get an Existing Section, Including Rules
[**get_sections_summary**](ManagementPlaneAPISecurityServicesFirewallApi.md#get_sections_summary) | **GET** /firewall/sections/summary | Get the summary of sections in the firewall configuration.
[**list_firewall_profiles**](ManagementPlaneAPISecurityServicesFirewallApi.md#list_firewall_profiles) | **GET** /firewall/profiles | Get firewall profiles available.
[**list_firewall_status**](ManagementPlaneAPISecurityServicesFirewallApi.md#list_firewall_status) | **GET** /firewall/status | List all firewall status for supported contexts
[**list_sections**](ManagementPlaneAPISecurityServicesFirewallApi.md#list_sections) | **GET** /firewall/sections | List All Firewall Sections
[**lock_section_lock**](ManagementPlaneAPISecurityServicesFirewallApi.md#lock_section_lock) | **POST** /firewall/sections/{section-id}?action&#x3D;lock | Lock a section
[**read_firewall_rule**](ManagementPlaneAPISecurityServicesFirewallApi.md#read_firewall_rule) | **GET** /firewall/rules/{rule-id} | Read an Existing Rule
[**remove_member_remove_member**](ManagementPlaneAPISecurityServicesFirewallApi.md#remove_member_remove_member) | **POST** /firewall/excludelist?action&#x3D;remove_member | Remove an existing object from the exclude list
[**reset_firewall_rule_stats_reset**](ManagementPlaneAPISecurityServicesFirewallApi.md#reset_firewall_rule_stats_reset) | **POST** /firewall/stats?action&#x3D;reset | Reset firewall rule statistics
[**revise_rule_revise**](ManagementPlaneAPISecurityServicesFirewallApi.md#revise_rule_revise) | **POST** /firewall/sections/{section-id}/rules/{rule-id}?action&#x3D;revise | Update an Existing Rule and Reorder the Rule
[**revise_section_revise**](ManagementPlaneAPISecurityServicesFirewallApi.md#revise_section_revise) | **POST** /firewall/sections/{section-id}?action&#x3D;revise | Update an Existing Section, Including Its Position
[**revise_section_with_rules_revise_with_rules**](ManagementPlaneAPISecurityServicesFirewallApi.md#revise_section_with_rules_revise_with_rules) | **POST** /firewall/sections/{section-id}?action&#x3D;revise_with_rules | Update an Existing Section with Rules
[**unlock_section_unlock**](ManagementPlaneAPISecurityServicesFirewallApi.md#unlock_section_unlock) | **POST** /firewall/sections/{section-id}?action&#x3D;unlock | Unlock a section
[**update_exclude_list**](ManagementPlaneAPISecurityServicesFirewallApi.md#update_exclude_list) | **PUT** /firewall/excludelist | Modify exclude list
[**update_firewall_profile**](ManagementPlaneAPISecurityServicesFirewallApi.md#update_firewall_profile) | **PUT** /firewall/profiles/{profile-id} | Update a firewall profile.
[**update_firewall_status**](ManagementPlaneAPISecurityServicesFirewallApi.md#update_firewall_status) | **PUT** /firewall/status/{context-type} | Update global firewall status for dfw context
[**update_rule**](ManagementPlaneAPISecurityServicesFirewallApi.md#update_rule) | **PUT** /firewall/sections/{section-id}/rules/{rule-id} | Update an Existing Rule
[**update_section**](ManagementPlaneAPISecurityServicesFirewallApi.md#update_section) | **PUT** /firewall/sections/{section-id} | Update an Existing Section
[**update_section_with_rules_update_with_rules**](ManagementPlaneAPISecurityServicesFirewallApi.md#update_section_with_rules_update_with_rules) | **POST** /firewall/sections/{section-id}?action&#x3D;update_with_rules | Update an Existing Section, Including Its Rules

# **add_member_add_member**
> ResourceReference add_member_add_member(body)

Add a new object in the exclude list

Add a new object in the exclude list

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResourceReference() # ResourceReference | 

try:
    # Add a new object in the exclude list
    api_response = api_instance.add_member_add_member(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->add_member_add_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceReference**](ResourceReference.md)|  | 

### Return type

[**ResourceReference**](ResourceReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_rule_in_section**
> FirewallRule add_rule_in_section(body, section_id, id=id, operation=operation)

Add a Single Rule in a Section

Adds a new firewall rule in existing firewall section. Adding firewall rule to a section modifies parent section entity and simultaneous update (modify) operations on same section are not allowed to prevent overwriting stale content to firewall section. If a concurrent update is performed, HTTP response code 409 will be returned to the client operating on stale data. That client should retrieve the firewall section again and re-apply its update. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallRule() # FirewallRule | 
section_id = 'section_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Add a Single Rule in a Section
    api_response = api_instance.add_rule_in_section(body, section_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->add_rule_in_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallRule**](FirewallRule.md)|  | 
 **section_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_rules_in_section_create_multiple**
> FirewallRuleList add_rules_in_section_create_multiple(body, section_id, id=id, operation=operation)

Add Multiple Rules in a Section

Create multiple firewall rules in existing firewall section bounded by limit of 1000 firewall rules per section. Adding multiple firewall rules in a section modifies parent section entity and simultaneous update (modify) operations on same section are not allowed to prevent overwriting stale contents to firewall section. If a concurrent update is performed, HTTP response code 409 will be returned to the client operating on stale data. That client should retrieve the firewall section again and re-apply its update. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallRuleList() # FirewallRuleList | 
section_id = 'section_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Add Multiple Rules in a Section
    api_response = api_instance.add_rules_in_section_create_multiple(body, section_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->add_rules_in_section_create_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallRuleList**](FirewallRuleList.md)|  | 
 **section_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**FirewallRuleList**](FirewallRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_section**
> FirewallSection add_section(body, id=id, operation=operation)

Create a New Empty Section

Creates new empty firewall section in the system. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallSection() # FirewallSection | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Create a New Empty Section
    api_response = api_instance.add_section(body, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->add_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallSection**](FirewallSection.md)|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**FirewallSection**](FirewallSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_section_with_rules_create_with_rules**
> FirewallSectionRuleList add_section_with_rules_create_with_rules(body, id=id, operation=operation)

Create a Section with Rules

Creates a new firewall section with rules. The limit on the number of rules is defined by maxItems in collection types for FirewallRule (FirewallRuleXXXList types). When invoked on a section with a large number of rules, this API is supported only at low rates of invocation (not more than 4-5 times per minute). The typical latency of this API with about 1024 rules is about 4-5 seconds. This API should not be invoked with large payloads at automation speeds. More than 50 rules with a large number of rule references is not supported.  Instead, to create sections, use: POST /api/v1/firewall/sections  To create rules, use: POST /api/v1/firewall/sections/&lt;section-id&gt;/rules 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallSectionRuleList() # FirewallSectionRuleList | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Create a Section with Rules
    api_response = api_instance.add_section_with_rules_create_with_rules(body, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->add_section_with_rules_create_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallSectionRuleList**](FirewallSectionRuleList.md)|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**FirewallSectionRuleList**](FirewallSectionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_member_if_exists_check_if_exists**
> ResourceReference check_member_if_exists_check_if_exists(object_id, deep_check=deep_check, object_type=object_type)

Check if the object a member of the exclude list

Check if the object a member of the exclude list

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
object_id = 'object_id_example' # str | identifier of the object
deep_check = false # bool | Check all parents (optional) (default to false)
object_type = 'object_type_example' # str | Object type of an entity (optional)

try:
    # Check if the object a member of the exclude list
    api_response = api_instance.check_member_if_exists_check_if_exists(object_id, deep_check=deep_check, object_type=object_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->check_member_if_exists_check_if_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| identifier of the object | 
 **deep_check** | **bool**| Check all parents | [optional] [default to false]
 **object_type** | **str**| Object type of an entity | [optional] 

### Return type

[**ResourceReference**](ResourceReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_firewall_profile**
> BaseFirewallProfile create_firewall_profile(body)

Create a firewall profile.

Create a firewall profile with values provided. It creates profile based resource_type in the payload. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.BaseFirewallProfile() # BaseFirewallProfile | 

try:
    # Create a firewall profile.
    api_response = api_instance.create_firewall_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->create_firewall_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseFirewallProfile**](BaseFirewallProfile.md)|  | 

### Return type

[**BaseFirewallProfile**](BaseFirewallProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_profile**
> delete_firewall_profile(profile_id)

Delete a firewall profile.

Deletes a firewall profile. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
profile_id = 'profile_id_example' # str | 

try:
    # Delete a firewall profile.
    api_instance.delete_firewall_profile(profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->delete_firewall_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule**
> delete_rule(section_id, rule_id)

Delete an Existing Rule

Delete existing firewall rule in a firewall section. Deleting firewall rule in a section modifies parent section and simultaneous update (modify) operations on same section are not allowed to prevent overwriting stale contents to firewall section. If a concurrent update is performed, HTTP response code 409 will be returned to the client operating on stale data. That client should retrieve the firewall section again and re-apply its update. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Delete an Existing Rule
    api_instance.delete_rule(section_id, rule_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->delete_rule: %s\n" % e)
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

# **delete_section**
> delete_section(section_id, cascade=cascade)

Delete an Existing Section and Its Associated Rules

Removes firewall section from the system. Firewall section with rules can only be deleted by passing \"cascade=true\" parameter. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
cascade = false # bool | Flag to cascade delete of this object to all it's child objects. (optional) (default to false)

try:
    # Delete an Existing Section and Its Associated Rules
    api_instance.delete_section(section_id, cascade=cascade)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->delete_section: %s\n" % e)
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

# **disable_firewall_on_target_resource_disable_firewall**
> TargetResourceStatus disable_firewall_on_target_resource_disable_firewall(context_type, id)

Disable firewall on target resource in dfw context

Disable firewall on target resource in dfw context

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
context_type = 'context_type_example' # str | 
id = 'id_example' # str | 

try:
    # Disable firewall on target resource in dfw context
    api_response = api_instance.disable_firewall_on_target_resource_disable_firewall(context_type, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->disable_firewall_on_target_resource_disable_firewall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_type** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**TargetResourceStatus**](TargetResourceStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_firewall_on_target_resource_enable_firewall**
> TargetResourceStatus enable_firewall_on_target_resource_enable_firewall(context_type, id)

Enable firewall on target resource in dfw context

Enable firewall on target resource in dfw context

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
context_type = 'context_type_example' # str | 
id = 'id_example' # str | 

try:
    # Enable firewall on target resource in dfw context
    api_response = api_instance.enable_firewall_on_target_resource_enable_firewall(context_type, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->enable_firewall_on_target_resource_enable_firewall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_type** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**TargetResourceStatus**](TargetResourceStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exclude_list**
> ExcludeList get_exclude_list()

Get list of entities in exclude list

Get list of entities in exclude list

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))

try:
    # Get list of entities in exclude list
    api_response = api_instance.get_exclude_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_exclude_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExcludeList**](ExcludeList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_profile**
> BaseFirewallProfile get_firewall_profile(profile_id)

Get all firewall session timer profiles.

Return firewall session timer profile. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
profile_id = 'profile_id_example' # str | 

try:
    # Get all firewall session timer profiles.
    api_response = api_instance.get_firewall_profile(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_firewall_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

[**BaseFirewallProfile**](BaseFirewallProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_section_stats**
> FirewallStatsList get_firewall_section_stats(section_id, source=source)

Get Firewall section level statistics section

Get aggregated statistics for all rules for a given firewall section. The API only supports access to cached (source=cached) statistical data collected offline in the system. Data includes total number of packets, bytes, sessions counters and popularity index for a firewall rule and overall session count, max session count and max popularity index for all firewall rules on transport nodes or edge nodes. Aggregated statistics like maximum popularity index, maximum session count and total session count are computed with lower frequency compared to individual generic rule statistics, hence they may have a computation delay up to 15 minutes to reflect in response to this API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get Firewall section level statistics section
    api_response = api_instance.get_firewall_section_stats(section_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_firewall_section_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**FirewallStatsList**](FirewallStatsList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_stats**
> FirewallStats get_firewall_stats(section_id, rule_id, source=source)

Get Firewall rule level statistics

Get aggregated statistics for a rule for given firewall section. The API only supports access to cached (source=cached) statistical data collected offline in the system. Data includes total number of packets, bytes, sessions counters and popularity index for a firewall rule and overall session count, max session count and max popularity index for all firewall rules on transport nodes or edge nodes. Aggregated statistics like maximum popularity index, maximum session count and total session count are computed with lower frequency compared to individual generic rule statistics, hence they may have a computation delay up to 15 minutes to reflect in response to this API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get Firewall rule level statistics
    api_response = api_instance.get_firewall_stats(section_id, rule_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_firewall_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 
 **rule_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**FirewallStats**](FirewallStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_status**
> FirewallStatus get_firewall_status(context_type)

Get firewall global status for dfw context

Get firewall global status for dfw context

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
context_type = 'context_type_example' # str | 

try:
    # Get firewall global status for dfw context
    api_response = api_instance.get_firewall_status(context_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_firewall_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_type** | **str**|  | 

### Return type

[**FirewallStatus**](FirewallStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_status_on_target_resource**
> TargetResourceStatus get_firewall_status_on_target_resource(context_type, id)

Get firewall status for target resource in dfw context

Get firewall status for target resource in dfw context

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
context_type = 'context_type_example' # str | 
id = 'id_example' # str | 

try:
    # Get firewall status for target resource in dfw context
    api_response = api_instance.get_firewall_status_on_target_resource(context_type, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_firewall_status_on_target_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_type** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**TargetResourceStatus**](TargetResourceStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule**
> FirewallRule get_rule(section_id, rule_id)

Read an Existing Rule

Return existing firewall rule information in a firewall section. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Read an Existing Rule
    api_response = api_instance.get_rule(section_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_state**
> RuleState get_rule_state(rule_id, barrier_id=barrier_id, request_id=request_id)

Get the Realized State of a Firewall Rule

Return realized state information of a firewall rule. Returned response is same as rule's section realization state response. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | 
barrier_id = 789 # int |  (optional)
request_id = 'request_id_example' # str | Realization request ID (optional)

try:
    # Get the Realized State of a Firewall Rule
    api_response = api_instance.get_rule_state(rule_id, barrier_id=barrier_id, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_rule_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **barrier_id** | **int**|  | [optional] 
 **request_id** | **str**| Realization request ID | [optional] 

### Return type

[**RuleState**](RuleState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules**
> FirewallRuleListResult get_rules(section_id, applied_tos=applied_tos, context_profiles=context_profiles, cursor=cursor, deep_search=deep_search, destinations=destinations, extended_sources=extended_sources, filter_type=filter_type, included_fields=included_fields, page_size=page_size, search_invalid_references=search_invalid_references, services=services, sort_ascending=sort_ascending, sort_by=sort_by, sources=sources)

Get All the Rules for a Section

Return all firewall rule(s) information for a given firewall section. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
applied_tos = 'applied_tos_example' # str | AppliedTo's referenced by this section or section's Distributed Service Rules . (optional)
context_profiles = 'context_profiles_example' # str | Limits results to sections having rules with specific Context Profiles. (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
deep_search = false # bool | Toggle to search with direct or indirect references. (optional) (default to false)
destinations = 'destinations_example' # str | Destinations referenced by this section's Distributed Service Rules . (optional)
extended_sources = 'extended_sources_example' # str | Limits results to sections having rules with specific Extended Sources. (optional)
filter_type = 'FILTER' # str | Filter type (optional) (default to FILTER)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
search_invalid_references = false # bool | Return invalid references in results. (optional) (default to false)
services = 'services_example' # str | NSService referenced by this section's Distributed Service Rules . (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
sources = 'sources_example' # str | Sources referenced by this section's Distributed Service Rules . (optional)

try:
    # Get All the Rules for a Section
    api_response = api_instance.get_rules(section_id, applied_tos=applied_tos, context_profiles=context_profiles, cursor=cursor, deep_search=deep_search, destinations=destinations, extended_sources=extended_sources, filter_type=filter_type, included_fields=included_fields, page_size=page_size, search_invalid_references=search_invalid_references, services=services, sort_ascending=sort_ascending, sort_by=sort_by, sources=sources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 
 **applied_tos** | **str**| AppliedTo&#x27;s referenced by this section or section&#x27;s Distributed Service Rules . | [optional] 
 **context_profiles** | **str**| Limits results to sections having rules with specific Context Profiles. | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **deep_search** | **bool**| Toggle to search with direct or indirect references. | [optional] [default to false]
 **destinations** | **str**| Destinations referenced by this section&#x27;s Distributed Service Rules . | [optional] 
 **extended_sources** | **str**| Limits results to sections having rules with specific Extended Sources. | [optional] 
 **filter_type** | **str**| Filter type | [optional] [default to FILTER]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **search_invalid_references** | **bool**| Return invalid references in results. | [optional] [default to false]
 **services** | **str**| NSService referenced by this section&#x27;s Distributed Service Rules . | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **sources** | **str**| Sources referenced by this section&#x27;s Distributed Service Rules . | [optional] 

### Return type

[**FirewallRuleListResult**](FirewallRuleListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section**
> FirewallSection get_section(section_id)

Get an Existing Section

Returns information about firewall section for the identifier. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 

try:
    # Get an Existing Section
    api_response = api_instance.get_section(section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 

### Return type

[**FirewallSection**](FirewallSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section_state**
> FirewallSectionState get_section_state(section_id, barrier_id=barrier_id, request_id=request_id)

Get the Realized State of a Firewall Section

Return realized state information of a firewall section. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
barrier_id = 789 # int |  (optional)
request_id = 'request_id_example' # str | Realization request ID (optional)

try:
    # Get the Realized State of a Firewall Section
    api_response = api_instance.get_section_state(section_id, barrier_id=barrier_id, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_section_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 
 **barrier_id** | **int**|  | [optional] 
 **request_id** | **str**| Realization request ID | [optional] 

### Return type

[**FirewallSectionState**](FirewallSectionState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section_with_rules_list_with_rules**
> FirewallSectionRuleList get_section_with_rules_list_with_rules(section_id)

Get an Existing Section, Including Rules

Returns firewall section information with rules for a section identifier. When invoked on a section with a large number of rules, this API is supported only at low rates of invocation (not more than 4-5 times per minute). The typical latency of this API with about 1024 rules is about 4-5 seconds. This API should not be invoked with large payloads at automation speeds. More than 50 rules with a large number rule references is not supported.  Instead, to read firewall rules, use: GET /api/v1/firewall/sections/&lt;section-id&gt;/rules with the appropriate page_size. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 

try:
    # Get an Existing Section, Including Rules
    api_response = api_instance.get_section_with_rules_list_with_rules(section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_section_with_rules_list_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 

### Return type

[**FirewallSectionRuleList**](FirewallSectionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sections_summary**
> FirewallSectionsSummaryList get_sections_summary(source=source)

Get the summary of sections in the firewall configuration.

List the summary of number of sections and number of rules for each firewall category (L2DFW, L3DFW). 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the summary of sections in the firewall configuration.
    api_response = api_instance.get_sections_summary(source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->get_sections_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Data source type. | [optional] 

### Return type

[**FirewallSectionsSummaryList**](FirewallSectionsSummaryList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firewall_profiles**
> FirewallProfileListResult list_firewall_profiles(resource_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get firewall profiles available.

List all the firewall profiles available by requested resource_type. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
resource_type = 'resource_type_example' # str | Profile resource type
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get firewall profiles available.
    api_response = api_instance.list_firewall_profiles(resource_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->list_firewall_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| Profile resource type | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**FirewallProfileListResult**](FirewallProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firewall_status**
> FirewallStatusListResult list_firewall_status()

List all firewall status for supported contexts

List all firewall status for supported contexts

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))

try:
    # List all firewall status for supported contexts
    api_response = api_instance.list_firewall_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->list_firewall_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FirewallStatusListResult**](FirewallStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sections**
> FirewallSectionListResult list_sections(applied_tos=applied_tos, context_profiles=context_profiles, cursor=cursor, deep_search=deep_search, destinations=destinations, enforced_on=enforced_on, exclude_applied_to_type=exclude_applied_to_type, extended_sources=extended_sources, filter_type=filter_type, include_applied_to_type=include_applied_to_type, included_fields=included_fields, locked=locked, page_size=page_size, search_invalid_references=search_invalid_references, search_scope=search_scope, services=services, sort_ascending=sort_ascending, sort_by=sort_by, sources=sources, type=type)

List All Firewall Sections

List all firewall section in paginated form. A default page size is limited to 1000 firewall sections. By default list of section is filtered by LAYER3 type. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
applied_tos = 'applied_tos_example' # str | AppliedTo's referenced by this section or section's Distributed Service Rules . (optional)
context_profiles = 'context_profiles_example' # str | Limits results to sections having rules with specific Context Profiles. (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
deep_search = false # bool | Toggle to search with direct or indirect references. (optional) (default to false)
destinations = 'destinations_example' # str | Destinations referenced by this section's Distributed Service Rules . (optional)
enforced_on = 'enforced_on_example' # str | Type of attachment for logical port; for query only. (optional)
exclude_applied_to_type = 'exclude_applied_to_type_example' # str | Resource type valid for use as AppliedTo filter in section API (optional)
extended_sources = 'extended_sources_example' # str | Limits results to sections having rules with specific Extended Sources. (optional)
filter_type = 'FILTER' # str | Filter type (optional) (default to FILTER)
include_applied_to_type = 'include_applied_to_type_example' # str | Resource type valid for use as AppliedTo filter in section API (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
locked = true # bool | Limit results to sections which are locked/unlocked (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
search_invalid_references = false # bool | Return invalid references in results. (optional) (default to false)
search_scope = 'search_scope_example' # str | Limit result to sections of a specific enforcement point (optional)
services = 'services_example' # str | NSService referenced by this section's Distributed Service Rules . (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
sources = 'sources_example' # str | Sources referenced by this section's Distributed Service Rules . (optional)
type = 'LAYER3' # str | Section Type (optional) (default to LAYER3)

try:
    # List All Firewall Sections
    api_response = api_instance.list_sections(applied_tos=applied_tos, context_profiles=context_profiles, cursor=cursor, deep_search=deep_search, destinations=destinations, enforced_on=enforced_on, exclude_applied_to_type=exclude_applied_to_type, extended_sources=extended_sources, filter_type=filter_type, include_applied_to_type=include_applied_to_type, included_fields=included_fields, locked=locked, page_size=page_size, search_invalid_references=search_invalid_references, search_scope=search_scope, services=services, sort_ascending=sort_ascending, sort_by=sort_by, sources=sources, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->list_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applied_tos** | **str**| AppliedTo&#x27;s referenced by this section or section&#x27;s Distributed Service Rules . | [optional] 
 **context_profiles** | **str**| Limits results to sections having rules with specific Context Profiles. | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **deep_search** | **bool**| Toggle to search with direct or indirect references. | [optional] [default to false]
 **destinations** | **str**| Destinations referenced by this section&#x27;s Distributed Service Rules . | [optional] 
 **enforced_on** | **str**| Type of attachment for logical port; for query only. | [optional] 
 **exclude_applied_to_type** | **str**| Resource type valid for use as AppliedTo filter in section API | [optional] 
 **extended_sources** | **str**| Limits results to sections having rules with specific Extended Sources. | [optional] 
 **filter_type** | **str**| Filter type | [optional] [default to FILTER]
 **include_applied_to_type** | **str**| Resource type valid for use as AppliedTo filter in section API | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **locked** | **bool**| Limit results to sections which are locked/unlocked | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **search_invalid_references** | **bool**| Return invalid references in results. | [optional] [default to false]
 **search_scope** | **str**| Limit result to sections of a specific enforcement point | [optional] 
 **services** | **str**| NSService referenced by this section&#x27;s Distributed Service Rules . | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **sources** | **str**| Sources referenced by this section&#x27;s Distributed Service Rules . | [optional] 
 **type** | **str**| Section Type | [optional] [default to LAYER3]

### Return type

[**FirewallSectionListResult**](FirewallSectionListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_section_lock**
> FirewallSection lock_section_lock(body, section_id)

Lock a section

Lock a section 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallSectionLock() # FirewallSectionLock | 
section_id = 'section_id_example' # str | 

try:
    # Lock a section
    api_response = api_instance.lock_section_lock(body, section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->lock_section_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallSectionLock**](FirewallSectionLock.md)|  | 
 **section_id** | **str**|  | 

### Return type

[**FirewallSection**](FirewallSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_firewall_rule**
> FirewallRule read_firewall_rule(rule_id)

Read an Existing Rule

Return existing firewall rule information. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | 

try:
    # Read an Existing Rule
    api_response = api_instance.read_firewall_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->read_firewall_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_member_remove_member**
> ResourceReference remove_member_remove_member(object_id, deep_check=deep_check, object_type=object_type)

Remove an existing object from the exclude list

Remove an existing object from the exclude list

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
object_id = 'object_id_example' # str | identifier of the object
deep_check = false # bool | Check all parents (optional) (default to false)
object_type = 'object_type_example' # str | Object type of an entity (optional)

try:
    # Remove an existing object from the exclude list
    api_response = api_instance.remove_member_remove_member(object_id, deep_check=deep_check, object_type=object_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->remove_member_remove_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| identifier of the object | 
 **deep_check** | **bool**| Check all parents | [optional] [default to false]
 **object_type** | **str**| Object type of an entity | [optional] 

### Return type

[**ResourceReference**](ResourceReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_firewall_rule_stats_reset**
> reset_firewall_rule_stats_reset(category)

Reset firewall rule statistics

Sets firewall rule statistics counter to zero. This operation is supported for given category, for example: L3DFW i.e. for all layer3 firewall (transport nodes only) rules or L3EDGE i.e. for all layer3 edge firewall (edge nodes only) rules or L3BRIDGEPORT i.e. for all layer3 bridge port firewall (bridge ports only) rules. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str | Aggregation statistic category

try:
    # Reset firewall rule statistics
    api_instance.reset_firewall_rule_stats_reset(category)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->reset_firewall_rule_stats_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Aggregation statistic category | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revise_rule_revise**
> FirewallRule revise_rule_revise(body, section_id, rule_id, id=id, operation=operation)

Update an Existing Rule and Reorder the Rule

Modifies existing firewall rule along with relative position among other firewall rules inside a firewall section. Revising firewall rule in a section modifies parent section entity and simultaneous update (modify) operations on same section are not allowed to prevent overwriting stale contents to firewall section. If a concurrent update is performed, HTTP response code 409 will be returned to the client operating on stale data. That client should retrieve the firewall section again and re-apply its update. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallRule() # FirewallRule | 
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Update an Existing Rule and Reorder the Rule
    api_response = api_instance.revise_rule_revise(body, section_id, rule_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->revise_rule_revise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallRule**](FirewallRule.md)|  | 
 **section_id** | **str**|  | 
 **rule_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revise_section_revise**
> FirewallSection revise_section_revise(body, section_id, id=id, operation=operation)

Update an Existing Section, Including Its Position

Modifies an existing firewall section along with its relative position among other firewall sections in the system. Simultaneous update (modify) operations on same section are not allowed to prevent overwriting stale contents to firewall section. If a concurrent update is performed, HTTP response code 409 will be returned to the client operating on stale data. That client should retrieve the firewall section again and re-apply its update. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallSection() # FirewallSection | 
section_id = 'section_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Update an Existing Section, Including Its Position
    api_response = api_instance.revise_section_revise(body, section_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->revise_section_revise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallSection**](FirewallSection.md)|  | 
 **section_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**FirewallSection**](FirewallSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revise_section_with_rules_revise_with_rules**
> FirewallSectionRuleList revise_section_with_rules_revise_with_rules(body, section_id, id=id, operation=operation)

Update an Existing Section with Rules

Modifies an existing firewall section along with its relative position among other firewall sections with rules. When invoked on a large number of rules, this API is supported only at low rates of invocation (not more than 2 times per minute). The typical latency of this API with about 1024 rules is about 15 seconds in a cluster setup. This API should not be invoked with large payloads at automation speeds.  Instead, to move a section above or below another section, use: POST /api/v1/firewall/sections/&lt;section-id&gt;?action=revise  To modify rules, use: PUT /api/v1/firewall/sections/&lt;section-id&gt;/rules/&lt;rule-id&gt;  Simultaneous update (modify) operations on same section are not allowed to prevent overwriting stale contents to firewall section. If a concurrent update is performed, HTTP response code 409 will be returned to the client operating on stale data. That client should retrieve the firewall section again and re-apply its update. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallSectionRuleList() # FirewallSectionRuleList | 
section_id = 'section_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Update an Existing Section with Rules
    api_response = api_instance.revise_section_with_rules_revise_with_rules(body, section_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->revise_section_with_rules_revise_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallSectionRuleList**](FirewallSectionRuleList.md)|  | 
 **section_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**FirewallSectionRuleList**](FirewallSectionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_section_unlock**
> FirewallSection unlock_section_unlock(body, section_id)

Unlock a section

Unlock a section 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallSectionLock() # FirewallSectionLock | 
section_id = 'section_id_example' # str | 

try:
    # Unlock a section
    api_response = api_instance.unlock_section_unlock(body, section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->unlock_section_unlock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallSectionLock**](FirewallSectionLock.md)|  | 
 **section_id** | **str**|  | 

### Return type

[**FirewallSection**](FirewallSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_exclude_list**
> ExcludeList update_exclude_list(body)

Modify exclude list

Modify exclude list

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExcludeList() # ExcludeList | 

try:
    # Modify exclude list
    api_response = api_instance.update_exclude_list(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->update_exclude_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExcludeList**](ExcludeList.md)|  | 

### Return type

[**ExcludeList**](ExcludeList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firewall_profile**
> BaseFirewallProfile update_firewall_profile(body, profile_id)

Update a firewall profile.

Update user configurable properties of firewall profile. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.BaseFirewallProfile() # BaseFirewallProfile | 
profile_id = 'profile_id_example' # str | 

try:
    # Update a firewall profile.
    api_response = api_instance.update_firewall_profile(body, profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->update_firewall_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseFirewallProfile**](BaseFirewallProfile.md)|  | 
 **profile_id** | **str**|  | 

### Return type

[**BaseFirewallProfile**](BaseFirewallProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firewall_status**
> FirewallStatus update_firewall_status(body, context_type)

Update global firewall status for dfw context

Update global firewall status for dfw context

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallStatus() # FirewallStatus | 
context_type = 'context_type_example' # str | 

try:
    # Update global firewall status for dfw context
    api_response = api_instance.update_firewall_status(body, context_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->update_firewall_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallStatus**](FirewallStatus.md)|  | 
 **context_type** | **str**|  | 

### Return type

[**FirewallStatus**](FirewallStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> FirewallRule update_rule(body, section_id, rule_id)

Update an Existing Rule

Modifies existing firewall rule in a firewall section. Updating firewall rule in a section modifies parent section entity and simultaneous update (modify) operations on same section are not allowed to prevent overwriting stale contents to firewall section. If a concurrent update is performed, HTTP response code 409 will be returned to the client operating on stale data. That client should retrieve the firewall section again and re-apply its update. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallRule() # FirewallRule | 
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Update an Existing Rule
    api_response = api_instance.update_rule(body, section_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->update_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallRule**](FirewallRule.md)|  | 
 **section_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_section**
> FirewallSection update_section(body, section_id)

Update an Existing Section

Modifies the specified section, but does not modify the section's associated rules. Simultaneous update (modify) operations on same section are not allowed to prevent overwriting stale contents to firewall section. If a concurrent update is performed, HTTP response code 409 will be returned to the client operating on stale data. That client should retrieve the firewall section again and re-apply its update. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallSection() # FirewallSection | 
section_id = 'section_id_example' # str | 

try:
    # Update an Existing Section
    api_response = api_instance.update_section(body, section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->update_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallSection**](FirewallSection.md)|  | 
 **section_id** | **str**|  | 

### Return type

[**FirewallSection**](FirewallSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_section_with_rules_update_with_rules**
> FirewallSectionRuleList update_section_with_rules_update_with_rules(body, section_id)

Update an Existing Section, Including Its Rules

Modifies existing firewall section along with its association with rules. When invoked on a large number of rules, this API is supported only at low rates of invocation (not more than 2 times per minute). The typical latency of this API with about 1024 rules is about 15 seconds in a cluster setup. This API should not be invoked with large payloads at automation speeds.  Instead, to update rule content, use: PUT /api/v1/firewall/sections/&lt;section-id&gt;/rules/&lt;rule-id&gt;  Simultaneous update (modify) operations on same section are not allowed to prevent overwriting stale contents to firewall section. If a concurrent update is performed, HTTP response code 409 will be returned to the client operating on stale data. That client should retrieve the firewall section again and re-apply its update. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesFirewallApi(swagger_client.ApiClient(configuration))
body = swagger_client.FirewallSectionRuleList() # FirewallSectionRuleList | 
section_id = 'section_id_example' # str | 

try:
    # Update an Existing Section, Including Its Rules
    api_response = api_instance.update_section_with_rules_update_with_rules(body, section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesFirewallApi->update_section_with_rules_update_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallSectionRuleList**](FirewallSectionRuleList.md)|  | 
 **section_id** | **str**|  | 

### Return type

[**FirewallSectionRuleList**](FirewallSectionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

