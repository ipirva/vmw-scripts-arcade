# swagger_client.SystemAdministrationConfigurationFabricContainersContainerApplicationsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_container_application**](SystemAdministrationConfigurationFabricContainersContainerApplicationsApi.md#get_container_application) | **GET** /fabric/container-applications/{container-application-id} | Return a Container Application within a container project
[**get_container_application_instance**](SystemAdministrationConfigurationFabricContainersContainerApplicationsApi.md#get_container_application_instance) | **GET** /fabric/container-application-instances/{container-application-instance-id} | Return a container application instance
[**list_container_application_instances**](SystemAdministrationConfigurationFabricContainersContainerApplicationsApi.md#list_container_application_instances) | **GET** /fabric/container-application-instances | Return the list of container application instance
[**list_container_applications**](SystemAdministrationConfigurationFabricContainersContainerApplicationsApi.md#list_container_applications) | **GET** /fabric/container-applications | Return the List of Container Applications

# **get_container_application**
> ContainerApplication get_container_application(container_application_id)

Return a Container Application within a container project

Returns information about a specific Container Application within a project.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricContainersContainerApplicationsApi(swagger_client.ApiClient(configuration))
container_application_id = 'container_application_id_example' # str | 

try:
    # Return a Container Application within a container project
    api_response = api_instance.get_container_application(container_application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricContainersContainerApplicationsApi->get_container_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_application_id** | **str**|  | 

### Return type

[**ContainerApplication**](ContainerApplication.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_application_instance**
> ContainerApplicationInstance get_container_application_instance(container_application_instance_id)

Return a container application instance

Returns information about a specific container application instance.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricContainersContainerApplicationsApi(swagger_client.ApiClient(configuration))
container_application_instance_id = 'container_application_instance_id_example' # str | 

try:
    # Return a container application instance
    api_response = api_instance.get_container_application_instance(container_application_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricContainersContainerApplicationsApi->get_container_application_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_application_instance_id** | **str**|  | 

### Return type

[**ContainerApplicationInstance**](ContainerApplicationInstance.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_container_application_instances**
> ContainerApplicationInstanceListResult list_container_application_instances(container_application_id=container_application_id, container_cluster_id=container_cluster_id, container_project_id=container_project_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return the list of container application instance

Returns information about all container application instance.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricContainersContainerApplicationsApi(swagger_client.ApiClient(configuration))
container_application_id = 'container_application_id_example' # str | Identifier of the container application (optional)
container_cluster_id = 'container_cluster_id_example' # str | Identifier of the container cluster (optional)
container_project_id = 'container_project_id_example' # str | Identifier of the container project (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the list of container application instance
    api_response = api_instance.list_container_application_instances(container_application_id=container_application_id, container_cluster_id=container_cluster_id, container_project_id=container_project_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricContainersContainerApplicationsApi->list_container_application_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_application_id** | **str**| Identifier of the container application | [optional] 
 **container_cluster_id** | **str**| Identifier of the container cluster | [optional] 
 **container_project_id** | **str**| Identifier of the container project | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ContainerApplicationInstanceListResult**](ContainerApplicationInstanceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_container_applications**
> ContainerApplicationListResult list_container_applications(container_cluster_id=container_cluster_id, container_project_id=container_project_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return the List of Container Applications

Returns information about all Container Applications.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricContainersContainerApplicationsApi(swagger_client.ApiClient(configuration))
container_cluster_id = 'container_cluster_id_example' # str | Identifier of the container cluster (optional)
container_project_id = 'container_project_id_example' # str | Identifier of the container project (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the List of Container Applications
    api_response = api_instance.list_container_applications(container_cluster_id=container_cluster_id, container_project_id=container_project_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricContainersContainerApplicationsApi->list_container_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_cluster_id** | **str**| Identifier of the container cluster | [optional] 
 **container_project_id** | **str**| Identifier of the container project | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ContainerApplicationListResult**](ContainerApplicationListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

