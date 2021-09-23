# swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagerRabbitmqConfigurationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_rabbit_mq_management_port**](SystemAdministrationConfigurationNSXManagersNodesManagerRabbitmqConfigurationApi.md#check_rabbit_mq_management_port) | **GET** /node/rabbitmq-management-port | Check if RabbitMQ management port is enabled or not
[**d_elete_rabbit_mq_management_port**](SystemAdministrationConfigurationNSXManagersNodesManagerRabbitmqConfigurationApi.md#d_elete_rabbit_mq_management_port) | **DELETE** /node/rabbitmq-management-port | Delete RabbitMQ management port
[**set_rabbit_mq_management_port**](SystemAdministrationConfigurationNSXManagersNodesManagerRabbitmqConfigurationApi.md#set_rabbit_mq_management_port) | **POST** /node/rabbitmq-management-port | Set RabbitMQ management port

# **check_rabbit_mq_management_port**
> PortStatus check_rabbit_mq_management_port()

Check if RabbitMQ management port is enabled or not

Returns status as true if RabbitMQ management port is enabled else false

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagerRabbitmqConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Check if RabbitMQ management port is enabled or not
    api_response = api_instance.check_rabbit_mq_management_port()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesManagerRabbitmqConfigurationApi->check_rabbit_mq_management_port: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PortStatus**](PortStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_elete_rabbit_mq_management_port**
> d_elete_rabbit_mq_management_port()

Delete RabbitMQ management port

Delete RabbitMQ management port

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagerRabbitmqConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Delete RabbitMQ management port
    api_instance.d_elete_rabbit_mq_management_port()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesManagerRabbitmqConfigurationApi->d_elete_rabbit_mq_management_port: %s\n" % e)
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

# **set_rabbit_mq_management_port**
> set_rabbit_mq_management_port()

Set RabbitMQ management port

Set RabbitMQ management port

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagerRabbitmqConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Set RabbitMQ management port
    api_instance.set_rabbit_mq_management_port()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesManagerRabbitmqConfigurationApi->set_rabbit_mq_management_port: %s\n" % e)
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

