# swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterVirtualIPApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_cluster_virtual_ip_clear_virtual_ip**](SystemAdministrationConfigurationNSXManagersClustersClusterVirtualIPApi.md#clear_cluster_virtual_ip_clear_virtual_ip) | **POST** /cluster/api-virtual-ip?action&#x3D;clear_virtual_ip | Clear cluster virtual IP address
[**get_cluster_virtual_ip**](SystemAdministrationConfigurationNSXManagersClustersClusterVirtualIPApi.md#get_cluster_virtual_ip) | **GET** /cluster/api-virtual-ip | Read cluster virtual IP address
[**set_cluster_virtual_ip_set_virtual_ip**](SystemAdministrationConfigurationNSXManagersClustersClusterVirtualIPApi.md#set_cluster_virtual_ip_set_virtual_ip) | **POST** /cluster/api-virtual-ip?action&#x3D;set_virtual_ip | Set cluster virtual IP address

# **clear_cluster_virtual_ip_clear_virtual_ip**
> ClusterVirtualIpProperties clear_cluster_virtual_ip_clear_virtual_ip()

Clear cluster virtual IP address

Clears the cluster virtual IP address. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterVirtualIPApi(swagger_client.ApiClient(configuration))

try:
    # Clear cluster virtual IP address
    api_response = api_instance.clear_cluster_virtual_ip_clear_virtual_ip()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterVirtualIPApi->clear_cluster_virtual_ip_clear_virtual_ip: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterVirtualIpProperties**](ClusterVirtualIpProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_virtual_ip**
> ClusterVirtualIpProperties get_cluster_virtual_ip()

Read cluster virtual IP address

Returns the configured cluster virtual IP address or null if not configured. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterVirtualIPApi(swagger_client.ApiClient(configuration))

try:
    # Read cluster virtual IP address
    api_response = api_instance.get_cluster_virtual_ip()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterVirtualIPApi->get_cluster_virtual_ip: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterVirtualIpProperties**](ClusterVirtualIpProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cluster_virtual_ip_set_virtual_ip**
> ClusterVirtualIpProperties set_cluster_virtual_ip_set_virtual_ip(ip_address)

Set cluster virtual IP address

Sets the cluster virtual IP address. Note, all nodes in the management cluster must be in the same subnet. If not, a 409 CONFLICT status is returned. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterVirtualIPApi(swagger_client.ApiClient(configuration))
ip_address = 'ip_address_example' # str | Virtual IP address, 0.0.0.0 if not configured

try:
    # Set cluster virtual IP address
    api_response = api_instance.set_cluster_virtual_ip_set_virtual_ip(ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterVirtualIPApi->set_cluster_virtual_ip_set_virtual_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| Virtual IP address, 0.0.0.0 if not configured | 

### Return type

[**ClusterVirtualIpProperties**](ClusterVirtualIpProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

