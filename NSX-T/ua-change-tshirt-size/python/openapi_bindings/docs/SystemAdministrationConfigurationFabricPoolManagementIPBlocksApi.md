# swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_or_release_from_ip_block_subnet**](SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi.md#allocate_or_release_from_ip_block_subnet) | **POST** /pools/ip-subnets/{subnet-id} | Allocate or Release an IP Address from a Ip Subnet
[**create_ip_block**](SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi.md#create_ip_block) | **POST** /pools/ip-blocks | Create a new IP address block.
[**create_ip_block_subnet**](SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi.md#create_ip_block_subnet) | **POST** /pools/ip-subnets | Create subnet of specified size within an IP block
[**delete_ip_block**](SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi.md#delete_ip_block) | **DELETE** /pools/ip-blocks/{block-id} | Delete an IP Address Block
[**delete_ip_block_subnet**](SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi.md#delete_ip_block_subnet) | **DELETE** /pools/ip-subnets/{subnet-id} | Delete subnet within an IP block
[**list_ip_block_subnets**](SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi.md#list_ip_block_subnets) | **GET** /pools/ip-subnets | List subnets within an IP block
[**list_ip_blocks**](SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi.md#list_ip_blocks) | **GET** /pools/ip-blocks | Returns list of configured IP address blocks.
[**read_ip_block**](SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi.md#read_ip_block) | **GET** /pools/ip-blocks/{block-id} | Get IP address block information.
[**read_ip_block_subnet**](SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi.md#read_ip_block_subnet) | **GET** /pools/ip-subnets/{subnet-id} | Get the subnet within an IP block
[**update_ip_block**](SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi.md#update_ip_block) | **PUT** /pools/ip-blocks/{block-id} | Update an IP Address Block

# **allocate_or_release_from_ip_block_subnet**
> AllocationIpAddress allocate_or_release_from_ip_block_subnet(body, action, subnet_id)

Allocate or Release an IP Address from a Ip Subnet

Allocates or releases an IP address from the specified IP subnet. To allocate an address, include ?action=ALLOCATE in the request and a \"{}\" in the request body. When the request is successful, the response is \"allocation_id\": \"<ip-address>\", where <ip-address> is an IP address from the specified pool. To release an IP address (return it back to the pool), include ?action=RELEASE in the request and \"allocation_id\":<ip-address> in the request body, where <ip-address> is the address to be released. When the request is successful, the response is NULL. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi(swagger_client.ApiClient(configuration))
body = swagger_client.AllocationIpAddress() # AllocationIpAddress | 
action = 'action_example' # str | Specifies allocate or release action
subnet_id = 'subnet_id_example' # str | IP subnet id

try:
    # Allocate or Release an IP Address from a Ip Subnet
    api_response = api_instance.allocate_or_release_from_ip_block_subnet(body, action, subnet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi->allocate_or_release_from_ip_block_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AllocationIpAddress**](AllocationIpAddress.md)|  | 
 **action** | **str**| Specifies allocate or release action | 
 **subnet_id** | **str**| IP subnet id | 

### Return type

[**AllocationIpAddress**](AllocationIpAddress.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ip_block**
> IpBlock create_ip_block(body)

Create a new IP address block.

Creates a new IPv4 address block using the specified cidr. cidr is a required parameter. display_name & description are optional parameters 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpBlock() # IpBlock | 

try:
    # Create a new IP address block.
    api_response = api_instance.create_ip_block(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi->create_ip_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpBlock**](IpBlock.md)|  | 

### Return type

[**IpBlock**](IpBlock.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ip_block_subnet**
> IpBlockSubnet create_ip_block_subnet(body)

Create subnet of specified size within an IP block

Carves out a subnet of requested size from the specified IP block. The \"size\" parameter  and the \"block_id \" are the requireds field while invoking this API. If the IP block has sufficient resources/space to allocate a subnet of specified size, the response will contain all the details of the newly created subnet including the display_name, description, cidr & allocation_ranges. Returns a conflict error if the IP block does not have enough resources/space to allocate a subnet of the requested size. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpBlockSubnet() # IpBlockSubnet | 

try:
    # Create subnet of specified size within an IP block
    api_response = api_instance.create_ip_block_subnet(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi->create_ip_block_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpBlockSubnet**](IpBlockSubnet.md)|  | 

### Return type

[**IpBlockSubnet**](IpBlockSubnet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_block**
> delete_ip_block(block_id)

Delete an IP Address Block

Deletes the IP address block with specified id if it exists. IP block cannot be deleted if there are allocated subnets from the block. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi(swagger_client.ApiClient(configuration))
block_id = 'block_id_example' # str | IP address block id

try:
    # Delete an IP Address Block
    api_instance.delete_ip_block(block_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi->delete_ip_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| IP address block id | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_block_subnet**
> delete_ip_block_subnet(subnet_id)

Delete subnet within an IP block

Deletes a subnet with specified id within a given IP address block. Deletion is allowed only when there are no allocated IP addresses from that subnet. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi(swagger_client.ApiClient(configuration))
subnet_id = 'subnet_id_example' # str | Subnet id

try:
    # Delete subnet within an IP block
    api_instance.delete_ip_block_subnet(subnet_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi->delete_ip_block_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet_id** | **str**| Subnet id | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_block_subnets**
> IpBlockSubnetListResult list_ip_block_subnets(block_id=block_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List subnets within an IP block

Returns information about all subnets present within an IP address block. Information includes subnet's id, display_name, description, cidr and allocation ranges. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi(swagger_client.ApiClient(configuration))
block_id = 'block_id_example' # str |  (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List subnets within an IP block
    api_response = api_instance.list_ip_block_subnets(block_id=block_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi->list_ip_block_subnets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**|  | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IpBlockSubnetListResult**](IpBlockSubnetListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_blocks**
> IpBlockListResult list_ip_blocks(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Returns list of configured IP address blocks.

Returns information about configured IP address blocks. Information includes the id, display name, description & CIDR of IP address blocks 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Returns list of configured IP address blocks.
    api_response = api_instance.list_ip_blocks(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi->list_ip_blocks: %s\n" % e)
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

[**IpBlockListResult**](IpBlockListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ip_block**
> IpBlock read_ip_block(block_id)

Get IP address block information.

Returns information about the IP address block with specified id. Information includes id, display_name, description & cidr. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi(swagger_client.ApiClient(configuration))
block_id = 'block_id_example' # str | IP address block id

try:
    # Get IP address block information.
    api_response = api_instance.read_ip_block(block_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi->read_ip_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **str**| IP address block id | 

### Return type

[**IpBlock**](IpBlock.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ip_block_subnet**
> IpBlockSubnet read_ip_block_subnet(subnet_id)

Get the subnet within an IP block

Returns information about the subnet with specified id within a given IP address block. Information includes display_name, description, cidr and allocation_ranges. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi(swagger_client.ApiClient(configuration))
subnet_id = 'subnet_id_example' # str | Subnet id

try:
    # Get the subnet within an IP block
    api_response = api_instance.read_ip_block_subnet(subnet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi->read_ip_block_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet_id** | **str**| Subnet id | 

### Return type

[**IpBlockSubnet**](IpBlockSubnet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_block**
> IpBlock update_ip_block(body, block_id)

Update an IP Address Block

Modifies the IP address block with specifed id. display_name, description and cidr are parameters that can be modified. If a new cidr is specified, it should contain all existing subnets in the IP block. Returns a conflict error if the IP address block cidr can not be modified due to the presence of subnets that it contains. Eg: If the IP block contains a subnet 192.168.0.1/24 and we try to change the IP block cidr to 10.1.0.1/16, it results in a conflict. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpBlock() # IpBlock | 
block_id = 'block_id_example' # str | IP address block id

try:
    # Update an IP Address Block
    api_response = api_instance.update_ip_block(body, block_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPBlocksApi->update_ip_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpBlock**](IpBlock.md)|  | 
 **block_id** | **str**| IP address block id | 

### Return type

[**IpBlock**](IpBlock.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

