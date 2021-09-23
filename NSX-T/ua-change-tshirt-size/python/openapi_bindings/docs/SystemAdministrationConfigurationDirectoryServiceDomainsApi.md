# swagger_client.SystemAdministrationConfigurationDirectoryServiceDomainsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_directory_domain**](SystemAdministrationConfigurationDirectoryServiceDomainsApi.md#create_directory_domain) | **POST** /directory/domains | Create a directory domain
[**delete_directory_domain**](SystemAdministrationConfigurationDirectoryServiceDomainsApi.md#delete_directory_domain) | **DELETE** /directory/domains/{domain-id} | Delete a specific domain with given identifier
[**fetch_directory_org_units**](SystemAdministrationConfigurationDirectoryServiceDomainsApi.md#fetch_directory_org_units) | **POST** /directory/org-units | Fetch all organization units for a LDAP server.
[**get_directory_domain**](SystemAdministrationConfigurationDirectoryServiceDomainsApi.md#get_directory_domain) | **GET** /directory/domains/{domain-id} | Get a specific domain with given identifier
[**get_directory_domain_sync_stats**](SystemAdministrationConfigurationDirectoryServiceDomainsApi.md#get_directory_domain_sync_stats) | **GET** /directory/domains/{domain-id}/sync-stats | Get domain sync statistics for the given identifier
[**list_directory_domains**](SystemAdministrationConfigurationDirectoryServiceDomainsApi.md#list_directory_domains) | **GET** /directory/domains | List all configured domains
[**request_directory_domain_sync**](SystemAdministrationConfigurationDirectoryServiceDomainsApi.md#request_directory_domain_sync) | **POST** /directory/domains/{domain-id} | Invoke full sync or delta sync for a specific domain, with additional delay in seconds if needed.  Stop sync will try to stop any pending sync if any to return to idle state.
[**scan_directory_domain_size**](SystemAdministrationConfigurationDirectoryServiceDomainsApi.md#scan_directory_domain_size) | **POST** /directory/domain-size | Scan  the size of a directory domain
[**update_directory_domain**](SystemAdministrationConfigurationDirectoryServiceDomainsApi.md#update_directory_domain) | **PUT** /directory/domains/{domain-id} | Update a directory domain

# **create_directory_domain**
> DirectoryDomain create_directory_domain(body)

Create a directory domain

Create a directory domain

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceDomainsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectoryDomain() # DirectoryDomain | 

try:
    # Create a directory domain
    api_response = api_instance.create_directory_domain(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceDomainsApi->create_directory_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectoryDomain**](DirectoryDomain.md)|  | 

### Return type

[**DirectoryDomain**](DirectoryDomain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_directory_domain**
> delete_directory_domain(domain_id, force=force)

Delete a specific domain with given identifier

Delete a specific domain with given identifier

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceDomainsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete a specific domain with given identifier
    api_instance.delete_directory_domain(domain_id, force=force)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceDomainsApi->delete_directory_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_directory_org_units**
> DirectoryOrgUnitListResults fetch_directory_org_units(body)

Fetch all organization units for a LDAP server.

Fetch all organization units for a LDAP server.

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceDomainsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectoryLdapServer() # DirectoryLdapServer | 

try:
    # Fetch all organization units for a LDAP server.
    api_response = api_instance.fetch_directory_org_units(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceDomainsApi->fetch_directory_org_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectoryLdapServer**](DirectoryLdapServer.md)|  | 

### Return type

[**DirectoryOrgUnitListResults**](DirectoryOrgUnitListResults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_domain**
> DirectoryDomain get_directory_domain(domain_id)

Get a specific domain with given identifier

Get a specific domain with given identifier

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceDomainsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier

try:
    # Get a specific domain with given identifier
    api_response = api_instance.get_directory_domain(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceDomainsApi->get_directory_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 

### Return type

[**DirectoryDomain**](DirectoryDomain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_domain_sync_stats**
> DirectoryDomainSyncStats get_directory_domain_sync_stats(domain_id)

Get domain sync statistics for the given identifier

Get domain sync statistics for the given identifier

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceDomainsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier

try:
    # Get domain sync statistics for the given identifier
    api_response = api_instance.get_directory_domain_sync_stats(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceDomainsApi->get_directory_domain_sync_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 

### Return type

[**DirectoryDomainSyncStats**](DirectoryDomainSyncStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_directory_domains**
> DirectoryDomainListResults list_directory_domains(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List all configured domains

List all configured domains

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceDomainsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List all configured domains
    api_response = api_instance.list_directory_domains(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceDomainsApi->list_directory_domains: %s\n" % e)
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

[**DirectoryDomainListResults**](DirectoryDomainListResults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_directory_domain_sync**
> request_directory_domain_sync(domain_id, action, delay=delay)

Invoke full sync or delta sync for a specific domain, with additional delay in seconds if needed.  Stop sync will try to stop any pending sync if any to return to idle state.

Invoke full sync or delta sync for a specific domain, with additional delay in seconds if needed.  Stop sync will try to stop any pending sync if any to return to idle state.

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceDomainsApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
action = 'action_example' # str | Sync type requested
delay = 0 # int | Request to execute the sync with some delay in seconds (optional) (default to 0)

try:
    # Invoke full sync or delta sync for a specific domain, with additional delay in seconds if needed.  Stop sync will try to stop any pending sync if any to return to idle state.
    api_instance.request_directory_domain_sync(domain_id, action, delay=delay)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceDomainsApi->request_directory_domain_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **action** | **str**| Sync type requested | 
 **delay** | **int**| Request to execute the sync with some delay in seconds | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_directory_domain_size**
> DirectoryDomainSize scan_directory_domain_size(body)

Scan  the size of a directory domain

This call scans the size of a directory domain. It may be very | expensive to run this call in some AD domain deployments. Please | use it with caution.

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceDomainsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectoryDomain() # DirectoryDomain | 

try:
    # Scan  the size of a directory domain
    api_response = api_instance.scan_directory_domain_size(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceDomainsApi->scan_directory_domain_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectoryDomain**](DirectoryDomain.md)|  | 

### Return type

[**DirectoryDomainSize**](DirectoryDomainSize.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_directory_domain**
> DirectoryDomain update_directory_domain(body, domain_id)

Update a directory domain

Update to any field in the directory domain will trigger a full sync

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceDomainsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectoryDomain() # DirectoryDomain | 
domain_id = 'domain_id_example' # str | Directory domain identifier

try:
    # Update a directory domain
    api_response = api_instance.update_directory_domain(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceDomainsApi->update_directory_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectoryDomain**](DirectoryDomain.md)|  | 
 **domain_id** | **str**| Directory domain identifier | 

### Return type

[**DirectoryDomain**](DirectoryDomain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

