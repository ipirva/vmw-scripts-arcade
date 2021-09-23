# swagger_client.SystemAdministrationConfigurationFabricCloudNativeServiceInstancesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cloud_native_service_instance**](SystemAdministrationConfigurationFabricCloudNativeServiceInstancesApi.md#get_cloud_native_service_instance) | **GET** /fabric/cloud-native-service-instances/{external-id} | Returns information about a particular cloud native service instance by external-id. 
[**list_all_cloud_native_service_instances**](SystemAdministrationConfigurationFabricCloudNativeServiceInstancesApi.md#list_all_cloud_native_service_instances) | **GET** /fabric/cloud-native-service-instances | Returns the List of cloud native service instances

# **get_cloud_native_service_instance**
> CloudNativeServiceInstance get_cloud_native_service_instance(external_id)

Returns information about a particular cloud native service instance by external-id. 

Returns information about a particular cloud native service instance by external-id. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricCloudNativeServiceInstancesApi(swagger_client.ApiClient(configuration))
external_id = 'external_id_example' # str | 

try:
    # Returns information about a particular cloud native service instance by external-id. 
    api_response = api_instance.get_cloud_native_service_instance(external_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricCloudNativeServiceInstancesApi->get_cloud_native_service_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | 

### Return type

[**CloudNativeServiceInstance**](CloudNativeServiceInstance.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_cloud_native_service_instances**
> CloudNativeServiceInstanceListResult list_all_cloud_native_service_instances(cursor=cursor, display_name=display_name, included_fields=included_fields, page_size=page_size, service_type=service_type, sort_ascending=sort_ascending, sort_by=sort_by, source=source)

Returns the List of cloud native service instances

Returns information about all cloud native service instances.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricCloudNativeServiceInstancesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
display_name = 'display_name_example' # str | Display Name of the cloud native service instance (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
service_type = 'service_type_example' # str | Type of cloud native service; possible values are ELB, RDS (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | NSX node id of the public cloud gateway that reported the service instance (optional)

try:
    # Returns the List of cloud native service instances
    api_response = api_instance.list_all_cloud_native_service_instances(cursor=cursor, display_name=display_name, included_fields=included_fields, page_size=page_size, service_type=service_type, sort_ascending=sort_ascending, sort_by=sort_by, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricCloudNativeServiceInstancesApi->list_all_cloud_native_service_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **display_name** | **str**| Display Name of the cloud native service instance | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **service_type** | **str**| Type of cloud native service; possible values are ELB, RDS | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| NSX node id of the public cloud gateway that reported the service instance | [optional] 

### Return type

[**CloudNativeServiceInstanceListResult**](CloudNativeServiceInstanceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

