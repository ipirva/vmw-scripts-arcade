# swagger_client.ManagementPlaneAPINetworkingVPNL2VPNSessionsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_l2_vpn_session**](ManagementPlaneAPINetworkingVPNL2VPNSessionsApi.md#create_l2_vpn_session) | **POST** /vpn/l2vpn/sessions | Create L2VPN session
[**delete_l2_vpn_session**](ManagementPlaneAPINetworkingVPNL2VPNSessionsApi.md#delete_l2_vpn_session) | **DELETE** /vpn/l2vpn/sessions/{l2vpn-session-id} | Delete a L2VPN session
[**get_l2_vpn_session**](ManagementPlaneAPINetworkingVPNL2VPNSessionsApi.md#get_l2_vpn_session) | **GET** /vpn/l2vpn/sessions/{l2vpn-session-id} | Get a L2VPN session
[**get_l2_vpn_session_peer_codes**](ManagementPlaneAPINetworkingVPNL2VPNSessionsApi.md#get_l2_vpn_session_peer_codes) | **GET** /vpn/l2vpn/sessions/{l2vpn-session-id}/peer-codes | Get peer codes for the L2VpnSession
[**list_l2_vpn_sessions**](ManagementPlaneAPINetworkingVPNL2VPNSessionsApi.md#list_l2_vpn_sessions) | **GET** /vpn/l2vpn/sessions | Get all L2VPN sessions
[**update_l2_vpn_session**](ManagementPlaneAPINetworkingVPNL2VPNSessionsApi.md#update_l2_vpn_session) | **PUT** /vpn/l2vpn/sessions/{l2vpn-session-id} | Edit a L2VPN session

# **create_l2_vpn_session**
> L2VpnSession create_l2_vpn_session(body)

Create L2VPN session

Create L2VPN session and bind to a L2VPNService

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNL2VPNSessionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.L2VpnSession() # L2VpnSession | 

try:
    # Create L2VPN session
    api_response = api_instance.create_l2_vpn_session(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNL2VPNSessionsApi->create_l2_vpn_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**L2VpnSession**](L2VpnSession.md)|  | 

### Return type

[**L2VpnSession**](L2VpnSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_l2_vpn_session**
> delete_l2_vpn_session(l2vpn_session_id)

Delete a L2VPN session

Delete a specific L2VPN session. If there are any logical switch ports attached to it, those needs to be deleted first.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNL2VPNSessionsApi(swagger_client.ApiClient(configuration))
l2vpn_session_id = 'l2vpn_session_id_example' # str | 

try:
    # Delete a L2VPN session
    api_instance.delete_l2_vpn_session(l2vpn_session_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNL2VPNSessionsApi->delete_l2_vpn_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **l2vpn_session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l2_vpn_session**
> L2VpnSession get_l2_vpn_session(l2vpn_session_id)

Get a L2VPN session

Get a specific L2VPN session

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNL2VPNSessionsApi(swagger_client.ApiClient(configuration))
l2vpn_session_id = 'l2vpn_session_id_example' # str | 

try:
    # Get a L2VPN session
    api_response = api_instance.get_l2_vpn_session(l2vpn_session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNL2VPNSessionsApi->get_l2_vpn_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **l2vpn_session_id** | **str**|  | 

### Return type

[**L2VpnSession**](L2VpnSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l2_vpn_session_peer_codes**
> L2VpnSessionPeerCodes get_l2_vpn_session_peer_codes(l2vpn_session_id)

Get peer codes for the L2VpnSession

Get peer codes for the L2VPN session to program the remote side of the tunnel.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNL2VPNSessionsApi(swagger_client.ApiClient(configuration))
l2vpn_session_id = 'l2vpn_session_id_example' # str | 

try:
    # Get peer codes for the L2VpnSession
    api_response = api_instance.get_l2_vpn_session_peer_codes(l2vpn_session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNL2VPNSessionsApi->get_l2_vpn_session_peer_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **l2vpn_session_id** | **str**|  | 

### Return type

[**L2VpnSessionPeerCodes**](L2VpnSessionPeerCodes.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_l2_vpn_sessions**
> L2VpnSessionListResult list_l2_vpn_sessions(cursor=cursor, included_fields=included_fields, l2vpn_service_id=l2vpn_service_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get all L2VPN sessions

Get paginated list of all L2VPN sessions

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNL2VPNSessionsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
l2vpn_service_id = 'l2vpn_service_id_example' # str | Id of the L2Vpn Service (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get all L2VPN sessions
    api_response = api_instance.list_l2_vpn_sessions(cursor=cursor, included_fields=included_fields, l2vpn_service_id=l2vpn_service_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNL2VPNSessionsApi->list_l2_vpn_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **l2vpn_service_id** | **str**| Id of the L2Vpn Service | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**L2VpnSessionListResult**](L2VpnSessionListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_l2_vpn_session**
> L2VpnSession update_l2_vpn_session(body, l2vpn_session_id)

Edit a L2VPN session

Edit a specific L2VPN session

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNL2VPNSessionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.L2VpnSession() # L2VpnSession | 
l2vpn_session_id = 'l2vpn_session_id_example' # str | 

try:
    # Edit a L2VPN session
    api_response = api_instance.update_l2_vpn_session(body, l2vpn_session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNL2VPNSessionsApi->update_l2_vpn_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**L2VpnSession**](L2VpnSession.md)|  | 
 **l2vpn_session_id** | **str**|  | 

### Return type

[**L2VpnSession**](L2VpnSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

