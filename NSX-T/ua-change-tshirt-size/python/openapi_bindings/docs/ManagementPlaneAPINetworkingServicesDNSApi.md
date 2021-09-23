# swagger_client.ManagementPlaneAPINetworkingServicesDNSApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_dns_forwarder_cache_clear_cache**](ManagementPlaneAPINetworkingServicesDNSApi.md#clear_dns_forwarder_cache_clear_cache) | **POST** /dns/forwarders/{forwarder-id}?action&#x3D;clear_cache | Clear the current cache of the DNS forwarder.
[**create_dns_forwader**](ManagementPlaneAPINetworkingServicesDNSApi.md#create_dns_forwader) | **POST** /dns/forwarders | Create a DNS forwader
[**delete_dns_forwarder**](ManagementPlaneAPINetworkingServicesDNSApi.md#delete_dns_forwarder) | **DELETE** /dns/forwarders/{forwarder-id} | Delete a specific DNS forwarder
[**disable_dns_forwarder_disable**](ManagementPlaneAPINetworkingServicesDNSApi.md#disable_dns_forwarder_disable) | **POST** /dns/forwarders/{forwarder-id}?action&#x3D;disable | Disable the DNS forwarder.
[**enable_dns_forwarder_enable**](ManagementPlaneAPINetworkingServicesDNSApi.md#enable_dns_forwarder_enable) | **POST** /dns/forwarders/{forwarder-id}?action&#x3D;enable | Enable the DNS forwarder.
[**get_dns_forwarder_state**](ManagementPlaneAPINetworkingServicesDNSApi.md#get_dns_forwarder_state) | **GET** /dns/forwarders/{forwarder-id}/state | Get the realized state of a DNS forwarder
[**get_dns_forwarder_status**](ManagementPlaneAPINetworkingServicesDNSApi.md#get_dns_forwarder_status) | **GET** /dns/forwarders/{forwarder-id}/status | Get current status of the given DNS forwarder
[**get_failed_dns_queries**](ManagementPlaneAPINetworkingServicesDNSApi.md#get_failed_dns_queries) | **GET** /dns/forwarders/{forwarder-id}/failed-queries | Get the recent failed DNS queries
[**list_dns_forwaders**](ManagementPlaneAPINetworkingServicesDNSApi.md#list_dns_forwaders) | **GET** /dns/forwarders | Get a paginated list of DNS forwarders
[**lookup_address**](ManagementPlaneAPINetworkingServicesDNSApi.md#lookup_address) | **GET** /dns/forwarders/{forwarder-id}/nslookup | Resolve a given address via the DNS forwarder
[**read_dns_forwader**](ManagementPlaneAPINetworkingServicesDNSApi.md#read_dns_forwader) | **GET** /dns/forwarders/{forwarder-id} | Retrieve a DNS forwarder
[**update_dns_forwarder**](ManagementPlaneAPINetworkingServicesDNSApi.md#update_dns_forwarder) | **PUT** /dns/forwarders/{forwarder-id} | Update a specific DNS forwarder

# **clear_dns_forwarder_cache_clear_cache**
> clear_dns_forwarder_cache_clear_cache(forwarder_id)

Clear the current cache of the DNS forwarder.

Clear the current cache of the DNS forwarder. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDNSApi(swagger_client.ApiClient(configuration))
forwarder_id = 'forwarder_id_example' # str | 

try:
    # Clear the current cache of the DNS forwarder.
    api_instance.clear_dns_forwarder_cache_clear_cache(forwarder_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDNSApi->clear_dns_forwarder_cache_clear_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dns_forwader**
> DnsForwarder create_dns_forwader(body)

Create a DNS forwader

Create a DNS forwader upon a logical router. There is only one DNS forwarder can be created upon a given logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDNSApi(swagger_client.ApiClient(configuration))
body = swagger_client.DnsForwarder() # DnsForwarder | 

try:
    # Create a DNS forwader
    api_response = api_instance.create_dns_forwader(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDNSApi->create_dns_forwader: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DnsForwarder**](DnsForwarder.md)|  | 

### Return type

[**DnsForwarder**](DnsForwarder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dns_forwarder**
> delete_dns_forwarder(forwarder_id)

Delete a specific DNS forwarder

Delete a specific DNS forwarder. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDNSApi(swagger_client.ApiClient(configuration))
forwarder_id = 'forwarder_id_example' # str | 

try:
    # Delete a specific DNS forwarder
    api_instance.delete_dns_forwarder(forwarder_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDNSApi->delete_dns_forwarder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_dns_forwarder_disable**
> disable_dns_forwarder_disable(forwarder_id)

Disable the DNS forwarder.

Disable the DNS forwarder if the forwarder is currently enbled. If the DNS forwarder is already disabled, the forwarder will not be re-disabled.  Please note, once a DNS forwarder is disabled then enabled, the previous DNS forwarder statistics counters will be reset. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDNSApi(swagger_client.ApiClient(configuration))
forwarder_id = 'forwarder_id_example' # str | 

try:
    # Disable the DNS forwarder.
    api_instance.disable_dns_forwarder_disable(forwarder_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDNSApi->disable_dns_forwarder_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_dns_forwarder_enable**
> enable_dns_forwarder_enable(forwarder_id)

Enable the DNS forwarder.

Enable the DNS forwarder if the forwarder is currently disabled. If the DNS forwarder is already enabled, the forwarder will not be re-enabled.  Please note, once a DNS forwarder is disabled then enabled, the previous DNS forwarder statistics counters will be reset. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDNSApi(swagger_client.ApiClient(configuration))
forwarder_id = 'forwarder_id_example' # str | 

try:
    # Enable the DNS forwarder.
    api_instance.enable_dns_forwarder_enable(forwarder_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDNSApi->enable_dns_forwarder_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_forwarder_state**
> ConfigurationState get_dns_forwarder_state(forwarder_id, barrier_id=barrier_id, request_id=request_id)

Get the realized state of a DNS forwarder

Return the realized state information of a DNS forwarder. After a DNS forwarder was created or updated, you can invoke this API to check the realization state of the forwarder. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDNSApi(swagger_client.ApiClient(configuration))
forwarder_id = 'forwarder_id_example' # str | 
barrier_id = 789 # int |  (optional)
request_id = 'request_id_example' # str | Realization request ID (optional)

try:
    # Get the realized state of a DNS forwarder
    api_response = api_instance.get_dns_forwarder_state(forwarder_id, barrier_id=barrier_id, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDNSApi->get_dns_forwarder_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**|  | 
 **barrier_id** | **int**|  | [optional] 
 **request_id** | **str**| Realization request ID | [optional] 

### Return type

[**ConfigurationState**](ConfigurationState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_forwarder_status**
> DnsForwarderStatus get_dns_forwarder_status(forwarder_id)

Get current status of the given DNS forwarder

Returns the current status of the given DNS forwarder. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDNSApi(swagger_client.ApiClient(configuration))
forwarder_id = 'forwarder_id_example' # str | 

try:
    # Get current status of the given DNS forwarder
    api_response = api_instance.get_dns_forwarder_status(forwarder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDNSApi->get_dns_forwarder_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**|  | 

### Return type

[**DnsForwarderStatus**](DnsForwarderStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_failed_dns_queries**
> DnsFailedQueries get_failed_dns_queries(forwarder_id, count=count)

Get the recent failed DNS queries

Return the given count of recent failed DNS queries from DNS forwarder. Since the DNS forwarder is running in Acitve/Standby HA mode on transport nodes, the given count of queries will be returned from each nodes. Hence the total queries returned could be doubled. If no count is specified, 100 recent failed queries are returned. If the recent failures is less than the given count, all the failures will be returned. The maximum count is 1,000. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDNSApi(swagger_client.ApiClient(configuration))
forwarder_id = 'forwarder_id_example' # str | 
count = 100 # int | The count of the failed DNS queries (optional) (default to 100)

try:
    # Get the recent failed DNS queries
    api_response = api_instance.get_failed_dns_queries(forwarder_id, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDNSApi->get_failed_dns_queries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**|  | 
 **count** | **int**| The count of the failed DNS queries | [optional] [default to 100]

### Return type

[**DnsFailedQueries**](DnsFailedQueries.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dns_forwaders**
> DnsForwarderListResult list_dns_forwaders(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get a paginated list of DNS forwarders

Get a paginated list of DNS forwarders. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDNSApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get a paginated list of DNS forwarders
    api_response = api_instance.list_dns_forwaders(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDNSApi->list_dns_forwaders: %s\n" % e)
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

[**DnsForwarderListResult**](DnsForwarderListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_address**
> DnsAnswer lookup_address(forwarder_id, address=address, server_ip=server_ip, source_ip=source_ip)

Resolve a given address via the DNS forwarder

Query the nameserver for an ip-address or a FQDN of the given an address optionally using an specified DNS server. If the address is a fqdn, nslookup will resolve ip-address with it. If the address is an ip-address, do a reverse lookup and answer fqdn(s). 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDNSApi(swagger_client.ApiClient(configuration))
forwarder_id = 'forwarder_id_example' # str | 
address = 'address_example' # str | IP address or FQDN for nslookup (optional)
server_ip = 'server_ip_example' # str | IPv4 address (optional)
source_ip = 'source_ip_example' # str | IPv4 address (optional)

try:
    # Resolve a given address via the DNS forwarder
    api_response = api_instance.lookup_address(forwarder_id, address=address, server_ip=server_ip, source_ip=source_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDNSApi->lookup_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**|  | 
 **address** | **str**| IP address or FQDN for nslookup | [optional] 
 **server_ip** | **str**| IPv4 address | [optional] 
 **source_ip** | **str**| IPv4 address | [optional] 

### Return type

[**DnsAnswer**](DnsAnswer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_dns_forwader**
> DnsForwarder read_dns_forwader(forwarder_id)

Retrieve a DNS forwarder

Retrieve a DNS forwarder. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDNSApi(swagger_client.ApiClient(configuration))
forwarder_id = 'forwarder_id_example' # str | 

try:
    # Retrieve a DNS forwarder
    api_response = api_instance.read_dns_forwader(forwarder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDNSApi->read_dns_forwader: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**|  | 

### Return type

[**DnsForwarder**](DnsForwarder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dns_forwarder**
> DnsForwarder update_dns_forwarder(body, forwarder_id)

Update a specific DNS forwarder

Update a specific DNS forwarder. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDNSApi(swagger_client.ApiClient(configuration))
body = swagger_client.DnsForwarder() # DnsForwarder | 
forwarder_id = 'forwarder_id_example' # str | 

try:
    # Update a specific DNS forwarder
    api_response = api_instance.update_dns_forwarder(body, forwarder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDNSApi->update_dns_forwarder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DnsForwarder**](DnsForwarder.md)|  | 
 **forwarder_id** | **str**|  | 

### Return type

[**DnsForwarder**](DnsForwarder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

