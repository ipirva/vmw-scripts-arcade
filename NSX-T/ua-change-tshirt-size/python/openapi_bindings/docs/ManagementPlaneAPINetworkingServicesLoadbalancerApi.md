# swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_load_balancer_application_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#create_load_balancer_application_profile) | **POST** /loadbalancer/application-profiles | Create a load balancer application profile
[**create_load_balancer_client_ssl_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#create_load_balancer_client_ssl_profile) | **POST** /loadbalancer/client-ssl-profiles | Create a load balancer client-ssl profile
[**create_load_balancer_monitor**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#create_load_balancer_monitor) | **POST** /loadbalancer/monitors | Create a load balancer monitor
[**create_load_balancer_persistence_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#create_load_balancer_persistence_profile) | **POST** /loadbalancer/persistence-profiles | Create a load balancer persistence profile
[**create_load_balancer_pool**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#create_load_balancer_pool) | **POST** /loadbalancer/pools | Create a load balancer pool
[**create_load_balancer_rule**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#create_load_balancer_rule) | **POST** /loadbalancer/rules | Create a load balancer rule
[**create_load_balancer_server_ssl_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#create_load_balancer_server_ssl_profile) | **POST** /loadbalancer/server-ssl-profiles | Create a load balancer server-ssl profile
[**create_load_balancer_service**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#create_load_balancer_service) | **POST** /loadbalancer/services | Create a load balancer service
[**create_load_balancer_virtual_server**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#create_load_balancer_virtual_server) | **POST** /loadbalancer/virtual-servers | Create a load balancer virtual server
[**create_load_balancer_virtual_server_with_rules_create_with_rules**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#create_load_balancer_virtual_server_with_rules_create_with_rules) | **POST** /loadbalancer/virtual-servers?action&#x3D;create_with_rules | Create a load balancer virtual server with rules
[**delete_load_balancer_application_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#delete_load_balancer_application_profile) | **DELETE** /loadbalancer/application-profiles/{application-profile-id} | Delete a load balancer application profile
[**delete_load_balancer_client_ssl_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#delete_load_balancer_client_ssl_profile) | **DELETE** /loadbalancer/client-ssl-profiles/{client-ssl-profile-id} | Delete a load balancer client-ssl profile
[**delete_load_balancer_monitor**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#delete_load_balancer_monitor) | **DELETE** /loadbalancer/monitors/{monitor-id} | Delete a load balancer monitor
[**delete_load_balancer_persistence_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#delete_load_balancer_persistence_profile) | **DELETE** /loadbalancer/persistence-profiles/{persistence-profile-id} | Delete a load balancer persistence profile
[**delete_load_balancer_pool**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#delete_load_balancer_pool) | **DELETE** /loadbalancer/pools/{pool-id} | Delete a load balancer pool
[**delete_load_balancer_rule**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#delete_load_balancer_rule) | **DELETE** /loadbalancer/rules/{rule-id} | Delete a load balancer rule
[**delete_load_balancer_server_ssl_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#delete_load_balancer_server_ssl_profile) | **DELETE** /loadbalancer/server-ssl-profiles/{server-ssl-profile-id} | Delete a load balancer server-ssl profile
[**delete_load_balancer_service**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#delete_load_balancer_service) | **DELETE** /loadbalancer/services/{service-id} | Delete a load balancer service
[**delete_load_balancer_virtual_server**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#delete_load_balancer_virtual_server) | **DELETE** /loadbalancer/virtual-servers/{virtual-server-id} | Delete a load balancer virtual server
[**get_load_balancer_pool_statistics**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#get_load_balancer_pool_statistics) | **GET** /loadbalancer/services/{service-id}/pools/{pool-id}/statistics | Get the statistics of load balancer pool
[**get_load_balancer_pool_status**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#get_load_balancer_pool_status) | **GET** /loadbalancer/services/{service-id}/pools/{pool-id}/status | Get the status of load balancer pool
[**get_load_balancer_service_statistics**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#get_load_balancer_service_statistics) | **GET** /loadbalancer/services/{service-id}/statistics | Get the statistics of load balancer service
[**get_load_balancer_service_status**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#get_load_balancer_service_status) | **GET** /loadbalancer/services/{service-id}/status | Get the status of the given load balancer service
[**get_load_balancer_virtual_server_statistics**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#get_load_balancer_virtual_server_statistics) | **GET** /loadbalancer/services/{service-id}/virtual-servers/{virtual-server-id}/statistics | Get the statistics of the given load balancer virtual server
[**get_load_balancer_virtual_server_status**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#get_load_balancer_virtual_server_status) | **GET** /loadbalancer/services/{service-id}/virtual-servers/{virtual-server-id}/status | Get the status of the load balancer virtual server
[**list_load_balancer_application_profiles**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_application_profiles) | **GET** /loadbalancer/application-profiles | Retrieve a paginated list of load balancer application profiles
[**list_load_balancer_client_ssl_profiles**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_client_ssl_profiles) | **GET** /loadbalancer/client-ssl-profiles | Retrieve a paginated list of load balancer client-ssl profiles
[**list_load_balancer_monitors**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_monitors) | **GET** /loadbalancer/monitors | Retrieve a paginated list of load balancer monitors
[**list_load_balancer_persistence_profiles**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_persistence_profiles) | **GET** /loadbalancer/persistence-profiles | Retrieve a paginated list of load balancer persistence profiles
[**list_load_balancer_pool_statistics**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_pool_statistics) | **GET** /loadbalancer/services/{service-id}/pools/statistics | Get the statistics list of load balancer pools
[**list_load_balancer_pool_statuses**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_pool_statuses) | **GET** /loadbalancer/services/{service-id}/pools/status | Get the status list of load balancer pools
[**list_load_balancer_pools**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_pools) | **GET** /loadbalancer/pools | Retrieve a paginated list of load balancer pools
[**list_load_balancer_rules**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_rules) | **GET** /loadbalancer/rules | Retrieve a paginated list of load balancer rules
[**list_load_balancer_server_ssl_profiles**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_server_ssl_profiles) | **GET** /loadbalancer/server-ssl-profiles | Retrieve a paginated list of load balancer server-ssl profiles
[**list_load_balancer_services**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_services) | **GET** /loadbalancer/services | Retrieve a paginated list of load balancer services
[**list_load_balancer_ssl_ciphers_and_protocols**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_ssl_ciphers_and_protocols) | **GET** /loadbalancer/ssl/ciphers-and-protocols | Retrieve a list of supported SSL ciphers and protocols
[**list_load_balancer_virtual_server_statuses**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_virtual_server_statuses) | **GET** /loadbalancer/services/{service-id}/virtual-servers/status | Get the status list of virtual servers in given load balancer service
[**list_load_balancer_virtual_servers**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_virtual_servers) | **GET** /loadbalancer/virtual-servers | Retrieve a paginated list of load balancer virtual servers
[**list_load_balancer_virtual_servers_statistics**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#list_load_balancer_virtual_servers_statistics) | **GET** /loadbalancer/services/{service-id}/virtual-servers/statistics | Get the statistics list of virtual servers
[**perform_pool_member_action**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#perform_pool_member_action) | **POST** /loadbalancer/pools/{pool-id} | Add, remove, or modify load balancer pool members
[**read_load_balancer_application_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_application_profile) | **GET** /loadbalancer/application-profiles/{application-profile-id} | Retrieve a load balancer application profile
[**read_load_balancer_client_ssl_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_client_ssl_profile) | **GET** /loadbalancer/client-ssl-profiles/{client-ssl-profile-id} | Retrieve a load balancer client-ssl profile
[**read_load_balancer_monitor**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_monitor) | **GET** /loadbalancer/monitors/{monitor-id} | Retrieve a load balancer monitor
[**read_load_balancer_node_usage**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_node_usage) | **GET** /loadbalancer/usage-per-node/{node-id} | Read load balancer usage for the given node
[**read_load_balancer_node_usage_summary**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_node_usage_summary) | **GET** /loadbalancer/node-usage-summary | Read load balancer node usage summary
[**read_load_balancer_persistence_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_persistence_profile) | **GET** /loadbalancer/persistence-profiles/{persistence-profile-id} | Retrieve a load balancer persistence profile
[**read_load_balancer_pool**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_pool) | **GET** /loadbalancer/pools/{pool-id} | Retrieve a load balancer pool
[**read_load_balancer_rule**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_rule) | **GET** /loadbalancer/rules/{rule-id} | Retrieve a load balancer rule
[**read_load_balancer_server_ssl_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_server_ssl_profile) | **GET** /loadbalancer/server-ssl-profiles/{server-ssl-profile-id} | Retrieve a load balancer server-ssl profile
[**read_load_balancer_service**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_service) | **GET** /loadbalancer/services/{service-id} | Retrieve a load balancer service
[**read_load_balancer_service_debug_info**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_service_debug_info) | **GET** /loadbalancer/services/{service-id}/debug-info | Read the debug information of the load balancer service
[**read_load_balancer_service_usage**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_service_usage) | **GET** /loadbalancer/services/{service-id}/usage | Read the usage information of the given load balancer service
[**read_load_balancer_virtual_server**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#read_load_balancer_virtual_server) | **GET** /loadbalancer/virtual-servers/{virtual-server-id} | Retrieve a load balancer virtual server
[**update_load_balancer_application_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#update_load_balancer_application_profile) | **PUT** /loadbalancer/application-profiles/{application-profile-id} | Update a load balancer application profile
[**update_load_balancer_client_ssl_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#update_load_balancer_client_ssl_profile) | **PUT** /loadbalancer/client-ssl-profiles/{client-ssl-profile-id} | Update a load balancer client-ssl profile
[**update_load_balancer_monitor**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#update_load_balancer_monitor) | **PUT** /loadbalancer/monitors/{monitor-id} | Update a load balancer monitor
[**update_load_balancer_persistence_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#update_load_balancer_persistence_profile) | **PUT** /loadbalancer/persistence-profiles/{persistence-profile-id} | Update a load balancer persistence profile
[**update_load_balancer_pool**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#update_load_balancer_pool) | **PUT** /loadbalancer/pools/{pool-id} | Update a load balancer pool
[**update_load_balancer_rule**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#update_load_balancer_rule) | **PUT** /loadbalancer/rules/{rule-id} | Update a load balancer rule
[**update_load_balancer_server_ssl_profile**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#update_load_balancer_server_ssl_profile) | **PUT** /loadbalancer/server-ssl-profiles/{server-ssl-profile-id} | Update a load balancer server-ssl profile
[**update_load_balancer_service**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#update_load_balancer_service) | **PUT** /loadbalancer/services/{service-id} | Update a load balancer service
[**update_load_balancer_virtual_server**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#update_load_balancer_virtual_server) | **PUT** /loadbalancer/virtual-servers/{virtual-server-id} | Update a load balancer virtual server
[**update_load_balancer_virtual_server_with_rules_update_with_rules**](ManagementPlaneAPINetworkingServicesLoadbalancerApi.md#update_load_balancer_virtual_server_with_rules_update_with_rules) | **PUT** /loadbalancer/virtual-servers/{virtual-server-id}?action&#x3D;update_with_rules | Update a load balancer virtual server with rules

# **create_load_balancer_application_profile**
> LbAppProfile create_load_balancer_application_profile(body)

Create a load balancer application profile

Create a load balancer application profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbAppProfile() # LbAppProfile | 

try:
    # Create a load balancer application profile
    api_response = api_instance.create_load_balancer_application_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->create_load_balancer_application_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbAppProfile**](LbAppProfile.md)|  | 

### Return type

[**LbAppProfile**](LbAppProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer_client_ssl_profile**
> LbClientSslProfile create_load_balancer_client_ssl_profile(body)

Create a load balancer client-ssl profile

Create a load balancer client-ssl profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbClientSslProfile() # LbClientSslProfile | 

try:
    # Create a load balancer client-ssl profile
    api_response = api_instance.create_load_balancer_client_ssl_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->create_load_balancer_client_ssl_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbClientSslProfile**](LbClientSslProfile.md)|  | 

### Return type

[**LbClientSslProfile**](LbClientSslProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer_monitor**
> LbMonitor create_load_balancer_monitor(body)

Create a load balancer monitor

Create a load balancer monitor. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbMonitor() # LbMonitor | 

try:
    # Create a load balancer monitor
    api_response = api_instance.create_load_balancer_monitor(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->create_load_balancer_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbMonitor**](LbMonitor.md)|  | 

### Return type

[**LbMonitor**](LbMonitor.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer_persistence_profile**
> LbPersistenceProfile create_load_balancer_persistence_profile(body)

Create a load balancer persistence profile

Create a load balancer persistence profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbPersistenceProfile() # LbPersistenceProfile | 

try:
    # Create a load balancer persistence profile
    api_response = api_instance.create_load_balancer_persistence_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->create_load_balancer_persistence_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbPersistenceProfile**](LbPersistenceProfile.md)|  | 

### Return type

[**LbPersistenceProfile**](LbPersistenceProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer_pool**
> LbPool create_load_balancer_pool(body)

Create a load balancer pool

Create a load balancer pool. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbPool() # LbPool | 

try:
    # Create a load balancer pool
    api_response = api_instance.create_load_balancer_pool(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->create_load_balancer_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbPool**](LbPool.md)|  | 

### Return type

[**LbPool**](LbPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer_rule**
> LbRule create_load_balancer_rule(body)

Create a load balancer rule

Create a load balancer rule. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbRule() # LbRule | 

try:
    # Create a load balancer rule
    api_response = api_instance.create_load_balancer_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->create_load_balancer_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbRule**](LbRule.md)|  | 

### Return type

[**LbRule**](LbRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer_server_ssl_profile**
> LbServerSslProfile create_load_balancer_server_ssl_profile(body)

Create a load balancer server-ssl profile

Create a load balancer server-ssl profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbServerSslProfile() # LbServerSslProfile | 

try:
    # Create a load balancer server-ssl profile
    api_response = api_instance.create_load_balancer_server_ssl_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->create_load_balancer_server_ssl_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbServerSslProfile**](LbServerSslProfile.md)|  | 

### Return type

[**LbServerSslProfile**](LbServerSslProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer_service**
> LbService create_load_balancer_service(body)

Create a load balancer service

Create a load balancer service. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbService() # LbService | 

try:
    # Create a load balancer service
    api_response = api_instance.create_load_balancer_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->create_load_balancer_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbService**](LbService.md)|  | 

### Return type

[**LbService**](LbService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer_virtual_server**
> LbVirtualServer create_load_balancer_virtual_server(body)

Create a load balancer virtual server

Create a load balancer virtual server. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbVirtualServer() # LbVirtualServer | 

try:
    # Create a load balancer virtual server
    api_response = api_instance.create_load_balancer_virtual_server(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->create_load_balancer_virtual_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbVirtualServer**](LbVirtualServer.md)|  | 

### Return type

[**LbVirtualServer**](LbVirtualServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer_virtual_server_with_rules_create_with_rules**
> LbVirtualServerWithRule create_load_balancer_virtual_server_with_rules_create_with_rules(body)

Create a load balancer virtual server with rules

It is used to create virtual servers, the associated rules and bind the rules to the virtual server. To add new rules, make sure the rules which have no identifier specified, the new rules are automatically generated and associated to the virtual server. If the virtual server need to consume some existed rules without change, those rules should not be specified in this array, otherwise, the rules are updated. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbVirtualServerWithRule() # LbVirtualServerWithRule | 

try:
    # Create a load balancer virtual server with rules
    api_response = api_instance.create_load_balancer_virtual_server_with_rules_create_with_rules(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->create_load_balancer_virtual_server_with_rules_create_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbVirtualServerWithRule**](LbVirtualServerWithRule.md)|  | 

### Return type

[**LbVirtualServerWithRule**](LbVirtualServerWithRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer_application_profile**
> delete_load_balancer_application_profile(application_profile_id)

Delete a load balancer application profile

Delete a load balancer application profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
application_profile_id = 'application_profile_id_example' # str | 

try:
    # Delete a load balancer application profile
    api_instance.delete_load_balancer_application_profile(application_profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->delete_load_balancer_application_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer_client_ssl_profile**
> delete_load_balancer_client_ssl_profile(client_ssl_profile_id)

Delete a load balancer client-ssl profile

Delete a load balancer client-ssl profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
client_ssl_profile_id = 'client_ssl_profile_id_example' # str | 

try:
    # Delete a load balancer client-ssl profile
    api_instance.delete_load_balancer_client_ssl_profile(client_ssl_profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->delete_load_balancer_client_ssl_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_ssl_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer_monitor**
> delete_load_balancer_monitor(monitor_id)

Delete a load balancer monitor

Delete a load balancer monitor. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
monitor_id = 'monitor_id_example' # str | 

try:
    # Delete a load balancer monitor
    api_instance.delete_load_balancer_monitor(monitor_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->delete_load_balancer_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer_persistence_profile**
> delete_load_balancer_persistence_profile(persistence_profile_id)

Delete a load balancer persistence profile

Delete a load balancer persistence profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
persistence_profile_id = 'persistence_profile_id_example' # str | 

try:
    # Delete a load balancer persistence profile
    api_instance.delete_load_balancer_persistence_profile(persistence_profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->delete_load_balancer_persistence_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **persistence_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer_pool**
> delete_load_balancer_pool(pool_id)

Delete a load balancer pool

Delete a load balancer pool. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
pool_id = 'pool_id_example' # str | 

try:
    # Delete a load balancer pool
    api_instance.delete_load_balancer_pool(pool_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->delete_load_balancer_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer_rule**
> delete_load_balancer_rule(rule_id)

Delete a load balancer rule

Delete a load balancer rule. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | 

try:
    # Delete a load balancer rule
    api_instance.delete_load_balancer_rule(rule_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->delete_load_balancer_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer_server_ssl_profile**
> delete_load_balancer_server_ssl_profile(server_ssl_profile_id)

Delete a load balancer server-ssl profile

Delete a load balancer server-ssl profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
server_ssl_profile_id = 'server_ssl_profile_id_example' # str | 

try:
    # Delete a load balancer server-ssl profile
    api_instance.delete_load_balancer_server_ssl_profile(server_ssl_profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->delete_load_balancer_server_ssl_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_ssl_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer_service**
> delete_load_balancer_service(service_id)

Delete a load balancer service

Delete a load balancer service. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 

try:
    # Delete a load balancer service
    api_instance.delete_load_balancer_service(service_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->delete_load_balancer_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer_virtual_server**
> delete_load_balancer_virtual_server(virtual_server_id, delete_associated_rules=delete_associated_rules)

Delete a load balancer virtual server

Delete a load balancer virtual server. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
virtual_server_id = 'virtual_server_id_example' # str | 
delete_associated_rules = false # bool | Delete associated rules (optional) (default to false)

try:
    # Delete a load balancer virtual server
    api_instance.delete_load_balancer_virtual_server(virtual_server_id, delete_associated_rules=delete_associated_rules)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->delete_load_balancer_virtual_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_server_id** | **str**|  | 
 **delete_associated_rules** | **bool**| Delete associated rules | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_pool_statistics**
> LbPoolStatistics get_load_balancer_pool_statistics(service_id, pool_id, source=source)

Get the statistics of load balancer pool

Returns the statistics of the given load balancer pool by given load balancer serives id and load balancer pool id. Currently, only realtime mode is supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
pool_id = 'pool_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the statistics of load balancer pool
    api_response = api_instance.get_load_balancer_pool_statistics(service_id, pool_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->get_load_balancer_pool_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **pool_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LbPoolStatistics**](LbPoolStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_pool_status**
> LbPoolStatus get_load_balancer_pool_status(service_id, pool_id, source=source)

Get the status of load balancer pool

Returns the status of the given load balancer pool by given load balancer serives id and load balancer pool id. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
pool_id = 'pool_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the status of load balancer pool
    api_response = api_instance.get_load_balancer_pool_status(service_id, pool_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->get_load_balancer_pool_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **pool_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LbPoolStatus**](LbPoolStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_service_statistics**
> LbServiceStatistics get_load_balancer_service_statistics(service_id, source=source)

Get the statistics of load balancer service

Returns the statistics of the given load balancer service. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the statistics of load balancer service
    api_response = api_instance.get_load_balancer_service_statistics(service_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->get_load_balancer_service_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LbServiceStatistics**](LbServiceStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_service_status**
> LbServiceStatus get_load_balancer_service_status(service_id, include_instance_details=include_instance_details, source=source, transport_node_ids=transport_node_ids)

Get the status of the given load balancer service

Returns the status of the given load balancer service. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
include_instance_details = false # bool | Flag to indicate whether include detail information (optional) (default to false)
source = 'source_example' # str | Data source type. (optional)
transport_node_ids = 'transport_node_ids_example' # str | The UUIDs of transport nodes (optional)

try:
    # Get the status of the given load balancer service
    api_response = api_instance.get_load_balancer_service_status(service_id, include_instance_details=include_instance_details, source=source, transport_node_ids=transport_node_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->get_load_balancer_service_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **include_instance_details** | **bool**| Flag to indicate whether include detail information | [optional] [default to false]
 **source** | **str**| Data source type. | [optional] 
 **transport_node_ids** | **str**| The UUIDs of transport nodes | [optional] 

### Return type

[**LbServiceStatus**](LbServiceStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_virtual_server_statistics**
> LbVirtualServerStatistics get_load_balancer_virtual_server_statistics(service_id, virtual_server_id, source=source)

Get the statistics of the given load balancer virtual server

Returns the statistics of the load balancer virtual server by given load  balancer serives id and load balancer virtual server id. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
virtual_server_id = 'virtual_server_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the statistics of the given load balancer virtual server
    api_response = api_instance.get_load_balancer_virtual_server_statistics(service_id, virtual_server_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->get_load_balancer_virtual_server_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **virtual_server_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LbVirtualServerStatistics**](LbVirtualServerStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_load_balancer_virtual_server_status**
> LbVirtualServerStatus get_load_balancer_virtual_server_status(service_id, virtual_server_id, source=source)

Get the status of the load balancer virtual server

Returns the status of the virtual server by given load balancer serives id and load balancer virtual server id. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
virtual_server_id = 'virtual_server_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the status of the load balancer virtual server
    api_response = api_instance.get_load_balancer_virtual_server_status(service_id, virtual_server_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->get_load_balancer_virtual_server_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **virtual_server_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LbVirtualServerStatus**](LbVirtualServerStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_application_profiles**
> LbAppProfileListResult list_load_balancer_application_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)

Retrieve a paginated list of load balancer application profiles

Retrieve a paginated list of load balancer application profiles. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
type = 'type_example' # str | application profile type (optional)

try:
    # Retrieve a paginated list of load balancer application profiles
    api_response = api_instance.list_load_balancer_application_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_application_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **type** | **str**| application profile type | [optional] 

### Return type

[**LbAppProfileListResult**](LbAppProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_client_ssl_profiles**
> LbClientSslProfileListResult list_load_balancer_client_ssl_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Retrieve a paginated list of load balancer client-ssl profiles

Retrieve a paginated list of load balancer client-ssl profiles. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Retrieve a paginated list of load balancer client-ssl profiles
    api_response = api_instance.list_load_balancer_client_ssl_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_client_ssl_profiles: %s\n" % e)
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

[**LbClientSslProfileListResult**](LbClientSslProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_monitors**
> LbMonitorListResult list_load_balancer_monitors(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)

Retrieve a paginated list of load balancer monitors

Retrieve a paginated list of load balancer monitors. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
type = 'type_example' # str | monitor query type (optional)

try:
    # Retrieve a paginated list of load balancer monitors
    api_response = api_instance.list_load_balancer_monitors(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_monitors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **type** | **str**| monitor query type | [optional] 

### Return type

[**LbMonitorListResult**](LbMonitorListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_persistence_profiles**
> LbPersistenceProfileListResult list_load_balancer_persistence_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)

Retrieve a paginated list of load balancer persistence profiles

Retrieve a paginated list of load balancer persistence profiles. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
type = 'type_example' # str | persistence profile type (optional)

try:
    # Retrieve a paginated list of load balancer persistence profiles
    api_response = api_instance.list_load_balancer_persistence_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_persistence_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **type** | **str**| persistence profile type | [optional] 

### Return type

[**LbPersistenceProfileListResult**](LbPersistenceProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_pool_statistics**
> LbPoolStatisticsListResult list_load_balancer_pool_statistics(service_id, source=source)

Get the statistics list of load balancer pools

Returns the statistics list of load balancer pools in given load balancer service. Currently, only realtime mode is supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the statistics list of load balancer pools
    api_response = api_instance.list_load_balancer_pool_statistics(service_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_pool_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LbPoolStatisticsListResult**](LbPoolStatisticsListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_pool_statuses**
> LbPoolStatusListResult list_load_balancer_pool_statuses(service_id, source=source)

Get the status list of load balancer pools

Returns the status list of load balancer pools in given load balancer service. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the status list of load balancer pools
    api_response = api_instance.list_load_balancer_pool_statuses(service_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_pool_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LbPoolStatusListResult**](LbPoolStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_pools**
> LbPoolListResult list_load_balancer_pools(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Retrieve a paginated list of load balancer pools

Retrieve a paginated list of load balancer pools. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Retrieve a paginated list of load balancer pools
    api_response = api_instance.list_load_balancer_pools(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_pools: %s\n" % e)
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

[**LbPoolListResult**](LbPoolListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_rules**
> LbRuleListResult list_load_balancer_rules(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Retrieve a paginated list of load balancer rules

Retrieve a paginated list of load balancer rules. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Retrieve a paginated list of load balancer rules
    api_response = api_instance.list_load_balancer_rules(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_rules: %s\n" % e)
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

[**LbRuleListResult**](LbRuleListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_server_ssl_profiles**
> LbServerSslProfileListResult list_load_balancer_server_ssl_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Retrieve a paginated list of load balancer server-ssl profiles

Retrieve a paginated list of load balancer server-ssl profiles. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Retrieve a paginated list of load balancer server-ssl profiles
    api_response = api_instance.list_load_balancer_server_ssl_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_server_ssl_profiles: %s\n" % e)
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

[**LbServerSslProfileListResult**](LbServerSslProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_services**
> LbServiceListResult list_load_balancer_services(cursor=cursor, included_fields=included_fields, logical_router_id=logical_router_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Retrieve a paginated list of load balancer services

Retrieve a paginated list of load balancer services. When logical_router_id is specified in request parameters, the associated load balancer services which are related to the given logical router returned. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
logical_router_id = 'logical_router_id_example' # str | Logical router identifier (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Retrieve a paginated list of load balancer services
    api_response = api_instance.list_load_balancer_services(cursor=cursor, included_fields=included_fields, logical_router_id=logical_router_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **logical_router_id** | **str**| Logical router identifier | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**LbServiceListResult**](LbServiceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_ssl_ciphers_and_protocols**
> LbSslCipherAndProtocolListResult list_load_balancer_ssl_ciphers_and_protocols(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Retrieve a list of supported SSL ciphers and protocols

Retrieve a list of supported SSL ciphers and protocols. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Retrieve a list of supported SSL ciphers and protocols
    api_response = api_instance.list_load_balancer_ssl_ciphers_and_protocols(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_ssl_ciphers_and_protocols: %s\n" % e)
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

[**LbSslCipherAndProtocolListResult**](LbSslCipherAndProtocolListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_virtual_server_statuses**
> LbVirtualServerStatusListResult list_load_balancer_virtual_server_statuses(service_id, source=source)

Get the status list of virtual servers in given load balancer service

Returns the status list of virtual servers in given load balancer service. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the status list of virtual servers in given load balancer service
    api_response = api_instance.list_load_balancer_virtual_server_statuses(service_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_virtual_server_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LbVirtualServerStatusListResult**](LbVirtualServerStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_virtual_servers**
> LbVirtualServerListResult list_load_balancer_virtual_servers(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Retrieve a paginated list of load balancer virtual servers

Retrieve a paginated list of load balancer virtual servers. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Retrieve a paginated list of load balancer virtual servers
    api_response = api_instance.list_load_balancer_virtual_servers(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_virtual_servers: %s\n" % e)
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

[**LbVirtualServerListResult**](LbVirtualServerListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_load_balancer_virtual_servers_statistics**
> LbVirtualServerStatisticsListResult list_load_balancer_virtual_servers_statistics(service_id, source=source)

Get the statistics list of virtual servers

Returns the statistics list of virtual servers in given load balancer service. Currently, only realtime mode is supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the statistics list of virtual servers
    api_response = api_instance.list_load_balancer_virtual_servers_statistics(service_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->list_load_balancer_virtual_servers_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LbVirtualServerStatisticsListResult**](LbVirtualServerStatisticsListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_pool_member_action**
> LbPool perform_pool_member_action(body, action, pool_id)

Add, remove, or modify load balancer pool members

For ADD_MEMBERS, pool members will be created and added to load balancer pool. This action is only valid for static pool members. For REMOVE_MEMBERS, pool members will be removed from load balancer pool via IP and port in pool member settings. This action is only valid for static pool members. For UPDATE_MEMBERS, pool members admin state will be updated. This action is valid for both static pool members and dynamic pool members. For dynamic pool members, this update will be stored in customized_members field in load balancer pool member group. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.PoolMemberSettingList() # PoolMemberSettingList | 
action = 'action_example' # str | Specifies addition, removal and modification action
pool_id = 'pool_id_example' # str | 

try:
    # Add, remove, or modify load balancer pool members
    api_response = api_instance.perform_pool_member_action(body, action, pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->perform_pool_member_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoolMemberSettingList**](PoolMemberSettingList.md)|  | 
 **action** | **str**| Specifies addition, removal and modification action | 
 **pool_id** | **str**|  | 

### Return type

[**LbPool**](LbPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_application_profile**
> LbAppProfile read_load_balancer_application_profile(application_profile_id)

Retrieve a load balancer application profile

Retrieve a load balancer application profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
application_profile_id = 'application_profile_id_example' # str | 

try:
    # Retrieve a load balancer application profile
    api_response = api_instance.read_load_balancer_application_profile(application_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_application_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_profile_id** | **str**|  | 

### Return type

[**LbAppProfile**](LbAppProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_client_ssl_profile**
> LbClientSslProfile read_load_balancer_client_ssl_profile(client_ssl_profile_id)

Retrieve a load balancer client-ssl profile

Retrieve a load balancer client-ssl profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
client_ssl_profile_id = 'client_ssl_profile_id_example' # str | 

try:
    # Retrieve a load balancer client-ssl profile
    api_response = api_instance.read_load_balancer_client_ssl_profile(client_ssl_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_client_ssl_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_ssl_profile_id** | **str**|  | 

### Return type

[**LbClientSslProfile**](LbClientSslProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_monitor**
> LbMonitor read_load_balancer_monitor(monitor_id)

Retrieve a load balancer monitor

Retrieve a load balancer monitor. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
monitor_id = 'monitor_id_example' # str | 

try:
    # Retrieve a load balancer monitor
    api_response = api_instance.read_load_balancer_monitor(monitor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_id** | **str**|  | 

### Return type

[**LbMonitor**](LbMonitor.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_node_usage**
> LbNodeUsage read_load_balancer_node_usage(node_id)

Read load balancer usage for the given node

API is used to retrieve the usage of load balancer entities which include current number and remaining number of credits, virtual Servers, pools, pool Members and different size of LB services from the given node. Currently only Edge node is supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Read load balancer usage for the given node
    api_response = api_instance.read_load_balancer_node_usage(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_node_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**LbNodeUsage**](LbNodeUsage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_node_usage_summary**
> LbNodeUsageSummary read_load_balancer_node_usage_summary(include_usages=include_usages)

Read load balancer node usage summary

API is used to retrieve the load balancer node usage summary for all nodes. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
include_usages = true # bool | Whether to include node usages (optional)

try:
    # Read load balancer node usage summary
    api_response = api_instance.read_load_balancer_node_usage_summary(include_usages=include_usages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_node_usage_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_usages** | **bool**| Whether to include node usages | [optional] 

### Return type

[**LbNodeUsageSummary**](LbNodeUsageSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_persistence_profile**
> LbPersistenceProfile read_load_balancer_persistence_profile(persistence_profile_id)

Retrieve a load balancer persistence profile

Retrieve a load balancer persistence profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
persistence_profile_id = 'persistence_profile_id_example' # str | 

try:
    # Retrieve a load balancer persistence profile
    api_response = api_instance.read_load_balancer_persistence_profile(persistence_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_persistence_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **persistence_profile_id** | **str**|  | 

### Return type

[**LbPersistenceProfile**](LbPersistenceProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_pool**
> LbPool read_load_balancer_pool(pool_id)

Retrieve a load balancer pool

Retrieve a load balancer pool. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
pool_id = 'pool_id_example' # str | 

try:
    # Retrieve a load balancer pool
    api_response = api_instance.read_load_balancer_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | 

### Return type

[**LbPool**](LbPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_rule**
> LbRule read_load_balancer_rule(rule_id)

Retrieve a load balancer rule

Retrieve a load balancer rule. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | 

try:
    # Retrieve a load balancer rule
    api_response = api_instance.read_load_balancer_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

[**LbRule**](LbRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_server_ssl_profile**
> LbServerSslProfile read_load_balancer_server_ssl_profile(server_ssl_profile_id)

Retrieve a load balancer server-ssl profile

Retrieve a load balancer server-ssl profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
server_ssl_profile_id = 'server_ssl_profile_id_example' # str | 

try:
    # Retrieve a load balancer server-ssl profile
    api_response = api_instance.read_load_balancer_server_ssl_profile(server_ssl_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_server_ssl_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_ssl_profile_id** | **str**|  | 

### Return type

[**LbServerSslProfile**](LbServerSslProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_service**
> LbService read_load_balancer_service(service_id)

Retrieve a load balancer service

Retrieve a load balancer service. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 

try:
    # Retrieve a load balancer service
    api_response = api_instance.read_load_balancer_service(service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**LbService**](LbService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_service_debug_info**
> LbServiceDebugInfo read_load_balancer_service_debug_info(service_id)

Read the debug information of the load balancer service

API to download below information which will be used for debugging and troubleshooting. 1) Load balancer service 2) Load balancer associated virtual servers 3) Load balancer associated pools 4) Load balancer associated profiles such as persistence, SSL, application. 5) Load balancer associated monitors 6) Load balancer associated rules 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 

try:
    # Read the debug information of the load balancer service
    api_response = api_instance.read_load_balancer_service_debug_info(service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_service_debug_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**LbServiceDebugInfo**](LbServiceDebugInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_service_usage**
> LbServiceUsage read_load_balancer_service_usage(service_id)

Read the usage information of the given load balancer service

API to fetch the capacity and current usage of the given load balancer service. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 

try:
    # Read the usage information of the given load balancer service
    api_response = api_instance.read_load_balancer_service_usage(service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_service_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**LbServiceUsage**](LbServiceUsage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_load_balancer_virtual_server**
> LbVirtualServer read_load_balancer_virtual_server(virtual_server_id)

Retrieve a load balancer virtual server

Retrieve a load balancer virtual server. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
virtual_server_id = 'virtual_server_id_example' # str | 

try:
    # Retrieve a load balancer virtual server
    api_response = api_instance.read_load_balancer_virtual_server(virtual_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->read_load_balancer_virtual_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_server_id** | **str**|  | 

### Return type

[**LbVirtualServer**](LbVirtualServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_balancer_application_profile**
> LbAppProfile update_load_balancer_application_profile(body, application_profile_id)

Update a load balancer application profile

Update a load balancer application profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbAppProfile() # LbAppProfile | 
application_profile_id = 'application_profile_id_example' # str | 

try:
    # Update a load balancer application profile
    api_response = api_instance.update_load_balancer_application_profile(body, application_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->update_load_balancer_application_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbAppProfile**](LbAppProfile.md)|  | 
 **application_profile_id** | **str**|  | 

### Return type

[**LbAppProfile**](LbAppProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_balancer_client_ssl_profile**
> LbClientSslProfile update_load_balancer_client_ssl_profile(body, client_ssl_profile_id)

Update a load balancer client-ssl profile

Update a load balancer client-ssl profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbClientSslProfile() # LbClientSslProfile | 
client_ssl_profile_id = 'client_ssl_profile_id_example' # str | 

try:
    # Update a load balancer client-ssl profile
    api_response = api_instance.update_load_balancer_client_ssl_profile(body, client_ssl_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->update_load_balancer_client_ssl_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbClientSslProfile**](LbClientSslProfile.md)|  | 
 **client_ssl_profile_id** | **str**|  | 

### Return type

[**LbClientSslProfile**](LbClientSslProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_balancer_monitor**
> LbMonitor update_load_balancer_monitor(body, monitor_id)

Update a load balancer monitor

Update a load balancer monitor. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbMonitor() # LbMonitor | 
monitor_id = 'monitor_id_example' # str | 

try:
    # Update a load balancer monitor
    api_response = api_instance.update_load_balancer_monitor(body, monitor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->update_load_balancer_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbMonitor**](LbMonitor.md)|  | 
 **monitor_id** | **str**|  | 

### Return type

[**LbMonitor**](LbMonitor.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_balancer_persistence_profile**
> LbPersistenceProfile update_load_balancer_persistence_profile(body, persistence_profile_id)

Update a load balancer persistence profile

Update a load balancer persistence profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbPersistenceProfile() # LbPersistenceProfile | 
persistence_profile_id = 'persistence_profile_id_example' # str | 

try:
    # Update a load balancer persistence profile
    api_response = api_instance.update_load_balancer_persistence_profile(body, persistence_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->update_load_balancer_persistence_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbPersistenceProfile**](LbPersistenceProfile.md)|  | 
 **persistence_profile_id** | **str**|  | 

### Return type

[**LbPersistenceProfile**](LbPersistenceProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_balancer_pool**
> LbPool update_load_balancer_pool(body, pool_id)

Update a load balancer pool

Update a load balancer pool. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbPool() # LbPool | 
pool_id = 'pool_id_example' # str | 

try:
    # Update a load balancer pool
    api_response = api_instance.update_load_balancer_pool(body, pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->update_load_balancer_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbPool**](LbPool.md)|  | 
 **pool_id** | **str**|  | 

### Return type

[**LbPool**](LbPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_balancer_rule**
> LbRule update_load_balancer_rule(body, rule_id)

Update a load balancer rule

Update a load balancer rule. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbRule() # LbRule | 
rule_id = 'rule_id_example' # str | 

try:
    # Update a load balancer rule
    api_response = api_instance.update_load_balancer_rule(body, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->update_load_balancer_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbRule**](LbRule.md)|  | 
 **rule_id** | **str**|  | 

### Return type

[**LbRule**](LbRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_balancer_server_ssl_profile**
> LbServerSslProfile update_load_balancer_server_ssl_profile(body, server_ssl_profile_id)

Update a load balancer server-ssl profile

Update a load balancer server-ssl profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbServerSslProfile() # LbServerSslProfile | 
server_ssl_profile_id = 'server_ssl_profile_id_example' # str | 

try:
    # Update a load balancer server-ssl profile
    api_response = api_instance.update_load_balancer_server_ssl_profile(body, server_ssl_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->update_load_balancer_server_ssl_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbServerSslProfile**](LbServerSslProfile.md)|  | 
 **server_ssl_profile_id** | **str**|  | 

### Return type

[**LbServerSslProfile**](LbServerSslProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_balancer_service**
> LbService update_load_balancer_service(body, service_id)

Update a load balancer service

Update a load balancer service. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbService() # LbService | 
service_id = 'service_id_example' # str | 

try:
    # Update a load balancer service
    api_response = api_instance.update_load_balancer_service(body, service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->update_load_balancer_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbService**](LbService.md)|  | 
 **service_id** | **str**|  | 

### Return type

[**LbService**](LbService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_balancer_virtual_server**
> LbVirtualServer update_load_balancer_virtual_server(body, virtual_server_id)

Update a load balancer virtual server

Update a load balancer virtual server. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbVirtualServer() # LbVirtualServer | 
virtual_server_id = 'virtual_server_id_example' # str | 

try:
    # Update a load balancer virtual server
    api_response = api_instance.update_load_balancer_virtual_server(body, virtual_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->update_load_balancer_virtual_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbVirtualServer**](LbVirtualServer.md)|  | 
 **virtual_server_id** | **str**|  | 

### Return type

[**LbVirtualServer**](LbVirtualServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_balancer_virtual_server_with_rules_update_with_rules**
> LbVirtualServerWithRule update_load_balancer_virtual_server_with_rules_update_with_rules(body, virtual_server_id)

Update a load balancer virtual server with rules

It is used to update virtual servers, the associated rules and update the binding of virtual server and rules. To add new rules, make sure the rules which have no identifier specified, the new rules are automatically generated and associated to the virtual server. To delete old rules, the rules should not be configured in new action, the UUID of deleted rules should be also removed from rule_ids. To update rules, the rules should be specified with new change and configured with identifier. If there are some rules which are not modified, those rule should not be specified in the rules list, the UUID list of rules should be specified in rule_ids of LbVirtualServer. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesLoadbalancerApi(swagger_client.ApiClient(configuration))
body = swagger_client.LbVirtualServerWithRule() # LbVirtualServerWithRule | 
virtual_server_id = 'virtual_server_id_example' # str | 

try:
    # Update a load balancer virtual server with rules
    api_response = api_instance.update_load_balancer_virtual_server_with_rules_update_with_rules(body, virtual_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesLoadbalancerApi->update_load_balancer_virtual_server_with_rules_update_with_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LbVirtualServerWithRule**](LbVirtualServerWithRule.md)|  | 
 **virtual_server_id** | **str**|  | 

### Return type

[**LbVirtualServerWithRule**](LbVirtualServerWithRule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

