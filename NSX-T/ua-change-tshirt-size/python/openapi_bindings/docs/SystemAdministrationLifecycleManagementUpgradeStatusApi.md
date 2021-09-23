# swagger_client.SystemAdministrationLifecycleManagementUpgradeStatusApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_uc_functional_state**](SystemAdministrationLifecycleManagementUpgradeStatusApi.md#get_uc_functional_state) | **GET** /upgrade/functional-state | Get functional state of the upgrade coordinator
[**get_uc_upgrade_status**](SystemAdministrationLifecycleManagementUpgradeStatusApi.md#get_uc_upgrade_status) | **GET** /upgrade/uc-upgrade-status | Get upgrade-coordinator upgrade status
[**get_upgrade_status_summary**](SystemAdministrationLifecycleManagementUpgradeStatusApi.md#get_upgrade_status_summary) | **GET** /upgrade/status-summary | Get upgrade status summary
[**get_upgrade_summary**](SystemAdministrationLifecycleManagementUpgradeStatusApi.md#get_upgrade_summary) | **GET** /upgrade/summary | Get upgrade summary

# **get_uc_functional_state**
> UcFunctionalState get_uc_functional_state()

Get functional state of the upgrade coordinator

Get the functional state of the upgrade coordinator. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeStatusApi(swagger_client.ApiClient(configuration))

try:
    # Get functional state of the upgrade coordinator
    api_response = api_instance.get_uc_functional_state()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeStatusApi->get_uc_functional_state: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UcFunctionalState**](UcFunctionalState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_uc_upgrade_status**
> UcUpgradeStatus get_uc_upgrade_status()

Get upgrade-coordinator upgrade status

Get upgrade-coordinator upgrade status 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeStatusApi(swagger_client.ApiClient(configuration))

try:
    # Get upgrade-coordinator upgrade status
    api_response = api_instance.get_uc_upgrade_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeStatusApi->get_uc_upgrade_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UcUpgradeStatus**](UcUpgradeStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_status_summary**
> UpgradeStatus get_upgrade_status_summary(component_type=component_type, selection_status=selection_status, show_history=show_history)

Get upgrade status summary

Get upgrade status summary

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeStatusApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which upgrade units to be filtered (optional)
selection_status = 'ALL' # str | Flag to indicate whether to return status for only selected, only deselected or both type of upgrade units (optional) (default to ALL)
show_history = true # bool | Get upgrade activity for a given component (optional)

try:
    # Get upgrade status summary
    api_response = api_instance.get_upgrade_status_summary(component_type=component_type, selection_status=selection_status, show_history=show_history)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeStatusApi->get_upgrade_status_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which upgrade units to be filtered | [optional] 
 **selection_status** | **str**| Flag to indicate whether to return status for only selected, only deselected or both type of upgrade units | [optional] [default to ALL]
 **show_history** | **bool**| Get upgrade activity for a given component | [optional] 

### Return type

[**UpgradeStatus**](UpgradeStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_summary**
> UpgradeSummary get_upgrade_summary()

Get upgrade summary

Get upgrade summary

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeStatusApi(swagger_client.ApiClient(configuration))

try:
    # Get upgrade summary
    api_response = api_instance.get_upgrade_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeStatusApi->get_upgrade_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpgradeSummary**](UpgradeSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

