# swagger_client.SystemAdministrationConfigurationFabricNodesDNSApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_node_name_servers**](SystemAdministrationConfigurationFabricNodesDNSApi.md#read_node_name_servers) | **GET** /node/network/name-servers | Read the Node&#x27;s Name Servers
[**read_node_search_domains**](SystemAdministrationConfigurationFabricNodesDNSApi.md#read_node_search_domains) | **GET** /node/network/search-domains | Read the Node&#x27;s Search Domains
[**update_node_name_servers**](SystemAdministrationConfigurationFabricNodesDNSApi.md#update_node_name_servers) | **PUT** /node/network/name-servers | Update the Node&#x27;s Name Servers
[**update_node_search_domains**](SystemAdministrationConfigurationFabricNodesDNSApi.md#update_node_search_domains) | **PUT** /node/network/search-domains | Update the Node&#x27;s Search Domains

# **read_node_name_servers**
> NodeNameServersProperties read_node_name_servers()

Read the Node's Name Servers

Returns the list of servers that the node uses to look up IP addresses associated with given domain names. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesDNSApi(swagger_client.ApiClient(configuration))

try:
    # Read the Node's Name Servers
    api_response = api_instance.read_node_name_servers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesDNSApi->read_node_name_servers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeNameServersProperties**](NodeNameServersProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_search_domains**
> NodeSearchDomainsProperties read_node_search_domains()

Read the Node's Search Domains

Returns the domain list that the node uses to complete unqualified host names. When a host name does not include a fully qualified domain name (FQDN), the NSX Management node appends the first-listed domain name to the host name before the host name is looked up. The NSX Management node continues this for each entry in the domain list until it finds a match. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesDNSApi(swagger_client.ApiClient(configuration))

try:
    # Read the Node's Search Domains
    api_response = api_instance.read_node_search_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesDNSApi->read_node_search_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSearchDomainsProperties**](NodeSearchDomainsProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_name_servers**
> NodeNameServersProperties update_node_name_servers(body)

Update the Node's Name Servers

Modifies the list of servers that the node uses to look up IP addresses associated with given domain names. If DHCP is configured, this method returns a 409 CONFLICT error, because DHCP manages the list of name servers. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesDNSApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeNameServersProperties() # NodeNameServersProperties | 

try:
    # Update the Node's Name Servers
    api_response = api_instance.update_node_name_servers(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesDNSApi->update_node_name_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeNameServersProperties**](NodeNameServersProperties.md)|  | 

### Return type

[**NodeNameServersProperties**](NodeNameServersProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_search_domains**
> NodeSearchDomainsProperties update_node_search_domains(body)

Update the Node's Search Domains

Modifies the list of domain names that the node uses to complete unqualified host names. If DHCP is configured, this method returns a 409 CONFLICT error, because DHCP manages the list of name servers. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesDNSApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeSearchDomainsProperties() # NodeSearchDomainsProperties | 

try:
    # Update the Node's Search Domains
    api_response = api_instance.update_node_search_domains(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesDNSApi->update_node_search_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeSearchDomainsProperties**](NodeSearchDomainsProperties.md)|  | 

### Return type

[**NodeSearchDomainsProperties**](NodeSearchDomainsProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

