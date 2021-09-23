# swagger_client.SystemAdministrationLifecycleManagementUpgradeEulaApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_upgrade_eula**](SystemAdministrationLifecycleManagementUpgradeEulaApi.md#accept_upgrade_eula) | **POST** /upgrade/eula/accept | Accept end user license agreement 
[**get_upgrade_eula_acceptance**](SystemAdministrationLifecycleManagementUpgradeEulaApi.md#get_upgrade_eula_acceptance) | **GET** /upgrade/eula/acceptance | Return the acceptance status of end user license agreement 
[**get_upgrade_eula_content**](SystemAdministrationLifecycleManagementUpgradeEulaApi.md#get_upgrade_eula_content) | **GET** /upgrade/eula/content | Return the content of end user license agreement 

# **accept_upgrade_eula**
> accept_upgrade_eula()

Accept end user license agreement 

Accept end user license agreement 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeEulaApi(swagger_client.ApiClient(configuration))

try:
    # Accept end user license agreement 
    api_instance.accept_upgrade_eula()
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeEulaApi->accept_upgrade_eula: %s\n" % e)
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

# **get_upgrade_eula_acceptance**
> EULAAcceptance get_upgrade_eula_acceptance()

Return the acceptance status of end user license agreement 

Return the acceptance status of end user license agreement 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeEulaApi(swagger_client.ApiClient(configuration))

try:
    # Return the acceptance status of end user license agreement 
    api_response = api_instance.get_upgrade_eula_acceptance()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeEulaApi->get_upgrade_eula_acceptance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EULAAcceptance**](EULAAcceptance.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_eula_content**
> EULAContent get_upgrade_eula_content(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, value_format=value_format)

Return the content of end user license agreement 

Return the content of end user license agreement in the specified format. By default, it's pure string without line break 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeEulaApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
value_format = 'value_format_example' # str | End User License Agreement content output format (optional)

try:
    # Return the content of end user license agreement 
    api_response = api_instance.get_upgrade_eula_content(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, value_format=value_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeEulaApi->get_upgrade_eula_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **value_format** | **str**| End User License Agreement content output format | [optional] 

### Return type

[**EULAContent**](EULAContent.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

