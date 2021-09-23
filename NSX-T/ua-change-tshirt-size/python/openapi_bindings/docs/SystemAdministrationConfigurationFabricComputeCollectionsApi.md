# swagger_client.SystemAdministrationConfigurationFabricComputeCollectionsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_compute_collection_fabric_template**](SystemAdministrationConfigurationFabricComputeCollectionsApi.md#create_compute_collection_fabric_template) | **POST** /fabric/compute-collection-fabric-templates | Create a compute collection fabric template
[**delete_compute_collection_fabric_template**](SystemAdministrationConfigurationFabricComputeCollectionsApi.md#delete_compute_collection_fabric_template) | **DELETE** /fabric/compute-collection-fabric-templates/{fabric-template-id} | Deletes compute collection fabric template
[**get_compute_collection_fabric_template**](SystemAdministrationConfigurationFabricComputeCollectionsApi.md#get_compute_collection_fabric_template) | **GET** /fabric/compute-collection-fabric-templates/{fabric-template-id} | Get compute collection fabric template by id
[**get_host_node_status_on_compute_collection**](SystemAdministrationConfigurationFabricComputeCollectionsApi.md#get_host_node_status_on_compute_collection) | **GET** /fabric/compute-collections/{cc-ext-id}/member-status | Get status of member host nodes of the compute-collection. Only nsx prepared host nodes in the specified compute-collection are included in the response. cc-ext-id should be of type VC_Cluster.
[**list_compute_collection_fabric_templates**](SystemAdministrationConfigurationFabricComputeCollectionsApi.md#list_compute_collection_fabric_templates) | **GET** /fabric/compute-collection-fabric-templates | Get compute collection fabric templates
[**list_compute_collection_physical_network_interfaces**](SystemAdministrationConfigurationFabricComputeCollectionsApi.md#list_compute_collection_physical_network_interfaces) | **GET** /fabric/compute-collections/{cc-ext-id}/network/physical-interfaces | List the Physical Network Interface for all discovered nodes
[**list_compute_collections**](SystemAdministrationConfigurationFabricComputeCollectionsApi.md#list_compute_collections) | **GET** /fabric/compute-collections | Return the List of Compute Collections
[**perform_action_on_compute_collection**](SystemAdministrationConfigurationFabricComputeCollectionsApi.md#perform_action_on_compute_collection) | **POST** /fabric/compute-collections/{cc-ext-id} | Perform action specific to NSX on the compute-collection. cc-ext-id should be of type VC_Cluster.
[**read_compute_collection**](SystemAdministrationConfigurationFabricComputeCollectionsApi.md#read_compute_collection) | **GET** /fabric/compute-collections/{cc-ext-id} | Return Compute Collection Information
[**update_compute_collection_fabric_template**](SystemAdministrationConfigurationFabricComputeCollectionsApi.md#update_compute_collection_fabric_template) | **PUT** /fabric/compute-collection-fabric-templates/{fabric-template-id} | Updates compute collection fabric template

# **create_compute_collection_fabric_template**
> ComputeCollectionFabricTemplate create_compute_collection_fabric_template(body)

Create a compute collection fabric template

Fabric templates are fabric configurations applied at the compute collection level. This configurations is used to decide what automated operations should be a run when a host membership changes. This functionality is deprecated. Use Transport Node Profiles instead of this template.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeCollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComputeCollectionFabricTemplate() # ComputeCollectionFabricTemplate | 

try:
    # Create a compute collection fabric template
    api_response = api_instance.create_compute_collection_fabric_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeCollectionsApi->create_compute_collection_fabric_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComputeCollectionFabricTemplate**](ComputeCollectionFabricTemplate.md)|  | 

### Return type

[**ComputeCollectionFabricTemplate**](ComputeCollectionFabricTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_compute_collection_fabric_template**
> delete_compute_collection_fabric_template(fabric_template_id)

Deletes compute collection fabric template

Deletes compute collection fabric template for the given id. This functionality is deprecated. Use Transport Node Profiles instead of this template.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeCollectionsApi(swagger_client.ApiClient(configuration))
fabric_template_id = 'fabric_template_id_example' # str | 

try:
    # Deletes compute collection fabric template
    api_instance.delete_compute_collection_fabric_template(fabric_template_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeCollectionsApi->delete_compute_collection_fabric_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric_template_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compute_collection_fabric_template**
> ComputeCollectionFabricTemplate get_compute_collection_fabric_template(fabric_template_id)

Get compute collection fabric template by id

Get compute collection fabric template for the given id. This functionality is deprecated. Use Transport Node Profiles instead of this template.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeCollectionsApi(swagger_client.ApiClient(configuration))
fabric_template_id = 'fabric_template_id_example' # str | 

try:
    # Get compute collection fabric template by id
    api_response = api_instance.get_compute_collection_fabric_template(fabric_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeCollectionsApi->get_compute_collection_fabric_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric_template_id** | **str**|  | 

### Return type

[**ComputeCollectionFabricTemplate**](ComputeCollectionFabricTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_node_status_on_compute_collection**
> HostNodeStatusListResult get_host_node_status_on_compute_collection(cc_ext_id)

Get status of member host nodes of the compute-collection. Only nsx prepared host nodes in the specified compute-collection are included in the response. cc-ext-id should be of type VC_Cluster.

Get status of member host nodes of the compute-collection. Only nsx prepared host nodes in the specified compute-collection are included in the response. cc-ext-id should be of type VC_Cluster.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeCollectionsApi(swagger_client.ApiClient(configuration))
cc_ext_id = 'cc_ext_id_example' # str | 

try:
    # Get status of member host nodes of the compute-collection. Only nsx prepared host nodes in the specified compute-collection are included in the response. cc-ext-id should be of type VC_Cluster.
    api_response = api_instance.get_host_node_status_on_compute_collection(cc_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeCollectionsApi->get_host_node_status_on_compute_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cc_ext_id** | **str**|  | 

### Return type

[**HostNodeStatusListResult**](HostNodeStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compute_collection_fabric_templates**
> ComputeCollectionFabricTemplateListResult list_compute_collection_fabric_templates(compute_collection_id=compute_collection_id)

Get compute collection fabric templates

Returns compute collection fabric templates. This functionality is deprecated. Use Transport Node Profiles instead of this template.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeCollectionsApi(swagger_client.ApiClient(configuration))
compute_collection_id = 'compute_collection_id_example' # str | Compute collection id (optional)

try:
    # Get compute collection fabric templates
    api_response = api_instance.list_compute_collection_fabric_templates(compute_collection_id=compute_collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeCollectionsApi->list_compute_collection_fabric_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_collection_id** | **str**| Compute collection id | [optional] 

### Return type

[**ComputeCollectionFabricTemplateListResult**](ComputeCollectionFabricTemplateListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compute_collection_physical_network_interfaces**
> ComputeCollectionNetworkInterfacesListResult list_compute_collection_physical_network_interfaces(cc_ext_id)

List the Physical Network Interface for all discovered nodes

Returns list of physical network interfaces for all discovered nodes in compute collection. Interface information includes PNIC name, hostswitch name it's attached to(if any) and MAC address. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeCollectionsApi(swagger_client.ApiClient(configuration))
cc_ext_id = 'cc_ext_id_example' # str | 

try:
    # List the Physical Network Interface for all discovered nodes
    api_response = api_instance.list_compute_collection_physical_network_interfaces(cc_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeCollectionsApi->list_compute_collection_physical_network_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cc_ext_id** | **str**|  | 

### Return type

[**ComputeCollectionNetworkInterfacesListResult**](ComputeCollectionNetworkInterfacesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compute_collections**
> ComputeCollectionListResult list_compute_collections(cm_local_id=cm_local_id, cursor=cursor, discovered_node_id=discovered_node_id, display_name=display_name, external_id=external_id, included_fields=included_fields, node_id=node_id, origin_id=origin_id, origin_type=origin_type, owner_id=owner_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return the List of Compute Collections

Returns information about all compute collections.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeCollectionsApi(swagger_client.ApiClient(configuration))
cm_local_id = 'cm_local_id_example' # str | Local Id of the compute collection in the Compute Manager (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
discovered_node_id = 'discovered_node_id_example' # str | Id of the discovered node which belongs to this Compute Collection  (optional)
display_name = 'display_name_example' # str | Name of the ComputeCollection in source compute manager (optional)
external_id = 'external_id_example' # str | External ID of the ComputeCollection in the source Compute manager, e.g. mo-ref in VC  (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
node_id = 'node_id_example' # str | Id of the fabric node created from a discovered node belonging to this Compute Collection  (optional)
origin_id = 'origin_id_example' # str | Id of the compute manager from where this Compute Collection was discovered (optional)
origin_type = 'origin_type_example' # str | ComputeCollection type like VC_Cluster. Here the Compute Manager type prefix would help in differentiating similar named Compute Collection types from different Compute Managers  (optional)
owner_id = 'owner_id_example' # str | Id of the owner of compute collection in the Compute Manager (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the List of Compute Collections
    api_response = api_instance.list_compute_collections(cm_local_id=cm_local_id, cursor=cursor, discovered_node_id=discovered_node_id, display_name=display_name, external_id=external_id, included_fields=included_fields, node_id=node_id, origin_id=origin_id, origin_type=origin_type, owner_id=owner_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeCollectionsApi->list_compute_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cm_local_id** | **str**| Local Id of the compute collection in the Compute Manager | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **discovered_node_id** | **str**| Id of the discovered node which belongs to this Compute Collection  | [optional] 
 **display_name** | **str**| Name of the ComputeCollection in source compute manager | [optional] 
 **external_id** | **str**| External ID of the ComputeCollection in the source Compute manager, e.g. mo-ref in VC  | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **node_id** | **str**| Id of the fabric node created from a discovered node belonging to this Compute Collection  | [optional] 
 **origin_id** | **str**| Id of the compute manager from where this Compute Collection was discovered | [optional] 
 **origin_type** | **str**| ComputeCollection type like VC_Cluster. Here the Compute Manager type prefix would help in differentiating similar named Compute Collection types from different Compute Managers  | [optional] 
 **owner_id** | **str**| Id of the owner of compute collection in the Compute Manager | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ComputeCollectionListResult**](ComputeCollectionListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_action_on_compute_collection**
> perform_action_on_compute_collection(cc_ext_id, action=action)

Perform action specific to NSX on the compute-collection. cc-ext-id should be of type VC_Cluster.

Perform action specific to NSX on the compute-collection. cc-ext-id should be of type VC_Cluster.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeCollectionsApi(swagger_client.ApiClient(configuration))
cc_ext_id = 'cc_ext_id_example' # str | 
action = 'action_example' # str | Supported actions on compute-collection (optional)

try:
    # Perform action specific to NSX on the compute-collection. cc-ext-id should be of type VC_Cluster.
    api_instance.perform_action_on_compute_collection(cc_ext_id, action=action)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeCollectionsApi->perform_action_on_compute_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cc_ext_id** | **str**|  | 
 **action** | **str**| Supported actions on compute-collection | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_compute_collection**
> ComputeCollection read_compute_collection(cc_ext_id)

Return Compute Collection Information

Returns information about a specific compute collection.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeCollectionsApi(swagger_client.ApiClient(configuration))
cc_ext_id = 'cc_ext_id_example' # str | 

try:
    # Return Compute Collection Information
    api_response = api_instance.read_compute_collection(cc_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeCollectionsApi->read_compute_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cc_ext_id** | **str**|  | 

### Return type

[**ComputeCollection**](ComputeCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_compute_collection_fabric_template**
> ComputeCollectionFabricTemplate update_compute_collection_fabric_template(body, fabric_template_id)

Updates compute collection fabric template

Updates compute collection fabric template for the given id. This functionality is deprecated. Use Transport Node Profiles instead of this template.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeCollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComputeCollectionFabricTemplate() # ComputeCollectionFabricTemplate | 
fabric_template_id = 'fabric_template_id_example' # str | 

try:
    # Updates compute collection fabric template
    api_response = api_instance.update_compute_collection_fabric_template(body, fabric_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeCollectionsApi->update_compute_collection_fabric_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComputeCollectionFabricTemplate**](ComputeCollectionFabricTemplate.md)|  | 
 **fabric_template_id** | **str**|  | 

### Return type

[**ComputeCollectionFabricTemplate**](ComputeCollectionFabricTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

