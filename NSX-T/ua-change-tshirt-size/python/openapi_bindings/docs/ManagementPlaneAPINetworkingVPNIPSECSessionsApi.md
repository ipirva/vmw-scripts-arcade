# swagger_client.ManagementPlaneAPINetworkingVPNIPSECSessionsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ip_sec_vpn_session**](ManagementPlaneAPINetworkingVPNIPSECSessionsApi.md#create_ip_sec_vpn_session) | **POST** /vpn/ipsec/sessions | Create new VPN session
[**delete_ip_sec_vpn_session**](ManagementPlaneAPINetworkingVPNIPSECSessionsApi.md#delete_ip_sec_vpn_session) | **DELETE** /vpn/ipsec/sessions/{ipsec-vpn-session-id} | Delete IPSec VPN session
[**get_ip_sec_vpn_session**](ManagementPlaneAPINetworkingVPNIPSECSessionsApi.md#get_ip_sec_vpn_session) | **GET** /vpn/ipsec/sessions/{ipsec-vpn-session-id} | Fetch IPSec VPN session
[**get_ip_sec_vpn_session_state**](ManagementPlaneAPINetworkingVPNIPSECSessionsApi.md#get_ip_sec_vpn_session_state) | **GET** /vpn/ipsec/sessions/{ipsec-vpn-session-id}/state | Get the Realized State of a IPSec VPN Session
[**get_peer_config**](ManagementPlaneAPINetworkingVPNIPSECSessionsApi.md#get_peer_config) | **GET** /vpn/ipsec/sessions/{ipsec-vpn-session-id}/peer-config | Get VPN configuration for the peer site
[**list_ip_sec_vpn_sessions**](ManagementPlaneAPINetworkingVPNIPSECSessionsApi.md#list_ip_sec_vpn_sessions) | **GET** /vpn/ipsec/sessions | Get IPSec VPN session list result
[**update_ip_sec_vpn_session**](ManagementPlaneAPINetworkingVPNIPSECSessionsApi.md#update_ip_sec_vpn_session) | **PUT** /vpn/ipsec/sessions/{ipsec-vpn-session-id} | Edit IPSec VPN session

# **create_ip_sec_vpn_session**
> IPSecVPNSession create_ip_sec_vpn_session(body)

Create new VPN session

Create new VPN session.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECSessionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNSession() # IPSecVPNSession | 

try:
    # Create new VPN session
    api_response = api_instance.create_ip_sec_vpn_session(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECSessionsApi->create_ip_sec_vpn_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNSession**](IPSecVPNSession.md)|  | 

### Return type

[**IPSecVPNSession**](IPSecVPNSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_sec_vpn_session**
> delete_ip_sec_vpn_session(ipsec_vpn_session_id, force=force)

Delete IPSec VPN session

Delete IPSec VPN session.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECSessionsApi(swagger_client.ApiClient(configuration))
ipsec_vpn_session_id = 'ipsec_vpn_session_id_example' # str | 
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete IPSec VPN session
    api_instance.delete_ip_sec_vpn_session(ipsec_vpn_session_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECSessionsApi->delete_ip_sec_vpn_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_session_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_sec_vpn_session**
> IPSecVPNSession get_ip_sec_vpn_session(ipsec_vpn_session_id)

Fetch IPSec VPN session

Fetch IPSec VPN session.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECSessionsApi(swagger_client.ApiClient(configuration))
ipsec_vpn_session_id = 'ipsec_vpn_session_id_example' # str | 

try:
    # Fetch IPSec VPN session
    api_response = api_instance.get_ip_sec_vpn_session(ipsec_vpn_session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECSessionsApi->get_ip_sec_vpn_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_session_id** | **str**|  | 

### Return type

[**IPSecVPNSession**](IPSecVPNSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_sec_vpn_session_state**
> IPSecVPNSessionState get_ip_sec_vpn_session_state(ipsec_vpn_session_id, barrier_id=barrier_id, request_id=request_id)

Get the Realized State of a IPSec VPN Session

Return realized state information of a ipsec vpn session. Any configuration update that affects the ipsec vpn session can use this API to get its realized state by passing a request_id returned by the configuration change operation. e.g. Update configuration of ipsec vpn session, service, endpoints, profiles, etc. It will return a service disabled error, if the ipsec vpn service associated with the session is disabled. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECSessionsApi(swagger_client.ApiClient(configuration))
ipsec_vpn_session_id = 'ipsec_vpn_session_id_example' # str | 
barrier_id = 789 # int |  (optional)
request_id = 'request_id_example' # str | Realization request ID (optional)

try:
    # Get the Realized State of a IPSec VPN Session
    api_response = api_instance.get_ip_sec_vpn_session_state(ipsec_vpn_session_id, barrier_id=barrier_id, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECSessionsApi->get_ip_sec_vpn_session_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_session_id** | **str**|  | 
 **barrier_id** | **int**|  | [optional] 
 **request_id** | **str**| Realization request ID | [optional] 

### Return type

[**IPSecVPNSessionState**](IPSecVPNSessionState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peer_config**
> str get_peer_config(ipsec_vpn_session_id)

Get VPN configuration for the peer site

API to download VPN configuration for the peer site. The configuration contains pre-shared key and secret; be careful when sharing or storing it.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECSessionsApi(swagger_client.ApiClient(configuration))
ipsec_vpn_session_id = 'ipsec_vpn_session_id_example' # str | 

try:
    # Get VPN configuration for the peer site
    api_response = api_instance.get_peer_config(ipsec_vpn_session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECSessionsApi->get_peer_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_session_id** | **str**|  | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_sec_vpn_sessions**
> IPSecVPNSessionListResult list_ip_sec_vpn_sessions(cursor=cursor, included_fields=included_fields, ipsec_vpn_service_id=ipsec_vpn_service_id, logical_router_id=logical_router_id, page_size=page_size, session_type=session_type, sort_ascending=sort_ascending, sort_by=sort_by)

Get IPSec VPN session list result

Get paginated list of all IPSec VPN sessions.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECSessionsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
ipsec_vpn_service_id = 'ipsec_vpn_service_id_example' # str | Id of the IPSec VPN service (optional)
logical_router_id = 'logical_router_id_example' # str | Id of logical router (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
session_type = 'session_type_example' # str | Resource types of IPsec VPN session (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get IPSec VPN session list result
    api_response = api_instance.list_ip_sec_vpn_sessions(cursor=cursor, included_fields=included_fields, ipsec_vpn_service_id=ipsec_vpn_service_id, logical_router_id=logical_router_id, page_size=page_size, session_type=session_type, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECSessionsApi->list_ip_sec_vpn_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **ipsec_vpn_service_id** | **str**| Id of the IPSec VPN service | [optional] 
 **logical_router_id** | **str**| Id of logical router | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **session_type** | **str**| Resource types of IPsec VPN session | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IPSecVPNSessionListResult**](IPSecVPNSessionListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_sec_vpn_session**
> IPSecVPNSession update_ip_sec_vpn_session(body, ipsec_vpn_session_id)

Edit IPSec VPN session

Edit IPSec VPN session.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECSessionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNSession() # IPSecVPNSession | 
ipsec_vpn_session_id = 'ipsec_vpn_session_id_example' # str | 

try:
    # Edit IPSec VPN session
    api_response = api_instance.update_ip_sec_vpn_session(body, ipsec_vpn_session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECSessionsApi->update_ip_sec_vpn_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNSession**](IPSecVPNSession.md)|  | 
 **ipsec_vpn_session_id** | **str**|  | 

### Return type

[**IPSecVPNSession**](IPSecVPNSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

