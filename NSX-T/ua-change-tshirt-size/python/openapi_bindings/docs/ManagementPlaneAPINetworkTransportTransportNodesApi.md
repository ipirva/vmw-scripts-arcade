# swagger_client.ManagementPlaneAPINetworkTransportTransportNodesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nvds_upgrade_precheck**](ManagementPlaneAPINetworkTransportTransportNodesApi.md#create_nvds_upgrade_precheck) | **POST** /nvds-urt/precheck | Start precheck for N-VDS to VDS migration
[**get_nvds_upgrade_precheck_id**](ManagementPlaneAPINetworkTransportTransportNodesApi.md#get_nvds_upgrade_precheck_id) | **GET** /nvds-urt/precheck | Retrieve latest precheck ID of the N-VDS to VDS migration
[**get_nvds_upgrade_readiness_check_summary**](ManagementPlaneAPINetworkTransportTransportNodesApi.md#get_nvds_upgrade_readiness_check_summary) | **GET** /nvds-urt/status-summary/{precheck-id} | Get summary of N-VDS to VDS migration
[**get_recommended_vds_topology**](ManagementPlaneAPINetworkTransportTransportNodesApi.md#get_recommended_vds_topology) | **GET** /nvds-urt/topology/{precheck-id} | Recommmended topology
[**ignore_migrate_status_ignore_migrate_status**](ManagementPlaneAPINetworkTransportTransportNodesApi.md#ignore_migrate_status_ignore_migrate_status) | **POST** /nvds-urt?action&#x3D;ignore_migrate_status | Set the migrate status key of ExtraConfigProfile of all Transport Nodes to IGNORE
[**migrate_transport_node_from_nvds_to_vds_migrate_to_vds**](ManagementPlaneAPINetworkTransportTransportNodesApi.md#migrate_transport_node_from_nvds_to_vds_migrate_to_vds) | **POST** /transport-nodes/{transport-node-id}?action&#x3D;migrate_to_vds | Trigger Migration of NVDS to VDS on this TransportNode.
[**nvds_upgrade_cleanup**](ManagementPlaneAPINetworkTransportTransportNodesApi.md#nvds_upgrade_cleanup) | **POST** /nvds-urt?action&#x3D;cleanup | Clean up all nvds upgrade related configurations
[**set_target_vds_topology_apply**](ManagementPlaneAPINetworkTransportTransportNodesApi.md#set_target_vds_topology_apply) | **POST** /nvds-urt/topology?action&#x3D;apply | Set VDS configuration and create it in vCenter

# **create_nvds_upgrade_precheck**
> NvdsUpgradePrecheckId create_nvds_upgrade_precheck()

Start precheck for N-VDS to VDS migration

Start precheck for N-VDS to VDS migration

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
api_instance = swagger_client.ManagementPlaneAPINetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))

try:
    # Start precheck for N-VDS to VDS migration
    api_response = api_instance.create_nvds_upgrade_precheck()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkTransportTransportNodesApi->create_nvds_upgrade_precheck: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NvdsUpgradePrecheckId**](NvdsUpgradePrecheckId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nvds_upgrade_precheck_id**
> NvdsUpgradePrecheckId get_nvds_upgrade_precheck_id()

Retrieve latest precheck ID of the N-VDS to VDS migration

Retrieve latest precheck ID of the N-VDS to VDS migration

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
api_instance = swagger_client.ManagementPlaneAPINetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve latest precheck ID of the N-VDS to VDS migration
    api_response = api_instance.get_nvds_upgrade_precheck_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkTransportTransportNodesApi->get_nvds_upgrade_precheck_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NvdsUpgradePrecheckId**](NvdsUpgradePrecheckId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nvds_upgrade_readiness_check_summary**
> NvdsUpgradeStatusSummary get_nvds_upgrade_readiness_check_summary(precheck_id)

Get summary of N-VDS to VDS migration

Get summary of N-VDS to VDS migration

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
api_instance = swagger_client.ManagementPlaneAPINetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
precheck_id = 'precheck_id_example' # str | 

try:
    # Get summary of N-VDS to VDS migration
    api_response = api_instance.get_nvds_upgrade_readiness_check_summary(precheck_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkTransportTransportNodesApi->get_nvds_upgrade_readiness_check_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **precheck_id** | **str**|  | 

### Return type

[**NvdsUpgradeStatusSummary**](NvdsUpgradeStatusSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_vds_topology**
> UpgradeTopology get_recommended_vds_topology(precheck_id, compute_manager_id=compute_manager_id, show_vds_config=show_vds_config)

Recommmended topology

Recommmended topology

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
api_instance = swagger_client.ManagementPlaneAPINetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
precheck_id = 'precheck_id_example' # str | 
compute_manager_id = 'compute_manager_id_example' # str | vCenter identifier (optional)
show_vds_config = true # bool | Flag to indicate if VdsTopology should contain VDS configuration (optional)

try:
    # Recommmended topology
    api_response = api_instance.get_recommended_vds_topology(precheck_id, compute_manager_id=compute_manager_id, show_vds_config=show_vds_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkTransportTransportNodesApi->get_recommended_vds_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **precheck_id** | **str**|  | 
 **compute_manager_id** | **str**| vCenter identifier | [optional] 
 **show_vds_config** | **bool**| Flag to indicate if VdsTopology should contain VDS configuration | [optional] 

### Return type

[**UpgradeTopology**](UpgradeTopology.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ignore_migrate_status_ignore_migrate_status**
> ignore_migrate_status_ignore_migrate_status()

Set the migrate status key of ExtraConfigProfile of all Transport Nodes to IGNORE

Set the migrate status key of ExtraConfigProfile of all Transport Nodes to IGNORE

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
api_instance = swagger_client.ManagementPlaneAPINetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))

try:
    # Set the migrate status key of ExtraConfigProfile of all Transport Nodes to IGNORE
    api_instance.ignore_migrate_status_ignore_migrate_status()
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkTransportTransportNodesApi->ignore_migrate_status_ignore_migrate_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_transport_node_from_nvds_to_vds_migrate_to_vds**
> migrate_transport_node_from_nvds_to_vds_migrate_to_vds(transport_node_id)

Trigger Migration of NVDS to VDS on this TransportNode.

Migrates all NVDS to VDS on given TransportNode. Upgrade precheck apis should have been run prior to invoking this API on transport node and a migration topology should be created. Please refer to Migration guide for details about migration APIs. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Trigger Migration of NVDS to VDS on this TransportNode.
    api_instance.migrate_transport_node_from_nvds_to_vds_migrate_to_vds(transport_node_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkTransportTransportNodesApi->migrate_transport_node_from_nvds_to_vds_migrate_to_vds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nvds_upgrade_cleanup**
> nvds_upgrade_cleanup()

Clean up all nvds upgrade related configurations

Clean up all nvds upgrade related configurations

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
api_instance = swagger_client.ManagementPlaneAPINetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))

try:
    # Clean up all nvds upgrade related configurations
    api_instance.nvds_upgrade_cleanup()
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkTransportTransportNodesApi->nvds_upgrade_cleanup: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_target_vds_topology_apply**
> UpgradeTopology set_target_vds_topology_apply(body)

Set VDS configuration and create it in vCenter

Set VDS configuration and create it in vCenter

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
api_instance = swagger_client.ManagementPlaneAPINetworkTransportTransportNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpgradeTopology() # UpgradeTopology | 

try:
    # Set VDS configuration and create it in vCenter
    api_response = api_instance.set_target_vds_topology_apply(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkTransportTransportNodesApi->set_target_vds_topology_apply: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeTopology**](UpgradeTopology.md)|  | 

### Return type

[**UpgradeTopology**](UpgradeTopology.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

