# swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ipfix_collector_config**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#create_ipfix_collector_config) | **POST** /ipfix/collectorconfigs | Create a new IPFIX collector configuration
[**create_ipfix_collector_upm_profile**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#create_ipfix_collector_upm_profile) | **POST** /ipfix-collector-profiles | Create a new IPFIX collector profile
[**create_ipfix_config**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#create_ipfix_config) | **POST** /ipfix/configs | Create a new IPFIX configuration
[**create_ipfix_upm_profile**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#create_ipfix_upm_profile) | **POST** /ipfix-profiles | Create a new IPFIX profile
[**delete_ipfix_collector_config**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#delete_ipfix_collector_config) | **DELETE** /ipfix/collectorconfigs/{collector-config-id} | Delete an existing IPFIX collector configuration
[**delete_ipfix_collector_upm_profile**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#delete_ipfix_collector_upm_profile) | **DELETE** /ipfix-collector-profiles/{ipfix-collector-profile-id} | Delete an existing IPFIX collector profile
[**delete_ipfix_config**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#delete_ipfix_config) | **DELETE** /ipfix/configs/{config-id} | Delete an existing IPFIX configuration
[**delete_ipfix_upm_profile**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#delete_ipfix_upm_profile) | **DELETE** /ipfix-profiles/{ipfix-profile-id} | Delete an existing IPFIX profile
[**get_ipfix_collector_config**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#get_ipfix_collector_config) | **GET** /ipfix/collectorconfigs/{collector-config-id} | Get an existing IPFIX collector configuration
[**get_ipfix_collector_upm_profile**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#get_ipfix_collector_upm_profile) | **GET** /ipfix-collector-profiles/{ipfix-collector-profile-id} | Get an existing IPFIX collector profile
[**get_ipfix_config**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#get_ipfix_config) | **GET** /ipfix/configs/{config-id} | Get an existing IPFIX configuration
[**get_ipfix_obs_points**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#get_ipfix_obs_points) | **GET** /ipfix-obs-points | Get the list of IPFIX observation points
[**get_ipfix_upm_profile**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#get_ipfix_upm_profile) | **GET** /ipfix-profiles/{ipfix-profile-id} | Get an existing IPFIX profile
[**get_switch_ipfix_config**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#get_switch_ipfix_config) | **GET** /ipfix-obs-points/switch-global | Read global switch IPFIX export configuration
[**list_ipfix_collector_config**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#list_ipfix_collector_config) | **GET** /ipfix/collectorconfigs | List IPFIX collector configurations
[**list_ipfix_collector_upm_profiles**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#list_ipfix_collector_upm_profiles) | **GET** /ipfix-collector-profiles | List IPFIX Collector Profies
[**list_ipfix_config**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#list_ipfix_config) | **GET** /ipfix/configs | List IPFIX configuration
[**list_ipfix_upm_profiles**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#list_ipfix_upm_profiles) | **GET** /ipfix-profiles | List IPFIX Profies
[**update_ipfix_collector_config**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#update_ipfix_collector_config) | **PUT** /ipfix/collectorconfigs/{collector-config-id} | Update an existing IPFIX collector configuration
[**update_ipfix_collector_upm_profile**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#update_ipfix_collector_upm_profile) | **PUT** /ipfix-collector-profiles/{ipfix-collector-profile-id} | Update an existing IPFIX collector profile
[**update_ipfix_config**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#update_ipfix_config) | **PUT** /ipfix/configs/{config-id} | Update an existing IPFIX configuration
[**update_ipfix_upm_profile**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#update_ipfix_upm_profile) | **PUT** /ipfix-profiles/{ipfix-profile-id} | Update an existing IPFIX profile
[**update_switch_ipfix_config**](ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi.md#update_switch_ipfix_config) | **PUT** /ipfix-obs-points/switch-global | Update global switch IPFIX export configuration

# **create_ipfix_collector_config**
> IpfixCollectorConfig create_ipfix_collector_config(body)

Create a new IPFIX collector configuration

Create a new IPFIX collector configuration

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixCollectorConfig() # IpfixCollectorConfig | 

try:
    # Create a new IPFIX collector configuration
    api_response = api_instance.create_ipfix_collector_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->create_ipfix_collector_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixCollectorConfig**](IpfixCollectorConfig.md)|  | 

### Return type

[**IpfixCollectorConfig**](IpfixCollectorConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ipfix_collector_upm_profile**
> IpfixCollectorUpmProfile create_ipfix_collector_upm_profile(body)

Create a new IPFIX collector profile

Create a new IPFIX collector profile with essential properties.

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixCollectorUpmProfile() # IpfixCollectorUpmProfile | 

try:
    # Create a new IPFIX collector profile
    api_response = api_instance.create_ipfix_collector_upm_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->create_ipfix_collector_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixCollectorUpmProfile**](IpfixCollectorUpmProfile.md)|  | 

### Return type

[**IpfixCollectorUpmProfile**](IpfixCollectorUpmProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ipfix_config**
> IpfixConfig create_ipfix_config(body)

Create a new IPFIX configuration

Create a new IPFIX configuration

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixConfig() # IpfixConfig | 

try:
    # Create a new IPFIX configuration
    api_response = api_instance.create_ipfix_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->create_ipfix_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixConfig**](IpfixConfig.md)|  | 

### Return type

[**IpfixConfig**](IpfixConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ipfix_upm_profile**
> IpfixUpmProfile create_ipfix_upm_profile(body)

Create a new IPFIX profile

Create a new IPFIX profile with essential properties.

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixUpmProfile() # IpfixUpmProfile | 

try:
    # Create a new IPFIX profile
    api_response = api_instance.create_ipfix_upm_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->create_ipfix_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixUpmProfile**](IpfixUpmProfile.md)|  | 

### Return type

[**IpfixUpmProfile**](IpfixUpmProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ipfix_collector_config**
> delete_ipfix_collector_config(collector_config_id)

Delete an existing IPFIX collector configuration

Delete an existing IPFIX collector configuration

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
collector_config_id = 'collector_config_id_example' # str | 

try:
    # Delete an existing IPFIX collector configuration
    api_instance.delete_ipfix_collector_config(collector_config_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->delete_ipfix_collector_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_config_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ipfix_collector_upm_profile**
> delete_ipfix_collector_upm_profile(ipfix_collector_profile_id)

Delete an existing IPFIX collector profile

Delete an existing IPFIX collector profile by ID.

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
ipfix_collector_profile_id = 'ipfix_collector_profile_id_example' # str | 

try:
    # Delete an existing IPFIX collector profile
    api_instance.delete_ipfix_collector_upm_profile(ipfix_collector_profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->delete_ipfix_collector_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipfix_collector_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ipfix_config**
> delete_ipfix_config(config_id)

Delete an existing IPFIX configuration

Delete an existing IPFIX configuration

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
config_id = 'config_id_example' # str | 

try:
    # Delete an existing IPFIX configuration
    api_instance.delete_ipfix_config(config_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->delete_ipfix_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ipfix_upm_profile**
> delete_ipfix_upm_profile(ipfix_profile_id)

Delete an existing IPFIX profile

Delete an existing IPFIX profile by ID.

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
ipfix_profile_id = 'ipfix_profile_id_example' # str | 

try:
    # Delete an existing IPFIX profile
    api_instance.delete_ipfix_upm_profile(ipfix_profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->delete_ipfix_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipfix_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipfix_collector_config**
> IpfixCollectorConfig get_ipfix_collector_config(collector_config_id)

Get an existing IPFIX collector configuration

Get an existing IPFIX collector configuration

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
collector_config_id = 'collector_config_id_example' # str | 

try:
    # Get an existing IPFIX collector configuration
    api_response = api_instance.get_ipfix_collector_config(collector_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->get_ipfix_collector_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_config_id** | **str**|  | 

### Return type

[**IpfixCollectorConfig**](IpfixCollectorConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipfix_collector_upm_profile**
> IpfixCollectorUpmProfile get_ipfix_collector_upm_profile(ipfix_collector_profile_id)

Get an existing IPFIX collector profile

Get an existing IPFIX collector profile by profile ID.

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
ipfix_collector_profile_id = 'ipfix_collector_profile_id_example' # str | 

try:
    # Get an existing IPFIX collector profile
    api_response = api_instance.get_ipfix_collector_upm_profile(ipfix_collector_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->get_ipfix_collector_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipfix_collector_profile_id** | **str**|  | 

### Return type

[**IpfixCollectorUpmProfile**](IpfixCollectorUpmProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipfix_config**
> IpfixConfig get_ipfix_config(config_id)

Get an existing IPFIX configuration

Get an existing IPFIX configuration

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
config_id = 'config_id_example' # str | 

try:
    # Get an existing IPFIX configuration
    api_response = api_instance.get_ipfix_config(config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->get_ipfix_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  | 

### Return type

[**IpfixConfig**](IpfixConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipfix_obs_points**
> IpfixObsPointsListResult get_ipfix_obs_points()

Get the list of IPFIX observation points

Deprecated - Please use /ipfix-profiles for switch IPFIX profile and /ipfix-collector-profiles for IPFIX collector profile. 

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))

try:
    # Get the list of IPFIX observation points
    api_response = api_instance.get_ipfix_obs_points()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->get_ipfix_obs_points: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IpfixObsPointsListResult**](IpfixObsPointsListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipfix_upm_profile**
> IpfixUpmProfile get_ipfix_upm_profile(ipfix_profile_id)

Get an existing IPFIX profile

Get an existing IPFIX profile by profile ID.

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
ipfix_profile_id = 'ipfix_profile_id_example' # str | 

try:
    # Get an existing IPFIX profile
    api_response = api_instance.get_ipfix_upm_profile(ipfix_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->get_ipfix_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipfix_profile_id** | **str**|  | 

### Return type

[**IpfixUpmProfile**](IpfixUpmProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_switch_ipfix_config**
> IpfixObsPointConfig get_switch_ipfix_config()

Read global switch IPFIX export configuration

Deprecated - Please use /ipfix-profiles/<ipfix-profile-id> for switch IPFIX profile and /ipfix-collector-profiles/<ipfix-collector-profile-id> for IPFIX collector profile. 

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))

try:
    # Read global switch IPFIX export configuration
    api_response = api_instance.get_switch_ipfix_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->get_switch_ipfix_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IpfixObsPointConfig**](IpfixObsPointConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ipfix_collector_config**
> IpfixCollectorConfigListResult list_ipfix_collector_config(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List IPFIX collector configurations

List IPFIX collector configurations

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List IPFIX collector configurations
    api_response = api_instance.list_ipfix_collector_config(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->list_ipfix_collector_config: %s\n" % e)
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

[**IpfixCollectorConfigListResult**](IpfixCollectorConfigListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ipfix_collector_upm_profiles**
> IpfixCollectorUpmProfileListResult list_ipfix_collector_upm_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, profile_types=profile_types, sort_ascending=sort_ascending, sort_by=sort_by)

List IPFIX Collector Profies

Query IPFIX collector profiles with list parameters. List result can be filtered by profile type defined by IpfixCollectorUpmProfileType. 

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
profile_types = 'profile_types_example' # str | IPFIX Collector Profile Type List (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List IPFIX Collector Profies
    api_response = api_instance.list_ipfix_collector_upm_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, profile_types=profile_types, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->list_ipfix_collector_upm_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **profile_types** | **str**| IPFIX Collector Profile Type List | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IpfixCollectorUpmProfileListResult**](IpfixCollectorUpmProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ipfix_config**
> IpfixConfigListResult list_ipfix_config(applied_to=applied_to, cursor=cursor, included_fields=included_fields, ipfix_config_type=ipfix_config_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List IPFIX configuration

List IPFIX configuration

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
applied_to = 'applied_to_example' # str | Applied To (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
ipfix_config_type = 'ipfix_config_type_example' # str | Supported IPFIX Config Types. (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List IPFIX configuration
    api_response = api_instance.list_ipfix_config(applied_to=applied_to, cursor=cursor, included_fields=included_fields, ipfix_config_type=ipfix_config_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->list_ipfix_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applied_to** | **str**| Applied To | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **ipfix_config_type** | **str**| Supported IPFIX Config Types. | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IpfixConfigListResult**](IpfixConfigListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ipfix_upm_profiles**
> IpfixUpmProfileListResult list_ipfix_upm_profiles(applied_to_entity_id=applied_to_entity_id, applied_to_entity_type=applied_to_entity_type, cursor=cursor, included_fields=included_fields, page_size=page_size, profile_types=profile_types, sort_ascending=sort_ascending, sort_by=sort_by)

List IPFIX Profies

Query IPFIX profiles with list parameters. List result can be filtered by profile type defined by IpfixUpmProfileType. 

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
applied_to_entity_id = 'applied_to_entity_id_example' # str | ID of Entity Applied with Profile (optional)
applied_to_entity_type = 'applied_to_entity_type_example' # str | Supported Entity Types (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
profile_types = 'profile_types_example' # str | IPFIX Profile Type List (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List IPFIX Profies
    api_response = api_instance.list_ipfix_upm_profiles(applied_to_entity_id=applied_to_entity_id, applied_to_entity_type=applied_to_entity_type, cursor=cursor, included_fields=included_fields, page_size=page_size, profile_types=profile_types, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->list_ipfix_upm_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applied_to_entity_id** | **str**| ID of Entity Applied with Profile | [optional] 
 **applied_to_entity_type** | **str**| Supported Entity Types | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **profile_types** | **str**| IPFIX Profile Type List | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IpfixUpmProfileListResult**](IpfixUpmProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ipfix_collector_config**
> IpfixCollectorConfig update_ipfix_collector_config(body, collector_config_id)

Update an existing IPFIX collector configuration

Update an existing IPFIX collector configuration

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixCollectorConfig() # IpfixCollectorConfig | 
collector_config_id = 'collector_config_id_example' # str | 

try:
    # Update an existing IPFIX collector configuration
    api_response = api_instance.update_ipfix_collector_config(body, collector_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->update_ipfix_collector_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixCollectorConfig**](IpfixCollectorConfig.md)|  | 
 **collector_config_id** | **str**|  | 

### Return type

[**IpfixCollectorConfig**](IpfixCollectorConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ipfix_collector_upm_profile**
> IpfixCollectorUpmProfile update_ipfix_collector_upm_profile(body, ipfix_collector_profile_id)

Update an existing IPFIX collector profile

Update an existing IPFIX collector profile with profile ID and modified properties. 

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixCollectorUpmProfile() # IpfixCollectorUpmProfile | 
ipfix_collector_profile_id = 'ipfix_collector_profile_id_example' # str | 

try:
    # Update an existing IPFIX collector profile
    api_response = api_instance.update_ipfix_collector_upm_profile(body, ipfix_collector_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->update_ipfix_collector_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixCollectorUpmProfile**](IpfixCollectorUpmProfile.md)|  | 
 **ipfix_collector_profile_id** | **str**|  | 

### Return type

[**IpfixCollectorUpmProfile**](IpfixCollectorUpmProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ipfix_config**
> IpfixConfig update_ipfix_config(body, config_id)

Update an existing IPFIX configuration

Update an existing IPFIX configuration

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixConfig() # IpfixConfig | 
config_id = 'config_id_example' # str | 

try:
    # Update an existing IPFIX configuration
    api_response = api_instance.update_ipfix_config(body, config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->update_ipfix_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixConfig**](IpfixConfig.md)|  | 
 **config_id** | **str**|  | 

### Return type

[**IpfixConfig**](IpfixConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ipfix_upm_profile**
> IpfixUpmProfile update_ipfix_upm_profile(body, ipfix_profile_id)

Update an existing IPFIX profile

Update an existing IPFIX profile with profile ID and modified properties. 

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixUpmProfile() # IpfixUpmProfile | 
ipfix_profile_id = 'ipfix_profile_id_example' # str | 

try:
    # Update an existing IPFIX profile
    api_response = api_instance.update_ipfix_upm_profile(body, ipfix_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->update_ipfix_upm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixUpmProfile**](IpfixUpmProfile.md)|  | 
 **ipfix_profile_id** | **str**|  | 

### Return type

[**IpfixUpmProfile**](IpfixUpmProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_switch_ipfix_config**
> IpfixObsPointConfig update_switch_ipfix_config(body)

Update global switch IPFIX export configuration

Deprecated - Please use /ipfix-profiles/<ipfix-profile-id> for switch IPFIX profile and /ipfix-collector-profiles/<ipfix-collector-profile-id> for IPFIX collector profile. 

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpfixObsPointConfig() # IpfixObsPointConfig | 

try:
    # Update global switch IPFIX export configuration
    api_response = api_instance.update_switch_ipfix_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringIPFIXApi->update_switch_ipfix_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpfixObsPointConfig**](IpfixObsPointConfig.md)|  | 

### Return type

[**IpfixObsPointConfig**](IpfixObsPointConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

