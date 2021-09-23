# swagger_client.SystemAdministrationSettingsCertificatesCRLApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_crl_distribution_point**](SystemAdministrationSettingsCertificatesCRLApi.md#create_crl_distribution_point) | **POST** /trust-management/crl-distribution-points | Create a Crl Distribution Point
[**delete_crl_distribution_point**](SystemAdministrationSettingsCertificatesCRLApi.md#delete_crl_distribution_point) | **DELETE** /trust-management/crl-distribution-points/{crl-distribution-point-id} | Delete a CrlDistributionPoint
[**get_crl_distribution_point**](SystemAdministrationSettingsCertificatesCRLApi.md#get_crl_distribution_point) | **GET** /trust-management/crl-distribution-points/{crl-distribution-point-id} | Return the CrlDistributionPoint with &lt;crl-distribution-point-id&gt;
[**get_crl_distribution_point_pem**](SystemAdministrationSettingsCertificatesCRLApi.md#get_crl_distribution_point_pem) | **POST** /trust-management/crl-distribution-points/pem-file | Return stored CRL in PEM format
[**get_crl_distribution_point_status**](SystemAdministrationSettingsCertificatesCRLApi.md#get_crl_distribution_point_status) | **GET** /trust-management/crl-distribution-points/{crl-distribution-point-id}/status | Return the status of the CrlDistributionPoint
[**list_crl_distribution_points**](SystemAdministrationSettingsCertificatesCRLApi.md#list_crl_distribution_points) | **GET** /trust-management/crl-distribution-points | Return the list of CrlDistributionPoints
[**update_crl_distribution_point**](SystemAdministrationSettingsCertificatesCRLApi.md#update_crl_distribution_point) | **PUT** /trust-management/crl-distribution-points/{crl-distribution-point-id} | Update CrlDistributionPoint with &lt;crl-distribution-point-id&gt; This allows updating the ManagedResource fields. 

# **create_crl_distribution_point**
> CrlDistributionPoint create_crl_distribution_point(body)

Create a Crl Distribution Point

Create an entity that will represent a Crl Distribution Point 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCRLApi(swagger_client.ApiClient(configuration))
body = swagger_client.CrlDistributionPoint() # CrlDistributionPoint | 

try:
    # Create a Crl Distribution Point
    api_response = api_instance.create_crl_distribution_point(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCRLApi->create_crl_distribution_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CrlDistributionPoint**](CrlDistributionPoint.md)|  | 

### Return type

[**CrlDistributionPoint**](CrlDistributionPoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_crl_distribution_point**
> delete_crl_distribution_point(crl_distribution_point_id)

Delete a CrlDistributionPoint

Delete a CrlDistributionPoint. It does not delete the actual CRL. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCRLApi(swagger_client.ApiClient(configuration))
crl_distribution_point_id = 'crl_distribution_point_id_example' # str | Unique id of the CrlDistributionPoint to delete

try:
    # Delete a CrlDistributionPoint
    api_instance.delete_crl_distribution_point(crl_distribution_point_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCRLApi->delete_crl_distribution_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crl_distribution_point_id** | **str**| Unique id of the CrlDistributionPoint to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crl_distribution_point**
> CrlDistributionPoint get_crl_distribution_point(crl_distribution_point_id)

Return the CrlDistributionPoint with <crl-distribution-point-id>

Return the CrlDistributionPoint with <crl-distribution-point-id>

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCRLApi(swagger_client.ApiClient(configuration))
crl_distribution_point_id = 'crl_distribution_point_id_example' # str | 

try:
    # Return the CrlDistributionPoint with <crl-distribution-point-id>
    api_response = api_instance.get_crl_distribution_point(crl_distribution_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCRLApi->get_crl_distribution_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crl_distribution_point_id** | **str**|  | 

### Return type

[**CrlDistributionPoint**](CrlDistributionPoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crl_distribution_point_pem**
> str get_crl_distribution_point_pem(body)

Return stored CRL in PEM format

Return stored CRL in PEM format

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCRLApi(swagger_client.ApiClient(configuration))
body = swagger_client.CrlPemRequestType() # CrlPemRequestType | 

try:
    # Return stored CRL in PEM format
    api_response = api_instance.get_crl_distribution_point_pem(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCRLApi->get_crl_distribution_point_pem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CrlPemRequestType**](CrlPemRequestType.md)|  | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crl_distribution_point_status**
> CrlDistributionPointStatus get_crl_distribution_point_status(crl_distribution_point_id)

Return the status of the CrlDistributionPoint

Return the status of the CrlDistributionPoint

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCRLApi(swagger_client.ApiClient(configuration))
crl_distribution_point_id = 'crl_distribution_point_id_example' # str | 

try:
    # Return the status of the CrlDistributionPoint
    api_response = api_instance.get_crl_distribution_point_status(crl_distribution_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCRLApi->get_crl_distribution_point_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crl_distribution_point_id** | **str**|  | 

### Return type

[**CrlDistributionPointStatus**](CrlDistributionPointStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crl_distribution_points**
> CrlDistributionPointList list_crl_distribution_points(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return the list of CrlDistributionPoints

Return the list of CrlDistributionPoints

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCRLApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the list of CrlDistributionPoints
    api_response = api_instance.list_crl_distribution_points(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCRLApi->list_crl_distribution_points: %s\n" % e)
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

[**CrlDistributionPointList**](CrlDistributionPointList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crl_distribution_point**
> CrlDistributionPoint update_crl_distribution_point(body, crl_distribution_point_id)

Update CrlDistributionPoint with <crl-distribution-point-id> This allows updating the ManagedResource fields. 

Update CrlDistributionPoint with <crl-distribution-point-id> This allows updating the ManagedResource fields. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCRLApi(swagger_client.ApiClient(configuration))
body = swagger_client.CrlDistributionPoint() # CrlDistributionPoint | 
crl_distribution_point_id = 'crl_distribution_point_id_example' # str | 

try:
    # Update CrlDistributionPoint with <crl-distribution-point-id> This allows updating the ManagedResource fields. 
    api_response = api_instance.update_crl_distribution_point(body, crl_distribution_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCRLApi->update_crl_distribution_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CrlDistributionPoint**](CrlDistributionPoint.md)|  | 
 **crl_distribution_point_id** | **str**|  | 

### Return type

[**CrlDistributionPoint**](CrlDistributionPoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

