# swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_instance_endpoint**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#add_instance_endpoint) | **POST** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-endpoints | Add an InstanceEndpoint for a Service Instance
[**add_service_attachment**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#add_service_attachment) | **POST** /serviceinsertion/service-attachments | Add a Service Attachment.
[**add_service_chain**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#add_service_chain) | **POST** /serviceinsertion/service-chains | Add Service Chain
[**add_service_insertion_exclude_list_member_add_member**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#add_service_insertion_exclude_list_member_add_member) | **POST** /serviceinsertion/excludelist?action&#x3D;add_member | Add a new member in the exclude list
[**add_service_insertion_rule_in_section**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#add_service_insertion_rule_in_section) | **POST** /serviceinsertion/sections/{section-id}/rules | Add a Single Rule in a Section
[**add_service_insertion_rules_in_section_create_multiple**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#add_service_insertion_rules_in_section_create_multiple) | **POST** /serviceinsertion/sections/{section-id}/rules?action&#x3D;create_multiple | Add Multiple Rules in a Section
[**add_service_insertion_section**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#add_service_insertion_section) | **POST** /serviceinsertion/sections | Create a New Empty Section
[**add_service_insertion_section_with_rules_create_with_rules**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#add_service_insertion_section_with_rules_create_with_rules) | **POST** /serviceinsertion/sections?action&#x3D;create_with_rules | Create a Section with Rules
[**add_service_insertion_service**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#add_service_insertion_service) | **POST** /serviceinsertion/services | Create a Service-Insertion Service
[**add_service_instance**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#add_service_instance) | **POST** /serviceinsertion/services/{service-id}/service-instances | Add a Service Instance for a specified Service.
[**add_si_service_profile**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#add_si_service_profile) | **POST** /serviceinsertion/services/{service-id}/service-profiles | Add ServiceProfile for a given Service.
[**add_vendor_template**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#add_vendor_template) | **POST** /serviceinsertion/services/{service-id}/vendor-templates | Add Vendor Template for a given Service
[**create_solution_config**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#create_solution_config) | **POST** /serviceinsertion/services/{service-id}/solution-configs | Add Solution Config for a given Service
[**delete_instance_endpoint**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_instance_endpoint) | **DELETE** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-endpoints/{instance-endpoint-id} | Delete a particular InstanceEndpoint.
[**delete_service_attachment**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_service_attachment) | **DELETE** /serviceinsertion/service-attachments/{service-attachment-id} | Delete an existing service attachment
[**delete_service_chain**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_service_chain) | **DELETE** /serviceinsertion/service-chains/{service-chain-id} | Delete a Service Chain.
[**delete_service_deployment**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_service_deployment) | **DELETE** /serviceinsertion/services/{service-id}/service-deployments/{service-deployment-id} | Remove service deployment
[**delete_service_insertion_rule**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_service_insertion_rule) | **DELETE** /serviceinsertion/sections/{section-id}/rules/{rule-id} | Delete an Existing Rule
[**delete_service_insertion_section**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_service_insertion_section) | **DELETE** /serviceinsertion/sections/{section-id} | Delete an Existing Section and Its Associated Rules
[**delete_service_insertion_service**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_service_insertion_service) | **DELETE** /serviceinsertion/services/{service-id} | Delete an existing Service and the Service-Instance associated with it.
[**delete_service_instance**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_service_instance) | **DELETE** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id} | Delete an existing Service-Instance
[**delete_service_manager**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_service_manager) | **DELETE** /serviceinsertion/service-managers/{service-manager-id} | Delete service manager
[**delete_service_v_ms_delete**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_service_v_ms_delete) | **POST** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes?action&#x3D;delete | Remove service VMs either as standalone or HA
[**delete_si_service_profile**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_si_service_profile) | **DELETE** /serviceinsertion/services/{service-id}/service-profiles/{service-profile-id} | Delete a particular ServiceProfile.
[**delete_solution_config**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_solution_config) | **DELETE** /serviceinsertion/services/{service-id}/solution-configs/{solution-config-id} | Deletes solution config information.
[**delete_vendor_template**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#delete_vendor_template) | **DELETE** /serviceinsertion/services/{service-id}/vendor-templates/{vendor-template-id} | Delete a particular vendor tempalte.
[**deploy_service**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#deploy_service) | **POST** /serviceinsertion/services/{service-id}/service-deployments | Deploys a particular service
[**deploy_service_v_ms_deploy**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#deploy_service_v_ms_deploy) | **POST** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes?action&#x3D;deploy | Deploy and set up service VMs either as standalone or HA
[**get_instance_endpoint**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_instance_endpoint) | **GET** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-endpoints/{instance-endpoint-id} | Get a particular instance endpoint for a service instance.
[**get_runtime_interface_operational_status**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_runtime_interface_operational_status) | **GET** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes/{instance-runtime-id}/interfaces/{interface_index}/status | Get operational status for an interface
[**get_runtime_interface_statistics**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_runtime_interface_statistics) | **GET** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes/{instance-runtime-id}/interfaces/{interface_index}/statistics | Get statistics for a given interface identified by the interface index
[**get_service_attachment**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_attachment) | **GET** /serviceinsertion/service-attachments/{service-attachment-id} | Get a particular service attachment.
[**get_service_chain**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_chain) | **GET** /serviceinsertion/service-chains/{service-chain-id} | Get a particular service chain.
[**get_service_deployment**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_deployment) | **GET** /serviceinsertion/services/{service-id}/service-deployments/{service-deployment-id} | Get a particular service deployment.
[**get_service_deployment_state**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_deployment_state) | **GET** /serviceinsertion/services/{service-id}/service-deployments/{service-deployment-id}/state | Get Service-Deployment state for Service.
[**get_service_deployment_status**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_deployment_status) | **GET** /serviceinsertion/services/{service-id}/service-deployments/{service-deployment-id}/status | Get a particular service deployment status.
[**get_service_deployments**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_deployments) | **GET** /serviceinsertion/services/{service-id}/service-deployments | Get all service deployments for the given service id
[**get_service_insertion_exclude_list**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_insertion_exclude_list) | **GET** /serviceinsertion/excludelist | Get list of members in exclude list
[**get_service_insertion_rule**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_insertion_rule) | **GET** /serviceinsertion/sections/{section-id}/rules/{rule-id} | Read an Existing Rule
[**get_service_insertion_rules**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_insertion_rules) | **GET** /serviceinsertion/sections/{section-id}/rules | Get All the Rules for a Section
[**get_service_insertion_section**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_insertion_section) | **GET** /serviceinsertion/sections/{section-id} | Get an Existing Section
[**get_service_insertion_section_with_rules_list_with_rules**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_insertion_section_with_rules_list_with_rules) | **POST** /serviceinsertion/sections/{section-id}?action&#x3D;list_with_rules | Get an Existing Section, Including Rules
[**get_service_insertion_service**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_insertion_service) | **GET** /serviceinsertion/services/{service-id} | Get an existing Service
[**get_service_insertion_status**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_insertion_status) | **GET** /serviceinsertion/status/{context-type} | Get ServiceInsertion global status for a context
[**get_service_instance**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_instance) | **GET** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id} | Get Service-Instance for Service.
[**get_service_instance_ns_groups**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_instance_ns_groups) | **GET** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/group-associations | Get NSgroups for a given ServiceInstance.
[**get_service_instance_state**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_instance_state) | **GET** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/state | Get Service-Instance state for Service.
[**get_service_instance_status**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_instance_status) | **GET** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/status | Get Service-Instance status for Service.
[**get_service_manager**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_manager) | **GET** /serviceinsertion/service-managers/{service-manager-id} | Get service manager
[**get_service_profile_ns_groups**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_service_profile_ns_groups) | **GET** /serviceinsertion/services/{service-id}/service-profiles/{service-profile-id}/nsgroups | Get NSgroups for a given ServiceProfile.
[**get_si_service_profile**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_si_service_profile) | **GET** /serviceinsertion/services/{service-id}/service-profiles/{service-profile-id} | Get a particular ServiceProfile for a Service.
[**get_solution_config**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_solution_config) | **GET** /serviceinsertion/services/{service-id}/solution-configs/{solution-config-id} | Get Solution Config Information for a given solution config id.
[**get_vendor_template**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#get_vendor_template) | **GET** /serviceinsertion/services/{service-id}/vendor-templates/{vendor-template-id} | Get a particular vendor template for a given service.
[**list_instance_endpoints**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_instance_endpoints) | **GET** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-endpoints | List all InstanceEndpoints of a Service Instance.
[**list_instance_runtimes**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_instance_runtimes) | **GET** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes | Returns list of instance runtimes of service VM being deployed
[**list_service_attachments**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_service_attachments) | **GET** /serviceinsertion/service-attachments | Get all service attachments.
[**list_service_chain_mappings**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_service_chain_mappings) | **GET** /serviceinsertion/services/{service-id}/service-profiles/{service-profile-id}/service-chain-mappings | List all ServiceChainMappings.
[**list_service_chains**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_service_chains) | **GET** /serviceinsertion/service-chains | List all ServiceChains.
[**list_service_insertion_sections**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_service_insertion_sections) | **GET** /serviceinsertion/sections | List All Service Insertion Sections
[**list_service_insertion_services**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_service_insertion_services) | **GET** /serviceinsertion/services | List all Service-Insertion Services.
[**list_service_insertion_status**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_service_insertion_status) | **GET** /serviceinsertion/status | List all service insertion status for supported contexts
[**list_service_instances**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_service_instances) | **GET** /serviceinsertion/service-instances | Get all Service-Instances present in system
[**list_service_instances_for_service**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_service_instances_for_service) | **GET** /serviceinsertion/services/{service-id}/service-instances | Get all Service-Instances for Service.
[**list_service_managers**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_service_managers) | **GET** /serviceinsertion/service-managers | List service managers
[**list_service_paths**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_service_paths) | **GET** /serviceinsertion/service-chains/{service-chain-id}/service-paths | List all service paths
[**list_si_service_profiles**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_si_service_profiles) | **GET** /serviceinsertion/services/{service-id}/service-profiles | List all Service Profiles of a Service.
[**list_solution_configs**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_solution_configs) | **GET** /serviceinsertion/services/{service-id}/solution-configs | Get Solution Config Information associated with a given service.
[**list_vendor_templates**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#list_vendor_templates) | **GET** /serviceinsertion/services/{service-id}/vendor-templates | List all VendorTemplates of a Service.
[**register_service_manager**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#register_service_manager) | **POST** /serviceinsertion/service-managers | Register service manager
[**remove_service_insertion_exclude_list_member_remove_member**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#remove_service_insertion_exclude_list_member_remove_member) | **POST** /serviceinsertion/excludelist?action&#x3D;remove_member | Remove an existing object from the exclude list
[**resolve_source_entities**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#resolve_source_entities) | **GET** /serviceinsertion/source-entities | Resolve &#x27;source node id&#x27; value to source entities.
[**revise_service_insertion_rule_revise**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#revise_service_insertion_rule_revise) | **POST** /serviceinsertion/sections/{section-id}/rules/{rule-id}?action&#x3D;revise | Update an Existing Rule and Reorder the Rule
[**revise_service_insertion_section_revise**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#revise_service_insertion_section_revise) | **POST** /serviceinsertion/sections/{section-id}?action&#x3D;revise | Update an Existing Section, Including Its Position
[**revise_service_insertion_section_with_rules_revise_with_rules**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#revise_service_insertion_section_with_rules_revise_with_rules) | **POST** /serviceinsertion/sections/{section-id}?action&#x3D;revise_with_rules | Update an Existing Section with Rules
[**update_service_attachment**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#update_service_attachment) | **PUT** /serviceinsertion/service-attachments/{service-attachment-id} | Update an existing service attachment.
[**update_service_deployment**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#update_service_deployment) | **PUT** /serviceinsertion/services/{service-id}/service-deployments/{service-deployment-id} | Update an existing Service Deployment.
[**update_service_insertion_exclude_list**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#update_service_insertion_exclude_list) | **PUT** /serviceinsertion/excludelist | Modify exclude list
[**update_service_insertion_rule**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#update_service_insertion_rule) | **PUT** /serviceinsertion/sections/{section-id}/rules/{rule-id} | Update an Existing Rule
[**update_service_insertion_section**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#update_service_insertion_section) | **PUT** /serviceinsertion/sections/{section-id} | Update an Existing Section
[**update_service_insertion_section_with_rules_update_with_rules**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#update_service_insertion_section_with_rules_update_with_rules) | **POST** /serviceinsertion/sections/{section-id}?action&#x3D;update_with_rules | Update an Existing Section, Including Its Rules
[**update_service_insertion_service**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#update_service_insertion_service) | **PUT** /serviceinsertion/services/{service-id} | Update an existing Service
[**update_service_insertion_status**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#update_service_insertion_status) | **PUT** /serviceinsertion/status/{context-type} | Update global ServiceInsertion status for a context
[**update_service_instance**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#update_service_instance) | **PUT** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id} | Update an existing Service-Instance.
[**update_service_manager**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#update_service_manager) | **PUT** /serviceinsertion/service-managers/{service-manager-id} | Update service manager
[**update_service_vm_state**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#update_service_vm_state) | **POST** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes/{instance-runtime-id} | Update maintenance mode or runtime state of a service VM
[**update_solution_config**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#update_solution_config) | **PUT** /serviceinsertion/services/{service-id}/solution-configs/{solution-config-id} | Updates Solution Config for a given Service
[**upgrade_service_deployment_upgrade**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#upgrade_service_deployment_upgrade) | **POST** /serviceinsertion/services/{service-id}/service-deployments/{service-deployment-id}?action&#x3D;upgrade | Upgrade all VMs part of this service deployment to new Spec OVF.
[**upgrade_service_v_ms_upgrade**](ManagementPlaneAPISecurityServicesServiceInsertionApi.md#upgrade_service_v_ms_upgrade) | **POST** /serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes?action&#x3D;upgrade | Upgrade service VMs using newer version of OVF

# **add_instance_endpoint**
> InstanceEndpoint add_instance_endpoint(body, service_id, service_instance_id)

Add an InstanceEndpoint for a Service Instance

Adds a new instance endpoint. It belongs to one service instance and is attached to one service attachment. It represents a redirection target for a Rule. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.InstanceEndpoint() # InstanceEndpoint | 
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 

try:
    # Add an InstanceEndpoint for a Service Instance
    api_response = api_instance.add_instance_endpoint(body, service_id, service_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->add_instance_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InstanceEndpoint**](InstanceEndpoint.md)|  | 
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 

### Return type

[**InstanceEndpoint**](InstanceEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_service_attachment**
> ServiceAttachment add_service_attachment(body)

Add a Service Attachment.

Adds a new Service attachment. A service attachment represents a point on NSX entity (Example: Logical Router) to which service instance can be connected through an InstanceEndpoint. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceAttachment() # ServiceAttachment | 

try:
    # Add a Service Attachment.
    api_response = api_instance.add_service_attachment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->add_service_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceAttachment**](ServiceAttachment.md)|  | 

### Return type

[**ServiceAttachment**](ServiceAttachment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_service_chain**
> ServiceChain add_service_chain(body)

Add Service Chain

Adds a new service chain. Service Chains is can contain profile belonging to same or different Service(s). It represents a redirection target for a Rule. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceChain() # ServiceChain | 

try:
    # Add Service Chain
    api_response = api_instance.add_service_chain(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->add_service_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceChain**](ServiceChain.md)|  | 

### Return type

[**ServiceChain**](ServiceChain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_service_insertion_exclude_list_member_add_member**
> ResourceReference add_service_insertion_exclude_list_member_add_member(body)

Add a new member in the exclude list

Note- POST serviceinsertion excludelist API is deprecated. Please use the policy serviceinsertion excludelist API instead. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResourceReference() # ResourceReference | 

try:
    # Add a new member in the exclude list
    api_response = api_instance.add_service_insertion_exclude_list_member_add_member(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->add_service_insertion_exclude_list_member_add_member: %s\n" % e)
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

# **add_service_insertion_rule_in_section**
> ServiceInsertionRule add_service_insertion_rule_in_section(body, section_id, id=id, operation=operation)

Add a Single Rule in a Section

Adds a new serviceinsertion rule in existing serviceinsertion section. Note- POST service insertion section API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceInsertionRule() # ServiceInsertionRule | 
section_id = 'section_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Add a Single Rule in a Section
    api_response = api_instance.add_service_insertion_rule_in_section(body, section_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->add_service_insertion_rule_in_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceInsertionRule**](ServiceInsertionRule.md)|  | 
 **section_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**ServiceInsertionRule**](ServiceInsertionRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_service_insertion_rules_in_section_create_multiple**
> ServiceInsertionRuleList add_service_insertion_rules_in_section_create_multiple(body, section_id, id=id, operation=operation)

Add Multiple Rules in a Section

Create multiple serviceinsertion rules in existing serviceinsertion section bounded by limit of 1000 serviceinsertion rules per section. Note- POST service insertion rules API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceInsertionRuleList() # ServiceInsertionRuleList | 
section_id = 'section_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Add Multiple Rules in a Section
    api_response = api_instance.add_service_insertion_rules_in_section_create_multiple(body, section_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->add_service_insertion_rules_in_section_create_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceInsertionRuleList**](ServiceInsertionRuleList.md)|  | 
 **section_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**ServiceInsertionRuleList**](ServiceInsertionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_service_insertion_section**
> ServiceInsertionSection add_service_insertion_section(body, id=id, operation=operation)

Create a New Empty Section

Creates new empty Service Insertion section in the system. Note- POST service insertion section API is deprecated. Please use the policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceInsertionSection() # ServiceInsertionSection | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Create a New Empty Section
    api_response = api_instance.add_service_insertion_section(body, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->add_service_insertion_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceInsertionSection**](ServiceInsertionSection.md)|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**ServiceInsertionSection**](ServiceInsertionSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_service_insertion_section_with_rules_create_with_rules**
> ServiceInsertionSectionRuleList add_service_insertion_section_with_rules_create_with_rules(body, id=id, operation=operation)

Create a Section with Rules

Creates a new serviceinsertion section with rules. The limit on the number of rules is defined by maxItems in collection types for ServiceInsertionRule (ServiceInsertionRuleXXXList types). When invoked on a section with a large number of rules, this API is supported only at low rates of invocation (not more than 4-5 times per minute). The typical latency of this API with about 1024 rules is about 4-5 seconds. This API should not be invoked with large payloads at automation speeds. More than 50 rules are not supported.  Instead, to create sections, use: POST /api/v1/serviceinsertion/sections  To create rules, use: POST /api/v1/serviceinsertion/sections/&lt;section-id&gt;/rules Note- POST service insertion section creation with rules API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceInsertionSectionRuleList() # ServiceInsertionSectionRuleList | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Create a Section with Rules
    api_response = api_instance.add_service_insertion_section_with_rules_create_with_rules(body, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->add_service_insertion_section_with_rules_create_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceInsertionSectionRuleList**](ServiceInsertionSectionRuleList.md)|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**ServiceInsertionSectionRuleList**](ServiceInsertionSectionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_service_insertion_service**
> ServiceDefinition add_service_insertion_service(body)

Create a Service-Insertion Service

Creates new Service-Insertion Service in the system. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceDefinition() # ServiceDefinition | 

try:
    # Create a Service-Insertion Service
    api_response = api_instance.add_service_insertion_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->add_service_insertion_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceDefinition**](ServiceDefinition.md)|  | 

### Return type

[**ServiceDefinition**](ServiceDefinition.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_service_instance**
> BaseServiceInstance add_service_instance(body, service_id)

Add a Service Instance for a specified Service.

Adds a new Service-Instance under the specified Service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.BaseServiceInstance() # BaseServiceInstance | 
service_id = 'service_id_example' # str | 

try:
    # Add a Service Instance for a specified Service.
    api_response = api_instance.add_service_instance(body, service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->add_service_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseServiceInstance**](BaseServiceInstance.md)|  | 
 **service_id** | **str**|  | 

### Return type

[**BaseServiceInstance**](BaseServiceInstance.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_si_service_profile**
> BaseServiceProfile add_si_service_profile(body, service_id)

Add ServiceProfile for a given Service.

Adds a new service profile. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.BaseServiceProfile() # BaseServiceProfile | 
service_id = 'service_id_example' # str | 

try:
    # Add ServiceProfile for a given Service.
    api_response = api_instance.add_si_service_profile(body, service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->add_si_service_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseServiceProfile**](BaseServiceProfile.md)|  | 
 **service_id** | **str**|  | 

### Return type

[**BaseServiceProfile**](BaseServiceProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_vendor_template**
> VendorTemplate add_vendor_template(body, service_id)

Add Vendor Template for a given Service

Adds a new vendor template. Vendor templates are service level objects, registered to be used in Service Profiles. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.VendorTemplate() # VendorTemplate | 
service_id = 'service_id_example' # str | 

try:
    # Add Vendor Template for a given Service
    api_response = api_instance.add_vendor_template(body, service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->add_vendor_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VendorTemplate**](VendorTemplate.md)|  | 
 **service_id** | **str**|  | 

### Return type

[**VendorTemplate**](VendorTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_solution_config**
> SolutionConfig create_solution_config(body, service_id)

Add Solution Config for a given Service

Adds a solution config. Solution Config are service level objects, required for configuring the NXGI partner Service after deployment. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.SolutionConfig() # SolutionConfig | 
service_id = 'service_id_example' # str | 

try:
    # Add Solution Config for a given Service
    api_response = api_instance.create_solution_config(body, service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->create_solution_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolutionConfig**](SolutionConfig.md)|  | 
 **service_id** | **str**|  | 

### Return type

[**SolutionConfig**](SolutionConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_instance_endpoint**
> delete_instance_endpoint(service_id, service_instance_id, instance_endpoint_id)

Delete a particular InstanceEndpoint.

Delete instance endpoint information for a given instace endpoint. Please make sure to delete all the Service Insertion Rules, which refer to this Endpoint as 'redirect_tos' target. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 
instance_endpoint_id = 'instance_endpoint_id_example' # str | 

try:
    # Delete a particular InstanceEndpoint.
    api_instance.delete_instance_endpoint(service_id, service_instance_id, instance_endpoint_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_instance_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 
 **instance_endpoint_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_attachment**
> delete_service_attachment(service_attachment_id)

Delete an existing service attachment

Delete existing service attachment from system. Before deletion, please make sure that, no instance endpoints are connected to this attachment. In turn no appliance should be connected to this attachment. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_attachment_id = 'service_attachment_id_example' # str | 

try:
    # Delete an existing service attachment
    api_instance.delete_service_attachment(service_attachment_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_service_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_attachment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_chain**
> delete_service_chain(service_chain_id)

Delete a Service Chain.

Delete a particular service chain. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_chain_id = 'service_chain_id_example' # str | 

try:
    # Delete a Service Chain.
    api_instance.delete_service_chain(service_chain_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_service_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_chain_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_deployment**
> delete_service_deployment(service_id, service_deployment_id, force=force)

Remove service deployment

Remove the service deployment. Will remove all the Service VMs that were created as part of this deployment. User can send optional force delete option which will force remove the deployment, but should be used only when the regular delete is not working. Regular delete will ensure proper cleanup of Service VMs and related objects. Directly calling this API without trying regular undeploy will result in unexpected results, and orphan objects. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_deployment_id = 'service_deployment_id_example' # str | 
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Remove service deployment
    api_instance.delete_service_deployment(service_id, service_deployment_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_service_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_deployment_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_insertion_rule**
> delete_service_insertion_rule(section_id, rule_id)

Delete an Existing Rule

Delete existing serviceinsertion rule in a serviceinsertion section. Note- DELETE service insertion rule API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Delete an Existing Rule
    api_instance.delete_service_insertion_rule(section_id, rule_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_service_insertion_rule: %s\n" % e)
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

# **delete_service_insertion_section**
> delete_service_insertion_section(section_id, cascade=cascade)

Delete an Existing Section and Its Associated Rules

Removes serviceinsertion section from the system. ServiceInsertion section with rules can only be deleted by passing \"cascade=true\" parameter. Note- DELETE service insertion section API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
cascade = false # bool | Flag to cascade delete of this object to all it's child objects. (optional) (default to false)

try:
    # Delete an Existing Section and Its Associated Rules
    api_instance.delete_service_insertion_section(section_id, cascade=cascade)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_service_insertion_section: %s\n" % e)
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

# **delete_service_insertion_service**
> delete_service_insertion_service(service_id, cascade=cascade)

Delete an existing Service and the Service-Instance associated with it.

Removes Service-Insertion Service from the system. A Service with Service-Instances can only be deleted by passing \"cascade=true\" parameter. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
cascade = false # bool | Flag to cascade delete all the child objects, associated with it. (optional) (default to false)

try:
    # Delete an existing Service and the Service-Instance associated with it.
    api_instance.delete_service_insertion_service(service_id, cascade=cascade)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_service_insertion_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **cascade** | **bool**| Flag to cascade delete all the child objects, associated with it. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_instance**
> delete_service_instance(service_id, service_instance_id)

Delete an existing Service-Instance

Delete existing Service-Instance for a given Service-Insertion Service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 

try:
    # Delete an existing Service-Instance
    api_instance.delete_service_instance(service_id, service_instance_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_service_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_manager**
> delete_service_manager(service_manager_id)

Delete service manager

Delete service-manager which is registered with NSX with basic details like name, username, password.

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_manager_id = 'service_manager_id_example' # str | 

try:
    # Delete service manager
    api_instance.delete_service_manager(service_manager_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_service_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_manager_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_v_ms_delete**
> delete_service_v_ms_delete(service_id, service_instance_id)

Remove service VMs either as standalone or HA

Undeploy one service VM as standalone or two service VMs as HA. Associated deployment information and instance runtime will also be deleted once service VMs have been un-deployed successfully. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 

try:
    # Remove service VMs either as standalone or HA
    api_instance.delete_service_v_ms_delete(service_id, service_instance_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_service_v_ms_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_si_service_profile**
> delete_si_service_profile(service_id, service_profile_id)

Delete a particular ServiceProfile.

Delete service profile for a given service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_profile_id = 'service_profile_id_example' # str | 

try:
    # Delete a particular ServiceProfile.
    api_instance.delete_si_service_profile(service_id, service_profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_si_service_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_solution_config**
> delete_solution_config(service_id, solution_config_id)

Deletes solution config information.

Deletes solution config information for a given service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
solution_config_id = 'solution_config_id_example' # str | 

try:
    # Deletes solution config information.
    api_instance.delete_solution_config(service_id, solution_config_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_solution_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **solution_config_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vendor_template**
> delete_vendor_template(service_id, vendor_template_id)

Delete a particular vendor tempalte.

Delete vendor template information for a given service. Please make sure to delete all the Service Profile(s), which refer to this vendor tempalte before deleting the template itself. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
vendor_template_id = 'vendor_template_id_example' # str | 

try:
    # Delete a particular vendor tempalte.
    api_instance.delete_vendor_template(service_id, vendor_template_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->delete_vendor_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **vendor_template_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_service**
> ServiceDeployment deploy_service(body, service_id)

Deploys a particular service

This will deploy a particular service on a given cluster / host. Internally multiple service instance can be created during the deployment. If there are no issues in the parameters, the call returns immediately, and the service VMs will be deployed asynchronously. To get the overall status of the deployment or to get the status of individual service vm, please use the deployment status APIs. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceDeployment() # ServiceDeployment | 
service_id = 'service_id_example' # str | 

try:
    # Deploys a particular service
    api_response = api_instance.deploy_service(body, service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->deploy_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceDeployment**](ServiceDeployment.md)|  | 
 **service_id** | **str**|  | 

### Return type

[**ServiceDeployment**](ServiceDeployment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_service_v_ms_deploy**
> deploy_service_v_ms_deploy(service_id, service_instance_id)

Deploy and set up service VMs either as standalone or HA

Deploys one service VM as standalone, or two service VMs as HA where one VM is active and another one is standby.  During the deployment of service VMs, service will be set up based on deployment events using callbacks. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 

try:
    # Deploy and set up service VMs either as standalone or HA
    api_instance.deploy_service_v_ms_deploy(service_id, service_instance_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->deploy_service_v_ms_deploy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_endpoint**
> InstanceEndpoint get_instance_endpoint(service_id, service_instance_id, instance_endpoint_id)

Get a particular instance endpoint for a service instance.

Returns detailed Endpoint information for a given InstanceEndpoint. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 
instance_endpoint_id = 'instance_endpoint_id_example' # str | 

try:
    # Get a particular instance endpoint for a service instance.
    api_response = api_instance.get_instance_endpoint(service_id, service_instance_id, instance_endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_instance_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 
 **instance_endpoint_id** | **str**|  | 

### Return type

[**InstanceEndpoint**](InstanceEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runtime_interface_operational_status**
> RuntimeInterfaceOperationalStatus get_runtime_interface_operational_status(service_id, service_instance_id, instance_runtime_id, interface_index, source=source)

Get operational status for an interface

Returns operational status of a specified interface

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 
instance_runtime_id = 'instance_runtime_id_example' # str | 
interface_index = 'interface_index_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get operational status for an interface
    api_response = api_instance.get_runtime_interface_operational_status(service_id, service_instance_id, instance_runtime_id, interface_index, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_runtime_interface_operational_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 
 **instance_runtime_id** | **str**|  | 
 **interface_index** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**RuntimeInterfaceOperationalStatus**](RuntimeInterfaceOperationalStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runtime_interface_statistics**
> RuntimeInterfaceStatistics get_runtime_interface_statistics(service_id, service_instance_id, instance_runtime_id, interface_index, source=source)

Get statistics for a given interface identified by the interface index

Returns statistics of a specified interface via associated logical port. If the logical port is attached to a logical router port, query parameter \"source=realtime\" is not supported. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 
instance_runtime_id = 'instance_runtime_id_example' # str | 
interface_index = 'interface_index_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get statistics for a given interface identified by the interface index
    api_response = api_instance.get_runtime_interface_statistics(service_id, service_instance_id, instance_runtime_id, interface_index, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_runtime_interface_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 
 **instance_runtime_id** | **str**|  | 
 **interface_index** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**RuntimeInterfaceStatistics**](RuntimeInterfaceStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_attachment**
> ServiceAttachment get_service_attachment(service_attachment_id)

Get a particular service attachment.

Returns detailed Attachment information for a given service attachment. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_attachment_id = 'service_attachment_id_example' # str | 

try:
    # Get a particular service attachment.
    api_response = api_instance.get_service_attachment(service_attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_attachment_id** | **str**|  | 

### Return type

[**ServiceAttachment**](ServiceAttachment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_chain**
> ServiceChain get_service_chain(service_chain_id)

Get a particular service chain.

Returns detailed service chain information. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_chain_id = 'service_chain_id_example' # str | 

try:
    # Get a particular service chain.
    api_response = api_instance.get_service_chain(service_chain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_chain_id** | **str**|  | 

### Return type

[**ServiceChain**](ServiceChain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_deployment**
> ServiceDeployment get_service_deployment(service_id, service_deployment_id)

Get a particular service deployment.

Returns detail of service deployment. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_deployment_id = 'service_deployment_id_example' # str | 

try:
    # Get a particular service deployment.
    api_response = api_instance.get_service_deployment(service_id, service_deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_deployment_id** | **str**|  | 

### Return type

[**ServiceDeployment**](ServiceDeployment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_deployment_state**
> ConfigurationState get_service_deployment_state(service_id, service_deployment_id)

Get Service-Deployment state for Service.

Returns configuration state of deployed partner service using service insertion framework. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_deployment_id = 'service_deployment_id_example' # str | 

try:
    # Get Service-Deployment state for Service.
    api_response = api_instance.get_service_deployment_state(service_id, service_deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_deployment_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_deployment_id** | **str**|  | 

### Return type

[**ConfigurationState**](ConfigurationState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_deployment_status**
> ServiceDeploymentStatus get_service_deployment_status(service_id, service_deployment_id, source=source)

Get a particular service deployment status.

Returns current status of the deployment of partner service. Available only for EPP Services. By default this API would return cached status. Caching happens every 3 minutes. For realtime status, query parameter \"source=realtime\" needs to be passed. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_deployment_id = 'service_deployment_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get a particular service deployment status.
    api_response = api_instance.get_service_deployment_status(service_id, service_deployment_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_deployment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_deployment_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**ServiceDeploymentStatus**](ServiceDeploymentStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_deployments**
> ServiceDeploymentListResult get_service_deployments(service_id)

Get all service deployments for the given service id

Returns the list of deployments for the given service 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 

try:
    # Get all service deployments for the given service id
    api_response = api_instance.get_service_deployments(service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**ServiceDeploymentListResult**](ServiceDeploymentListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_insertion_exclude_list**
> SIExcludeList get_service_insertion_exclude_list()

Get list of members in exclude list

Note- GET serviceinsertion excludelist API is deprecated. Please use the policy serviceinsertion excludelist API instead. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))

try:
    # Get list of members in exclude list
    api_response = api_instance.get_service_insertion_exclude_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_insertion_exclude_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SIExcludeList**](SIExcludeList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_insertion_rule**
> ServiceInsertionRule get_service_insertion_rule(section_id, rule_id)

Read an Existing Rule

Return existing serviceinsertion rule information in a serviceinsertion section. Note- GET service insertion rule API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Read an Existing Rule
    api_response = api_instance.get_service_insertion_rule(section_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_insertion_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**ServiceInsertionRule**](ServiceInsertionRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_insertion_rules**
> ServiceInsertionRuleListResult get_service_insertion_rules(section_id, applied_tos=applied_tos, cursor=cursor, destinations=destinations, filter_type=filter_type, included_fields=included_fields, page_size=page_size, services=services, sort_ascending=sort_ascending, sort_by=sort_by, sources=sources)

Get All the Rules for a Section

Return all serviceinsertion rule(s) information for a given serviceinsertion section. Note- GET service insertion rules API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
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
    api_response = api_instance.get_service_insertion_rules(section_id, applied_tos=applied_tos, cursor=cursor, destinations=destinations, filter_type=filter_type, included_fields=included_fields, page_size=page_size, services=services, sort_ascending=sort_ascending, sort_by=sort_by, sources=sources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_insertion_rules: %s\n" % e)
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

[**ServiceInsertionRuleListResult**](ServiceInsertionRuleListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_insertion_section**
> ServiceInsertionSection get_service_insertion_section(section_id)

Get an Existing Section

Returns information about serviceinsertion section for the identifier. Note- GET service insertion section API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 

try:
    # Get an Existing Section
    api_response = api_instance.get_service_insertion_section(section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_insertion_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 

### Return type

[**ServiceInsertionSection**](ServiceInsertionSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_insertion_section_with_rules_list_with_rules**
> ServiceInsertionSectionRuleList get_service_insertion_section_with_rules_list_with_rules(section_id)

Get an Existing Section, Including Rules

Returns serviceinsertion section information with rules for a section identifier. When invoked on a section with a large number of rules, this API is supported only at low rates of invocation (not more than 4-5 times per minute). The typical latency of this API with about 1024 rules is about 4-5 seconds. This API should not be invoked with large payloads at automation speeds. More than 50 rules are not supported.  Instead, to read serviceinsertion rules, use: GET /api/v1/serviceinsertion/sections/&lt;section-id&gt;/rules with the appropriate page_size. Note- GET service insertion section with rules API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
section_id = 'section_id_example' # str | 

try:
    # Get an Existing Section, Including Rules
    api_response = api_instance.get_service_insertion_section_with_rules_list_with_rules(section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_insertion_section_with_rules_list_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | 

### Return type

[**ServiceInsertionSectionRuleList**](ServiceInsertionSectionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_insertion_service**
> ServiceDefinition get_service_insertion_service(service_id)

Get an existing Service

Returns information about Service-Insertion Service with the given identifier. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 

try:
    # Get an existing Service
    api_response = api_instance.get_service_insertion_service(service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_insertion_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**ServiceDefinition**](ServiceDefinition.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_insertion_status**
> ServiceInsertionStatus get_service_insertion_status(context_type)

Get ServiceInsertion global status for a context

Get ServiceInsertion global status for a context

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
context_type = 'context_type_example' # str | 

try:
    # Get ServiceInsertion global status for a context
    api_response = api_instance.get_service_insertion_status(context_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_insertion_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_type** | **str**|  | 

### Return type

[**ServiceInsertionStatus**](ServiceInsertionStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_instance**
> BaseServiceInstance get_service_instance(service_id, service_instance_id)

Get Service-Instance for Service.

Returns Service-Instance information for a given Service-Insertion Service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 

try:
    # Get Service-Instance for Service.
    api_response = api_instance.get_service_instance(service_id, service_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 

### Return type

[**BaseServiceInstance**](BaseServiceInstance.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_instance_ns_groups**
> ServiceInstanceNSGroups get_service_instance_ns_groups(service_id, service_instance_id)

Get NSgroups for a given ServiceInstance.

Returns list of NSGroups used in Service Insertion North-South rules for a given Service Instance. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 

try:
    # Get NSgroups for a given ServiceInstance.
    api_response = api_instance.get_service_instance_ns_groups(service_id, service_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_instance_ns_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 

### Return type

[**ServiceInstanceNSGroups**](ServiceInstanceNSGroups.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_instance_state**
> ConfigurationState get_service_instance_state(service_id, service_instance_id)

Get Service-Instance state for Service.

Returns configuration state of one instance of a deployed partner service using service insertion framework. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 

try:
    # Get Service-Instance state for Service.
    api_response = api_instance.get_service_instance_state(service_id, service_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_instance_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 

### Return type

[**ConfigurationState**](ConfigurationState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_instance_status**
> ServiceInstanceStatus get_service_instance_status(service_id, service_instance_id, source=source)

Get Service-Instance status for Service.

Returns status of one instance of a deployed partner service using service insertion framework. By default this API would return cached status. Caching happens every 3 minutes. For realtime status, query parameter \"source=realtime\" needs to be passed. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get Service-Instance status for Service.
    api_response = api_instance.get_service_instance_status(service_id, service_instance_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_instance_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**ServiceInstanceStatus**](ServiceInstanceStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_manager**
> ServiceManager get_service_manager(service_manager_id)

Get service manager

Retrieve service-manager details like name, username, password, vendor ID, thumbprint for a given ID.

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_manager_id = 'service_manager_id_example' # str | 

try:
    # Get service manager
    api_response = api_instance.get_service_manager(service_manager_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_manager_id** | **str**|  | 

### Return type

[**ServiceManager**](ServiceManager.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_profile_ns_groups**
> ServiceProfileNSGroups get_service_profile_ns_groups(service_id, service_profile_id)

Get NSgroups for a given ServiceProfile.

Returns list of NSGroups used in Service Insertion rules for a given Service Profile. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_profile_id = 'service_profile_id_example' # str | 

try:
    # Get NSgroups for a given ServiceProfile.
    api_response = api_instance.get_service_profile_ns_groups(service_id, service_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_service_profile_ns_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_profile_id** | **str**|  | 

### Return type

[**ServiceProfileNSGroups**](ServiceProfileNSGroups.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_si_service_profile**
> BaseServiceProfile get_si_service_profile(service_id, service_profile_id)

Get a particular ServiceProfile for a Service.

Returns detailed service profile information for a given Service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_profile_id = 'service_profile_id_example' # str | 

try:
    # Get a particular ServiceProfile for a Service.
    api_response = api_instance.get_si_service_profile(service_id, service_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_si_service_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_profile_id** | **str**|  | 

### Return type

[**BaseServiceProfile**](BaseServiceProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution_config**
> SolutionConfig get_solution_config(service_id, solution_config_id)

Get Solution Config Information for a given solution config id.

Returns Solution Config information for a given solution config id. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
solution_config_id = 'solution_config_id_example' # str | 

try:
    # Get Solution Config Information for a given solution config id.
    api_response = api_instance.get_solution_config(service_id, solution_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_solution_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **solution_config_id** | **str**|  | 

### Return type

[**SolutionConfig**](SolutionConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_template**
> VendorTemplate get_vendor_template(service_id, vendor_template_id)

Get a particular vendor template for a given service.

Returns detailed vendor template information for a given service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
vendor_template_id = 'vendor_template_id_example' # str | 

try:
    # Get a particular vendor template for a given service.
    api_response = api_instance.get_vendor_template(service_id, vendor_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->get_vendor_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **vendor_template_id** | **str**|  | 

### Return type

[**VendorTemplate**](VendorTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instance_endpoints**
> InstanceEndpointListResult list_instance_endpoints(service_id, service_instance_id)

List all InstanceEndpoints of a Service Instance.

List all InstanceEndpoints of a service instance. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 

try:
    # List all InstanceEndpoints of a Service Instance.
    api_response = api_instance.list_instance_endpoints(service_id, service_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_instance_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 

### Return type

[**InstanceEndpointListResult**](InstanceEndpointListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instance_runtimes**
> InstanceRuntimeListResult list_instance_runtimes(service_id, service_instance_id)

Returns list of instance runtimes of service VM being deployed

Returns list of instance runtimes of service VMs being deployed for a given service instance id 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 

try:
    # Returns list of instance runtimes of service VM being deployed
    api_response = api_instance.list_instance_runtimes(service_id, service_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_instance_runtimes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 

### Return type

[**InstanceRuntimeListResult**](InstanceRuntimeListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_attachments**
> ServiceAttachmentListResult list_service_attachments()

Get all service attachments.

Returns all Service-Attachement(s) present in the system. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))

try:
    # Get all service attachments.
    api_response = api_instance.list_service_attachments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_service_attachments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceAttachmentListResult**](ServiceAttachmentListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_chain_mappings**
> ServiceChainMappingListResult list_service_chain_mappings(service_id, service_profile_id)

List all ServiceChainMappings.

List all service chain mappings in the system for the given service profile. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_profile_id = 'service_profile_id_example' # str | 

try:
    # List all ServiceChainMappings.
    api_response = api_instance.list_service_chain_mappings(service_id, service_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_service_chain_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_profile_id** | **str**|  | 

### Return type

[**ServiceChainMappingListResult**](ServiceChainMappingListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_chains**
> ServiceChainListResult list_service_chains()

List all ServiceChains.

List all service chains in the system. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))

try:
    # List all ServiceChains.
    api_response = api_instance.list_service_chains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_service_chains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceChainListResult**](ServiceChainListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_insertion_sections**
> ServiceInsertionSectionListResult list_service_insertion_sections(applied_tos=applied_tos, cursor=cursor, destinations=destinations, exclude_applied_to_type=exclude_applied_to_type, filter_type=filter_type, include_applied_to_type=include_applied_to_type, included_fields=included_fields, page_size=page_size, services=services, sort_ascending=sort_ascending, sort_by=sort_by, sources=sources, type=type)

List All Service Insertion Sections

List all Service Insertion section in paginated form. A default page size is limited to 1000 sections. By default, the list of section is filtered by L3REDIRECT type. Note- GET service insertion sections API is deprecated. Please use the policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
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
type = 'L3REDIRECT' # str | Section Type (optional) (default to L3REDIRECT)

try:
    # List All Service Insertion Sections
    api_response = api_instance.list_service_insertion_sections(applied_tos=applied_tos, cursor=cursor, destinations=destinations, exclude_applied_to_type=exclude_applied_to_type, filter_type=filter_type, include_applied_to_type=include_applied_to_type, included_fields=included_fields, page_size=page_size, services=services, sort_ascending=sort_ascending, sort_by=sort_by, sources=sources, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_service_insertion_sections: %s\n" % e)
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
 **type** | **str**| Section Type | [optional] [default to L3REDIRECT]

### Return type

[**ServiceInsertionSectionListResult**](ServiceInsertionSectionListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_insertion_services**
> ServiceInsertionServiceListResult list_service_insertion_services()

List all Service-Insertion Services.

List all Service-Insertion Service Definitions. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))

try:
    # List all Service-Insertion Services.
    api_response = api_instance.list_service_insertion_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_service_insertion_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceInsertionServiceListResult**](ServiceInsertionServiceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_insertion_status**
> ServiceInsertionStatusListResult list_service_insertion_status()

List all service insertion status for supported contexts

List all service insertion status for supported contexts

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))

try:
    # List all service insertion status for supported contexts
    api_response = api_instance.list_service_insertion_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_service_insertion_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceInsertionStatusListResult**](ServiceInsertionStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_instances**
> ServiceInstanceListResult list_service_instances(deployed_to=deployed_to, service_deployment_id=service_deployment_id)

Get all Service-Instances present in system

Returns all Service-Instance(s) of all Services present in system. When request parameter (deployed_to or service_deployment_id) is provided as a part of request, it will filter out Service-Instances accordingly. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
deployed_to = 'deployed_to_example' # str | Deployed_to referenced by service instances present in system (optional)
service_deployment_id = 'service_deployment_id_example' # str | Service Deployment Id using which the instances were deployed (optional)

try:
    # Get all Service-Instances present in system
    api_response = api_instance.list_service_instances(deployed_to=deployed_to, service_deployment_id=service_deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_service_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployed_to** | **str**| Deployed_to referenced by service instances present in system | [optional] 
 **service_deployment_id** | **str**| Service Deployment Id using which the instances were deployed | [optional] 

### Return type

[**ServiceInstanceListResult**](ServiceInstanceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_instances_for_service**
> ServiceInstanceListResult list_service_instances_for_service(service_id)

Get all Service-Instances for Service.

Returns all Service-Instance(s) for a given Service-Insertion Service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 

try:
    # Get all Service-Instances for Service.
    api_response = api_instance.list_service_instances_for_service(service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_service_instances_for_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**ServiceInstanceListResult**](ServiceInstanceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_managers**
> ServiceManagerListResult list_service_managers()

List service managers

List all service managers. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))

try:
    # List service managers
    api_response = api_instance.list_service_managers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_service_managers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceManagerListResult**](ServiceManagerListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_paths**
> ServicePathListResult list_service_paths(service_chain_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List all service paths

List all service paths for the given service chain for the given service chain id NOTE: GET service paths api is deprecated, please use the policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_chain_id = 'service_chain_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List all service paths
    api_response = api_instance.list_service_paths(service_chain_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_service_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_chain_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ServicePathListResult**](ServicePathListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_si_service_profiles**
> SIServiceProfileListResult list_si_service_profiles(service_id)

List all Service Profiles of a Service.

List all service profiles of a service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 

try:
    # List all Service Profiles of a Service.
    api_response = api_instance.list_si_service_profiles(service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_si_service_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**SIServiceProfileListResult**](SIServiceProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_solution_configs**
> SolutionConfigListResult list_solution_configs(service_id)

Get Solution Config Information associated with a given service.

Returns Solution Config information for a given service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 

try:
    # Get Solution Config Information associated with a given service.
    api_response = api_instance.list_solution_configs(service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_solution_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**SolutionConfigListResult**](SolutionConfigListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vendor_templates**
> VendorTemplateListResult list_vendor_templates(service_id, vendor_template_name=vendor_template_name)

List all VendorTemplates of a Service.

List all vendor templates of a service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
vendor_template_name = 'vendor_template_name_example' # str | Name of vendor template (optional)

try:
    # List all VendorTemplates of a Service.
    api_response = api_instance.list_vendor_templates(service_id, vendor_template_name=vendor_template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->list_vendor_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **vendor_template_name** | **str**| Name of vendor template | [optional] 

### Return type

[**VendorTemplateListResult**](VendorTemplateListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_service_manager**
> ServiceManager register_service_manager(body)

Register service manager

Register service-manager with NSX with basic details like name, username, password.

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceManager() # ServiceManager | 

try:
    # Register service manager
    api_response = api_instance.register_service_manager(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->register_service_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceManager**](ServiceManager.md)|  | 

### Return type

[**ServiceManager**](ServiceManager.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_service_insertion_exclude_list_member_remove_member**
> ResourceReference remove_service_insertion_exclude_list_member_remove_member(object_id)

Remove an existing object from the exclude list

Note- POST serviceinsertion excludelist API is deprecated. Please use the policy serviceinsertion excludelist API instead. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
object_id = 'object_id_example' # str | Identifier of the object

try:
    # Remove an existing object from the exclude list
    api_response = api_instance.remove_service_insertion_exclude_list_member_remove_member(object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->remove_service_insertion_exclude_list_member_remove_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier of the object | 

### Return type

[**ResourceReference**](ResourceReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_source_entities**
> SourceEntityResult resolve_source_entities(source_node_value)

Resolve 'source node id' value to source entities.

Service insertion data path inserts unique 'source node id' value into each packet. This API can be used to identify the source of the packet using this value. It can be resolved to multiple source entities. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
source_node_value = 'source_node_value_example' # str | value

try:
    # Resolve 'source node id' value to source entities.
    api_response = api_instance.resolve_source_entities(source_node_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->resolve_source_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_node_value** | **str**| value | 

### Return type

[**SourceEntityResult**](SourceEntityResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revise_service_insertion_rule_revise**
> ServiceInsertionRule revise_service_insertion_rule_revise(body, section_id, rule_id, id=id, operation=operation)

Update an Existing Rule and Reorder the Rule

Modifies existing serviceinsertion rule along with relative position among other serviceinsertion rules inside a serviceinsertion section. Note- POST service insertion rule API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceInsertionRule() # ServiceInsertionRule | 
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Update an Existing Rule and Reorder the Rule
    api_response = api_instance.revise_service_insertion_rule_revise(body, section_id, rule_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->revise_service_insertion_rule_revise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceInsertionRule**](ServiceInsertionRule.md)|  | 
 **section_id** | **str**|  | 
 **rule_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**ServiceInsertionRule**](ServiceInsertionRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revise_service_insertion_section_revise**
> ServiceInsertionSection revise_service_insertion_section_revise(body, section_id, id=id, operation=operation)

Update an Existing Section, Including Its Position

Modifies an existing serviceinsertion section along with its relative position among other serviceinsertion sections in the system. Note- POST service insertion section API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceInsertionSection() # ServiceInsertionSection | 
section_id = 'section_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Update an Existing Section, Including Its Position
    api_response = api_instance.revise_service_insertion_section_revise(body, section_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->revise_service_insertion_section_revise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceInsertionSection**](ServiceInsertionSection.md)|  | 
 **section_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**ServiceInsertionSection**](ServiceInsertionSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revise_service_insertion_section_with_rules_revise_with_rules**
> ServiceInsertionSectionRuleList revise_service_insertion_section_with_rules_revise_with_rules(body, section_id, id=id, operation=operation)

Update an Existing Section with Rules

Modifies an existing serviceinsertion section along with its relative position among other serviceinsertion sections with rules. When invoked on a large number of rules, this API is supported only at low rates of invocation (not more than 2 times per minute). The typical latency of this API with about 1024 rules is about 15 seconds in a cluster setup. This API should not be invoked with large payloads at automation speeds.  Instead, to move a section above or below another section, use: POST /api/v1/serviceinsertion/sections/&lt;section-id&gt;?action=revise  To modify rules, use: PUT /api/v1/serviceinsertion/sections/&lt;section-id&gt;/rules/&lt;rule-id&gt; Note- POST service insertion section API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceInsertionSectionRuleList() # ServiceInsertionSectionRuleList | 
section_id = 'section_id_example' # str | 
id = 'id_example' # str | Identifier of the anchor rule or section. This is a required field in case operation like 'insert_before' and 'insert_after'. (optional)
operation = 'insert_top' # str | Operation (optional) (default to insert_top)

try:
    # Update an Existing Section with Rules
    api_response = api_instance.revise_service_insertion_section_with_rules_revise_with_rules(body, section_id, id=id, operation=operation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->revise_service_insertion_section_with_rules_revise_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceInsertionSectionRuleList**](ServiceInsertionSectionRuleList.md)|  | 
 **section_id** | **str**|  | 
 **id** | **str**| Identifier of the anchor rule or section. This is a required field in case operation like &#x27;insert_before&#x27; and &#x27;insert_after&#x27;. | [optional] 
 **operation** | **str**| Operation | [optional] [default to insert_top]

### Return type

[**ServiceInsertionSectionRuleList**](ServiceInsertionSectionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_attachment**
> ServiceAttachment update_service_attachment(body, service_attachment_id)

Update an existing service attachment.

Modifies an existing service attachment. Updates to name, description and Logical Router list only supported. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceAttachment() # ServiceAttachment | 
service_attachment_id = 'service_attachment_id_example' # str | 

try:
    # Update an existing service attachment.
    api_response = api_instance.update_service_attachment(body, service_attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->update_service_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceAttachment**](ServiceAttachment.md)|  | 
 **service_attachment_id** | **str**|  | 

### Return type

[**ServiceAttachment**](ServiceAttachment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_deployment**
> ServiceDeployment update_service_deployment(body, service_id, service_deployment_id)

Update an existing Service Deployment.

This API is deprecated since only property we can change on service deployment is display name, which is used for the SVM name. Changing the name will cause the name of the deployment to go out of sync with the deployed VM. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceDeployment() # ServiceDeployment | 
service_id = 'service_id_example' # str | 
service_deployment_id = 'service_deployment_id_example' # str | 

try:
    # Update an existing Service Deployment.
    api_response = api_instance.update_service_deployment(body, service_id, service_deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->update_service_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceDeployment**](ServiceDeployment.md)|  | 
 **service_id** | **str**|  | 
 **service_deployment_id** | **str**|  | 

### Return type

[**ServiceDeployment**](ServiceDeployment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_insertion_exclude_list**
> SIExcludeList update_service_insertion_exclude_list(body)

Modify exclude list

Modify exclude list. This includes adding/removing members in the list. Note- PUT serviceinsertion excludelist API is deprecated. Please use the policy serviceinsertion excludelist API instead. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.SIExcludeList() # SIExcludeList | 

try:
    # Modify exclude list
    api_response = api_instance.update_service_insertion_exclude_list(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->update_service_insertion_exclude_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SIExcludeList**](SIExcludeList.md)|  | 

### Return type

[**SIExcludeList**](SIExcludeList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_insertion_rule**
> ServiceInsertionRule update_service_insertion_rule(body, section_id, rule_id)

Update an Existing Rule

Modifies existing serviceinsertion rule in a serviceinsertion section. Note- PUT service insertion rule API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceInsertionRule() # ServiceInsertionRule | 
section_id = 'section_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Update an Existing Rule
    api_response = api_instance.update_service_insertion_rule(body, section_id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->update_service_insertion_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceInsertionRule**](ServiceInsertionRule.md)|  | 
 **section_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**ServiceInsertionRule**](ServiceInsertionRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_insertion_section**
> ServiceInsertionSection update_service_insertion_section(body, section_id)

Update an Existing Section

Modifies the specified section, but does not modify the section's associated rules. Note- PUT service insertion section API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceInsertionSection() # ServiceInsertionSection | 
section_id = 'section_id_example' # str | 

try:
    # Update an Existing Section
    api_response = api_instance.update_service_insertion_section(body, section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->update_service_insertion_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceInsertionSection**](ServiceInsertionSection.md)|  | 
 **section_id** | **str**|  | 

### Return type

[**ServiceInsertionSection**](ServiceInsertionSection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_insertion_section_with_rules_update_with_rules**
> ServiceInsertionSectionRuleList update_service_insertion_section_with_rules_update_with_rules(body, section_id)

Update an Existing Section, Including Its Rules

Modifies existing serviceinsertion section along with its association with rules. When invoked on a large number of rules, this API is supported only at low rates of invocation (not more than 2 times per minute). The typical latency of this API with about 1024 rules is about 15 seconds in a cluster setup. This API should not be invoked with large payloads at automation speeds.  Instead, to update rule content, use: PUT /api/v1/serviceinsertion/sections/&lt;section-id&gt;/rules/&lt;rule-id&gt; Note- POST service insertion section with rules API is deprecated. Please use policy redirection-policy API. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceInsertionSectionRuleList() # ServiceInsertionSectionRuleList | 
section_id = 'section_id_example' # str | 

try:
    # Update an Existing Section, Including Its Rules
    api_response = api_instance.update_service_insertion_section_with_rules_update_with_rules(body, section_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->update_service_insertion_section_with_rules_update_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceInsertionSectionRuleList**](ServiceInsertionSectionRuleList.md)|  | 
 **section_id** | **str**|  | 

### Return type

[**ServiceInsertionSectionRuleList**](ServiceInsertionSectionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_insertion_service**
> ServiceDefinition update_service_insertion_service(body, service_id)

Update an existing Service

Modifies the specified Service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceDefinition() # ServiceDefinition | 
service_id = 'service_id_example' # str | 

try:
    # Update an existing Service
    api_response = api_instance.update_service_insertion_service(body, service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->update_service_insertion_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceDefinition**](ServiceDefinition.md)|  | 
 **service_id** | **str**|  | 

### Return type

[**ServiceDefinition**](ServiceDefinition.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_insertion_status**
> ServiceInsertionStatus update_service_insertion_status(body, context_type)

Update global ServiceInsertion status for a context

Update global ServiceInsertion status for a context

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceInsertionStatus() # ServiceInsertionStatus | 
context_type = 'context_type_example' # str | 

try:
    # Update global ServiceInsertion status for a context
    api_response = api_instance.update_service_insertion_status(body, context_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->update_service_insertion_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceInsertionStatus**](ServiceInsertionStatus.md)|  | 
 **context_type** | **str**|  | 

### Return type

[**ServiceInsertionStatus**](ServiceInsertionStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_instance**
> BaseServiceInstance update_service_instance(body, service_id, service_instance_id)

Update an existing Service-Instance.

Modifies an existing Service-Instance for a given Service-Insertion Service. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.BaseServiceInstance() # BaseServiceInstance | 
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 

try:
    # Update an existing Service-Instance.
    api_response = api_instance.update_service_instance(body, service_id, service_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->update_service_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BaseServiceInstance**](BaseServiceInstance.md)|  | 
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 

### Return type

[**BaseServiceInstance**](BaseServiceInstance.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_manager**
> ServiceManager update_service_manager(body, service_manager_id)

Update service manager

Update service-manager which is registered with NSX with basic details like name, username, password.

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceManager() # ServiceManager | 
service_manager_id = 'service_manager_id_example' # str | 

try:
    # Update service manager
    api_response = api_instance.update_service_manager(body, service_manager_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->update_service_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceManager**](ServiceManager.md)|  | 
 **service_manager_id** | **str**|  | 

### Return type

[**ServiceManager**](ServiceManager.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_vm_state**
> update_service_vm_state(service_id, service_instance_id, instance_runtime_id, action=action, unhealthy_reason=unhealthy_reason)

Update maintenance mode or runtime state of a service VM

Set service VM either in or out of maintenance mode for maintenance mode, or in service or out of service for runtime state. Only one value can be set at one time. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 
instance_runtime_id = 'instance_runtime_id_example' # str | 
action = 'action_example' # str |  (optional)
unhealthy_reason = 'unhealthy_reason_example' # str | Reason for the unhealthy state (optional)

try:
    # Update maintenance mode or runtime state of a service VM
    api_instance.update_service_vm_state(service_id, service_instance_id, instance_runtime_id, action=action, unhealthy_reason=unhealthy_reason)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->update_service_vm_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 
 **instance_runtime_id** | **str**|  | 
 **action** | **str**|  | [optional] 
 **unhealthy_reason** | **str**| Reason for the unhealthy state | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_solution_config**
> SolutionConfig update_solution_config(body, service_id, solution_config_id)

Updates Solution Config for a given Service

Updates a solution config. Solution Config are service level objects, required for configuring the NXGI partner Service after deployment. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.SolutionConfig() # SolutionConfig | 
service_id = 'service_id_example' # str | 
solution_config_id = 'solution_config_id_example' # str | 

try:
    # Updates Solution Config for a given Service
    api_response = api_instance.update_solution_config(body, service_id, solution_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->update_solution_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolutionConfig**](SolutionConfig.md)|  | 
 **service_id** | **str**|  | 
 **solution_config_id** | **str**|  | 

### Return type

[**SolutionConfig**](SolutionConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_service_deployment_upgrade**
> upgrade_service_deployment_upgrade(body, service_id, service_deployment_id)

Upgrade all VMs part of this service deployment to new Spec OVF.

If new deployment spec is provided, the deployment will be moved to the provided spec provided that current deployment state is either UPGRADE_FAILED or DEPLOYMENT_SUCCESSFUL If same deployment spec is provided, upgrade will be done only if current deployment state is UPGRADE_FAILED  

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeploymentSpecName() # DeploymentSpecName | 
service_id = 'service_id_example' # str | 
service_deployment_id = 'service_deployment_id_example' # str | 

try:
    # Upgrade all VMs part of this service deployment to new Spec OVF.
    api_instance.upgrade_service_deployment_upgrade(body, service_id, service_deployment_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->upgrade_service_deployment_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeploymentSpecName**](DeploymentSpecName.md)|  | 
 **service_id** | **str**|  | 
 **service_deployment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_service_v_ms_upgrade**
> upgrade_service_v_ms_upgrade(service_id, service_instance_id)

Upgrade service VMs using newer version of OVF

Upgrade service VMs using newer version of OVF. Upgrade is a 2 step process. Update the 'deployment_spec_name' in the ServiceInstance to the new DeploymentSpec to which the service VMs will be upgraded, folowed by this 'upgrade' api. In case of HA, the stand-by service VM will be upgrade first. Once it has been upgraded, it switches to be the Active one and then the other VM will be upgrade. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServicesServiceInsertionApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
service_instance_id = 'service_instance_id_example' # str | 

try:
    # Upgrade service VMs using newer version of OVF
    api_instance.upgrade_service_v_ms_upgrade(service_id, service_instance_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServicesServiceInsertionApi->upgrade_service_v_ms_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **service_instance_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

