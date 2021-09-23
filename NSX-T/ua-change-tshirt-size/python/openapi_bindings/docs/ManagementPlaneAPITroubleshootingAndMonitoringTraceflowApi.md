# swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_traceflow**](ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi.md#create_traceflow) | **POST** /traceflows | Initiate a Traceflow Operation on the Specified Port
[**delete_traceflow**](ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi.md#delete_traceflow) | **DELETE** /traceflows/{traceflow-id} | Delete the Traceflow round
[**get_traceflow**](ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi.md#get_traceflow) | **GET** /traceflows/{traceflow-id} | Get the Traceflow round status and result summary
[**get_traceflow_observations**](ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi.md#get_traceflow_observations) | **GET** /traceflows/{traceflow-id}/observations | Get observations for the Traceflow round
[**list_traceflows**](ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi.md#list_traceflows) | **GET** /traceflows | List all Traceflow rounds

# **create_traceflow**
> Traceflow create_traceflow(body)

Initiate a Traceflow Operation on the Specified Port

Initiate a Traceflow Operation on the Specified Port

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi(swagger_client.ApiClient(configuration))
body = swagger_client.TraceflowRequest() # TraceflowRequest | 

try:
    # Initiate a Traceflow Operation on the Specified Port
    api_response = api_instance.create_traceflow(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi->create_traceflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TraceflowRequest**](TraceflowRequest.md)|  | 

### Return type

[**Traceflow**](Traceflow.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_traceflow**
> delete_traceflow(traceflow_id)

Delete the Traceflow round

Delete the Traceflow round

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi(swagger_client.ApiClient(configuration))
traceflow_id = 'traceflow_id_example' # str | 

try:
    # Delete the Traceflow round
    api_instance.delete_traceflow(traceflow_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi->delete_traceflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **traceflow_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_traceflow**
> Traceflow get_traceflow(traceflow_id)

Get the Traceflow round status and result summary

Get the Traceflow round status and result summary

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi(swagger_client.ApiClient(configuration))
traceflow_id = 'traceflow_id_example' # str | 

try:
    # Get the Traceflow round status and result summary
    api_response = api_instance.get_traceflow(traceflow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi->get_traceflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **traceflow_id** | **str**|  | 

### Return type

[**Traceflow**](Traceflow.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_traceflow_observations**
> TraceflowObservationListResult get_traceflow_observations(traceflow_id, component_name=component_name, component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, resource_type=resource_type, sort_ascending=sort_ascending, sort_by=sort_by, transport_node_name=transport_node_name)

Get observations for the Traceflow round

Get observations for the Traceflow round

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi(swagger_client.ApiClient(configuration))
traceflow_id = 'traceflow_id_example' # str | 
component_name = 'component_name_example' # str | Observations having the given component name will be listed. (optional)
component_type = 'component_type_example' # str | Observations having the given component type will be listed. (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
resource_type = 'resource_type_example' # str | The type of observations that will be listed. (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
transport_node_name = 'transport_node_name_example' # str | Observations having the given transport node name will be listed. (optional)

try:
    # Get observations for the Traceflow round
    api_response = api_instance.get_traceflow_observations(traceflow_id, component_name=component_name, component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, resource_type=resource_type, sort_ascending=sort_ascending, sort_by=sort_by, transport_node_name=transport_node_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi->get_traceflow_observations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **traceflow_id** | **str**|  | 
 **component_name** | **str**| Observations having the given component name will be listed. | [optional] 
 **component_type** | **str**| Observations having the given component type will be listed. | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **resource_type** | **str**| The type of observations that will be listed. | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **transport_node_name** | **str**| Observations having the given transport node name will be listed. | [optional] 

### Return type

[**TraceflowObservationListResult**](TraceflowObservationListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_traceflows**
> TraceflowListResult list_traceflows(cursor=cursor, included_fields=included_fields, lport_id=lport_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List all Traceflow rounds

List all Traceflow rounds; if a logical port id is given as a query parameter, only those originated from the logical port are returned. 

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
lport_id = 'lport_id_example' # str | id of the source logical port where the trace flows originated (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List all Traceflow rounds
    api_response = api_instance.list_traceflows(cursor=cursor, included_fields=included_fields, lport_id=lport_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringTraceflowApi->list_traceflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **lport_id** | **str**| id of the source logical port where the trace flows originated | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**TraceflowListResult**](TraceflowListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

