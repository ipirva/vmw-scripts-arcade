# swagger_client.DefaultApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_certificate_apply_certificate**](DefaultApi.md#apply_certificate_apply_certificate) | **POST** /trust-management/certificates/{cert-id}?action&#x3D;apply_certificate | Apply a certificate for a CertificateProfile
[**set_principal_identity_certificate_for_federation_set_pi_certificate_for_federation**](DefaultApi.md#set_principal_identity_certificate_for_federation_set_pi_certificate_for_federation) | **POST** /trust-management/certificates?action&#x3D;set_pi_certificate_for_federation | Set a certificate as a GM or LM Principal Identity certificate
[**validate_certificate_validate**](DefaultApi.md#validate_certificate_validate) | **GET** /trust-management/certificates/{cert-id}?action&#x3D;validate | Validate a certificate

# **apply_certificate_apply_certificate**
> apply_certificate_apply_certificate(cert_id, service_type, node_id=node_id)

Apply a certificate for a CertificateProfile

Look up the Certificate Profile matching the service-type and apply the certificate. When the Certificate Profile has cluster_certificate=false, the node_id parameter is required to designate the node where the certificate needs to be applied. 

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
cert_id = 'cert_id_example' # str | ID of certificate to apply
service_type = 'service_type_example' # str | Supported service types, that are using certificates.
node_id = 'node_id_example' # str | Node Id (optional)

try:
    # Apply a certificate for a CertificateProfile
    api_instance.apply_certificate_apply_certificate(cert_id, service_type, node_id=node_id)
except ApiException as e:
    print("Exception when calling DefaultApi->apply_certificate_apply_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| ID of certificate to apply | 
 **service_type** | **str**| Supported service types, that are using certificates. | 
 **node_id** | **str**| Node Id | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_principal_identity_certificate_for_federation_set_pi_certificate_for_federation**
> set_principal_identity_certificate_for_federation_set_pi_certificate_for_federation(body)

Set a certificate as a GM or LM Principal Identity certificate

Set a certificate that has been imported to be either the principal identity certificate for the local cluster with either GM or LM service type. Currently, the service type specified must match the current service type of the local cluster. 

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetPrincipalIdentityCertificateForFederationRequest() # SetPrincipalIdentityCertificateForFederationRequest | 

try:
    # Set a certificate as a GM or LM Principal Identity certificate
    api_instance.set_principal_identity_certificate_for_federation_set_pi_certificate_for_federation(body)
except ApiException as e:
    print("Exception when calling DefaultApi->set_principal_identity_certificate_for_federation_set_pi_certificate_for_federation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetPrincipalIdentityCertificateForFederationRequest**](SetPrincipalIdentityCertificateForFederationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_certificate_validate**
> CertificateCheckingStatus validate_certificate_validate(cert_id, usage=usage)

Validate a certificate

Checks whether certificate is valid. When the certificate contains a chain, the full chain is validated. The usage parameter can be SERVER (default) or CLIENT. This indicates whether the certificate needs to be validated as a server-auth or a client-auth certificate. 

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
cert_id = 'cert_id_example' # str | ID of certificate to validate
usage = 'usage_example' # str | Usage Type of the Certificate, SERVER or CLIENT. Default is SERVER (optional)

try:
    # Validate a certificate
    api_response = api_instance.validate_certificate_validate(cert_id, usage=usage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->validate_certificate_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| ID of certificate to validate | 
 **usage** | **str**| Usage Type of the Certificate, SERVER or CLIENT. Default is SERVER | [optional] 

### Return type

[**CertificateCheckingStatus**](CertificateCheckingStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

