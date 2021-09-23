# swagger_client.SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_failure_domain**](SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi.md#create_failure_domain) | **POST** /failure-domains | Create Failure Domain
[**delete_failure_domain**](SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi.md#delete_failure_domain) | **DELETE** /failure-domains/{failure-domain-id} | Delete Failure Domain
[**get_failure_domain**](SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi.md#get_failure_domain) | **GET** /failure-domains/{failure-domain-id} | Get a Failure Domain
[**list_failure_domains**](SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi.md#list_failure_domains) | **GET** /failure-domains | List Failure Domains
[**update_failure_domain**](SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi.md#update_failure_domain) | **PUT** /failure-domains/{failure-domain-id} | Update Failure Domain

# **create_failure_domain**
> FailureDomain create_failure_domain(body)

Create Failure Domain

Creates a new failure domain. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi(swagger_client.ApiClient(configuration))
body = swagger_client.FailureDomain() # FailureDomain | 

try:
    # Create Failure Domain
    api_response = api_instance.create_failure_domain(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi->create_failure_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FailureDomain**](FailureDomain.md)|  | 

### Return type

[**FailureDomain**](FailureDomain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_failure_domain**
> delete_failure_domain(failure_domain_id)

Delete Failure Domain

Deletes an existing failure domain. You can not delete system generated default failure domain. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi(swagger_client.ApiClient(configuration))
failure_domain_id = 'failure_domain_id_example' # str | 

try:
    # Delete Failure Domain
    api_instance.delete_failure_domain(failure_domain_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi->delete_failure_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **failure_domain_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_failure_domain**
> FailureDomain get_failure_domain(failure_domain_id)

Get a Failure Domain

Returns information about a single failure domain.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi(swagger_client.ApiClient(configuration))
failure_domain_id = 'failure_domain_id_example' # str | 

try:
    # Get a Failure Domain
    api_response = api_instance.get_failure_domain(failure_domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi->get_failure_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **failure_domain_id** | **str**|  | 

### Return type

[**FailureDomain**](FailureDomain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_failure_domains**
> FailureDomainListResult list_failure_domains()

List Failure Domains

Returns information about configured failure domains.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi(swagger_client.ApiClient(configuration))

try:
    # List Failure Domains
    api_response = api_instance.list_failure_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi->list_failure_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FailureDomainListResult**](FailureDomainListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_failure_domain**
> FailureDomain update_failure_domain(body, failure_domain_id)

Update Failure Domain

Updates an existing failure domain. Modifiable parameters are display_name, preferred_active_edge_services flag. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi(swagger_client.ApiClient(configuration))
body = swagger_client.FailureDomain() # FailureDomain | 
failure_domain_id = 'failure_domain_id_example' # str | 

try:
    # Update Failure Domain
    api_response = api_instance.update_failure_domain(body, failure_domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersFailureDomainsApi->update_failure_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FailureDomain**](FailureDomain.md)|  | 
 **failure_domain_id** | **str**|  | 

### Return type

[**FailureDomain**](FailureDomain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

