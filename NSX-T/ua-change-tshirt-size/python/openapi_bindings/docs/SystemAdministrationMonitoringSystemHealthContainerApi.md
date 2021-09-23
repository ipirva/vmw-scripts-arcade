# swagger_client.SystemAdministrationMonitoringSystemHealthContainerApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_container_cluster_status**](SystemAdministrationMonitoringSystemHealthContainerApi.md#create_container_cluster_status) | **POST** /systemhealth/container-cluster/ncp/status | Create container cluster status list
[**delete_container_cluster_summary**](SystemAdministrationMonitoringSystemHealthContainerApi.md#delete_container_cluster_summary) | **DELETE** /systemhealth/container-cluster/{cluster-id}/ncp/status | Create container cluster status list
[**read_container_cluster_status**](SystemAdministrationMonitoringSystemHealthContainerApi.md#read_container_cluster_status) | **GET** /systemhealth/container-cluster/{cluster-id}/ncp/status | Get the container cluster status by given id
[**read_container_cluster_status_list**](SystemAdministrationMonitoringSystemHealthContainerApi.md#read_container_cluster_status_list) | **GET** /systemhealth/container-cluster/ncp/status | Get all the container cluster status
[**read_tn_container_agent_status**](SystemAdministrationMonitoringSystemHealthContainerApi.md#read_tn_container_agent_status) | **GET** /systemhealth/transport-nodes/{node-id}/container/agent/status | Get the containter status on given node
[**read_tn_hyperbus_status**](SystemAdministrationMonitoringSystemHealthContainerApi.md#read_tn_hyperbus_status) | **GET** /systemhealth/transport-nodes/{node-id}/container/hyperbus/status | Get the containter hyperbus status on given node

# **create_container_cluster_status**
> ContainerClusterStatus create_container_cluster_status(body)

Create container cluster status list

Create container cluster status list

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthContainerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ContainerClusterStatus() # ContainerClusterStatus | 

try:
    # Create container cluster status list
    api_response = api_instance.create_container_cluster_status(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthContainerApi->create_container_cluster_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContainerClusterStatus**](ContainerClusterStatus.md)|  | 

### Return type

[**ContainerClusterStatus**](ContainerClusterStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_container_cluster_summary**
> delete_container_cluster_summary(cluster_id)

Create container cluster status list

Create container cluster status list

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthContainerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    # Create container cluster status list
    api_instance.delete_container_cluster_summary(cluster_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthContainerApi->delete_container_cluster_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_container_cluster_status**
> ContainerClusterSummary read_container_cluster_status(cluster_id)

Get the container cluster status by given id

Get the container cluster status by given id

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthContainerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    # Get the container cluster status by given id
    api_response = api_instance.read_container_cluster_status(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthContainerApi->read_container_cluster_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ContainerClusterSummary**](ContainerClusterSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_container_cluster_status_list**
> ContainerClusterStatusList read_container_cluster_status_list(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get all the container cluster status

Get all the container cluster status

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthContainerApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get all the container cluster status
    api_response = api_instance.read_container_cluster_status_list(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthContainerApi->read_container_cluster_status_list: %s\n" % e)
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

[**ContainerClusterStatusList**](ContainerClusterStatusList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_tn_container_agent_status**
> TnNodeAgentStatusListResult read_tn_container_agent_status(node_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get the containter status on given node

Get the containter status on given node

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthContainerApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get the containter status on given node
    api_response = api_instance.read_tn_container_agent_status(node_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthContainerApi->read_tn_container_agent_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**TnNodeAgentStatusListResult**](TnNodeAgentStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_tn_hyperbus_status**
> TnHyperbusStatus read_tn_hyperbus_status(node_id)

Get the containter hyperbus status on given node

Get the containter hyperbus status on given node

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthContainerApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Get the containter hyperbus status on given node
    api_response = api_instance.read_tn_hyperbus_status(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthContainerApi->read_tn_hyperbus_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**TnHyperbusStatus**](TnHyperbusStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

