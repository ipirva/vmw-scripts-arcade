# swagger_client.ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ip_sec_vpn_tunnel_profile**](ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi.md#create_ip_sec_vpn_tunnel_profile) | **POST** /vpn/ipsec/tunnel-profiles | Create custom IPSec tunnel profile
[**delete_ip_sec_vpn_tunnel_profile**](ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi.md#delete_ip_sec_vpn_tunnel_profile) | **DELETE** /vpn/ipsec/tunnel-profiles/{ipsec-vpn-tunnel-profile-id} | Delete custom IPSecTunnelProfile
[**get_ip_sec_vpn_tunnel_profile**](ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi.md#get_ip_sec_vpn_tunnel_profile) | **GET** /vpn/ipsec/tunnel-profiles/{ipsec-vpn-tunnel-profile-id} | Get IPSec tunnel profile
[**list_ip_sec_vpn_tunnel_profiles**](ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi.md#list_ip_sec_vpn_tunnel_profiles) | **GET** /vpn/ipsec/tunnel-profiles | Get IPSecTunnelProfile List Result
[**update_ip_sec_vpn_tunnel_profile**](ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi.md#update_ip_sec_vpn_tunnel_profile) | **PUT** /vpn/ipsec/tunnel-profiles/{ipsec-vpn-tunnel-profile-id} | Edit custom IPSecTunnelProfile

# **create_ip_sec_vpn_tunnel_profile**
> IPSecVPNTunnelProfile create_ip_sec_vpn_tunnel_profile(body)

Create custom IPSec tunnel profile

Create custom IPSec tunnel profile. IPSec tunnel profile is a reusable profile that captures phase two negotiation parameters and tunnel properties. System will be provisioned with system owned non editable default IPSec tunnel profile. Any change in profile affects all sessions consuming this profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNTunnelProfile() # IPSecVPNTunnelProfile | 

try:
    # Create custom IPSec tunnel profile
    api_response = api_instance.create_ip_sec_vpn_tunnel_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi->create_ip_sec_vpn_tunnel_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNTunnelProfile**](IPSecVPNTunnelProfile.md)|  | 

### Return type

[**IPSecVPNTunnelProfile**](IPSecVPNTunnelProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_sec_vpn_tunnel_profile**
> delete_ip_sec_vpn_tunnel_profile(ipsec_vpn_tunnel_profile_id, force=force)

Delete custom IPSecTunnelProfile

Delete custom IPSec Tunnel Profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi(swagger_client.ApiClient(configuration))
ipsec_vpn_tunnel_profile_id = 'ipsec_vpn_tunnel_profile_id_example' # str | 
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete custom IPSecTunnelProfile
    api_instance.delete_ip_sec_vpn_tunnel_profile(ipsec_vpn_tunnel_profile_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi->delete_ip_sec_vpn_tunnel_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_tunnel_profile_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_sec_vpn_tunnel_profile**
> IPSecVPNTunnelProfile get_ip_sec_vpn_tunnel_profile(ipsec_vpn_tunnel_profile_id)

Get IPSec tunnel profile

Get custom IPSec Tunnel Profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi(swagger_client.ApiClient(configuration))
ipsec_vpn_tunnel_profile_id = 'ipsec_vpn_tunnel_profile_id_example' # str | 

try:
    # Get IPSec tunnel profile
    api_response = api_instance.get_ip_sec_vpn_tunnel_profile(ipsec_vpn_tunnel_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi->get_ip_sec_vpn_tunnel_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_tunnel_profile_id** | **str**|  | 

### Return type

[**IPSecVPNTunnelProfile**](IPSecVPNTunnelProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_sec_vpn_tunnel_profiles**
> IPSecVPNTunnelProfileListResult list_ip_sec_vpn_tunnel_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get IPSecTunnelProfile List Result

Get paginated list of all IPSecTunnelProfiles.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get IPSecTunnelProfile List Result
    api_response = api_instance.list_ip_sec_vpn_tunnel_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi->list_ip_sec_vpn_tunnel_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IPSecVPNTunnelProfileListResult**](IPSecVPNTunnelProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_sec_vpn_tunnel_profile**
> IPSecVPNTunnelProfile update_ip_sec_vpn_tunnel_profile(body, ipsec_vpn_tunnel_profile_id)

Edit custom IPSecTunnelProfile

Edit custom IPSec Tunnel Profile. System owned profiles are non editable.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNTunnelProfile() # IPSecVPNTunnelProfile | 
ipsec_vpn_tunnel_profile_id = 'ipsec_vpn_tunnel_profile_id_example' # str | 

try:
    # Edit custom IPSecTunnelProfile
    api_response = api_instance.update_ip_sec_vpn_tunnel_profile(body, ipsec_vpn_tunnel_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi->update_ip_sec_vpn_tunnel_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNTunnelProfile**](IPSecVPNTunnelProfile.md)|  | 
 **ipsec_vpn_tunnel_profile_id** | **str**|  | 

### Return type

[**IPSecVPNTunnelProfile**](IPSecVPNTunnelProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

