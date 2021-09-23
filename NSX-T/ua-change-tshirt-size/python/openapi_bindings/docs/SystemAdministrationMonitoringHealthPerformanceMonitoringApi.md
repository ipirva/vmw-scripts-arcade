# swagger_client.SystemAdministrationMonitoringHealthPerformanceMonitoringApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collect_alarms**](SystemAdministrationMonitoringHealthPerformanceMonitoringApi.md#collect_alarms) | **GET** /hpm/alarms | Collect alarms from all NSX nodes
[**get_aggregation_service_global_config**](SystemAdministrationMonitoringHealthPerformanceMonitoringApi.md#get_aggregation_service_global_config) | **GET** /hpm/global-config | Read global health performance monitoring configuration
[**get_feature_stack_configuration**](SystemAdministrationMonitoringHealthPerformanceMonitoringApi.md#get_feature_stack_configuration) | **GET** /hpm/features/{feature-stack-name} | Read health performance monitoring configuration for feature stack
[**list_feature_stack_configurations**](SystemAdministrationMonitoringHealthPerformanceMonitoringApi.md#list_feature_stack_configurations) | **GET** /hpm/features | List all health performance monitoring feature stacks
[**reset_aggregation_service_feature_stack_configuration_reset_collection_frequency**](SystemAdministrationMonitoringHealthPerformanceMonitoringApi.md#reset_aggregation_service_feature_stack_configuration_reset_collection_frequency) | **POST** /hpm/features/{feature-stack-name}?action&#x3D;reset_collection_frequency | Reset the data collection frequency configuration setting to the default values
[**update_aggregation_service_global_config**](SystemAdministrationMonitoringHealthPerformanceMonitoringApi.md#update_aggregation_service_global_config) | **PUT** /hpm/global-config | Set the global configuration for aggregation service related data collection
[**update_feature_stack_configuration**](SystemAdministrationMonitoringHealthPerformanceMonitoringApi.md#update_feature_stack_configuration) | **PUT** /hpm/features/{feature-stack-name} | Update health performance monitoring configuration for feature stack

# **collect_alarms**
> AlarmListResult collect_alarms(cursor=cursor, fields=fields, page_size=page_size)

Collect alarms from all NSX nodes

This API is executed on a manager node to return current alarms from all NSX nodes. This API is deprecated as part of alarm framework enhancements. Please use below new APIs: GET /alarms GET /alarms/&lt;alarm-id&gt; POST /alarms/&lt;alarm-id&gt;?action=set_status POST /alarms?action=set_status GET /events GET /events/&lt;event-id&gt; PUT /events/&lt;event-id&gt; POST /events/&lt;event-id&gt;?action=set_default 

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
api_instance = swagger_client.SystemAdministrationMonitoringHealthPerformanceMonitoringApi(swagger_client.ApiClient(configuration))
cursor = 789 # int | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
fields = 'fields_example' # str | Fields to include in query results (optional)
page_size = 100 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 100)

try:
    # Collect alarms from all NSX nodes
    api_response = api_instance.collect_alarms(cursor=cursor, fields=fields, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringHealthPerformanceMonitoringApi->collect_alarms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **int**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **fields** | **str**| Fields to include in query results | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 100]

### Return type

[**AlarmListResult**](AlarmListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregation_service_global_config**
> GlobalCollectionConfiguration get_aggregation_service_global_config()

Read global health performance monitoring configuration

Read global health performance monitoring configuration

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
api_instance = swagger_client.SystemAdministrationMonitoringHealthPerformanceMonitoringApi(swagger_client.ApiClient(configuration))

try:
    # Read global health performance monitoring configuration
    api_response = api_instance.get_aggregation_service_global_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringHealthPerformanceMonitoringApi->get_aggregation_service_global_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GlobalCollectionConfiguration**](GlobalCollectionConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_stack_configuration**
> FeatureStackCollectionConfiguration get_feature_stack_configuration(feature_stack_name)

Read health performance monitoring configuration for feature stack

Returns the complete set of client type data collection configuration records for the specified feature stack. 

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
api_instance = swagger_client.SystemAdministrationMonitoringHealthPerformanceMonitoringApi(swagger_client.ApiClient(configuration))
feature_stack_name = 'feature_stack_name_example' # str | 

try:
    # Read health performance monitoring configuration for feature stack
    api_response = api_instance.get_feature_stack_configuration(feature_stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringHealthPerformanceMonitoringApi->get_feature_stack_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_stack_name** | **str**|  | 

### Return type

[**FeatureStackCollectionConfiguration**](FeatureStackCollectionConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_feature_stack_configurations**
> FeatureStackCollectionConfigurationList list_feature_stack_configurations()

List all health performance monitoring feature stacks

List all health performance monitoring feature stacks

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
api_instance = swagger_client.SystemAdministrationMonitoringHealthPerformanceMonitoringApi(swagger_client.ApiClient(configuration))

try:
    # List all health performance monitoring feature stacks
    api_response = api_instance.list_feature_stack_configurations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringHealthPerformanceMonitoringApi->list_feature_stack_configurations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FeatureStackCollectionConfigurationList**](FeatureStackCollectionConfigurationList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_aggregation_service_feature_stack_configuration_reset_collection_frequency**
> FeatureStackCollectionConfiguration reset_aggregation_service_feature_stack_configuration_reset_collection_frequency(feature_stack_name)

Reset the data collection frequency configuration setting to the default values

Reset the data collection frequency configuration setting to the default values

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
api_instance = swagger_client.SystemAdministrationMonitoringHealthPerformanceMonitoringApi(swagger_client.ApiClient(configuration))
feature_stack_name = 'feature_stack_name_example' # str | 

try:
    # Reset the data collection frequency configuration setting to the default values
    api_response = api_instance.reset_aggregation_service_feature_stack_configuration_reset_collection_frequency(feature_stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringHealthPerformanceMonitoringApi->reset_aggregation_service_feature_stack_configuration_reset_collection_frequency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_stack_name** | **str**|  | 

### Return type

[**FeatureStackCollectionConfiguration**](FeatureStackCollectionConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aggregation_service_global_config**
> GlobalCollectionConfiguration update_aggregation_service_global_config(body)

Set the global configuration for aggregation service related data collection

Set the global configuration for aggregation service related data collection

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
api_instance = swagger_client.SystemAdministrationMonitoringHealthPerformanceMonitoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.GlobalCollectionConfiguration() # GlobalCollectionConfiguration | 

try:
    # Set the global configuration for aggregation service related data collection
    api_response = api_instance.update_aggregation_service_global_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringHealthPerformanceMonitoringApi->update_aggregation_service_global_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GlobalCollectionConfiguration**](GlobalCollectionConfiguration.md)|  | 

### Return type

[**GlobalCollectionConfiguration**](GlobalCollectionConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feature_stack_configuration**
> FeatureStackCollectionConfiguration update_feature_stack_configuration(body, feature_stack_name)

Update health performance monitoring configuration for feature stack

Apply the data collection configuration for the specified feature stack. 

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
api_instance = swagger_client.SystemAdministrationMonitoringHealthPerformanceMonitoringApi(swagger_client.ApiClient(configuration))
body = swagger_client.FeatureStackCollectionConfiguration() # FeatureStackCollectionConfiguration | 
feature_stack_name = 'feature_stack_name_example' # str | 

try:
    # Update health performance monitoring configuration for feature stack
    api_response = api_instance.update_feature_stack_configuration(body, feature_stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringHealthPerformanceMonitoringApi->update_feature_stack_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeatureStackCollectionConfiguration**](FeatureStackCollectionConfiguration.md)|  | 
 **feature_stack_name** | **str**|  | 

### Return type

[**FeatureStackCollectionConfiguration**](FeatureStackCollectionConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

