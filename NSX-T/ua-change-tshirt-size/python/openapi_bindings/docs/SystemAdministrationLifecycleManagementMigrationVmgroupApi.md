# swagger_client.SystemAdministrationLifecycleManagementMigrationVmgroupApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_vm_group_migrate_post_migrate**](SystemAdministrationLifecycleManagementMigrationVmgroupApi.md#post_vm_group_migrate_post_migrate) | **POST** /migration/vmgroup?action&#x3D;post_migrate | Perform steps required after migrating a VM group.
[**pre_vm_group_migrate_pre_migrate**](SystemAdministrationLifecycleManagementMigrationVmgroupApi.md#pre_vm_group_migrate_pre_migrate) | **POST** /migration/vmgroup?action&#x3D;pre_migrate | Perform steps required before migrating a VM group.

# **post_vm_group_migrate_post_migrate**
> post_vm_group_migrate_post_migrate(body)

Perform steps required after migrating a VM group.

For each VM group, the following three high level steps are performed in sequence. 1. Call pre VM group migrate API. 2. Migrate (by vmotion,in place, etc.,) VMs in the VM group. This step will be done by user independent of MC. 3. Call post VM group migrate API with the same VM group id used in the pre VM group migrate API. This API specifically deals with post VM group migrate API. When post VM group migrate API is invoked for a VM group id, MC performs following actions.  - Add security tags on the VMs migrated. For the VMs mentioned in the failed VM instance uuids, this operation is    skipped. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationVmgroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostVmGroupMigrationSpec() # PostVmGroupMigrationSpec | 

try:
    # Perform steps required after migrating a VM group.
    api_instance.post_vm_group_migrate_post_migrate(body)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationVmgroupApi->post_vm_group_migrate_post_migrate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostVmGroupMigrationSpec**](PostVmGroupMigrationSpec.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_vm_group_migrate_pre_migrate**
> pre_vm_group_migrate_pre_migrate(body)

Perform steps required before migrating a VM group.

For each VM group, the following three high level steps are performed in sequence. 1. Call pre VM group migrate API. 2. Migrate (by vmotion,in place, etc.,) VMs in the VM group. This step will be done by user independent of MC. 3. Call post VM group migrate API with the same VM group id used in the pre VM group migrate API. This API specifically deals with pre VM group migrate API. When pre VM group migrate API is invoked for a VM group id, MC performs following actions.  - Checks segmentation realization state.  - Creates segment ports.  - Creates temporary security groups. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationVmgroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.PreVmGroupMigrationSpec() # PreVmGroupMigrationSpec | 

try:
    # Perform steps required before migrating a VM group.
    api_instance.pre_vm_group_migrate_pre_migrate(body)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationVmgroupApi->pre_vm_group_migrate_pre_migrate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PreVmGroupMigrationSpec**](PreVmGroupMigrationSpec.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

