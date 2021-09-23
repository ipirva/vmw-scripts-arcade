# swagger_client.SystemAdministrationMonitoringAlarmsAndEventsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_alarms_set_status**](SystemAdministrationMonitoringAlarmsAndEventsApi.md#bulk_update_alarms_set_status) | **POST** /alarms?action&#x3D;set_status | Bulk update the status of zero or more Alarms.
[**get_alarm**](SystemAdministrationMonitoringAlarmsAndEventsApi.md#get_alarm) | **GET** /alarms/{alarm-id} | Get Alarm identified by alarm-id.
[**get_alarms**](SystemAdministrationMonitoringAlarmsAndEventsApi.md#get_alarms) | **GET** /alarms | Get the list of all Alarms currently known to the system.
[**get_event**](SystemAdministrationMonitoringAlarmsAndEventsApi.md#get_event) | **GET** /events/{event-id} | Get Events identified by event-id.
[**list_events**](SystemAdministrationMonitoringAlarmsAndEventsApi.md#list_events) | **GET** /events | Get the list of all Events defined in NSX.
[**reset_event_values_set_default**](SystemAdministrationMonitoringAlarmsAndEventsApi.md#reset_event_values_set_default) | **POST** /events/{event-id}?action&#x3D;set_default | Reset all user configurable values to factory defaults.
[**update_alarm_status_set_status**](SystemAdministrationMonitoringAlarmsAndEventsApi.md#update_alarm_status_set_status) | **POST** /alarms/{alarm-id}?action&#x3D;set_status | Update staus of alarm identified by alarm-id.
[**update_event**](SystemAdministrationMonitoringAlarmsAndEventsApi.md#update_event) | **PUT** /events/{event-id} | Update event associated with event-id.

# **bulk_update_alarms_set_status**
> bulk_update_alarms_set_status(new_status, after=after, before=before, cursor=cursor, event_type=event_type, feature_name=feature_name, id=id, intent_path=intent_path, node_id=node_id, node_resource_type=node_resource_type, page_size=page_size, severity=severity, sort_ascending=sort_ascending, sort_by=sort_by, status=status, suppress_duration=suppress_duration)

Bulk update the status of zero or more Alarms.

Bulk update the status of zero or more Alarms that match the specified filters. The new_status value can be OPEN, ACKNOWLEDGED, SUPPRESSED, or RESOLVED. If new_status is SUPPRESSED, the suppress_duration query parameter must also be specified.

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
api_instance = swagger_client.SystemAdministrationMonitoringAlarmsAndEventsApi(swagger_client.ApiClient(configuration))
new_status = 'new_status_example' # str | Status
after = 789 # int | Timestamp in milliseconds since epoch (optional)
before = 789 # int | Timestamp in milliseconds since epoch (optional)
cursor = 'cursor_example' # str | Cursor for pagination (optional)
event_type = 'event_type_example' # str | Event Type Filter (optional)
feature_name = 'feature_name_example' # str | Feature Name (optional)
id = 'id_example' # str | Alarm ID (optional)
intent_path = 'intent_path_example' # str | Intent Path for entity ID (optional)
node_id = 'node_id_example' # str | Node ID (optional)
node_resource_type = 'node_resource_type_example' # str | Node Resource Type (optional)
page_size = 789 # int | Page Size for pagination (optional)
severity = 'severity_example' # str | Severity (optional)
sort_ascending = true # bool | Represents order of sorting the values (optional) (default to true)
sort_by = 'sort_by_example' # str | Key for sorting on this column (optional)
status = 'status_example' # str | Status (optional)
suppress_duration = 789 # int | Duration in hours for which Alarm should be suppressed (optional)

try:
    # Bulk update the status of zero or more Alarms.
    api_instance.bulk_update_alarms_set_status(new_status, after=after, before=before, cursor=cursor, event_type=event_type, feature_name=feature_name, id=id, intent_path=intent_path, node_id=node_id, node_resource_type=node_resource_type, page_size=page_size, severity=severity, sort_ascending=sort_ascending, sort_by=sort_by, status=status, suppress_duration=suppress_duration)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringAlarmsAndEventsApi->bulk_update_alarms_set_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_status** | **str**| Status | 
 **after** | **int**| Timestamp in milliseconds since epoch | [optional] 
 **before** | **int**| Timestamp in milliseconds since epoch | [optional] 
 **cursor** | **str**| Cursor for pagination | [optional] 
 **event_type** | **str**| Event Type Filter | [optional] 
 **feature_name** | **str**| Feature Name | [optional] 
 **id** | **str**| Alarm ID | [optional] 
 **intent_path** | **str**| Intent Path for entity ID | [optional] 
 **node_id** | **str**| Node ID | [optional] 
 **node_resource_type** | **str**| Node Resource Type | [optional] 
 **page_size** | **int**| Page Size for pagination | [optional] 
 **severity** | **str**| Severity | [optional] 
 **sort_ascending** | **bool**| Represents order of sorting the values | [optional] [default to true]
 **sort_by** | **str**| Key for sorting on this column | [optional] 
 **status** | **str**| Status | [optional] 
 **suppress_duration** | **int**| Duration in hours for which Alarm should be suppressed | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarm**
> Alarm get_alarm(alarm_id)

Get Alarm identified by alarm-id.

Returns alarm associated with alarm-id. If HTTP status 404 is returned, this means the specified alarm-id is invalid or the alarm with alarm-id has been deleted. An alarm is deleted by the system if it is RESOLVED and older than eight days. The system can also delete the remaining RESOLVED alarms sooner to free system resources when too many alarms are being generated. When this happens the oldest day's RESOLVED alarms are deleted first. 

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
api_instance = swagger_client.SystemAdministrationMonitoringAlarmsAndEventsApi(swagger_client.ApiClient(configuration))
alarm_id = 'alarm_id_example' # str | 

try:
    # Get Alarm identified by alarm-id.
    api_response = api_instance.get_alarm(alarm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringAlarmsAndEventsApi->get_alarm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_id** | **str**|  | 

### Return type

[**Alarm**](Alarm.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarms**
> AlarmsListResult get_alarms(after=after, before=before, cursor=cursor, event_type=event_type, feature_name=feature_name, id=id, intent_path=intent_path, node_id=node_id, node_resource_type=node_resource_type, page_size=page_size, severity=severity, sort_ascending=sort_ascending, sort_by=sort_by, status=status)

Get the list of all Alarms currently known to the system.

Returns a list of all Alarms currently known to the system.

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
api_instance = swagger_client.SystemAdministrationMonitoringAlarmsAndEventsApi(swagger_client.ApiClient(configuration))
after = 789 # int | Timestamp in milliseconds since epoch (optional)
before = 789 # int | Timestamp in milliseconds since epoch (optional)
cursor = 'cursor_example' # str | Cursor for pagination (optional)
event_type = 'event_type_example' # str | Event Type Filter (optional)
feature_name = 'feature_name_example' # str | Feature Name (optional)
id = 'id_example' # str | Alarm ID (optional)
intent_path = 'intent_path_example' # str | Intent Path for entity ID (optional)
node_id = 'node_id_example' # str | Node ID (optional)
node_resource_type = 'node_resource_type_example' # str | Node Resource Type (optional)
page_size = 789 # int | Page Size for pagination (optional)
severity = 'severity_example' # str | Severity (optional)
sort_ascending = true # bool | Represents order of sorting the values (optional) (default to true)
sort_by = 'sort_by_example' # str | Key for sorting on this column (optional)
status = 'status_example' # str | Status (optional)

try:
    # Get the list of all Alarms currently known to the system.
    api_response = api_instance.get_alarms(after=after, before=before, cursor=cursor, event_type=event_type, feature_name=feature_name, id=id, intent_path=intent_path, node_id=node_id, node_resource_type=node_resource_type, page_size=page_size, severity=severity, sort_ascending=sort_ascending, sort_by=sort_by, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringAlarmsAndEventsApi->get_alarms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **int**| Timestamp in milliseconds since epoch | [optional] 
 **before** | **int**| Timestamp in milliseconds since epoch | [optional] 
 **cursor** | **str**| Cursor for pagination | [optional] 
 **event_type** | **str**| Event Type Filter | [optional] 
 **feature_name** | **str**| Feature Name | [optional] 
 **id** | **str**| Alarm ID | [optional] 
 **intent_path** | **str**| Intent Path for entity ID | [optional] 
 **node_id** | **str**| Node ID | [optional] 
 **node_resource_type** | **str**| Node Resource Type | [optional] 
 **page_size** | **int**| Page Size for pagination | [optional] 
 **severity** | **str**| Severity | [optional] 
 **sort_ascending** | **bool**| Represents order of sorting the values | [optional] [default to true]
 **sort_by** | **str**| Key for sorting on this column | [optional] 
 **status** | **str**| Status | [optional] 

### Return type

[**AlarmsListResult**](AlarmsListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event**
> MonitoringEvent get_event(event_id)

Get Events identified by event-id.

Returns event associated with event-id.

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
api_instance = swagger_client.SystemAdministrationMonitoringAlarmsAndEventsApi(swagger_client.ApiClient(configuration))
event_id = 'event_id_example' # str | 

try:
    # Get Events identified by event-id.
    api_response = api_instance.get_event(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringAlarmsAndEventsApi->get_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

[**MonitoringEvent**](MonitoringEvent.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_events**
> EventListResult list_events()

Get the list of all Events defined in NSX.

Returns a list of all Events defined in NSX.

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
api_instance = swagger_client.SystemAdministrationMonitoringAlarmsAndEventsApi(swagger_client.ApiClient(configuration))

try:
    # Get the list of all Events defined in NSX.
    api_response = api_instance.list_events()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringAlarmsAndEventsApi->list_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EventListResult**](EventListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_event_values_set_default**
> MonitoringEvent reset_event_values_set_default(event_id)

Reset all user configurable values to factory defaults.

Reset all user configurable values for event identified by event-id to factory defaults.

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
api_instance = swagger_client.SystemAdministrationMonitoringAlarmsAndEventsApi(swagger_client.ApiClient(configuration))
event_id = 'event_id_example' # str | 

try:
    # Reset all user configurable values to factory defaults.
    api_response = api_instance.reset_event_values_set_default(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringAlarmsAndEventsApi->reset_event_values_set_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

[**MonitoringEvent**](MonitoringEvent.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alarm_status_set_status**
> Alarm update_alarm_status_set_status(alarm_id, new_status, suppress_duration=suppress_duration)

Update staus of alarm identified by alarm-id.

Update status of an Alarm. The new_status value can be OPEN, ACKNOWLEDGED, SUPPRESSED, or RESOLVED. If new_status is SUPPRESSED, the suppress_duration query parameter must also be specified.

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
api_instance = swagger_client.SystemAdministrationMonitoringAlarmsAndEventsApi(swagger_client.ApiClient(configuration))
alarm_id = 'alarm_id_example' # str | 
new_status = 'new_status_example' # str | Status
suppress_duration = 789 # int | Duration in hours for which Alarm should be suppressed (optional)

try:
    # Update staus of alarm identified by alarm-id.
    api_response = api_instance.update_alarm_status_set_status(alarm_id, new_status, suppress_duration=suppress_duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringAlarmsAndEventsApi->update_alarm_status_set_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_id** | **str**|  | 
 **new_status** | **str**| Status | 
 **suppress_duration** | **int**| Duration in hours for which Alarm should be suppressed | [optional] 

### Return type

[**Alarm**](Alarm.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event**
> MonitoringEvent update_event(body, event_id)

Update event associated with event-id.

Update event identified by event-id.

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
api_instance = swagger_client.SystemAdministrationMonitoringAlarmsAndEventsApi(swagger_client.ApiClient(configuration))
body = swagger_client.MonitoringEvent() # MonitoringEvent | 
event_id = 'event_id_example' # str | 

try:
    # Update event associated with event-id.
    api_response = api_instance.update_event(body, event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringAlarmsAndEventsApi->update_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringEvent**](MonitoringEvent.md)|  | 
 **event_id** | **str**|  | 

### Return type

[**MonitoringEvent**](MonitoringEvent.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

