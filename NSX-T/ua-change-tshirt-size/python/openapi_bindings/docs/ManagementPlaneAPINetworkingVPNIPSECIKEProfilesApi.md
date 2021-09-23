# swagger_client.ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ip_sec_vpnike_profile**](ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi.md#create_ip_sec_vpnike_profile) | **POST** /vpn/ipsec/ike-profiles | Create custom internet key exchange (IKE) Profile
[**delete_ip_sec_vpnike_profile**](ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi.md#delete_ip_sec_vpnike_profile) | **DELETE** /vpn/ipsec/ike-profiles/{ipsec-vpn-ike-profile-id} | Delete custom IKE Profile
[**get_ip_sec_vpnike_profile**](ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi.md#get_ip_sec_vpnike_profile) | **GET** /vpn/ipsec/ike-profiles/{ipsec-vpn-ike-profile-id} | Get IKE Profile
[**list_ip_sec_vpnike_profiles**](ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi.md#list_ip_sec_vpnike_profiles) | **GET** /vpn/ipsec/ike-profiles | List IKE profiles
[**update_ip_sec_vpnike_profile**](ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi.md#update_ip_sec_vpnike_profile) | **PUT** /vpn/ipsec/ike-profiles/{ipsec-vpn-ike-profile-id} | Edit custom IKE Profile

# **create_ip_sec_vpnike_profile**
> IPSecVPNIKEProfile create_ip_sec_vpnike_profile(body)

Create custom internet key exchange (IKE) Profile

Create custom internet key exchange (IKE) Profile. IKE Profile is a reusable profile that captures IKE and phase one negotiation parameters. System will be pre provisioned with system owned non editable default IKE profile and suggested set of profiles that can be used for peering with popular remote peers like AWS VPN. User can create custom profiles as needed. Any change in profile affects all sessions consuming this profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNIKEProfile() # IPSecVPNIKEProfile | 

try:
    # Create custom internet key exchange (IKE) Profile
    api_response = api_instance.create_ip_sec_vpnike_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi->create_ip_sec_vpnike_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNIKEProfile**](IPSecVPNIKEProfile.md)|  | 

### Return type

[**IPSecVPNIKEProfile**](IPSecVPNIKEProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_sec_vpnike_profile**
> delete_ip_sec_vpnike_profile(ipsec_vpn_ike_profile_id, force=force)

Delete custom IKE Profile

Delete custom IKE Profile. Profile can not be deleted if profile has references to it.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi(swagger_client.ApiClient(configuration))
ipsec_vpn_ike_profile_id = 'ipsec_vpn_ike_profile_id_example' # str | 
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete custom IKE Profile
    api_instance.delete_ip_sec_vpnike_profile(ipsec_vpn_ike_profile_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi->delete_ip_sec_vpnike_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_ike_profile_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_sec_vpnike_profile**
> IPSecVPNIKEProfile get_ip_sec_vpnike_profile(ipsec_vpn_ike_profile_id)

Get IKE Profile

Get custom IKE Profile, given the particular id.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi(swagger_client.ApiClient(configuration))
ipsec_vpn_ike_profile_id = 'ipsec_vpn_ike_profile_id_example' # str | 

try:
    # Get IKE Profile
    api_response = api_instance.get_ip_sec_vpnike_profile(ipsec_vpn_ike_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi->get_ip_sec_vpnike_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_ike_profile_id** | **str**|  | 

### Return type

[**IPSecVPNIKEProfile**](IPSecVPNIKEProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_sec_vpnike_profiles**
> IPSecVPNIKEProfileListResult list_ip_sec_vpnike_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List IKE profiles

Get paginated list of all IKE Profiles.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List IKE profiles
    api_response = api_instance.list_ip_sec_vpnike_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi->list_ip_sec_vpnike_profiles: %s\n" % e)
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

[**IPSecVPNIKEProfileListResult**](IPSecVPNIKEProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_sec_vpnike_profile**
> IPSecVPNIKEProfile update_ip_sec_vpnike_profile(body, ipsec_vpn_ike_profile_id)

Edit custom IKE Profile

Edit custom IKE Profile. System owned profiles are non editable.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNIKEProfile() # IPSecVPNIKEProfile | 
ipsec_vpn_ike_profile_id = 'ipsec_vpn_ike_profile_id_example' # str | 

try:
    # Edit custom IKE Profile
    api_response = api_instance.update_ip_sec_vpnike_profile(body, ipsec_vpn_ike_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECIKEProfilesApi->update_ip_sec_vpnike_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNIKEProfile**](IPSecVPNIKEProfile.md)|  | 
 **ipsec_vpn_ike_profile_id** | **str**|  | 

### Return type

[**IPSecVPNIKEProfile**](IPSecVPNIKEProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

