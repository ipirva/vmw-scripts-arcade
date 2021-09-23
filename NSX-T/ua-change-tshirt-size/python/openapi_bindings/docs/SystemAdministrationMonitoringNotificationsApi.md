# swagger_client.SystemAdministrationMonitoringNotificationsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_notification_watcher**](SystemAdministrationMonitoringNotificationsApi.md#add_notification_watcher) | **POST** /notification-watchers | Add a new notification watcher.
[**add_uri_filters_add_uri_filters**](SystemAdministrationMonitoringNotificationsApi.md#add_uri_filters_add_uri_filters) | **POST** /notification-watchers/{watcher-id}/notifications?action&#x3D;add_uri_filters | Add uri filters for the specified watcher ID.
[**delete_notification_watcher**](SystemAdministrationMonitoringNotificationsApi.md#delete_notification_watcher) | **DELETE** /notification-watchers/{watcher-id} | Delete an existing Notification-Watcher.
[**delete_uri_filters_delete_uri_filters**](SystemAdministrationMonitoringNotificationsApi.md#delete_uri_filters_delete_uri_filters) | **POST** /notification-watchers/{watcher-id}/notifications?action&#x3D;delete_uri_filters | Delete uri filters for the specified watcher ID.
[**get_notification_watcher**](SystemAdministrationMonitoringNotificationsApi.md#get_notification_watcher) | **GET** /notification-watchers/{watcher-id} | Returns notification watcher by watcher id.
[**get_notifications**](SystemAdministrationMonitoringNotificationsApi.md#get_notifications) | **GET** /notification-watchers/{watcher-id}/notifications | Get notifications for the specified watcher ID.
[**list_notification_watchers**](SystemAdministrationMonitoringNotificationsApi.md#list_notification_watchers) | **GET** /notification-watchers | Returns a list of registered notification watchers.
[**update_notification_watcher**](SystemAdministrationMonitoringNotificationsApi.md#update_notification_watcher) | **PUT** /notification-watchers/{watcher-id} | Update notification watcher.
[**update_notifications**](SystemAdministrationMonitoringNotificationsApi.md#update_notifications) | **PUT** /notification-watchers/{watcher-id}/notifications | Update notifications for the specified watcher ID.

# **add_notification_watcher**
> NotificationWatcher add_notification_watcher(body)

Add a new notification watcher.

Add a new notification watcher.

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
api_instance = swagger_client.SystemAdministrationMonitoringNotificationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.NotificationWatcher() # NotificationWatcher | 

try:
    # Add a new notification watcher.
    api_response = api_instance.add_notification_watcher(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringNotificationsApi->add_notification_watcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationWatcher**](NotificationWatcher.md)|  | 

### Return type

[**NotificationWatcher**](NotificationWatcher.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_uri_filters_add_uri_filters**
> NotificationsList add_uri_filters_add_uri_filters(body, watcher_id)

Add uri filters for the specified watcher ID.

Add uri filters for the specified watcher ID.

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
api_instance = swagger_client.SystemAdministrationMonitoringNotificationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Notification() # Notification | 
watcher_id = 'watcher_id_example' # str | 

try:
    # Add uri filters for the specified watcher ID.
    api_response = api_instance.add_uri_filters_add_uri_filters(body, watcher_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringNotificationsApi->add_uri_filters_add_uri_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Notification**](Notification.md)|  | 
 **watcher_id** | **str**|  | 

### Return type

[**NotificationsList**](NotificationsList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_watcher**
> delete_notification_watcher(watcher_id)

Delete an existing Notification-Watcher.

Delete notification watcher. 

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
api_instance = swagger_client.SystemAdministrationMonitoringNotificationsApi(swagger_client.ApiClient(configuration))
watcher_id = 'watcher_id_example' # str | 

try:
    # Delete an existing Notification-Watcher.
    api_instance.delete_notification_watcher(watcher_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringNotificationsApi->delete_notification_watcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watcher_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_uri_filters_delete_uri_filters**
> NotificationsList delete_uri_filters_delete_uri_filters(body, watcher_id)

Delete uri filters for the specified watcher ID.

Delete uri filters for the specified watcher ID.

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
api_instance = swagger_client.SystemAdministrationMonitoringNotificationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Notification() # Notification | 
watcher_id = 'watcher_id_example' # str | 

try:
    # Delete uri filters for the specified watcher ID.
    api_response = api_instance.delete_uri_filters_delete_uri_filters(body, watcher_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringNotificationsApi->delete_uri_filters_delete_uri_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Notification**](Notification.md)|  | 
 **watcher_id** | **str**|  | 

### Return type

[**NotificationsList**](NotificationsList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_watcher**
> NotificationWatcher get_notification_watcher(watcher_id)

Returns notification watcher by watcher id.

Returns notification watcher by watcher id.

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
api_instance = swagger_client.SystemAdministrationMonitoringNotificationsApi(swagger_client.ApiClient(configuration))
watcher_id = 'watcher_id_example' # str | 

try:
    # Returns notification watcher by watcher id.
    api_response = api_instance.get_notification_watcher(watcher_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringNotificationsApi->get_notification_watcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watcher_id** | **str**|  | 

### Return type

[**NotificationWatcher**](NotificationWatcher.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications**
> NotificationsList get_notifications(watcher_id)

Get notifications for the specified watcher ID.

Get notifications for the specified watcher ID.

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
api_instance = swagger_client.SystemAdministrationMonitoringNotificationsApi(swagger_client.ApiClient(configuration))
watcher_id = 'watcher_id_example' # str | 

try:
    # Get notifications for the specified watcher ID.
    api_response = api_instance.get_notifications(watcher_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringNotificationsApi->get_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watcher_id** | **str**|  | 

### Return type

[**NotificationsList**](NotificationsList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_watchers**
> NotificationWatcherListResult list_notification_watchers()

Returns a list of registered notification watchers.

Returns a list of registered notification watchers.

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
api_instance = swagger_client.SystemAdministrationMonitoringNotificationsApi(swagger_client.ApiClient(configuration))

try:
    # Returns a list of registered notification watchers.
    api_response = api_instance.list_notification_watchers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringNotificationsApi->list_notification_watchers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationWatcherListResult**](NotificationWatcherListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_watcher**
> NotificationWatcher update_notification_watcher(body, watcher_id)

Update notification watcher.

Update notification watcher.

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
api_instance = swagger_client.SystemAdministrationMonitoringNotificationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.NotificationWatcher() # NotificationWatcher | 
watcher_id = 'watcher_id_example' # str | 

try:
    # Update notification watcher.
    api_response = api_instance.update_notification_watcher(body, watcher_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringNotificationsApi->update_notification_watcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationWatcher**](NotificationWatcher.md)|  | 
 **watcher_id** | **str**|  | 

### Return type

[**NotificationWatcher**](NotificationWatcher.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notifications**
> NotificationsList update_notifications(body, watcher_id)

Update notifications for the specified watcher ID.

Update notifications for the specified watcher ID.

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
api_instance = swagger_client.SystemAdministrationMonitoringNotificationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.NotificationsList() # NotificationsList | 
watcher_id = 'watcher_id_example' # str | 

try:
    # Update notifications for the specified watcher ID.
    api_response = api_instance.update_notifications(body, watcher_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringNotificationsApi->update_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationsList**](NotificationsList.md)|  | 
 **watcher_id** | **str**|  | 

### Return type

[**NotificationsList**](NotificationsList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

