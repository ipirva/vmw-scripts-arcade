# swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterCertificateApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_cluster_certificate_clear_cluster_certificate**](SystemAdministrationConfigurationNSXManagersClustersClusterCertificateApi.md#clear_cluster_certificate_clear_cluster_certificate) | **POST** /cluster/api-certificate?action&#x3D;clear_cluster_certificate | Clear the cluster certificate
[**get_cluster_certificate_id**](SystemAdministrationConfigurationNSXManagersClustersClusterCertificateApi.md#get_cluster_certificate_id) | **GET** /cluster/api-certificate | Read cluster certificate ID
[**set_cluster_certificate_set_cluster_certificate**](SystemAdministrationConfigurationNSXManagersClustersClusterCertificateApi.md#set_cluster_certificate_set_cluster_certificate) | **POST** /cluster/api-certificate?action&#x3D;set_cluster_certificate | Set the cluster certificate

# **clear_cluster_certificate_clear_cluster_certificate**
> ClusterCertificateId clear_cluster_certificate_clear_cluster_certificate(certificate_id)

Clear the cluster certificate

Clears the certificate used for the MP cluster. This does not affect the certificate itself. This API is deprecated. Instead use the  /api/v1/cluster/api-certificate?action=set_cluster_certificate API to set the cluster certificate to a different one. It just means that from now on, individual certificates will be used on each MP node. This affects all nodes in the cluster. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterCertificateApi(swagger_client.ApiClient(configuration))
certificate_id = 'certificate_id_example' # str | Certificate ID

try:
    # Clear the cluster certificate
    api_response = api_instance.clear_cluster_certificate_clear_cluster_certificate(certificate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterCertificateApi->clear_cluster_certificate_clear_cluster_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| Certificate ID | 

### Return type

[**ClusterCertificateId**](ClusterCertificateId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_certificate_id**
> ClusterCertificateId get_cluster_certificate_id()

Read cluster certificate ID

Returns the ID of the certificate that is used as the cluster certificate for MP 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterCertificateApi(swagger_client.ApiClient(configuration))

try:
    # Read cluster certificate ID
    api_response = api_instance.get_cluster_certificate_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterCertificateApi->get_cluster_certificate_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterCertificateId**](ClusterCertificateId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cluster_certificate_set_cluster_certificate**
> ClusterCertificateId set_cluster_certificate_set_cluster_certificate(certificate_id)

Set the cluster certificate

Sets the certificate used for the MP cluster. This affects all nodes in the cluster. If the certificate used is a CA signed certificate,the request fails if the whole chain(leaf, intermediate, root) is not imported. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterCertificateApi(swagger_client.ApiClient(configuration))
certificate_id = 'certificate_id_example' # str | Certificate ID

try:
    # Set the cluster certificate
    api_response = api_instance.set_cluster_certificate_set_cluster_certificate(certificate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterCertificateApi->set_cluster_certificate_set_cluster_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| Certificate ID | 

### Return type

[**ClusterCertificateId**](ClusterCertificateId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

