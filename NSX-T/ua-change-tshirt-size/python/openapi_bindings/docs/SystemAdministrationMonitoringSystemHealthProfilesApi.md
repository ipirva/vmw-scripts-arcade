# swagger_client.SystemAdministrationMonitoringSystemHealthProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_system_health_agent_profile**](SystemAdministrationMonitoringSystemHealthProfilesApi.md#create_system_health_agent_profile) | **POST** /systemhealth/profiles | Create a system health profile
[**delete_system_health_agent_profile**](SystemAdministrationMonitoringSystemHealthProfilesApi.md#delete_system_health_agent_profile) | **DELETE** /systemhealth/profiles/{profile-id} | Delete an existing system health profile
[**list_system_health_agent_profiles**](SystemAdministrationMonitoringSystemHealthProfilesApi.md#list_system_health_agent_profiles) | **GET** /systemhealth/profiles | List all system health profiles
[**show_system_health_agent_profile**](SystemAdministrationMonitoringSystemHealthProfilesApi.md#show_system_health_agent_profile) | **GET** /systemhealth/profiles/{profile-id} | Show the details of a system health profile
[**update_system_health_agent_profile**](SystemAdministrationMonitoringSystemHealthProfilesApi.md#update_system_health_agent_profile) | **PUT** /systemhealth/profiles/{profile-id} | Update a system health profile

# **create_system_health_agent_profile**
> SystemHealthAgentProfile create_system_health_agent_profile(body)

Create a system health profile

Create a system health profile. 

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SystemHealthAgentProfile() # SystemHealthAgentProfile | 

try:
    # Create a system health profile
    api_response = api_instance.create_system_health_agent_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthProfilesApi->create_system_health_agent_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemHealthAgentProfile**](SystemHealthAgentProfile.md)|  | 

### Return type

[**SystemHealthAgentProfile**](SystemHealthAgentProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_system_health_agent_profile**
> delete_system_health_agent_profile(profile_id)

Delete an existing system health profile

Delete an existing system health profile by ID.

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthProfilesApi(swagger_client.ApiClient(configuration))
profile_id = 'profile_id_example' # str | 

try:
    # Delete an existing system health profile
    api_instance.delete_system_health_agent_profile(profile_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthProfilesApi->delete_system_health_agent_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_system_health_agent_profiles**
> SystemHealthAgentProfileListResult list_system_health_agent_profiles()

List all system health profiles

List all system health profiles. 

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthProfilesApi(swagger_client.ApiClient(configuration))

try:
    # List all system health profiles
    api_response = api_instance.list_system_health_agent_profiles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthProfilesApi->list_system_health_agent_profiles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemHealthAgentProfileListResult**](SystemHealthAgentProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_system_health_agent_profile**
> SystemHealthAgentProfile show_system_health_agent_profile(profile_id)

Show the details of a system health profile

Show the details of a system health profile. 

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthProfilesApi(swagger_client.ApiClient(configuration))
profile_id = 'profile_id_example' # str | 

try:
    # Show the details of a system health profile
    api_response = api_instance.show_system_health_agent_profile(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthProfilesApi->show_system_health_agent_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

[**SystemHealthAgentProfile**](SystemHealthAgentProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_system_health_agent_profile**
> SystemHealthAgentProfile update_system_health_agent_profile(body, profile_id)

Update a system health profile

Update a system health profile definition. 

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SystemHealthAgentProfile() # SystemHealthAgentProfile | 
profile_id = 'profile_id_example' # str | 

try:
    # Update a system health profile
    api_response = api_instance.update_system_health_agent_profile(body, profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthProfilesApi->update_system_health_agent_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemHealthAgentProfile**](SystemHealthAgentProfile.md)|  | 
 **profile_id** | **str**|  | 

### Return type

[**SystemHealthAgentProfile**](SystemHealthAgentProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

