# swagger_client.ManagementPlaneAPIGroupingObjectsNSProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ip_set**](ManagementPlaneAPIGroupingObjectsNSProfilesApi.md#create_ip_set) | **POST** /ip-sets | Create IPSet
[**delete_ns_profile**](ManagementPlaneAPIGroupingObjectsNSProfilesApi.md#delete_ns_profile) | **DELETE** /ns-profiles/{ns-profile-id} | Delete NSProfile
[**list_ns_profiles**](ManagementPlaneAPIGroupingObjectsNSProfilesApi.md#list_ns_profiles) | **GET** /ns-profiles | List NSProfiles
[**list_ns_supported_attributes**](ManagementPlaneAPIGroupingObjectsNSProfilesApi.md#list_ns_supported_attributes) | **GET** /ns-profiles/attributes | List NSProfile supported attribute and sub-attributes
[**list_ns_supported_attributes_types**](ManagementPlaneAPIGroupingObjectsNSProfilesApi.md#list_ns_supported_attributes_types) | **GET** /ns-profiles/attribute-types | List NSProfile supported attribute types
[**read_ns_profile**](ManagementPlaneAPIGroupingObjectsNSProfilesApi.md#read_ns_profile) | **GET** /ns-profiles/{ns-profile-id} | Read NSProfile
[**update_ns_profile**](ManagementPlaneAPIGroupingObjectsNSProfilesApi.md#update_ns_profile) | **PUT** /ns-profiles/{ns-profile-id} | Update NSProfile

# **create_ip_set**
> IPSet create_ip_set(body)

Create IPSet

Creates a new IPSet that can group either IPv4 or IPv6 individual ip addresses, ranges or subnets. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSet() # IPSet | 

try:
    # Create IPSet
    api_response = api_instance.create_ip_set(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSProfilesApi->create_ip_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSet**](IPSet.md)|  | 

### Return type

[**IPSet**](IPSet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ns_profile**
> delete_ns_profile(ns_profile_id, force=force)

Delete NSProfile

Deletes the specified NSProfile. By default, if the NSProfile is consumed in a Firewall rule, it won't get deleted. In such situations, pass \"force=true\" as query param to force delete the NSProfile. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSProfilesApi(swagger_client.ApiClient(configuration))
ns_profile_id = 'ns_profile_id_example' # str | NSProfile Id
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete NSProfile
    api_instance.delete_ns_profile(ns_profile_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSProfilesApi->delete_ns_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_profile_id** | **str**| NSProfile Id | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ns_profiles**
> NSProfileListResult list_ns_profiles(attribute_type=attribute_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List NSProfiles

List the NSProfiles created in a paginated format.The page size is restricted to 50 NSProfiles, so that the size of the response remains small even when there are high number of NSProfiles with multiple attributes and multiple attribute values for each attribute. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSProfilesApi(swagger_client.ApiClient(configuration))
attribute_type = 'attribute_type_example' # str | Fetch NSProfiles for the given attribute type (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List NSProfiles
    api_response = api_instance.list_ns_profiles(attribute_type=attribute_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSProfilesApi->list_ns_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type** | **str**| Fetch NSProfiles for the given attribute type | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**NSProfileListResult**](NSProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ns_supported_attributes**
> NSSupportedAttributesListResult list_ns_supported_attributes(attribute_source=attribute_source, attribute_type=attribute_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List NSProfile supported attribute and sub-attributes

Returns supported attribute and sub-attributes for specified attribute type with their supported values, if provided in query/request parameter, else will fetch all supported attribute and sub-attributes for all supported attribute types. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSProfilesApi(swagger_client.ApiClient(configuration))
attribute_source = 'attribute_source_example' # str | Fetch attributes source (optional)
attribute_type = 'attribute_type_example' # str | Fetch attributes and sub-attributes for the given attribute type (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List NSProfile supported attribute and sub-attributes
    api_response = api_instance.list_ns_supported_attributes(attribute_source=attribute_source, attribute_type=attribute_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSProfilesApi->list_ns_supported_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_source** | **str**| Fetch attributes source | [optional] 
 **attribute_type** | **str**| Fetch attributes and sub-attributes for the given attribute type | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**NSSupportedAttributesListResult**](NSSupportedAttributesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ns_supported_attributes_types**
> NSSupportedAttributeTypesResult list_ns_supported_attributes_types()

List NSProfile supported attribute types

Returns supported attribute type strings for NSProfile. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSProfilesApi(swagger_client.ApiClient(configuration))

try:
    # List NSProfile supported attribute types
    api_response = api_instance.list_ns_supported_attributes_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSProfilesApi->list_ns_supported_attributes_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NSSupportedAttributeTypesResult**](NSSupportedAttributeTypesResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ns_profile**
> NSProfile read_ns_profile(ns_profile_id)

Read NSProfile

Returns information about the specified NSProfile. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSProfilesApi(swagger_client.ApiClient(configuration))
ns_profile_id = 'ns_profile_id_example' # str | NSProfile Id

try:
    # Read NSProfile
    api_response = api_instance.read_ns_profile(ns_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSProfilesApi->read_ns_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_profile_id** | **str**| NSProfile Id | 

### Return type

[**NSProfile**](NSProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ns_profile**
> NSProfile update_ns_profile(body, ns_profile_id)

Update NSProfile

Updates the specified NSProfile. Rules for using attributes and sub-attributes in single NSProfile 1. One type of attribute can't have multiple occurrences. ( Example -  Attribute type APP_ID can be used only once per NSProfile.) 2. Values for an attribute are mentioned as array of strings.  ( Example - For type APP_ID , values can be mentioned as [\"SSL\",\"FTP\"].) 3. If sub-attribtes are mentioned for an attribute, then only single  value is allowed for that attribute. 4. To get a list of supported  attributes and sub-attributes fire the following REST API  GET https://&lt;nsx-mgr&gt;/api/v1/ns-profiles/attributes 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.NSProfile() # NSProfile | 
ns_profile_id = 'ns_profile_id_example' # str | NSProfile Id

try:
    # Update NSProfile
    api_response = api_instance.update_ns_profile(body, ns_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSProfilesApi->update_ns_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NSProfile**](NSProfile.md)|  | 
 **ns_profile_id** | **str**| NSProfile Id | 

### Return type

[**NSProfile**](NSProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

