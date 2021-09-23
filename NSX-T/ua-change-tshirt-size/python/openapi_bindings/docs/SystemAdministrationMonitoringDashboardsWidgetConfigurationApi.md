# swagger_client.SystemAdministrationMonitoringDashboardsWidgetConfigurationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_widget_configuration**](SystemAdministrationMonitoringDashboardsWidgetConfigurationApi.md#create_widget_configuration) | **POST** /ui-views/{view-id}/widgetconfigurations | Creates a new Widget Configuration.
[**delete_widget_configuration**](SystemAdministrationMonitoringDashboardsWidgetConfigurationApi.md#delete_widget_configuration) | **DELETE** /ui-views/{view-id}/widgetconfigurations/{widgetconfiguration-id} | Delete Widget Configuration
[**get_widget_configuration**](SystemAdministrationMonitoringDashboardsWidgetConfigurationApi.md#get_widget_configuration) | **GET** /ui-views/{view-id}/widgetconfigurations/{widgetconfiguration-id} | Returns Widget Configuration Information
[**list_widget_configurations**](SystemAdministrationMonitoringDashboardsWidgetConfigurationApi.md#list_widget_configurations) | **GET** /ui-views/{view-id}/widgetconfigurations | Returns the Widget Configurations based on query criteria defined in WidgetQueryParameters.
[**update_widget_configuration**](SystemAdministrationMonitoringDashboardsWidgetConfigurationApi.md#update_widget_configuration) | **PUT** /ui-views/{view-id}/widgetconfigurations/{widgetconfiguration-id} | Update Widget Configuration

# **create_widget_configuration**
> WidgetConfiguration create_widget_configuration(body, view_id)

Creates a new Widget Configuration.

Creates a new Widget Configuration and adds it to the specified view. Supported resource_types are LabelValueConfiguration, DonutConfiguration, GridConfiguration, StatsConfiguration, MultiWidgetConfiguration, GraphConfiguration and ContainerConfiguration.  Note: Expressions should be given in a single line. If an expression spans   multiple lines, then form the expression in a single line. For label-value pairs, expressions are evaluated as follows:   a. First, render configurations are evaluated in their order of      appearance in the widget config. The 'field' is evaluated at the end.   b. Second, when render configuration is provided then the order of      evaluation is      1. If expressions provided in 'condition' and 'display value' are         well-formed and free of runtime-errors such as 'null pointers' and         evaluates to 'true'; Then remaining render configurations are not         evaluated, and the current render configuration's 'display value'         is taken as the final value.      2. If expression provided in 'condition' of render configuration is         false, then next render configuration is evaluated.      3. Finally, 'field' is evaluated only when every render configuration         evaluates to false and no error occurs during steps 1 and 2 above.  If an error occurs during evaluation of render configuration, then an   error message is shown. The display value corresponding to that label is   not shown and evaluation of the remaining render configurations continues   to collect and show all the error messages (marked with the 'Label' for   identification) as 'Error_Messages: {}'.  If during evaluation of expressions for any label-value pair an error   occurs, then it is marked with error. The errors are shown in the report,   along with the label value pairs that are error-free.  Important: For elements that take expressions, strings should be provided   by escaping them with a back-slash. These elements are - condition, field,   tooltip text and render_configuration's display_value. 

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsWidgetConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.WidgetConfiguration() # WidgetConfiguration | 
view_id = 'view_id_example' # str | 

try:
    # Creates a new Widget Configuration.
    api_response = api_instance.create_widget_configuration(body, view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsWidgetConfigurationApi->create_widget_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WidgetConfiguration**](WidgetConfiguration.md)|  | 
 **view_id** | **str**|  | 

### Return type

[**WidgetConfiguration**](WidgetConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_widget_configuration**
> delete_widget_configuration(view_id, widgetconfiguration_id)

Delete Widget Configuration

Detaches widget from a given view. If the widget is no longer part of any view, then it will be purged. 

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsWidgetConfigurationApi(swagger_client.ApiClient(configuration))
view_id = 'view_id_example' # str | 
widgetconfiguration_id = 'widgetconfiguration_id_example' # str | 

try:
    # Delete Widget Configuration
    api_instance.delete_widget_configuration(view_id, widgetconfiguration_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsWidgetConfigurationApi->delete_widget_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 
 **widgetconfiguration_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_configuration**
> WidgetConfiguration get_widget_configuration(view_id, widgetconfiguration_id)

Returns Widget Configuration Information

Returns Information about a specific Widget Configuration. 

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsWidgetConfigurationApi(swagger_client.ApiClient(configuration))
view_id = 'view_id_example' # str | 
widgetconfiguration_id = 'widgetconfiguration_id_example' # str | 

try:
    # Returns Widget Configuration Information
    api_response = api_instance.get_widget_configuration(view_id, widgetconfiguration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsWidgetConfigurationApi->get_widget_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 
 **widgetconfiguration_id** | **str**|  | 

### Return type

[**WidgetConfiguration**](WidgetConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_widget_configurations**
> WidgetConfigurationList list_widget_configurations(view_id, container=container, widget_ids=widget_ids)

Returns the Widget Configurations based on query criteria defined in WidgetQueryParameters.

If no query params are specified then all the Widget Configurations of the specified view are returned. 

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsWidgetConfigurationApi(swagger_client.ApiClient(configuration))
view_id = 'view_id_example' # str | 
container = 'container_example' # str | Id of the container (optional)
widget_ids = 'widget_ids_example' # str | Ids of the WidgetConfigurations (optional)

try:
    # Returns the Widget Configurations based on query criteria defined in WidgetQueryParameters.
    api_response = api_instance.list_widget_configurations(view_id, container=container, widget_ids=widget_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsWidgetConfigurationApi->list_widget_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 
 **container** | **str**| Id of the container | [optional] 
 **widget_ids** | **str**| Ids of the WidgetConfigurations | [optional] 

### Return type

[**WidgetConfigurationList**](WidgetConfigurationList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_widget_configuration**
> WidgetConfiguration update_widget_configuration(body, view_id, widgetconfiguration_id)

Update Widget Configuration

Updates the widget at the given view. If the widget is referenced by other views, then the widget will be updated in all the views that it is part of. 

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsWidgetConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.WidgetConfiguration() # WidgetConfiguration | 
view_id = 'view_id_example' # str | 
widgetconfiguration_id = 'widgetconfiguration_id_example' # str | 

try:
    # Update Widget Configuration
    api_response = api_instance.update_widget_configuration(body, view_id, widgetconfiguration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsWidgetConfigurationApi->update_widget_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WidgetConfiguration**](WidgetConfiguration.md)|  | 
 **view_id** | **str**|  | 
 **widgetconfiguration_id** | **str**|  | 

### Return type

[**WidgetConfiguration**](WidgetConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

