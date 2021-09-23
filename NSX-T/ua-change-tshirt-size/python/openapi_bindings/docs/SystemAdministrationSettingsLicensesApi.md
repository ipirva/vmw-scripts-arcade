# swagger_client.SystemAdministrationSettingsLicensesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_eula**](SystemAdministrationSettingsLicensesApi.md#accept_eula) | **POST** /eula/accept | Accept end user license agreement 
[**create_license**](SystemAdministrationSettingsLicensesApi.md#create_license) | **POST** /licenses | Add a new license key
[**delete_license**](SystemAdministrationSettingsLicensesApi.md#delete_license) | **DELETE** /licenses/{license-key} | Deprecated. Remove a license identified by the license-key
[**delete_license_key_delete**](SystemAdministrationSettingsLicensesApi.md#delete_license_key_delete) | **POST** /licenses?action&#x3D;delete | Remove a license
[**get_eula_acceptance**](SystemAdministrationSettingsLicensesApi.md#get_eula_acceptance) | **GET** /eula/acceptance | Return the acceptance status of end user license agreement 
[**get_eula_content**](SystemAdministrationSettingsLicensesApi.md#get_eula_content) | **GET** /eula/content | Return the content of end user license agreement 
[**get_license**](SystemAdministrationSettingsLicensesApi.md#get_license) | **GET** /license | Deprecated. Return the Enterprise License 
[**get_license_by_key**](SystemAdministrationSettingsLicensesApi.md#get_license_by_key) | **GET** /licenses/{license-key} | Deprecated. Get license properties for license identified by the license-key
[**get_license_usage_report**](SystemAdministrationSettingsLicensesApi.md#get_license_usage_report) | **GET** /licenses/licenses-usage | Get usage report of all registered modules
[**get_license_usage_report_in_csv_format_csv**](SystemAdministrationSettingsLicensesApi.md#get_license_usage_report_in_csv_format_csv) | **GET** /licenses/licenses-usage?format&#x3D;csv | Get usage report of all registred modules in CSV format
[**get_licenses**](SystemAdministrationSettingsLicensesApi.md#get_licenses) | **GET** /licenses | Get all licenses
[**update_license**](SystemAdministrationSettingsLicensesApi.md#update_license) | **PUT** /license | Deprecated. Assign an Updated Enterprise License Key 

# **accept_eula**
> accept_eula()

Accept end user license agreement 

Accept end user license agreement 

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
api_instance = swagger_client.SystemAdministrationSettingsLicensesApi(swagger_client.ApiClient(configuration))

try:
    # Accept end user license agreement 
    api_instance.accept_eula()
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsLicensesApi->accept_eula: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_license**
> License create_license(body)

Add a new license key

This will add a license key to the system. The API supports adding only one license key for each license edition type - Standard, Advanced or Enterprise. If a new license key is tried to add for an edition for which the license key already exists, then this API will return an error. 

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
api_instance = swagger_client.SystemAdministrationSettingsLicensesApi(swagger_client.ApiClient(configuration))
body = swagger_client.License() # License | 

try:
    # Add a new license key
    api_response = api_instance.create_license(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsLicensesApi->create_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**License**](License.md)|  | 

### Return type

[**License**](License.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_license**
> delete_license(license_key)

Deprecated. Remove a license identified by the license-key

Deprecated. Use POST /licenses?action=delete API instead. 

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
api_instance = swagger_client.SystemAdministrationSettingsLicensesApi(swagger_client.ApiClient(configuration))
license_key = 'license_key_example' # str | 

try:
    # Deprecated. Remove a license identified by the license-key
    api_instance.delete_license(license_key)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsLicensesApi->delete_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_license_key_delete**
> delete_license_key_delete(body)

Remove a license

This will delete the license key identified in the request body by \"license_key\" and its properties from the system. Attempting to delete the last license key will result in an error. 

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
api_instance = swagger_client.SystemAdministrationSettingsLicensesApi(swagger_client.ApiClient(configuration))
body = swagger_client.License() # License | 

try:
    # Remove a license
    api_instance.delete_license_key_delete(body)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsLicensesApi->delete_license_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**License**](License.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eula_acceptance**
> EULAAcceptance get_eula_acceptance()

Return the acceptance status of end user license agreement 

Return the acceptance status of end user license agreement 

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
api_instance = swagger_client.SystemAdministrationSettingsLicensesApi(swagger_client.ApiClient(configuration))

try:
    # Return the acceptance status of end user license agreement 
    api_response = api_instance.get_eula_acceptance()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsLicensesApi->get_eula_acceptance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EULAAcceptance**](EULAAcceptance.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eula_content**
> EULAContent get_eula_content(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, value_format=value_format)

Return the content of end user license agreement 

Return the content of end user license agreement in the specified format. By default, it's pure string without line break 

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
api_instance = swagger_client.SystemAdministrationSettingsLicensesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
value_format = 'value_format_example' # str | End User License Agreement content output format (optional)

try:
    # Return the content of end user license agreement 
    api_response = api_instance.get_eula_content(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, value_format=value_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsLicensesApi->get_eula_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **value_format** | **str**| End User License Agreement content output format | [optional] 

### Return type

[**EULAContent**](EULAContent.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license**
> License get_license()

Deprecated. Return the Enterprise License 

Deprecated. Use the GET /licenses API instead. 

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
api_instance = swagger_client.SystemAdministrationSettingsLicensesApi(swagger_client.ApiClient(configuration))

try:
    # Deprecated. Return the Enterprise License 
    api_response = api_instance.get_license()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsLicensesApi->get_license: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**License**](License.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_by_key**
> License get_license_by_key(license_key)

Deprecated. Get license properties for license identified by the license-key

Deprecated. Use GET /licenses API instead.

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
api_instance = swagger_client.SystemAdministrationSettingsLicensesApi(swagger_client.ApiClient(configuration))
license_key = 'license_key_example' # str | 

try:
    # Deprecated. Get license properties for license identified by the license-key
    api_response = api_instance.get_license_by_key(license_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsLicensesApi->get_license_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_key** | **str**|  | 

### Return type

[**License**](License.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_usage_report**
> FeatureUsageList get_license_usage_report()

Get usage report of all registered modules

Returns usage report of all registered modules 

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
api_instance = swagger_client.SystemAdministrationSettingsLicensesApi(swagger_client.ApiClient(configuration))

try:
    # Get usage report of all registered modules
    api_response = api_instance.get_license_usage_report()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsLicensesApi->get_license_usage_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FeatureUsageList**](FeatureUsageList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_usage_report_in_csv_format_csv**
> FeatureUsageListInCsvFormat get_license_usage_report_in_csv_format_csv()

Get usage report of all registred modules in CSV format

Returns usage report of all registered modules in CSV format 

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
api_instance = swagger_client.SystemAdministrationSettingsLicensesApi(swagger_client.ApiClient(configuration))

try:
    # Get usage report of all registred modules in CSV format
    api_response = api_instance.get_license_usage_report_in_csv_format_csv()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsLicensesApi->get_license_usage_report_in_csv_format_csv: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FeatureUsageListInCsvFormat**](FeatureUsageListInCsvFormat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_licenses**
> LicensesListResult get_licenses()

Get all licenses

Returns all licenses. 

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
api_instance = swagger_client.SystemAdministrationSettingsLicensesApi(swagger_client.ApiClient(configuration))

try:
    # Get all licenses
    api_response = api_instance.get_licenses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsLicensesApi->get_licenses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LicensesListResult**](LicensesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license**
> License update_license(body)

Deprecated. Assign an Updated Enterprise License Key 

Deprecated. Use the POST /licenses API instead 

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
api_instance = swagger_client.SystemAdministrationSettingsLicensesApi(swagger_client.ApiClient(configuration))
body = swagger_client.License() # License | 

try:
    # Deprecated. Assign an Updated Enterprise License Key 
    api_response = api_instance.update_license(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsLicensesApi->update_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**License**](License.md)|  | 

### Return type

[**License**](License.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

