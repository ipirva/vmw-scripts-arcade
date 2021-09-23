# swagger_client.SystemAdministrationSettingsCertificatesCSRApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_crl_import**](SystemAdministrationSettingsCertificatesCSRApi.md#add_crl_import) | **POST** /trust-management/crls?action&#x3D;import | Add a New Certificate Revocation List
[**delete_crl**](SystemAdministrationSettingsCertificatesCSRApi.md#delete_crl) | **DELETE** /trust-management/crls/{crl-id} | Delete a CRL
[**delete_csr**](SystemAdministrationSettingsCertificatesCSRApi.md#delete_csr) | **DELETE** /trust-management/csrs/{csr-id} | Delete a CSR
[**generate_csr**](SystemAdministrationSettingsCertificatesCSRApi.md#generate_csr) | **POST** /trust-management/csrs | Generate a New Certificate Signing Request
[**get_crl**](SystemAdministrationSettingsCertificatesCSRApi.md#get_crl) | **GET** /trust-management/crls/{crl-id} | Show CRL Data for the Given CRL ID
[**get_crls**](SystemAdministrationSettingsCertificatesCSRApi.md#get_crls) | **GET** /trust-management/crls | Return All Added CRLs
[**get_csr**](SystemAdministrationSettingsCertificatesCSRApi.md#get_csr) | **GET** /trust-management/csrs/{csr-id} | Show CSR Data for the Given CSR ID
[**get_csr_pem**](SystemAdministrationSettingsCertificatesCSRApi.md#get_csr_pem) | **GET** /trust-management/csrs/{csr-id}/pem-file | Get CSR PEM File for the Given CSR ID
[**get_csrs**](SystemAdministrationSettingsCertificatesCSRApi.md#get_csrs) | **GET** /trust-management/csrs | Return All the Generated CSRs
[**get_trust_objects**](SystemAdministrationSettingsCertificatesCSRApi.md#get_trust_objects) | **GET** /trust-management | Return the Properties of a Trust Manager
[**import_certificate_import**](SystemAdministrationSettingsCertificatesCSRApi.md#import_certificate_import) | **POST** /trust-management/csrs/{csr-id}?action&#x3D;import | Import a Certificate Associated with an Approved CSR
[**self_sign_certificate_self_sign**](SystemAdministrationSettingsCertificatesCSRApi.md#self_sign_certificate_self_sign) | **POST** /trust-management/csrs/{csr-id}?action&#x3D;self_sign | Self-Sign the CSR
[**update_crl**](SystemAdministrationSettingsCertificatesCSRApi.md#update_crl) | **PUT** /trust-management/crls/{crl-id} | Update CRL for the Given CRL ID

# **add_crl_import**
> CrlList add_crl_import(body)

Add a New Certificate Revocation List

Adds a new certificate revocation list (CRL). The CRL is used to verify the client certificate status against the revocation lists published by the CA. For this reason, the administrator needs to add the CRL in certificate repository as well. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))
body = swagger_client.CrlObjectData() # CrlObjectData | 

try:
    # Add a New Certificate Revocation List
    api_response = api_instance.add_crl_import(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->add_crl_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CrlObjectData**](CrlObjectData.md)|  | 

### Return type

[**CrlList**](CrlList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_crl**
> delete_crl(crl_id)

Delete a CRL

Deletes an existing CRL.

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))
crl_id = 'crl_id_example' # str | ID of CRL to delete

try:
    # Delete a CRL
    api_instance.delete_crl(crl_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->delete_crl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crl_id** | **str**| ID of CRL to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_csr**
> delete_csr(csr_id)

Delete a CSR

Removes a specified CSR. If a CSR is not used for verification, you can delete it. Note that the CSR import and upload POST actions automatically delete the associated CSR. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))
csr_id = 'csr_id_example' # str | ID of CSR to delete

try:
    # Delete a CSR
    api_instance.delete_csr(csr_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->delete_csr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csr_id** | **str**| ID of CSR to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_csr**
> Csr generate_csr(body)

Generate a New Certificate Signing Request

Creates a new certificate signing request (CSR). A CSR is encrypted text that contains information about your organization (organization name, country, and so on) and your Web server's public key, which is a public certificate the is generated on the server that can be used to forward this request to a certificate authority (CA). A private key is also usually created at the same time as the CSR. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))
body = swagger_client.Csr() # Csr | 

try:
    # Generate a New Certificate Signing Request
    api_response = api_instance.generate_csr(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->generate_csr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Csr**](Csr.md)|  | 

### Return type

[**Csr**](Csr.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crl**
> Crl get_crl(crl_id, details=details)

Show CRL Data for the Given CRL ID

Returns information about the specified CRL. For additional information, include the ?details=true modifier at the end of the request URI. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))
crl_id = 'crl_id_example' # str | ID of CRL to read
details = false # bool | whether to expand the pem data and show all its details (optional) (default to false)

try:
    # Show CRL Data for the Given CRL ID
    api_response = api_instance.get_crl(crl_id, details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->get_crl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crl_id** | **str**| ID of CRL to read | 
 **details** | **bool**| whether to expand the pem data and show all its details | [optional] [default to false]

### Return type

[**Crl**](Crl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crls**
> CrlList get_crls(cursor=cursor, details=details, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)

Return All Added CRLs

Returns information about all CRLs. For additional information, include the ?details=true modifier at the end of the request URI. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
details = false # bool | whether to expand the pem data and show all its details (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
type = 'type_example' # str | Type of certificate to return (optional)

try:
    # Return All Added CRLs
    api_response = api_instance.get_crls(cursor=cursor, details=details, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->get_crls: %s\n" % e)
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

[**CrlList**](CrlList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csr**
> Csr get_csr(csr_id)

Show CSR Data for the Given CSR ID

Returns information about the specified CSR.

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))
csr_id = 'csr_id_example' # str | ID of CSR to read

try:
    # Show CSR Data for the Given CSR ID
    api_response = api_instance.get_csr(csr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->get_csr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csr_id** | **str**| ID of CSR to read | 

### Return type

[**Csr**](Csr.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csr_pem**
> str get_csr_pem(csr_id)

Get CSR PEM File for the Given CSR ID

Downloads the CSR PEM file for a specified CSR. Clients must include an Accept: text/plain request header.

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))
csr_id = 'csr_id_example' # str | ID of CSR to read

try:
    # Get CSR PEM File for the Given CSR ID
    api_response = api_instance.get_csr_pem(csr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->get_csr_pem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csr_id** | **str**| ID of CSR to read | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csrs**
> CsrList get_csrs(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return All the Generated CSRs

Returns information about all of the CSRs that have been created.

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return All the Generated CSRs
    api_response = api_instance.get_csrs(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->get_csrs: %s\n" % e)
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

[**CsrList**](CsrList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trust_objects**
> TrustManagementData get_trust_objects()

Return the Properties of a Trust Manager

Returns information about the supported algorithms and key sizes.

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))

try:
    # Return the Properties of a Trust Manager
    api_response = api_instance.get_trust_objects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->get_trust_objects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TrustManagementData**](TrustManagementData.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_certificate_import**
> CertificateList import_certificate_import(body, csr_id)

Import a Certificate Associated with an Approved CSR

Imports a certificate authority (CA)-signed certificate for a CSR. This action links the certificate to the private key created by the CSR. The pem_encoded string in the request body is the signed certificate provided by your CA in response to the CSR that you provide to them. The import POST action automatically deletes the associated CSR. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrustObjectData() # TrustObjectData | 
csr_id = 'csr_id_example' # str | CSR this certificate is associated with

try:
    # Import a Certificate Associated with an Approved CSR
    api_response = api_instance.import_certificate_import(body, csr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->import_certificate_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrustObjectData**](TrustObjectData.md)|  | 
 **csr_id** | **str**| CSR this certificate is associated with | 

### Return type

[**CertificateList**](CertificateList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **self_sign_certificate_self_sign**
> Certificate self_sign_certificate_self_sign(csr_id, days_valid)

Self-Sign the CSR

Self-signs the previously generated CSR. This action is similar to the import certificate action, but instead of using a public certificate signed by a CA, the self_sign POST action uses a certificate that is signed with NSX's own private key. For validity, if a value greater than 825 days is provided, it will be set to 825 days. 

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))
csr_id = 'csr_id_example' # str | CSR this certificate is associated with
days_valid = 825 # int | Number of days the certificate will be valid, default 825 days (default to 825)

try:
    # Self-Sign the CSR
    api_response = api_instance.self_sign_certificate_self_sign(csr_id, days_valid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->self_sign_certificate_self_sign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csr_id** | **str**| CSR this certificate is associated with | 
 **days_valid** | **int**| Number of days the certificate will be valid, default 825 days | [default to 825]

### Return type

[**Certificate**](Certificate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crl**
> Crl update_crl(body, crl_id)

Update CRL for the Given CRL ID

Updates an existing CRL.

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
api_instance = swagger_client.SystemAdministrationSettingsCertificatesCSRApi(swagger_client.ApiClient(configuration))
body = swagger_client.Crl() # Crl | 
crl_id = 'crl_id_example' # str | ID of CRL to update

try:
    # Update CRL for the Given CRL ID
    api_response = api_instance.update_crl(body, crl_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCertificatesCSRApi->update_crl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Crl**](Crl.md)|  | 
 **crl_id** | **str**| ID of CRL to update | 

### Return type

[**Crl**](Crl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

