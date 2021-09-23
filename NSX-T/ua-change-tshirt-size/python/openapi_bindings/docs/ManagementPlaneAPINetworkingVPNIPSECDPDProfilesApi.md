# swagger_client.ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ip_sec_vpndpd_profile**](ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi.md#create_ip_sec_vpndpd_profile) | **POST** /vpn/ipsec/dpd-profiles | Create dead peer detection (DPD) profile
[**delete_ip_sec_vpndpd_profile**](ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi.md#delete_ip_sec_vpndpd_profile) | **DELETE** /vpn/ipsec/dpd-profiles/{ipsec-vpn-dpd-profile-id} | Delete dead peer detection (DPD) profile
[**get_ip_sec_vpndpd_profile**](ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi.md#get_ip_sec_vpndpd_profile) | **GET** /vpn/ipsec/dpd-profiles/{ipsec-vpn-dpd-profile-id} | Get IPSec dead peer detection (DPD) profile
[**list_ip_sec_vpndpd_profiles**](ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi.md#list_ip_sec_vpndpd_profiles) | **GET** /vpn/ipsec/dpd-profiles | Get IPSec dead peer detection (DPD)  profile list result
[**update_ip_sec_vpndpd_profile**](ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi.md#update_ip_sec_vpndpd_profile) | **PUT** /vpn/ipsec/dpd-profiles/{ipsec-vpn-dpd-profile-id} | Edit IPSec dead peer detection (DPD) profile

# **create_ip_sec_vpndpd_profile**
> IPSecVPNDPDProfile create_ip_sec_vpndpd_profile(body)

Create dead peer detection (DPD) profile

Create dead peer detection (DPD) profile. Any change in profile affects all sessions consuming this profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNDPDProfile() # IPSecVPNDPDProfile | 

try:
    # Create dead peer detection (DPD) profile
    api_response = api_instance.create_ip_sec_vpndpd_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi->create_ip_sec_vpndpd_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNDPDProfile**](IPSecVPNDPDProfile.md)|  | 

### Return type

[**IPSecVPNDPDProfile**](IPSecVPNDPDProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_sec_vpndpd_profile**
> delete_ip_sec_vpndpd_profile(ipsec_vpn_dpd_profile_id, force=force)

Delete dead peer detection (DPD) profile

Delete dead peer detection (DPD) profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi(swagger_client.ApiClient(configuration))
ipsec_vpn_dpd_profile_id = 'ipsec_vpn_dpd_profile_id_example' # str | 
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete dead peer detection (DPD) profile
    api_instance.delete_ip_sec_vpndpd_profile(ipsec_vpn_dpd_profile_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi->delete_ip_sec_vpndpd_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_dpd_profile_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_sec_vpndpd_profile**
> IPSecVPNDPDProfile get_ip_sec_vpndpd_profile(ipsec_vpn_dpd_profile_id)

Get IPSec dead peer detection (DPD) profile

Get IPSec dead peer detection (DPD) profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi(swagger_client.ApiClient(configuration))
ipsec_vpn_dpd_profile_id = 'ipsec_vpn_dpd_profile_id_example' # str | 

try:
    # Get IPSec dead peer detection (DPD) profile
    api_response = api_instance.get_ip_sec_vpndpd_profile(ipsec_vpn_dpd_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi->get_ip_sec_vpndpd_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_vpn_dpd_profile_id** | **str**|  | 

### Return type

[**IPSecVPNDPDProfile**](IPSecVPNDPDProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_sec_vpndpd_profiles**
> IPSecVPNDPDProfileListResult list_ip_sec_vpndpd_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get IPSec dead peer detection (DPD)  profile list result

Get paginated list of all dead peer detection (DPD) profiles.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get IPSec dead peer detection (DPD)  profile list result
    api_response = api_instance.list_ip_sec_vpndpd_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi->list_ip_sec_vpndpd_profiles: %s\n" % e)
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

[**IPSecVPNDPDProfileListResult**](IPSecVPNDPDProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_sec_vpndpd_profile**
> IPSecVPNDPDProfile update_ip_sec_vpndpd_profile(body, ipsec_vpn_dpd_profile_id)

Edit IPSec dead peer detection (DPD) profile

Edit IPSec dead peer detection (DPD) profile.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSecVPNDPDProfile() # IPSecVPNDPDProfile | 
ipsec_vpn_dpd_profile_id = 'ipsec_vpn_dpd_profile_id_example' # str | 

try:
    # Edit IPSec dead peer detection (DPD) profile
    api_response = api_instance.update_ip_sec_vpndpd_profile(body, ipsec_vpn_dpd_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNIPSECDPDProfilesApi->update_ip_sec_vpndpd_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSecVPNDPDProfile**](IPSecVPNDPDProfile.md)|  | 
 **ipsec_vpn_dpd_profile_id** | **str**|  | 

### Return type

[**IPSecVPNDPDProfile**](IPSecVPNDPDProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

