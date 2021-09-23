# swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_oidc_end_point**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#add_oidc_end_point) | **POST** /trust-management/oidc-uris | Add an OpenID Connect end-point.
[**delete_principal_identity**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#delete_principal_identity) | **DELETE** /trust-management/principal-identities/{principal-identity-id} | Delete a principal identity
[**delete_token_based_principal_identity**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#delete_token_based_principal_identity) | **DELETE** /trust-management/token-principal-identities/{principal-identity-id} | Delete a token-based principal identity
[**get_oidc_end_point**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#get_oidc_end_point) | **GET** /trust-management/oidc-uris/{id} | Get an OpenID Connect end-point.
[**get_principal_identities**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#get_principal_identities) | **GET** /trust-management/principal-identities | Return the list of principal identities
[**get_principal_identity**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#get_principal_identity) | **GET** /trust-management/principal-identities/{principal-identity-id} | Get a principal identity
[**get_token_based_principal_identity**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#get_token_based_principal_identity) | **GET** /trust-management/token-principal-identities/{principal-identity-id} | Get a token-based principal identity
[**list_oidc_end_points**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#list_oidc_end_points) | **GET** /trust-management/oidc-uris | Return the list of OpenID Connect end-points.
[**list_token_based_principal_identities**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#list_token_based_principal_identities) | **GET** /trust-management/token-principal-identities | Return the list of token-based principal identities. | These don&#x27;t have certificate or role information.
[**register_principal_identity**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#register_principal_identity) | **POST** /trust-management/principal-identities | Register a name-certificate combination.
[**register_principal_identity_with_certificate**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#register_principal_identity_with_certificate) | **POST** /trust-management/principal-identities/with-certificate | Register a name-certificate combination.
[**register_token_based_principal_identity**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#register_token_based_principal_identity) | **POST** /trust-management/token-principal-identities | Register a token-based principal identity.
[**update_oidc_end_point_thumbprint_update_thumbprint**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#update_oidc_end_point_thumbprint_update_thumbprint) | **POST** /trust-management/oidc-uris?action&#x3D;update_thumbprint | Update a OpenID Connect end-point&#x27;s thumbprint
[**update_principal_identity_certificate_update_certificate**](SystemAdministrationSettingsUserManagementPrincipalIdentityApi.md#update_principal_identity_certificate_update_certificate) | **POST** /trust-management/principal-identities?action&#x3D;update_certificate | Update a principal identity&#x27;s certificate

# **add_oidc_end_point**
> OidcEndPoint add_oidc_end_point(body)

Add an OpenID Connect end-point.

This request also fetches the issuer and jwks_uri meta-data from the OIDC end-point and stores it. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
body = swagger_client.OidcEndPoint() # OidcEndPoint | 

try:
    # Add an OpenID Connect end-point.
    api_response = api_instance.add_oidc_end_point(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->add_oidc_end_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OidcEndPoint**](OidcEndPoint.md)|  | 

### Return type

[**OidcEndPoint**](OidcEndPoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_principal_identity**
> delete_principal_identity(principal_identity_id)

Delete a principal identity

Delete a principal identity. It does not delete the certificate. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
principal_identity_id = 'principal_identity_id_example' # str | Unique id of the principal identity to delete

try:
    # Delete a principal identity
    api_instance.delete_principal_identity(principal_identity_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->delete_principal_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_identity_id** | **str**| Unique id of the principal identity to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_based_principal_identity**
> delete_token_based_principal_identity(principal_identity_id)

Delete a token-based principal identity

Delete a token-based principal identity. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
principal_identity_id = 'principal_identity_id_example' # str | Unique id of the token-based principal identity to delete

try:
    # Delete a token-based principal identity
    api_instance.delete_token_based_principal_identity(principal_identity_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->delete_token_based_principal_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_identity_id** | **str**| Unique id of the token-based principal identity to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oidc_end_point**
> OidcEndPoint get_oidc_end_point(id, refresh=refresh)

Get an OpenID Connect end-point.

When ?refresh=true is added to the request, the meta-data is newly fetched from the OIDC end-point. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
refresh = false # bool | Refresh meta-data (optional) (default to false)

try:
    # Get an OpenID Connect end-point.
    api_response = api_instance.get_oidc_end_point(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->get_oidc_end_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **refresh** | **bool**| Refresh meta-data | [optional] [default to false]

### Return type

[**OidcEndPoint**](OidcEndPoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_principal_identities**
> PrincipalIdentityList get_principal_identities()

Return the list of principal identities

Returns the list of principals registered with a certificate.

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))

try:
    # Return the list of principal identities
    api_response = api_instance.get_principal_identities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->get_principal_identities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PrincipalIdentityList**](PrincipalIdentityList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_principal_identity**
> PrincipalIdentity get_principal_identity(principal_identity_id)

Get a principal identity

Get a stored principal identity 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
principal_identity_id = 'principal_identity_id_example' # str | ID of the principal identity to get

try:
    # Get a principal identity
    api_response = api_instance.get_principal_identity(principal_identity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->get_principal_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_identity_id** | **str**| ID of the principal identity to get | 

### Return type

[**PrincipalIdentity**](PrincipalIdentity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_based_principal_identity**
> TokenBasedPrincipalIdentity get_token_based_principal_identity(principal_identity_id)

Get a token-based principal identity

Get a stored token-based principal identity 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
principal_identity_id = 'principal_identity_id_example' # str | ID of the principal identity to get

try:
    # Get a token-based principal identity
    api_response = api_instance.get_token_based_principal_identity(principal_identity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->get_token_based_principal_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_identity_id** | **str**| ID of the principal identity to get | 

### Return type

[**TokenBasedPrincipalIdentity**](TokenBasedPrincipalIdentity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_oidc_end_points**
> OidcEndPointListResult list_oidc_end_points()

Return the list of OpenID Connect end-points.

Return the list of OpenID Connect end-points.

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))

try:
    # Return the list of OpenID Connect end-points.
    api_response = api_instance.list_oidc_end_points()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->list_oidc_end_points: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OidcEndPointListResult**](OidcEndPointListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_token_based_principal_identities**
> TokenBasedPrincipalIdentityListResult list_token_based_principal_identities()

Return the list of token-based principal identities. | These don't have certificate or role information.

Return the list of token-based principal identities. | These don't have certificate or role information.

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))

try:
    # Return the list of token-based principal identities. | These don't have certificate or role information.
    api_response = api_instance.list_token_based_principal_identities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->list_token_based_principal_identities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenBasedPrincipalIdentityListResult**](TokenBasedPrincipalIdentityListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_principal_identity**
> PrincipalIdentity register_principal_identity(body)

Register a name-certificate combination.

Associates a principal's name with a certificate that is used to authenticate. The combination name and node_id needs to be unique across token-based and certificate-based principal identities. Deprecated, use POST /trust-management/principal-identities/with-certificate instead. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
body = swagger_client.PrincipalIdentity() # PrincipalIdentity | 

try:
    # Register a name-certificate combination.
    api_response = api_instance.register_principal_identity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->register_principal_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrincipalIdentity**](PrincipalIdentity.md)|  | 

### Return type

[**PrincipalIdentity**](PrincipalIdentity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_principal_identity_with_certificate**
> PrincipalIdentity register_principal_identity_with_certificate(body)

Register a name-certificate combination.

Create a principal identity with a new, unused, certificate. The combination name and node_id needs to be unique across token-based and certificate-based principal identities. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
body = swagger_client.PrincipalIdentityWithCertificate() # PrincipalIdentityWithCertificate | 

try:
    # Register a name-certificate combination.
    api_response = api_instance.register_principal_identity_with_certificate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->register_principal_identity_with_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrincipalIdentityWithCertificate**](PrincipalIdentityWithCertificate.md)|  | 

### Return type

[**PrincipalIdentity**](PrincipalIdentity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_token_based_principal_identity**
> TokenBasedPrincipalIdentity register_token_based_principal_identity(body)

Register a token-based principal identity.

Register a principal identity that is going to be authenticated through a token. The combination name and node_id needs to be unique across token-based and certificate-based principal identities. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
body = swagger_client.TokenBasedPrincipalIdentity() # TokenBasedPrincipalIdentity | 

try:
    # Register a token-based principal identity.
    api_response = api_instance.register_token_based_principal_identity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->register_token_based_principal_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenBasedPrincipalIdentity**](TokenBasedPrincipalIdentity.md)|  | 

### Return type

[**TokenBasedPrincipalIdentity**](TokenBasedPrincipalIdentity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_oidc_end_point_thumbprint_update_thumbprint**
> OidcEndPoint update_oidc_end_point_thumbprint_update_thumbprint(body)

Update a OpenID Connect end-point's thumbprint

Update a OpenID Connect end-point's thumbprint used to connect to the oidc_uri through SSL 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateOidcEndPointThumbprintRequest() # UpdateOidcEndPointThumbprintRequest | 

try:
    # Update a OpenID Connect end-point's thumbprint
    api_response = api_instance.update_oidc_end_point_thumbprint_update_thumbprint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->update_oidc_end_point_thumbprint_update_thumbprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOidcEndPointThumbprintRequest**](UpdateOidcEndPointThumbprintRequest.md)|  | 

### Return type

[**OidcEndPoint**](OidcEndPoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_principal_identity_certificate_update_certificate**
> PrincipalIdentity update_principal_identity_certificate_update_certificate(body)

Update a principal identity's certificate

Update a principal identity's certificate 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementPrincipalIdentityApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdatePrincipalIdentityCertificateRequest() # UpdatePrincipalIdentityCertificateRequest | 

try:
    # Update a principal identity's certificate
    api_response = api_instance.update_principal_identity_certificate_update_certificate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementPrincipalIdentityApi->update_principal_identity_certificate_update_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePrincipalIdentityCertificateRequest**](UpdatePrincipalIdentityCertificateRequest.md)|  | 

### Return type

[**PrincipalIdentity**](PrincipalIdentity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

