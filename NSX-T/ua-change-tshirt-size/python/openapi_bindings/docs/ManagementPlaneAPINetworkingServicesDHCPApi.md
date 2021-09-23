# swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dhcp_ip_pool**](ManagementPlaneAPINetworkingServicesDHCPApi.md#create_dhcp_ip_pool) | **POST** /dhcp/servers/{server-id}/ip-pools | Create an ip pool for a DHCP server
[**create_dhcp_profile**](ManagementPlaneAPINetworkingServicesDHCPApi.md#create_dhcp_profile) | **POST** /dhcp/server-profiles | Create a DHCP server profile
[**create_dhcp_server**](ManagementPlaneAPINetworkingServicesDHCPApi.md#create_dhcp_server) | **POST** /dhcp/servers | Create a DHCP server
[**create_dhcp_static_binding**](ManagementPlaneAPINetworkingServicesDHCPApi.md#create_dhcp_static_binding) | **POST** /dhcp/servers/{server-id}/static-bindings | Create a static binding for a DHCP server
[**create_dhcp_v6_ip_pool**](ManagementPlaneAPINetworkingServicesDHCPApi.md#create_dhcp_v6_ip_pool) | **POST** /dhcp/servers/{server-id}/ipv6-ip-pools | Create an ip pool for a DHCP IPv6 server
[**create_dhcp_v6_static_binding**](ManagementPlaneAPINetworkingServicesDHCPApi.md#create_dhcp_v6_static_binding) | **POST** /dhcp/servers/{server-id}/ipv6-static-bindings | Create a static binding for a DHCP IPv6 server
[**delete_a_dhcp_lease**](ManagementPlaneAPINetworkingServicesDHCPApi.md#delete_a_dhcp_lease) | **DELETE** /dhcp/servers/{server-id}/leases | Delete a single DHCP lease entry specified by ip and mac.
[**delete_dhcp_ip_pool**](ManagementPlaneAPINetworkingServicesDHCPApi.md#delete_dhcp_ip_pool) | **DELETE** /dhcp/servers/{server-id}/ip-pools/{pool-id} | Delete a DHCP server&#x27;s IP pool
[**delete_dhcp_profile**](ManagementPlaneAPINetworkingServicesDHCPApi.md#delete_dhcp_profile) | **DELETE** /dhcp/server-profiles/{profile-id} | Delete a DHCP server profile
[**delete_dhcp_server**](ManagementPlaneAPINetworkingServicesDHCPApi.md#delete_dhcp_server) | **DELETE** /dhcp/servers/{server-id} | Delete a DHCP server
[**delete_dhcp_static_binding**](ManagementPlaneAPINetworkingServicesDHCPApi.md#delete_dhcp_static_binding) | **DELETE** /dhcp/servers/{server-id}/static-bindings/{binding-id} | Delete a static binding
[**delete_dhcp_v6_ip_pool**](ManagementPlaneAPINetworkingServicesDHCPApi.md#delete_dhcp_v6_ip_pool) | **DELETE** /dhcp/servers/{server-id}/ipv6-ip-pools/{pool-id} | Delete a DHCP IPv6 server&#x27;s IP pool
[**delete_dhcp_v6_static_binding**](ManagementPlaneAPINetworkingServicesDHCPApi.md#delete_dhcp_v6_static_binding) | **DELETE** /dhcp/servers/{server-id}/ipv6-static-bindings/{binding-id} | Delete a static binding for DHCP IPv6 server
[**get_dhcp_ip_pool_state**](ManagementPlaneAPINetworkingServicesDHCPApi.md#get_dhcp_ip_pool_state) | **GET** /dhcp/servers/{server-id}/ip-pools/{pool-id}/state | Get the realized state of a dhcp ip pool
[**get_dhcp_server_state**](ManagementPlaneAPINetworkingServicesDHCPApi.md#get_dhcp_server_state) | **GET** /dhcp/servers/{server-id}/state | Get the realized state of a dhcp server
[**get_dhcp_static_binding_state**](ManagementPlaneAPINetworkingServicesDHCPApi.md#get_dhcp_static_binding_state) | **GET** /dhcp/servers/{server-id}/static-bindings/{binding-id}/state | Get the realized state of a dhcp static binding
[**get_dhcp_status**](ManagementPlaneAPINetworkingServicesDHCPApi.md#get_dhcp_status) | **GET** /dhcp/servers/{server-id}/status | Get DHCP service status with given dhcp server id
[**list_dhcp_ip_pools**](ManagementPlaneAPINetworkingServicesDHCPApi.md#list_dhcp_ip_pools) | **GET** /dhcp/servers/{server-id}/ip-pools | Get a paginated list of a DHCP server&#x27;s IP pools
[**list_dhcp_profiles**](ManagementPlaneAPINetworkingServicesDHCPApi.md#list_dhcp_profiles) | **GET** /dhcp/server-profiles | Get a paginated list of DHCP server profiles
[**list_dhcp_servers**](ManagementPlaneAPINetworkingServicesDHCPApi.md#list_dhcp_servers) | **GET** /dhcp/servers | Get a paginated list of DHCP servers
[**list_dhcp_static_bindings**](ManagementPlaneAPINetworkingServicesDHCPApi.md#list_dhcp_static_bindings) | **GET** /dhcp/servers/{server-id}/static-bindings | Get a paginated list of a DHCP server&#x27;s static bindings
[**list_dhcp_v6_ip_pools**](ManagementPlaneAPINetworkingServicesDHCPApi.md#list_dhcp_v6_ip_pools) | **GET** /dhcp/servers/{server-id}/ipv6-ip-pools | Get a paginated list of a DHCP IPv6 server&#x27;s IP pools
[**list_dhcp_v6_static_bindings**](ManagementPlaneAPINetworkingServicesDHCPApi.md#list_dhcp_v6_static_bindings) | **GET** /dhcp/servers/{server-id}/ipv6-static-bindings | Get a paginated list of a DHCP IPv6 server&#x27;s static bindings
[**read_dhcp_ip_pool**](ManagementPlaneAPINetworkingServicesDHCPApi.md#read_dhcp_ip_pool) | **GET** /dhcp/servers/{server-id}/ip-pools/{pool-id} | Get a DHCP server&#x27;s IP pool with the specified pool ID
[**read_dhcp_profile**](ManagementPlaneAPINetworkingServicesDHCPApi.md#read_dhcp_profile) | **GET** /dhcp/server-profiles/{profile-id} | Get a DHCP server profile
[**read_dhcp_server**](ManagementPlaneAPINetworkingServicesDHCPApi.md#read_dhcp_server) | **GET** /dhcp/servers/{server-id} | Get a DHCP server with v4 and/or v6 servers
[**read_dhcp_static_binding**](ManagementPlaneAPINetworkingServicesDHCPApi.md#read_dhcp_static_binding) | **GET** /dhcp/servers/{server-id}/static-bindings/{binding-id} | Get a DHCP server&#x27;s static binding with the specified binding ID
[**read_dhcp_v6_ip_pool**](ManagementPlaneAPINetworkingServicesDHCPApi.md#read_dhcp_v6_ip_pool) | **GET** /dhcp/servers/{server-id}/ipv6-ip-pools/{pool-id} | Get a DHCP IPv6 server&#x27;s IP pool with the specified pool ID
[**read_dhcp_v6_static_binding**](ManagementPlaneAPINetworkingServicesDHCPApi.md#read_dhcp_v6_static_binding) | **GET** /dhcp/servers/{server-id}/ipv6-static-bindings/{binding-id} | Get a DHCP IPv6 server&#x27;s static binding with the specified binding ID
[**reallocate_dhcp_profile_edge_cluster_reallocate**](ManagementPlaneAPINetworkingServicesDHCPApi.md#reallocate_dhcp_profile_edge_cluster_reallocate) | **POST** /dhcp/server-profiles/{server-profile-id}?action&#x3D;reallocate | Reallocate edge cluster and members of given DHCP profile.
[**update_dhcp_ip_pool**](ManagementPlaneAPINetworkingServicesDHCPApi.md#update_dhcp_ip_pool) | **PUT** /dhcp/servers/{server-id}/ip-pools/{pool-id} | Update a DHCP server&#x27;s IP pool
[**update_dhcp_profile**](ManagementPlaneAPINetworkingServicesDHCPApi.md#update_dhcp_profile) | **PUT** /dhcp/server-profiles/{profile-id} | Update a DHCP server profile
[**update_dhcp_server**](ManagementPlaneAPINetworkingServicesDHCPApi.md#update_dhcp_server) | **PUT** /dhcp/servers/{server-id} | Update a DHCP server with v4 and/or v6 servers
[**update_dhcp_static_binding**](ManagementPlaneAPINetworkingServicesDHCPApi.md#update_dhcp_static_binding) | **PUT** /dhcp/servers/{server-id}/static-bindings/{binding-id} | Update a DHCP server&#x27;s static binding
[**update_dhcp_v6_ip_pool**](ManagementPlaneAPINetworkingServicesDHCPApi.md#update_dhcp_v6_ip_pool) | **PUT** /dhcp/servers/{server-id}/ipv6-ip-pools/{pool-id} | Update a DHCP IPv6 server&#x27;s IP pool
[**update_dhcp_v6_static_binding**](ManagementPlaneAPINetworkingServicesDHCPApi.md#update_dhcp_v6_static_binding) | **PUT** /dhcp/servers/{server-id}/ipv6-static-bindings/{binding-id} | Update a DHCP IPv6 server&#x27;s static binding

# **create_dhcp_ip_pool**
> DhcpIpPool create_dhcp_ip_pool(body, server_id)

Create an ip pool for a DHCP server

Create an ip pool for a local DHCP server

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpIpPool() # DhcpIpPool | 
server_id = 'server_id_example' # str | 

try:
    # Create an ip pool for a DHCP server
    api_response = api_instance.create_dhcp_ip_pool(body, server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->create_dhcp_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpIpPool**](DhcpIpPool.md)|  | 
 **server_id** | **str**|  | 

### Return type

[**DhcpIpPool**](DhcpIpPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dhcp_profile**
> DhcpProfile create_dhcp_profile(body)

Create a DHCP server profile

Create a DHCP server profile. If no edge member is specified, edge members to run the dhcp servers will be auto-allocated from the edge cluster. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpProfile() # DhcpProfile | 

try:
    # Create a DHCP server profile
    api_response = api_instance.create_dhcp_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->create_dhcp_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpProfile**](DhcpProfile.md)|  | 

### Return type

[**DhcpProfile**](DhcpProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dhcp_server**
> LogicalDhcpServer create_dhcp_server(body)

Create a DHCP server

Create a logical DHCP server with v4 and/or v6 servers. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.LogicalDhcpServer() # LogicalDhcpServer | 

try:
    # Create a DHCP server
    api_response = api_instance.create_dhcp_server(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->create_dhcp_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogicalDhcpServer**](LogicalDhcpServer.md)|  | 

### Return type

[**LogicalDhcpServer**](LogicalDhcpServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dhcp_static_binding**
> DhcpStaticBinding create_dhcp_static_binding(body, server_id)

Create a static binding for a DHCP server

Create a static binding for a logical DHCP server.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpStaticBinding() # DhcpStaticBinding | 
server_id = 'server_id_example' # str | 

try:
    # Create a static binding for a DHCP server
    api_response = api_instance.create_dhcp_static_binding(body, server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->create_dhcp_static_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpStaticBinding**](DhcpStaticBinding.md)|  | 
 **server_id** | **str**|  | 

### Return type

[**DhcpStaticBinding**](DhcpStaticBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dhcp_v6_ip_pool**
> DhcpV6IpPool create_dhcp_v6_ip_pool(body, server_id)

Create an ip pool for a DHCP IPv6 server

Create an ip pool for a local DHCP IPv6 server

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpV6IpPool() # DhcpV6IpPool | 
server_id = 'server_id_example' # str | 

try:
    # Create an ip pool for a DHCP IPv6 server
    api_response = api_instance.create_dhcp_v6_ip_pool(body, server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->create_dhcp_v6_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpV6IpPool**](DhcpV6IpPool.md)|  | 
 **server_id** | **str**|  | 

### Return type

[**DhcpV6IpPool**](DhcpV6IpPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dhcp_v6_static_binding**
> DhcpV6StaticBinding create_dhcp_v6_static_binding(body, server_id)

Create a static binding for a DHCP IPv6 server

Create a static binding for a logical DHCP IPv6 server.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpV6StaticBinding() # DhcpV6StaticBinding | 
server_id = 'server_id_example' # str | 

try:
    # Create a static binding for a DHCP IPv6 server
    api_response = api_instance.create_dhcp_v6_static_binding(body, server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->create_dhcp_v6_static_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpV6StaticBinding**](DhcpV6StaticBinding.md)|  | 
 **server_id** | **str**|  | 

### Return type

[**DhcpV6StaticBinding**](DhcpV6StaticBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_dhcp_lease**
> delete_a_dhcp_lease(server_id, ip, mac)

Delete a single DHCP lease entry specified by ip and mac.

Delete a single DHCP lease entry specified by ip and mac.  The DHCP server matches the DHCP lease with the given ip address and the mac address. The matched lease entry will be deleted. If no lease matches, the request is ignored.  The DHCP lease to be deleted will be removed by the system from both active and standby node. The system will report error if the DHCP lease could not be removed from both nodes. If the DHCP lease could not be removed on either node, please check the DHCP server status. Once the DHCP server status is UP, please invoke the deletion API again to ensure the lease gets deleted from both nodes. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
ip = 'ip_example' # str | IPv4 or IPv6 address
mac = 'mac_example' # str | MAC Address

try:
    # Delete a single DHCP lease entry specified by ip and mac.
    api_instance.delete_a_dhcp_lease(server_id, ip, mac)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->delete_a_dhcp_lease: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **ip** | **str**| IPv4 or IPv6 address | 
 **mac** | **str**| MAC Address | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dhcp_ip_pool**
> delete_dhcp_ip_pool(server_id, pool_id)

Delete a DHCP server's IP pool

Delete a specific ip pool of a given logical DHCP server.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
pool_id = 'pool_id_example' # str | 

try:
    # Delete a DHCP server's IP pool
    api_instance.delete_dhcp_ip_pool(server_id, pool_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->delete_dhcp_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **pool_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dhcp_profile**
> delete_dhcp_profile(profile_id)

Delete a DHCP server profile

Delete a DHCP server profile specified by the profile id.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
profile_id = 'profile_id_example' # str | 

try:
    # Delete a DHCP server profile
    api_instance.delete_dhcp_profile(profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->delete_dhcp_profile: %s\n" % e)
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

# **delete_dhcp_server**
> delete_dhcp_server(server_id)

Delete a DHCP server

Delete a logical DHCP server specified by server id.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 

try:
    # Delete a DHCP server
    api_instance.delete_dhcp_server(server_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->delete_dhcp_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dhcp_static_binding**
> delete_dhcp_static_binding(server_id, binding_id)

Delete a static binding

Delete a specific static binding of a given logical DHCP server.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
binding_id = 'binding_id_example' # str | 

try:
    # Delete a static binding
    api_instance.delete_dhcp_static_binding(server_id, binding_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->delete_dhcp_static_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **binding_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dhcp_v6_ip_pool**
> delete_dhcp_v6_ip_pool(server_id, pool_id)

Delete a DHCP IPv6 server's IP pool

Delete a specific ip pool of a given logical DHCP IPv6 server.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
pool_id = 'pool_id_example' # str | 

try:
    # Delete a DHCP IPv6 server's IP pool
    api_instance.delete_dhcp_v6_ip_pool(server_id, pool_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->delete_dhcp_v6_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **pool_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dhcp_v6_static_binding**
> delete_dhcp_v6_static_binding(server_id, binding_id)

Delete a static binding for DHCP IPv6 server

Delete a specific static binding of a given logical DHCP IPv6 server.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
binding_id = 'binding_id_example' # str | 

try:
    # Delete a static binding for DHCP IPv6 server
    api_instance.delete_dhcp_v6_static_binding(server_id, binding_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->delete_dhcp_v6_static_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **binding_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dhcp_ip_pool_state**
> ConfigurationState get_dhcp_ip_pool_state(server_id, pool_id, barrier_id=barrier_id, request_id=request_id)

Get the realized state of a dhcp ip pool

Return realized state information of a dhcp ip pool. After a dhcp ip pool is created or updated, you can invoke this API to get the realization information of the ip pool. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
pool_id = 'pool_id_example' # str | 
barrier_id = 789 # int |  (optional)
request_id = 'request_id_example' # str | Realization request ID (optional)

try:
    # Get the realized state of a dhcp ip pool
    api_response = api_instance.get_dhcp_ip_pool_state(server_id, pool_id, barrier_id=barrier_id, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->get_dhcp_ip_pool_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **pool_id** | **str**|  | 
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

# **get_dhcp_server_state**
> ConfigurationState get_dhcp_server_state(server_id, barrier_id=barrier_id, request_id=request_id)

Get the realized state of a dhcp server

Return realized state information of a dhcp server. After a dhcp server is created or updated, you can invoke this API to get the realization information of the server. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
barrier_id = 789 # int |  (optional)
request_id = 'request_id_example' # str | Realization request ID (optional)

try:
    # Get the realized state of a dhcp server
    api_response = api_instance.get_dhcp_server_state(server_id, barrier_id=barrier_id, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->get_dhcp_server_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
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

# **get_dhcp_static_binding_state**
> ConfigurationState get_dhcp_static_binding_state(server_id, binding_id, barrier_id=barrier_id, request_id=request_id)

Get the realized state of a dhcp static binding

Return realized state information of a dhcp static binding. After a dhcp static binding is created or updated, you can invoke this API to get the realization information of the static binding. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
binding_id = 'binding_id_example' # str | 
barrier_id = 789 # int |  (optional)
request_id = 'request_id_example' # str | Realization request ID (optional)

try:
    # Get the realized state of a dhcp static binding
    api_response = api_instance.get_dhcp_static_binding_state(server_id, binding_id, barrier_id=barrier_id, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->get_dhcp_static_binding_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **binding_id** | **str**|  | 
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

# **get_dhcp_status**
> DhcpServerStatus get_dhcp_status(server_id)

Get DHCP service status with given dhcp server id

Returns the service status of the given dhcp server. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 

try:
    # Get DHCP service status with given dhcp server id
    api_response = api_instance.get_dhcp_status(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->get_dhcp_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 

### Return type

[**DhcpServerStatus**](DhcpServerStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dhcp_ip_pools**
> DhcpIpPoolListResult list_dhcp_ip_pools(server_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get a paginated list of a DHCP server's IP pools

List the ip pools of a logical DHCP server with pagination support. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get a paginated list of a DHCP server's IP pools
    api_response = api_instance.list_dhcp_ip_pools(server_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->list_dhcp_ip_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**DhcpIpPoolListResult**](DhcpIpPoolListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dhcp_profiles**
> DhcpProfileListResult list_dhcp_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get a paginated list of DHCP server profiles

Get a paginated list of DHCP server profiles.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get a paginated list of DHCP server profiles
    api_response = api_instance.list_dhcp_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->list_dhcp_profiles: %s\n" % e)
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

[**DhcpProfileListResult**](DhcpProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dhcp_servers**
> LogicalDhcpServerListResult list_dhcp_servers(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get a paginated list of DHCP servers

List logical DHCP servers with pagination support.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get a paginated list of DHCP servers
    api_response = api_instance.list_dhcp_servers(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->list_dhcp_servers: %s\n" % e)
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

[**LogicalDhcpServerListResult**](LogicalDhcpServerListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dhcp_static_bindings**
> DhcpStaticBindingListResult list_dhcp_static_bindings(server_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get a paginated list of a DHCP server's static bindings

Return a paginated list of a static bindings of a given logical DHCP server. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get a paginated list of a DHCP server's static bindings
    api_response = api_instance.list_dhcp_static_bindings(server_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->list_dhcp_static_bindings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**DhcpStaticBindingListResult**](DhcpStaticBindingListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dhcp_v6_ip_pools**
> DhcpV6IpPoolListResult list_dhcp_v6_ip_pools(server_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get a paginated list of a DHCP IPv6 server's IP pools

List the ip pools of a logical DHCP IPv6 server with pagination support. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get a paginated list of a DHCP IPv6 server's IP pools
    api_response = api_instance.list_dhcp_v6_ip_pools(server_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->list_dhcp_v6_ip_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**DhcpV6IpPoolListResult**](DhcpV6IpPoolListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dhcp_v6_static_bindings**
> DhcpV6StaticBindingListResult list_dhcp_v6_static_bindings(server_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get a paginated list of a DHCP IPv6 server's static bindings

Return a paginated list of a static bindings of a given logical DHCP IPv6 server. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get a paginated list of a DHCP IPv6 server's static bindings
    api_response = api_instance.list_dhcp_v6_static_bindings(server_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->list_dhcp_v6_static_bindings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**DhcpV6StaticBindingListResult**](DhcpV6StaticBindingListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_dhcp_ip_pool**
> DhcpIpPool read_dhcp_ip_pool(server_id, pool_id)

Get a DHCP server's IP pool with the specified pool ID

Return a specific ip pool of a given logical DHCP server.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
pool_id = 'pool_id_example' # str | 

try:
    # Get a DHCP server's IP pool with the specified pool ID
    api_response = api_instance.read_dhcp_ip_pool(server_id, pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->read_dhcp_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **pool_id** | **str**|  | 

### Return type

[**DhcpIpPool**](DhcpIpPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_dhcp_profile**
> DhcpProfile read_dhcp_profile(profile_id)

Get a DHCP server profile

Return the DHCP profile specified by the profile id.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
profile_id = 'profile_id_example' # str | 

try:
    # Get a DHCP server profile
    api_response = api_instance.read_dhcp_profile(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->read_dhcp_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

[**DhcpProfile**](DhcpProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_dhcp_server**
> LogicalDhcpServer read_dhcp_server(server_id)

Get a DHCP server with v4 and/or v6 servers

Retrieve a logical DHCP server specified by server id.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 

try:
    # Get a DHCP server with v4 and/or v6 servers
    api_response = api_instance.read_dhcp_server(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->read_dhcp_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 

### Return type

[**LogicalDhcpServer**](LogicalDhcpServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_dhcp_static_binding**
> DhcpStaticBinding read_dhcp_static_binding(server_id, binding_id)

Get a DHCP server's static binding with the specified binding ID

Return a specific static binding of a given logical DHCP server. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
binding_id = 'binding_id_example' # str | 

try:
    # Get a DHCP server's static binding with the specified binding ID
    api_response = api_instance.read_dhcp_static_binding(server_id, binding_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->read_dhcp_static_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **binding_id** | **str**|  | 

### Return type

[**DhcpStaticBinding**](DhcpStaticBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_dhcp_v6_ip_pool**
> DhcpV6IpPool read_dhcp_v6_ip_pool(server_id, pool_id)

Get a DHCP IPv6 server's IP pool with the specified pool ID

Return a specific ip pool of a given logical DHCP IPv6 server.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
pool_id = 'pool_id_example' # str | 

try:
    # Get a DHCP IPv6 server's IP pool with the specified pool ID
    api_response = api_instance.read_dhcp_v6_ip_pool(server_id, pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->read_dhcp_v6_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **pool_id** | **str**|  | 

### Return type

[**DhcpV6IpPool**](DhcpV6IpPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_dhcp_v6_static_binding**
> DhcpV6StaticBinding read_dhcp_v6_static_binding(server_id, binding_id)

Get a DHCP IPv6 server's static binding with the specified binding ID

Return a specific static binding of a given logical DHCP IPv6 server. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
server_id = 'server_id_example' # str | 
binding_id = 'binding_id_example' # str | 

try:
    # Get a DHCP IPv6 server's static binding with the specified binding ID
    api_response = api_instance.read_dhcp_v6_static_binding(server_id, binding_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->read_dhcp_v6_static_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **binding_id** | **str**|  | 

### Return type

[**DhcpV6StaticBinding**](DhcpV6StaticBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reallocate_dhcp_profile_edge_cluster_reallocate**
> DhcpProfile reallocate_dhcp_profile_edge_cluster_reallocate(body, server_profile_id)

Reallocate edge cluster and members of given DHCP profile.

As changing edge-cluster-id of a DhcpProfile by a PUT is disallowed, this re-allocate API is used to modify the edge-cluster-id and members of a given DhcpProfile.  Only the edge-cluster-id and the edge-cluster-member-indexes fields will be picked up by this re-allication API. The othere fields in the payload will be ignored.  If the edge-cluster-id in the payload DhcpProfile is different from the current edge-cluster-id of the profile, the referencing DHCP server(s) will be re-allocated to the new edge cluster. If the edge-cluster-id is not changed, the referencing DHCP server(s) will be re-allocated to the given edge members in the edge cluster. In this case, this REST API will act same as that of updating a DhcpProfile.  If the edge cluster member indexes are provided, they should exist in the given edge cluster. If the indexes are not specified in the DhcpProfile, edge members will be auto-allocated from the given edge cluster.  Please note that re-allocating edge-cluster will cause lose of all exisitng DHCP lease information. This API is used only when loosing DHCP leases is not a real problem, e.g. cross-site migration or failover and all client hosts will be reboot and get new IP addresses. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpProfile() # DhcpProfile | 
server_profile_id = 'server_profile_id_example' # str | 

try:
    # Reallocate edge cluster and members of given DHCP profile.
    api_response = api_instance.reallocate_dhcp_profile_edge_cluster_reallocate(body, server_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->reallocate_dhcp_profile_edge_cluster_reallocate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpProfile**](DhcpProfile.md)|  | 
 **server_profile_id** | **str**|  | 

### Return type

[**DhcpProfile**](DhcpProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dhcp_ip_pool**
> DhcpIpPool update_dhcp_ip_pool(body, server_id, pool_id)

Update a DHCP server's IP pool

Update a specific ip pool of a given logical DHCP server.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpIpPool() # DhcpIpPool | 
server_id = 'server_id_example' # str | 
pool_id = 'pool_id_example' # str | 

try:
    # Update a DHCP server's IP pool
    api_response = api_instance.update_dhcp_ip_pool(body, server_id, pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->update_dhcp_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpIpPool**](DhcpIpPool.md)|  | 
 **server_id** | **str**|  | 
 **pool_id** | **str**|  | 

### Return type

[**DhcpIpPool**](DhcpIpPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dhcp_profile**
> DhcpProfile update_dhcp_profile(body, profile_id)

Update a DHCP server profile

If both the edge_cluster_member_indexes in the DhcpProfile are changed in a same PUT API, e.g. change from [a,b] to [x,y], the current DHCP server leases will be lost, which could cause the network crash due to ip conflicts. Hence the suggestion is to change only one member index in one single update, e.g. from [a, b] to [a,y].  Please note, the edge_cluster_id in DhcpProfile can NOT be changed by this PUT operation because all existing DHCP leases will lost. If losing leases is not a problem, a dedicated re-allocation API is suggested to modify the edge-cluster-id, i.e. \"POST /api/v1/dhcp/dhcp-profiles/<profileId>?action=reallocate\".  Meanwhile, if the edge_cluster_member_indexes was specified currently but now is changed to none (not specified) via a PUT operation, the edge nodes will not be auto-selected from edge cluster. Instead, the previously-allocated edge nodes will continue to be used by the DHCP server. This is because changing both edge nodes of a DHCP server will lose all existing leases. In case re-allocation is required and leases lost is not a problem (or can be recovered), please invoke the reallocate API mentioned above with new DhcpProfile to accomplish the intent. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpProfile() # DhcpProfile | 
profile_id = 'profile_id_example' # str | 

try:
    # Update a DHCP server profile
    api_response = api_instance.update_dhcp_profile(body, profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->update_dhcp_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpProfile**](DhcpProfile.md)|  | 
 **profile_id** | **str**|  | 

### Return type

[**DhcpProfile**](DhcpProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dhcp_server**
> LogicalDhcpServer update_dhcp_server(body, server_id)

Update a DHCP server with v4 and/or v6 servers

Update a logical DHCP server with new configurations.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.LogicalDhcpServer() # LogicalDhcpServer | 
server_id = 'server_id_example' # str | 

try:
    # Update a DHCP server with v4 and/or v6 servers
    api_response = api_instance.update_dhcp_server(body, server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->update_dhcp_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogicalDhcpServer**](LogicalDhcpServer.md)|  | 
 **server_id** | **str**|  | 

### Return type

[**LogicalDhcpServer**](LogicalDhcpServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dhcp_static_binding**
> DhcpStaticBinding update_dhcp_static_binding(body, server_id, binding_id)

Update a DHCP server's static binding

Update a specific static binding of a given local DHCP server.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpStaticBinding() # DhcpStaticBinding | 
server_id = 'server_id_example' # str | 
binding_id = 'binding_id_example' # str | 

try:
    # Update a DHCP server's static binding
    api_response = api_instance.update_dhcp_static_binding(body, server_id, binding_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->update_dhcp_static_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpStaticBinding**](DhcpStaticBinding.md)|  | 
 **server_id** | **str**|  | 
 **binding_id** | **str**|  | 

### Return type

[**DhcpStaticBinding**](DhcpStaticBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dhcp_v6_ip_pool**
> DhcpV6IpPool update_dhcp_v6_ip_pool(body, server_id, pool_id)

Update a DHCP IPv6 server's IP pool

Update a specific ip pool of a given logical DHCP IPv6 server.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpV6IpPool() # DhcpV6IpPool | 
server_id = 'server_id_example' # str | 
pool_id = 'pool_id_example' # str | 

try:
    # Update a DHCP IPv6 server's IP pool
    api_response = api_instance.update_dhcp_v6_ip_pool(body, server_id, pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->update_dhcp_v6_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpV6IpPool**](DhcpV6IpPool.md)|  | 
 **server_id** | **str**|  | 
 **pool_id** | **str**|  | 

### Return type

[**DhcpV6IpPool**](DhcpV6IpPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dhcp_v6_static_binding**
> DhcpV6StaticBinding update_dhcp_v6_static_binding(body, server_id, binding_id)

Update a DHCP IPv6 server's static binding

Update a specific static binding of a given local DHCP IPv6 server.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesDHCPApi(swagger_client.ApiClient(configuration))
body = swagger_client.DhcpV6StaticBinding() # DhcpV6StaticBinding | 
server_id = 'server_id_example' # str | 
binding_id = 'binding_id_example' # str | 

try:
    # Update a DHCP IPv6 server's static binding
    api_response = api_instance.update_dhcp_v6_static_binding(body, server_id, binding_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesDHCPApi->update_dhcp_v6_static_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpV6StaticBinding**](DhcpV6StaticBinding.md)|  | 
 **server_id** | **str**|  | 
 **binding_id** | **str**|  | 

### Return type

[**DhcpV6StaticBinding**](DhcpV6StaticBinding.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

