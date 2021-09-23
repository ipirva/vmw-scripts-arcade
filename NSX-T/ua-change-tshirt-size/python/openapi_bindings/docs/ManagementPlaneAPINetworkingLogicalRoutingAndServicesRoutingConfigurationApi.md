# swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bgp_neighbor**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#add_bgp_neighbor) | **POST** /logical-routers/{logical-router-id}/routing/bgp/neighbors | Add a new BGP Neighbor on a Logical Router
[**add_ip_prefix_list**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#add_ip_prefix_list) | **POST** /logical-routers/{logical-router-id}/routing/ip-prefix-lists | Add IPPrefixList on a Logical Router
[**add_route_map**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#add_route_map) | **POST** /logical-routers/{logical-router-id}/routing/route-maps | Add RouteMap on a Logical Router
[**add_static_route**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#add_static_route) | **POST** /logical-routers/{logical-router-id}/routing/static-routes | Add Static Routes on a Logical Router
[**create_bgp_community_list**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#create_bgp_community_list) | **POST** /logical-routers/{logical-router-id}/routing/bgp/community-lists | Create a new BGP community list on a logical router
[**create_dad_profile**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#create_dad_profile) | **POST** /ipv6/dad-profiles | Create a new DADProfile
[**create_ndra_profile**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#create_ndra_profile) | **POST** /ipv6/nd-ra-profiles | Create a new NDRA Profile
[**delete_bgp_community_list**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#delete_bgp_community_list) | **DELETE** /logical-routers/{logical-router-id}/routing/bgp/community-lists/{community-list-id} | Delete a specific BGP community list from a logical router
[**delete_bgp_neighbor**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#delete_bgp_neighbor) | **DELETE** /logical-routers/{logical-router-id}/routing/bgp/neighbors/{id} | Delete a specific BGP Neighbor on a Logical Router
[**delete_dad_profile**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#delete_dad_profile) | **DELETE** /ipv6/dad-profiles/{dad-profile-id} | Delete DAD Profile
[**delete_ip_prefix_list**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#delete_ip_prefix_list) | **DELETE** /logical-routers/{logical-router-id}/routing/ip-prefix-lists/{id} | Delete a specific IPPrefixList on a Logical Router
[**delete_ndra_profile**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#delete_ndra_profile) | **DELETE** /ipv6/nd-ra-profiles/{nd-ra-profile-id} | Delete NDRA Profile
[**delete_route_map**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#delete_route_map) | **DELETE** /logical-routers/{logical-router-id}/routing/route-maps/{id} | Delete a specific RouteMap on a Logical Router
[**delete_static_route**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#delete_static_route) | **DELETE** /logical-routers/{logical-router-id}/routing/static-routes/{id} | Delete a specific Static Route on a Logical Router
[**list_bgp_community_lists**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#list_bgp_community_lists) | **GET** /logical-routers/{logical-router-id}/routing/bgp/community-lists | Paginated list of BGP community lists on a logical router
[**list_bgp_neighbors**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#list_bgp_neighbors) | **GET** /logical-routers/{logical-router-id}/routing/bgp/neighbors | Paginated list of BGP Neighbors on a Logical Router
[**list_dad_profiles**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#list_dad_profiles) | **GET** /ipv6/dad-profiles | Read All IPV6 DADProfiles
[**list_ip_prefix_lists**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#list_ip_prefix_lists) | **GET** /logical-routers/{logical-router-id}/routing/ip-prefix-lists | Paginated List of IPPrefixLists
[**list_ndra_profiles**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#list_ndra_profiles) | **GET** /ipv6/nd-ra-profiles | Read All IPV6 NDRA Profiles
[**list_route_maps**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#list_route_maps) | **GET** /logical-routers/{logical-router-id}/routing/route-maps | Paginated List of RouteMaps
[**list_static_routes**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#list_static_routes) | **GET** /logical-routers/{logical-router-id}/routing/static-routes | Paginated List of Static Routes
[**read_advertise_rule_list**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_advertise_rule_list) | **GET** /logical-routers/{logical-router-id}/routing/advertisement/rules | Read the Advertisement Rules on a Logical Router
[**read_advertisement_config**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_advertisement_config) | **GET** /logical-routers/{logical-router-id}/routing/advertisement | Read the Advertisement Configuration on a Logical Router
[**read_bgp_community_list**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_bgp_community_list) | **GET** /logical-routers/{logical-router-id}/routing/bgp/community-lists/{community-list-id} | Read a specific BGP community list from a logical router
[**read_bgp_config**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_bgp_config) | **GET** /logical-routers/{logical-router-id}/routing/bgp | Read the BGP Configuration on a Logical Router
[**read_bgp_neighbor**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_bgp_neighbor) | **GET** /logical-routers/{logical-router-id}/routing/bgp/neighbors/{id} | Read a specific BGP Neighbor on a Logical Router
[**read_bgp_neighbor_with_password_show_sensitive_data**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_bgp_neighbor_with_password_show_sensitive_data) | **GET** /logical-routers/{logical-router-id}/routing/bgp/neighbors/{id}?action&#x3D;show-sensitive-data | Read a specific BGP Neighbor with password on a Logical Router
[**read_dad_profile**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_dad_profile) | **GET** /ipv6/dad-profiles/{dad-profile-id} | Read specified IPV6 DADProfile
[**read_debug_info_text**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_debug_info_text) | **GET** /logical-routers/{logical-router-id}/debug-info?format&#x3D;text | Read the debug information for the logical router
[**read_ip_prefix_list**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_ip_prefix_list) | **GET** /logical-routers/{logical-router-id}/routing/ip-prefix-lists/{id} | Get a specific IPPrefixList on a Logical Router
[**read_ndra_profile**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_ndra_profile) | **GET** /ipv6/nd-ra-profiles/{nd-ra-profile-id} | Read specified IPV6 NDRA Profile
[**read_redistribution_config**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_redistribution_config) | **GET** /logical-routers/{logical-router-id}/routing/redistribution | Read the Redistribution Configuration on a Logical Router
[**read_redistribution_rule_list**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_redistribution_rule_list) | **GET** /logical-routers/{logical-router-id}/routing/redistribution/rules | Read All the Redistribution Rules on a Logical Router
[**read_route_map**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_route_map) | **GET** /logical-routers/{logical-router-id}/routing/route-maps/{id} | Get a specific RouteMap on a Logical Router
[**read_routing_config**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_routing_config) | **GET** /logical-routers/{logical-router-id}/routing | Read the Routing Configuration
[**read_static_route**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#read_static_route) | **GET** /logical-routers/{logical-router-id}/routing/static-routes/{id} | Get a specific Static Route on a Logical Router
[**un_set_password_on_bgp_neighbor**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#un_set_password_on_bgp_neighbor) | **POST** /logical-routers/{logical-router-id}/routing/bgp/neighbors/{id} | Unset/Delete password property on specific BGP Neighbor on Logical Router
[**update_advertise_rule_list**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_advertise_rule_list) | **PUT** /logical-routers/{logical-router-id}/routing/advertisement/rules | Update the Advertisement Rules on a Logical Router
[**update_advertisement_config**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_advertisement_config) | **PUT** /logical-routers/{logical-router-id}/routing/advertisement | Update the Advertisement Configuration on a Logical Router
[**update_bgp_community_list**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_bgp_community_list) | **PUT** /logical-routers/{logical-router-id}/routing/bgp/community-lists/{community-list-id} | Update a specific BGP community list from a logical router
[**update_bgp_community_list_old**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_bgp_community_list_old) | **PUT** /logical-routers/{logical-router-id}/routing/bgp/communty-lists/{community-list-id} | Update a specific BGP community list from a logical router
[**update_bgp_config**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_bgp_config) | **PUT** /logical-routers/{logical-router-id}/routing/bgp | Update the BGP Configuration on a Logical Router
[**update_bgp_neighbor**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_bgp_neighbor) | **PUT** /logical-routers/{logical-router-id}/routing/bgp/neighbors/{id} | Update a specific BGP Neighbor on a Logical Router
[**update_dad_profile**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_dad_profile) | **PUT** /ipv6/dad-profiles/{dad-profile-id} | Update DADProfile
[**update_ip_prefix_list**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_ip_prefix_list) | **PUT** /logical-routers/{logical-router-id}/routing/ip-prefix-lists/{id} | Update a specific IPPrefixList on a Logical Router
[**update_ndra_profile**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_ndra_profile) | **PUT** /ipv6/nd-ra-profiles/{nd-ra-profile-id} | Update NDRA Profile
[**update_redistribution_config**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_redistribution_config) | **PUT** /logical-routers/{logical-router-id}/routing/redistribution | Update the Redistribution Configuration on a Logical Router
[**update_redistribution_rule_list**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_redistribution_rule_list) | **PUT** /logical-routers/{logical-router-id}/routing/redistribution/rules | Update All the Redistribution Rules on a Logical Router
[**update_route_map**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_route_map) | **PUT** /logical-routers/{logical-router-id}/routing/route-maps/{id} | Update a specific RouteMap on a Logical Router
[**update_routing_config**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_routing_config) | **PUT** /logical-routers/{logical-router-id}/routing | Update the Routing Configuration
[**update_static_route**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi.md#update_static_route) | **PUT** /logical-routers/{logical-router-id}/routing/static-routes/{id} | Update a specific Static Route Rule on a Logical Router

# **add_bgp_neighbor**
> BgpNeighbor add_bgp_neighbor(body, logical_router_id)

Add a new BGP Neighbor on a Logical Router

Add a new BGP Neighbor on a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.BgpNeighbor() # BgpNeighbor | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Add a new BGP Neighbor on a Logical Router
    api_response = api_instance.add_bgp_neighbor(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->add_bgp_neighbor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BgpNeighbor**](BgpNeighbor.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**BgpNeighbor**](BgpNeighbor.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_ip_prefix_list**
> IPPrefixList add_ip_prefix_list(body, logical_router_id)

Add IPPrefixList on a Logical Router

Adds a new IPPrefixList on a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPPrefixList() # IPPrefixList | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Add IPPrefixList on a Logical Router
    api_response = api_instance.add_ip_prefix_list(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->add_ip_prefix_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPPrefixList**](IPPrefixList.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**IPPrefixList**](IPPrefixList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_route_map**
> RouteMap add_route_map(body, logical_router_id)

Add RouteMap on a Logical Router

Adds a new RouteMap on a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.RouteMap() # RouteMap | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Add RouteMap on a Logical Router
    api_response = api_instance.add_route_map(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->add_route_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RouteMap**](RouteMap.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**RouteMap**](RouteMap.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_static_route**
> StaticRoute add_static_route(body, logical_router_id)

Add Static Routes on a Logical Router

Adds a new static route on a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.StaticRoute() # StaticRoute | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Add Static Routes on a Logical Router
    api_response = api_instance.add_static_route(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->add_static_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StaticRoute**](StaticRoute.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**StaticRoute**](StaticRoute.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bgp_community_list**
> BGPCommunityList create_bgp_community_list(body, logical_router_id)

Create a new BGP community list on a logical router

Add a new BGP Community List on a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.BGPCommunityList() # BGPCommunityList | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Create a new BGP community list on a logical router
    api_response = api_instance.create_bgp_community_list(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->create_bgp_community_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BGPCommunityList**](BGPCommunityList.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**BGPCommunityList**](BGPCommunityList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dad_profile**
> DADProfile create_dad_profile(body)

Create a new DADProfile

Adds a new DADProfile 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.DADProfile() # DADProfile | 

try:
    # Create a new DADProfile
    api_response = api_instance.create_dad_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->create_dad_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DADProfile**](DADProfile.md)|  | 

### Return type

[**DADProfile**](DADProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ndra_profile**
> NDRAProfile create_ndra_profile(body)

Create a new NDRA Profile

Adds a new NDRAProfile 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.NDRAProfile() # NDRAProfile | 

try:
    # Create a new NDRA Profile
    api_response = api_instance.create_ndra_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->create_ndra_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NDRAProfile**](NDRAProfile.md)|  | 

### Return type

[**NDRAProfile**](NDRAProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bgp_community_list**
> delete_bgp_community_list(logical_router_id, community_list_id)

Delete a specific BGP community list from a logical router

Delete a specific BGP community list from a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
community_list_id = 'community_list_id_example' # str | 

try:
    # Delete a specific BGP community list from a logical router
    api_instance.delete_bgp_community_list(logical_router_id, community_list_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->delete_bgp_community_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **community_list_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bgp_neighbor**
> delete_bgp_neighbor(logical_router_id, id)

Delete a specific BGP Neighbor on a Logical Router

Delete a specific BGP Neighbor on a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Delete a specific BGP Neighbor on a Logical Router
    api_instance.delete_bgp_neighbor(logical_router_id, id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->delete_bgp_neighbor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dad_profile**
> delete_dad_profile(dad_profile_id)

Delete DAD Profile

Delete DADProfile 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
dad_profile_id = 'dad_profile_id_example' # str | 

try:
    # Delete DAD Profile
    api_instance.delete_dad_profile(dad_profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->delete_dad_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dad_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_prefix_list**
> delete_ip_prefix_list(logical_router_id, id)

Delete a specific IPPrefixList on a Logical Router

Deletes a specific IPPrefixList on the specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Delete a specific IPPrefixList on a Logical Router
    api_instance.delete_ip_prefix_list(logical_router_id, id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->delete_ip_prefix_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ndra_profile**
> delete_ndra_profile(nd_ra_profile_id)

Delete NDRA Profile

Delete NDRAProfile 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
nd_ra_profile_id = 'nd_ra_profile_id_example' # str | 

try:
    # Delete NDRA Profile
    api_instance.delete_ndra_profile(nd_ra_profile_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->delete_ndra_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nd_ra_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_route_map**
> delete_route_map(logical_router_id, id)

Delete a specific RouteMap on a Logical Router

Deletes a specific RouteMap on the specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Delete a specific RouteMap on a Logical Router
    api_instance.delete_route_map(logical_router_id, id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->delete_route_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_static_route**
> delete_static_route(logical_router_id, id)

Delete a specific Static Route on a Logical Router

Deletes a specific static route on the specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Delete a specific Static Route on a Logical Router
    api_instance.delete_static_route(logical_router_id, id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->delete_static_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bgp_community_lists**
> BGPCommunityListListResult list_bgp_community_lists(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Paginated list of BGP community lists on a logical router

Paginated list of BGP Community Lists on a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Paginated list of BGP community lists on a logical router
    api_response = api_instance.list_bgp_community_lists(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->list_bgp_community_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**BGPCommunityListListResult**](BGPCommunityListListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bgp_neighbors**
> BgpNeighborListResult list_bgp_neighbors(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Paginated list of BGP Neighbors on a Logical Router

Paginated list of BGP Neighbors on a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Paginated list of BGP Neighbors on a Logical Router
    api_response = api_instance.list_bgp_neighbors(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->list_bgp_neighbors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**BgpNeighborListResult**](BgpNeighborListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dad_profiles**
> DADProfileListResult list_dad_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Read All IPV6 DADProfiles

Returns all IPv6 DADProfiles. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Read All IPV6 DADProfiles
    api_response = api_instance.list_dad_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->list_dad_profiles: %s\n" % e)
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

[**DADProfileListResult**](DADProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_prefix_lists**
> IPPrefixListListResult list_ip_prefix_lists(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Paginated List of IPPrefixLists

Paginated List of IPPrefixLists

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Paginated List of IPPrefixLists
    api_response = api_instance.list_ip_prefix_lists(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->list_ip_prefix_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IPPrefixListListResult**](IPPrefixListListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ndra_profiles**
> NDRAProfileListResult list_ndra_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Read All IPV6 NDRA Profiles

Returns all IPv6 NDRA Profiles. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Read All IPV6 NDRA Profiles
    api_response = api_instance.list_ndra_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->list_ndra_profiles: %s\n" % e)
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

[**NDRAProfileListResult**](NDRAProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_route_maps**
> RouteMapListResult list_route_maps(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Paginated List of RouteMaps

Paginated List of RouteMaps

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Paginated List of RouteMaps
    api_response = api_instance.list_route_maps(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->list_route_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**RouteMapListResult**](RouteMapListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_static_routes**
> StaticRouteListResult list_static_routes(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Paginated List of Static Routes

Returns information about configured static routes, including the network address and next hops for each static route. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Paginated List of Static Routes
    api_response = api_instance.list_static_routes(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->list_static_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**StaticRouteListResult**](StaticRouteListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_advertise_rule_list**
> AdvertiseRuleList read_advertise_rule_list(logical_router_id)

Read the Advertisement Rules on a Logical Router

Returns the advertisement rule list for the specified TIER1 logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Read the Advertisement Rules on a Logical Router
    api_response = api_instance.read_advertise_rule_list(logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_advertise_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 

### Return type

[**AdvertiseRuleList**](AdvertiseRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_advertisement_config**
> AdvertisementConfig read_advertisement_config(logical_router_id)

Read the Advertisement Configuration on a Logical Router

Returns information about the routes to be advertised by the specified TIER1 logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Read the Advertisement Configuration on a Logical Router
    api_response = api_instance.read_advertisement_config(logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_advertisement_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 

### Return type

[**AdvertisementConfig**](AdvertisementConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_bgp_community_list**
> BGPCommunityList read_bgp_community_list(logical_router_id, community_list_id)

Read a specific BGP community list from a logical router

Read a specific BGP community list from a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
community_list_id = 'community_list_id_example' # str | 

try:
    # Read a specific BGP community list from a logical router
    api_response = api_instance.read_bgp_community_list(logical_router_id, community_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_bgp_community_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **community_list_id** | **str**|  | 

### Return type

[**BGPCommunityList**](BGPCommunityList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_bgp_config**
> BgpConfig read_bgp_config(logical_router_id)

Read the BGP Configuration on a Logical Router

Returns information about the BGP configuration on a specified logical router. Information includes whether or not the BGP configuration is enabled, the AS number, and whether or not graceful restart is enabled. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Read the BGP Configuration on a Logical Router
    api_response = api_instance.read_bgp_config(logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_bgp_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 

### Return type

[**BgpConfig**](BgpConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_bgp_neighbor**
> BgpNeighbor read_bgp_neighbor(logical_router_id, id)

Read a specific BGP Neighbor on a Logical Router

Read a specific BGP Neighbor on a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Read a specific BGP Neighbor on a Logical Router
    api_response = api_instance.read_bgp_neighbor(logical_router_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_bgp_neighbor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**BgpNeighbor**](BgpNeighbor.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_bgp_neighbor_with_password_show_sensitive_data**
> BgpNeighbor read_bgp_neighbor_with_password_show_sensitive_data(logical_router_id, id)

Read a specific BGP Neighbor with password on a Logical Router

Read a specific BGP Neighbor details with password on a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Read a specific BGP Neighbor with password on a Logical Router
    api_response = api_instance.read_bgp_neighbor_with_password_show_sensitive_data(logical_router_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_bgp_neighbor_with_password_show_sensitive_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**BgpNeighbor**](BgpNeighbor.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_dad_profile**
> DADProfile read_dad_profile(dad_profile_id)

Read specified IPV6 DADProfile

Returns information about specified IPv6 DADProfile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
dad_profile_id = 'dad_profile_id_example' # str | 

try:
    # Read specified IPV6 DADProfile
    api_response = api_instance.read_dad_profile(dad_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_dad_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dad_profile_id** | **str**|  | 

### Return type

[**DADProfile**](DADProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_debug_info_text**
> str read_debug_info_text(logical_router_id)

Read the debug information for the logical router

API to download below information as text which will be used for debugging and troubleshooting. 1) Logical router sub-components and ports. 2) Routing configuration as sent to central control plane. 3) TIER1 advertised network information. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Read the debug information for the logical router
    api_response = api_instance.read_debug_info_text(logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_debug_info_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ip_prefix_list**
> IPPrefixList read_ip_prefix_list(logical_router_id, id)

Get a specific IPPrefixList on a Logical Router

Read a specific IPPrefixList on the specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Get a specific IPPrefixList on a Logical Router
    api_response = api_instance.read_ip_prefix_list(logical_router_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_ip_prefix_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**IPPrefixList**](IPPrefixList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ndra_profile**
> NDRAProfile read_ndra_profile(nd_ra_profile_id)

Read specified IPV6 NDRA Profile

Returns information about specified IPv6 NDRA Profile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
nd_ra_profile_id = 'nd_ra_profile_id_example' # str | 

try:
    # Read specified IPV6 NDRA Profile
    api_response = api_instance.read_ndra_profile(nd_ra_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_ndra_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nd_ra_profile_id** | **str**|  | 

### Return type

[**NDRAProfile**](NDRAProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_redistribution_config**
> RedistributionConfig read_redistribution_config(logical_router_id)

Read the Redistribution Configuration on a Logical Router

Returns information about configured route redistribution for the specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Read the Redistribution Configuration on a Logical Router
    api_response = api_instance.read_redistribution_config(logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_redistribution_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 

### Return type

[**RedistributionConfig**](RedistributionConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_redistribution_rule_list**
> RedistributionRuleList read_redistribution_rule_list(logical_router_id)

Read All the Redistribution Rules on a Logical Router

Returns all the route redistribution rules for the specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Read All the Redistribution Rules on a Logical Router
    api_response = api_instance.read_redistribution_rule_list(logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_redistribution_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 

### Return type

[**RedistributionRuleList**](RedistributionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_route_map**
> RouteMap read_route_map(logical_router_id, id)

Get a specific RouteMap on a Logical Router

Read a specific RouteMap on the specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Get a specific RouteMap on a Logical Router
    api_response = api_instance.read_route_map(logical_router_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_route_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**RouteMap**](RouteMap.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_routing_config**
> RoutingConfig read_routing_config(logical_router_id)

Read the Routing Configuration

Returns the routing configuration for a specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Read the Routing Configuration
    api_response = api_instance.read_routing_config(logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_routing_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 

### Return type

[**RoutingConfig**](RoutingConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_static_route**
> StaticRoute read_static_route(logical_router_id, id)

Get a specific Static Route on a Logical Router

Read a specific static routes on the specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Get a specific Static Route on a Logical Router
    api_response = api_instance.read_static_route(logical_router_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->read_static_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**StaticRoute**](StaticRoute.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_set_password_on_bgp_neighbor**
> BgpNeighbor un_set_password_on_bgp_neighbor(logical_router_id, id, action=action)

Unset/Delete password property on specific BGP Neighbor on Logical Router

Unset/Delete the password property on the specific BGP Neighbor. No other property of the BgpNeighbor can be updated using this API 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 
action = 'action_example' # str |  (optional)

try:
    # Unset/Delete password property on specific BGP Neighbor on Logical Router
    api_response = api_instance.un_set_password_on_bgp_neighbor(logical_router_id, id, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->un_set_password_on_bgp_neighbor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 
 **action** | **str**|  | [optional] 

### Return type

[**BgpNeighbor**](BgpNeighbor.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_advertise_rule_list**
> AdvertiseRuleList update_advertise_rule_list(body, logical_router_id)

Update the Advertisement Rules on a Logical Router

Modifies the advertisement rules on the specified logical router. The PUT request must include all the rules with the networks parameter. Modifiable parameters are networks, display_name, and description. Set the rules list to empty to delete/clear all rules. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdvertiseRuleList() # AdvertiseRuleList | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Update the Advertisement Rules on a Logical Router
    api_response = api_instance.update_advertise_rule_list(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_advertise_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdvertiseRuleList**](AdvertiseRuleList.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**AdvertiseRuleList**](AdvertiseRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_advertisement_config**
> AdvertisementConfig update_advertisement_config(body, logical_router_id)

Update the Advertisement Configuration on a Logical Router

Modifies the route advertisement configuration on the specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdvertisementConfig() # AdvertisementConfig | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Update the Advertisement Configuration on a Logical Router
    api_response = api_instance.update_advertisement_config(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_advertisement_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdvertisementConfig**](AdvertisementConfig.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**AdvertisementConfig**](AdvertisementConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bgp_community_list**
> BGPCommunityList update_bgp_community_list(body, logical_router_id, community_list_id)

Update a specific BGP community list from a logical router

Update a specific BGP community list from a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.BGPCommunityList() # BGPCommunityList | 
logical_router_id = 'logical_router_id_example' # str | 
community_list_id = 'community_list_id_example' # str | 

try:
    # Update a specific BGP community list from a logical router
    api_response = api_instance.update_bgp_community_list(body, logical_router_id, community_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_bgp_community_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BGPCommunityList**](BGPCommunityList.md)|  | 
 **logical_router_id** | **str**|  | 
 **community_list_id** | **str**|  | 

### Return type

[**BGPCommunityList**](BGPCommunityList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bgp_community_list_old**
> BGPCommunityList update_bgp_community_list_old(body, logical_router_id, community_list_id)

Update a specific BGP community list from a logical router

Update a specific BGP community list from a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.BGPCommunityList() # BGPCommunityList | 
logical_router_id = 'logical_router_id_example' # str | 
community_list_id = 'community_list_id_example' # str | 

try:
    # Update a specific BGP community list from a logical router
    api_response = api_instance.update_bgp_community_list_old(body, logical_router_id, community_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_bgp_community_list_old: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BGPCommunityList**](BGPCommunityList.md)|  | 
 **logical_router_id** | **str**|  | 
 **community_list_id** | **str**|  | 

### Return type

[**BGPCommunityList**](BGPCommunityList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bgp_config**
> BgpConfig update_bgp_config(body, logical_router_id)

Update the BGP Configuration on a Logical Router

Modifies the BGP configuration on a specified TIER0 logical router. Modifiable parameters include enabled, graceful_restart, as_number. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.BgpConfig() # BgpConfig | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Update the BGP Configuration on a Logical Router
    api_response = api_instance.update_bgp_config(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_bgp_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BgpConfig**](BgpConfig.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**BgpConfig**](BgpConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bgp_neighbor**
> BgpNeighbor update_bgp_neighbor(body, logical_router_id, id)

Update a specific BGP Neighbor on a Logical Router

Update a specific BGP Neighbor on a Logical Router 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.BgpNeighbor() # BgpNeighbor | 
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Update a specific BGP Neighbor on a Logical Router
    api_response = api_instance.update_bgp_neighbor(body, logical_router_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_bgp_neighbor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BgpNeighbor**](BgpNeighbor.md)|  | 
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**BgpNeighbor**](BgpNeighbor.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dad_profile**
> DADProfile update_dad_profile(body, dad_profile_id)

Update DADProfile

Update DADProfile. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.DADProfile() # DADProfile | 
dad_profile_id = 'dad_profile_id_example' # str | 

try:
    # Update DADProfile
    api_response = api_instance.update_dad_profile(body, dad_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_dad_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DADProfile**](DADProfile.md)|  | 
 **dad_profile_id** | **str**|  | 

### Return type

[**DADProfile**](DADProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_prefix_list**
> IPPrefixList update_ip_prefix_list(body, logical_router_id, id)

Update a specific IPPrefixList on a Logical Router

Update a specific IPPrefixList on the specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPPrefixList() # IPPrefixList | 
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Update a specific IPPrefixList on a Logical Router
    api_response = api_instance.update_ip_prefix_list(body, logical_router_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_ip_prefix_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPPrefixList**](IPPrefixList.md)|  | 
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**IPPrefixList**](IPPrefixList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ndra_profile**
> NDRAProfile update_ndra_profile(body, nd_ra_profile_id)

Update NDRA Profile

Update NDRAProfile 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.NDRAProfile() # NDRAProfile | 
nd_ra_profile_id = 'nd_ra_profile_id_example' # str | 

try:
    # Update NDRA Profile
    api_response = api_instance.update_ndra_profile(body, nd_ra_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_ndra_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NDRAProfile**](NDRAProfile.md)|  | 
 **nd_ra_profile_id** | **str**|  | 

### Return type

[**NDRAProfile**](NDRAProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_redistribution_config**
> RedistributionConfig update_redistribution_config(body, logical_router_id)

Update the Redistribution Configuration on a Logical Router

Modifies existing route redistribution rules for the specified TIER0 logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.RedistributionConfig() # RedistributionConfig | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Update the Redistribution Configuration on a Logical Router
    api_response = api_instance.update_redistribution_config(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_redistribution_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RedistributionConfig**](RedistributionConfig.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**RedistributionConfig**](RedistributionConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_redistribution_rule_list**
> RedistributionRuleList update_redistribution_rule_list(body, logical_router_id)

Update All the Redistribution Rules on a Logical Router

Modifies all route redistribution rules for the specified TIER0 logical router. Set the rules list to empty to delete/clear all rules. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.RedistributionRuleList() # RedistributionRuleList | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Update All the Redistribution Rules on a Logical Router
    api_response = api_instance.update_redistribution_rule_list(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_redistribution_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RedistributionRuleList**](RedistributionRuleList.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**RedistributionRuleList**](RedistributionRuleList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_route_map**
> RouteMap update_route_map(body, logical_router_id, id)

Update a specific RouteMap on a Logical Router

Update a specific RouteMap on the specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.RouteMap() # RouteMap | 
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Update a specific RouteMap on a Logical Router
    api_response = api_instance.update_route_map(body, logical_router_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_route_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RouteMap**](RouteMap.md)|  | 
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**RouteMap**](RouteMap.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_routing_config**
> RoutingConfig update_routing_config(body, logical_router_id)

Update the Routing Configuration

Modifies the routing configuration for a specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoutingConfig() # RoutingConfig | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Update the Routing Configuration
    api_response = api_instance.update_routing_config(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_routing_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoutingConfig**](RoutingConfig.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**RoutingConfig**](RoutingConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_static_route**
> StaticRoute update_static_route(body, logical_router_id, id)

Update a specific Static Route Rule on a Logical Router

Update a specific static route on the specified logical router. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.StaticRoute() # StaticRoute | 
logical_router_id = 'logical_router_id_example' # str | 
id = 'id_example' # str | 

try:
    # Update a specific Static Route Rule on a Logical Router
    api_response = api_instance.update_static_route(body, logical_router_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesRoutingConfigurationApi->update_static_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StaticRoute**](StaticRoute.md)|  | 
 **logical_router_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**StaticRoute**](StaticRoute.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

