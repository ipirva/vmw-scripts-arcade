# swagger_client.ManagementPlaneAPISecurityIdentityFirewallMonitoringApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_compute_collection_status_by_id**](ManagementPlaneAPISecurityIdentityFirewallMonitoringApi.md#get_compute_collection_status_by_id) | **GET** /idfw/compute-collections/{compute-collection-ext-id}/status | Get list of compute collections and status.
[**list_compute_collection_statuses**](ManagementPlaneAPISecurityIdentityFirewallMonitoringApi.md#list_compute_collection_statuses) | **GET** /idfw/compute-collections/status | List all IDFW enabled ComputeCollection statuses.
[**list_transport_node_statuses_by_compute_collection_id**](ManagementPlaneAPISecurityIdentityFirewallMonitoringApi.md#list_transport_node_statuses_by_compute_collection_id) | **GET** /idfw/compute-collections/{cc-ext-id}/transport-nodes/status | List all transport node and statuses based on idfw enabled ComputeCollection ID.
[**list_virtual_machine_statuses_by_transport_node_id**](ManagementPlaneAPISecurityIdentityFirewallMonitoringApi.md#list_virtual_machine_statuses_by_transport_node_id) | **GET** /idfw/transport-nodes/{transport-node-id}/vms/status | List all VM and statuses based on transport node ID of idfw enabled compute collection.

# **get_compute_collection_status_by_id**
> IdfwComputeCollectionStatus get_compute_collection_status_by_id(compute_collection_ext_id)

Get list of compute collections and status.

Retrieve the compute collection status by ID. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallMonitoringApi(swagger_client.ApiClient(configuration))
compute_collection_ext_id = 'compute_collection_ext_id_example' # str | 

try:
    # Get list of compute collections and status.
    api_response = api_instance.get_compute_collection_status_by_id(compute_collection_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallMonitoringApi->get_compute_collection_status_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_collection_ext_id** | **str**|  | 

### Return type

[**IdfwComputeCollectionStatus**](IdfwComputeCollectionStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compute_collection_statuses**
> IdfwComputeCollectionListResult list_compute_collection_statuses()

List all IDFW enabled ComputeCollection statuses.

Retrieve all the Compute collection status. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallMonitoringApi(swagger_client.ApiClient(configuration))

try:
    # List all IDFW enabled ComputeCollection statuses.
    api_response = api_instance.list_compute_collection_statuses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallMonitoringApi->list_compute_collection_statuses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdfwComputeCollectionListResult**](IdfwComputeCollectionListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_node_statuses_by_compute_collection_id**
> IdfwTransportNodeStatusListResult list_transport_node_statuses_by_compute_collection_id(cc_ext_id)

List all transport node and statuses based on idfw enabled ComputeCollection ID.

Retrieve all the transport node and status by idfw enabled   ComputeCollection ID in the request. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallMonitoringApi(swagger_client.ApiClient(configuration))
cc_ext_id = 'cc_ext_id_example' # str | 

try:
    # List all transport node and statuses based on idfw enabled ComputeCollection ID.
    api_response = api_instance.list_transport_node_statuses_by_compute_collection_id(cc_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallMonitoringApi->list_transport_node_statuses_by_compute_collection_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cc_ext_id** | **str**|  | 

### Return type

[**IdfwTransportNodeStatusListResult**](IdfwTransportNodeStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_statuses_by_transport_node_id**
> IdfwVirtualMachineStatusListResult list_virtual_machine_statuses_by_transport_node_id(transport_node_id)

List all VM and statuses based on transport node ID of idfw enabled compute collection.

Retrieve all the VM and status by transport node ID of idfw enabled compute collection in the request. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallMonitoringApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # List all VM and statuses based on transport node ID of idfw enabled compute collection.
    api_response = api_instance.list_virtual_machine_statuses_by_transport_node_id(transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallMonitoringApi->list_virtual_machine_statuses_by_transport_node_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

[**IdfwVirtualMachineStatusListResult**](IdfwVirtualMachineStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

