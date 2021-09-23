# swagger_client.SystemAdministrationConfigurationDirectoryServiceLDAPServersApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_directory_ldap_server**](SystemAdministrationConfigurationDirectoryServiceLDAPServersApi.md#create_directory_ldap_server) | **POST** /directory/domains/{domain-id}/ldap-servers | Create a LDAP server for directory domain
[**delete_directory_ldap_server**](SystemAdministrationConfigurationDirectoryServiceLDAPServersApi.md#delete_directory_ldap_server) | **DELETE** /directory/domains/{domain-id}/ldap-servers/{server-id} | Delete a LDAP server for directory domain
[**get_directory_ldap_server**](SystemAdministrationConfigurationDirectoryServiceLDAPServersApi.md#get_directory_ldap_server) | **GET** /directory/domains/{domain-id}/ldap-servers/{server-id} | Get a specific LDAP server for a given directory domain
[**list_directory_ldap_servers**](SystemAdministrationConfigurationDirectoryServiceLDAPServersApi.md#list_directory_ldap_servers) | **GET** /directory/domains/{domain-id}/ldap-servers | List all configured domain LDAP servers
[**test_directory_ldap_server**](SystemAdministrationConfigurationDirectoryServiceLDAPServersApi.md#test_directory_ldap_server) | **POST** /directory/domains/{domain-id}/ldap-servers/{server-id} | Test a LDAP server connection for directory domain
[**update_directory_ldap_server**](SystemAdministrationConfigurationDirectoryServiceLDAPServersApi.md#update_directory_ldap_server) | **PUT** /directory/domains/{domain-id}/ldap-servers/{server-id} | Update a LDAP server for directory domain
[**verify_directory_ldap_server**](SystemAdministrationConfigurationDirectoryServiceLDAPServersApi.md#verify_directory_ldap_server) | **POST** /directory/ldap-server | Test a directory domain LDAP server connectivity

# **create_directory_ldap_server**
> DirectoryLdapServer create_directory_ldap_server(body, domain_id)

Create a LDAP server for directory domain

More than one LDAP server can be created and only one LDAP server is used to synchronize directory objects. If more than one LDAP server is configured, NSX will try all the servers until it is able to successfully connect to one.

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceLDAPServersApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectoryLdapServer() # DirectoryLdapServer | 
domain_id = 'domain_id_example' # str | Directory domain identifier

try:
    # Create a LDAP server for directory domain
    api_response = api_instance.create_directory_ldap_server(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceLDAPServersApi->create_directory_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectoryLdapServer**](DirectoryLdapServer.md)|  | 
 **domain_id** | **str**| Directory domain identifier | 

### Return type

[**DirectoryLdapServer**](DirectoryLdapServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_directory_ldap_server**
> delete_directory_ldap_server(domain_id, server_id)

Delete a LDAP server for directory domain

Delete a LDAP server for directory domain

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceLDAPServersApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
server_id = 'server_id_example' # str | LDAP server identifier

try:
    # Delete a LDAP server for directory domain
    api_instance.delete_directory_ldap_server(domain_id, server_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceLDAPServersApi->delete_directory_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **server_id** | **str**| LDAP server identifier | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_ldap_server**
> DirectoryLdapServer get_directory_ldap_server(domain_id, server_id)

Get a specific LDAP server for a given directory domain

Get a specific LDAP server for a given directory domain

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceLDAPServersApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
server_id = 'server_id_example' # str | LDAP server identifier

try:
    # Get a specific LDAP server for a given directory domain
    api_response = api_instance.get_directory_ldap_server(domain_id, server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceLDAPServersApi->get_directory_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **server_id** | **str**| LDAP server identifier | 

### Return type

[**DirectoryLdapServer**](DirectoryLdapServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_directory_ldap_servers**
> DirectoryLdapServerListResults list_directory_ldap_servers(domain_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List all configured domain LDAP servers

List all configured domain LDAP servers

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceLDAPServersApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List all configured domain LDAP servers
    api_response = api_instance.list_directory_ldap_servers(domain_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceLDAPServersApi->list_directory_ldap_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**DirectoryLdapServerListResults**](DirectoryLdapServerListResults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_directory_ldap_server**
> test_directory_ldap_server(domain_id, server_id, action)

Test a LDAP server connection for directory domain

The API tests a LDAP server connection for an already configured domain. If the connection is successful, the response will be HTTP status 200. Otherwise the response will be HTTP status 500 and corresponding error message will be returned.

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceLDAPServersApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | Directory domain identifier
server_id = 'server_id_example' # str | LDAP server identifier
action = 'action_example' # str | LDAP server test requested

try:
    # Test a LDAP server connection for directory domain
    api_instance.test_directory_ldap_server(domain_id, server_id, action)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceLDAPServersApi->test_directory_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Directory domain identifier | 
 **server_id** | **str**| LDAP server identifier | 
 **action** | **str**| LDAP server test requested | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_directory_ldap_server**
> DirectoryLdapServer update_directory_ldap_server(body, domain_id, server_id)

Update a LDAP server for directory domain

Update a LDAP server for directory domain

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceLDAPServersApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectoryLdapServer() # DirectoryLdapServer | 
domain_id = 'domain_id_example' # str | Directory domain identifier
server_id = 'server_id_example' # str | LDAP server identifier

try:
    # Update a LDAP server for directory domain
    api_response = api_instance.update_directory_ldap_server(body, domain_id, server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceLDAPServersApi->update_directory_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectoryLdapServer**](DirectoryLdapServer.md)|  | 
 **domain_id** | **str**| Directory domain identifier | 
 **server_id** | **str**| LDAP server identifier | 

### Return type

[**DirectoryLdapServer**](DirectoryLdapServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_directory_ldap_server**
> DirectoryLdapServerStatus verify_directory_ldap_server(body, action)

Test a directory domain LDAP server connectivity

This API tests a LDAP server connectivity before the actual domain or LDAP server is configured. If the connectivity is good, the response will be HTTP status 200. Otherwise the response will be HTTP status 500 and corresponding error message will be returned.

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
api_instance = swagger_client.SystemAdministrationConfigurationDirectoryServiceLDAPServersApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectoryLdapServer() # DirectoryLdapServer | 
action = 'action_example' # str | LDAP server test requested

try:
    # Test a directory domain LDAP server connectivity
    api_response = api_instance.verify_directory_ldap_server(body, action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationDirectoryServiceLDAPServersApi->verify_directory_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectoryLdapServer**](DirectoryLdapServer.md)|  | 
 **action** | **str**| LDAP server test requested | 

### Return type

[**DirectoryLdapServerStatus**](DirectoryLdapServerStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

