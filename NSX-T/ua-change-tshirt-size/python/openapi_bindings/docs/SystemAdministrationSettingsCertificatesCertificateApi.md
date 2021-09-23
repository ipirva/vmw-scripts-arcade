# swagger_client.SystemAdministrationSettingsCertificatesCertificateApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_certificate_import**](SystemAdministrationSettingsCertificatesCertificateApi.md#add_certificate_import) | **POST** /trust-management/certificates?action&#x3D;import | Add a New Certificate
[**delete_certificate**](SystemAdministrationSettingsCertificatesCertificateApi.md#delete_certificate) | **DELETE** /trust-management/certificates/{cert-id} | Delete Certificate for the Given Certificate ID
[**get_certificate**](SystemAdministrationSettingsCertificatesCertificateApi.md#get_certificate) | **GET** /trust-management/certificates/{cert-id} | Show Certificate Data for the Given Certificate ID
[**get_certificate_profile**](SystemAdministrationSettingsCertificatesCertificateApi.md#get_certificate_profile) | **GET** /trust-management/certificate-profile/{service-type} | Get the certificate profile for the given service type
[**get_certificates**](SystemAdministrationSettingsCertificatesCertificateApi.md#get_certificates) | **GET** /trust-management/certificates | Return All the User-Facing Components&#x27; Certificates
[**list_certificate_profiles**](SystemAdministrationSettingsCertificatesCertificateApi.md#list_certificate_profiles) | **GET** /trust-management/certificate-profiles | Return the list of certificate profiles. |

# **add_certificate_import**
> CertificateList add_certificate_import(body)

Add a New Certificate

Adds a new private-public certificate or a chain of certificates (CAs) and, optionally, a private key that can be applied to one of the user-facing components (appliance management or edge). The certificate and the key should be stored in PEM format. If no private key is provided, the certificate is used as a client certificate in the trust store. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCertificateApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrustObjectData() # TrustObjectData | 

try:
    # Add a New Certificate
    api_response = api_instance.add_certificate_import(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCertificateApi->add_certificate_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrustObjectData**](TrustObjectData.md)|  | 

### Return type

[**CertificateList**](CertificateList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificate**
> delete_certificate(cert_id)

Delete Certificate for the Given Certificate ID

Removes the specified certificate. The private key associated with the certificate is also deleted. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCertificateApi(swagger_client.ApiClient(configuration))
cert_id = 'cert_id_example' # str | ID of certificate to delete

try:
    # Delete Certificate for the Given Certificate ID
    api_instance.delete_certificate(cert_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCertificateApi->delete_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| ID of certificate to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate**
> Certificate get_certificate(cert_id, details=details)

Show Certificate Data for the Given Certificate ID

Returns information for the specified certificate ID, including the certificate's UUID; resource_type (for example, certificate_self_signed, certificate_ca, or certificate_signed); pem_encoded data; and history of the certificate (who created or modified it and when). For additional information, include the ?details=true modifier at the end of the request URI. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCertificateApi(swagger_client.ApiClient(configuration))
cert_id = 'cert_id_example' # str | ID of certificate to read
details = false # bool | whether to expand the pem data and show all its details (optional) (default to false)

try:
    # Show Certificate Data for the Given Certificate ID
    api_response = api_instance.get_certificate(cert_id, details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCertificateApi->get_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| ID of certificate to read | 
 **details** | **bool**| whether to expand the pem data and show all its details | [optional] [default to false]

### Return type

[**Certificate**](Certificate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_profile**
> CertificateProfile get_certificate_profile(service_type)

Get the certificate profile for the given service type

Get an available certificate profile 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCertificateApi(swagger_client.ApiClient(configuration))
service_type = 'service_type_example' # str | Unique Service Type of the Certificate Profile

try:
    # Get the certificate profile for the given service type
    api_response = api_instance.get_certificate_profile(service_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCertificateApi->get_certificate_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_type** | **str**| Unique Service Type of the Certificate Profile | 

### Return type

[**CertificateProfile**](CertificateProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificates**
> CertificateList get_certificates(cursor=cursor, details=details, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)

Return All the User-Facing Components' Certificates

Returns all certificate information viewable by the user, including each certificate's UUID; resource_type (for example, certificate_self_signed, certificate_ca, or certificate_signed); pem_encoded data; and history of the certificate (who created or modified it and when). For additional information, include the ?details=true modifier at the end of the request URI. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCertificateApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
details = false # bool | whether to expand the pem data and show all its details (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
type = 'type_example' # str | Type of certificate to return (optional)

try:
    # Return All the User-Facing Components' Certificates
    api_response = api_instance.get_certificates(cursor=cursor, details=details, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCertificateApi->get_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **details** | **bool**| whether to expand the pem data and show all its details | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **type** | **str**| Type of certificate to return | [optional] 

### Return type

[**CertificateList**](CertificateList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificate_profiles**
> CertificateProfileListResult list_certificate_profiles()

Return the list of certificate profiles. |

Return the list of certificate profiles. |

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCertificateApi(swagger_client.ApiClient(configuration))

try:
    # Return the list of certificate profiles. |
    api_response = api_instance.list_certificate_profiles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCertificateApi->list_certificate_profiles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CertificateProfileListResult**](CertificateProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

