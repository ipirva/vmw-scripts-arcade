# swagger_client.SystemAdministrationMonitoringDashboardsUIViewsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_view**](SystemAdministrationMonitoringDashboardsUIViewsApi.md#create_view) | **POST** /ui-views | Creates a new View.
[**delet_view**](SystemAdministrationMonitoringDashboardsUIViewsApi.md#delet_view) | **DELETE** /ui-views/{view-id} | Delete View
[**get_view**](SystemAdministrationMonitoringDashboardsUIViewsApi.md#get_view) | **GET** /ui-views/{view-id} | Returns View Information
[**list_views**](SystemAdministrationMonitoringDashboardsUIViewsApi.md#list_views) | **GET** /ui-views | Returns the Views based on query criteria defined in ViewQueryParameters.
[**update_view**](SystemAdministrationMonitoringDashboardsUIViewsApi.md#update_view) | **PUT** /ui-views/{view-id} | Update View

# **create_view**
> View create_view(body)

Creates a new View.

Creates a new View.

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsUIViewsApi(swagger_client.ApiClient(configuration))
body = swagger_client.View() # View | 

try:
    # Creates a new View.
    api_response = api_instance.create_view(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsUIViewsApi->create_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**View**](View.md)|  | 

### Return type

[**View**](View.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delet_view**
> delet_view(view_id)

Delete View

Delete View

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsUIViewsApi(swagger_client.ApiClient(configuration))
view_id = 'view_id_example' # str | 

try:
    # Delete View
    api_instance.delet_view(view_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsUIViewsApi->delet_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view**
> View get_view(view_id)

Returns View Information

Returns Information about a specific View. 

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsUIViewsApi(swagger_client.ApiClient(configuration))
view_id = 'view_id_example' # str | 

try:
    # Returns View Information
    api_response = api_instance.get_view(view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsUIViewsApi->get_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 

### Return type

[**View**](View.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_views**
> ViewList list_views(tag=tag, view_ids=view_ids, widget_id=widget_id)

Returns the Views based on query criteria defined in ViewQueryParameters.

If no query params are specified then all the views entitled for the user are returned. The views to which a user is entitled to include the views created by the user and the shared views. 

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsUIViewsApi(swagger_client.ApiClient(configuration))
tag = 'tag_example' # str | The tag for which associated views to be queried. (optional)
view_ids = 'view_ids_example' # str | Ids of the Views (optional)
widget_id = 'widget_id_example' # str | Id of widget configuration (optional)

try:
    # Returns the Views based on query criteria defined in ViewQueryParameters.
    api_response = api_instance.list_views(tag=tag, view_ids=view_ids, widget_id=widget_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsUIViewsApi->list_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| The tag for which associated views to be queried. | [optional] 
 **view_ids** | **str**| Ids of the Views | [optional] 
 **widget_id** | **str**| Id of widget configuration | [optional] 

### Return type

[**ViewList**](ViewList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_view**
> View update_view(body, view_id)

Update View

Update View

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsUIViewsApi(swagger_client.ApiClient(configuration))
body = swagger_client.View() # View | 
view_id = 'view_id_example' # str | 

try:
    # Update View
    api_response = api_instance.update_view(body, view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsUIViewsApi->update_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**View**](View.md)|  | 
 **view_id** | **str**|  | 

### Return type

[**View**](View.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

