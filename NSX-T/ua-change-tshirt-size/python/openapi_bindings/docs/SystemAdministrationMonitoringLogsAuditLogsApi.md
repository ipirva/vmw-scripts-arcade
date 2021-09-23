# swagger_client.SystemAdministrationMonitoringLogsAuditLogsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collect_audit_logs**](SystemAdministrationMonitoringLogsAuditLogsApi.md#collect_audit_logs) | **POST** /administration/audit-logs | Collect audit logs from registered manager nodes

# **collect_audit_logs**
> AuditLogListResult collect_audit_logs(body, cursor=cursor, fields=fields, page_size=page_size)

Collect audit logs from registered manager nodes

This API is executed on a manager node to display audit logs from all nodes inside the management plane cluster. An audit log collection will be triggered if the local master audit log is outdated. 

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
api_instance = swagger_client.SystemAdministrationMonitoringLogsAuditLogsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuditLogRequest() # AuditLogRequest | 
cursor = 789 # int | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
fields = 'fields_example' # str | Fields to include in query results (optional)
page_size = 100 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 100)

try:
    # Collect audit logs from registered manager nodes
    api_response = api_instance.collect_audit_logs(body, cursor=cursor, fields=fields, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringLogsAuditLogsApi->collect_audit_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuditLogRequest**](AuditLogRequest.md)|  | 
 **cursor** | **int**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **fields** | **str**| Fields to include in query results | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 100]

### Return type

[**AuditLogListResult**](AuditLogListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

