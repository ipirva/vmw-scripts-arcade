# coding: utf-8

"""
    NSX-T Manager API

    VMware NSX-T Manager REST API  # noqa: E501

    OpenAPI spec version: 3.1.0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SystemAdministrationLifecycleManagementMigrationVmgroupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_vm_group_migrate_post_migrate(self, body, **kwargs):  # noqa: E501
        """Perform steps required after migrating a VM group.  # noqa: E501

        For each VM group, the following three high level steps are performed in sequence. 1. Call pre VM group migrate API. 2. Migrate (by vmotion,in place, etc.,) VMs in the VM group. This step will be done by user independent of MC. 3. Call post VM group migrate API with the same VM group id used in the pre VM group migrate API. This API specifically deals with post VM group migrate API. When post VM group migrate API is invoked for a VM group id, MC performs following actions.  - Add security tags on the VMs migrated. For the VMs mentioned in the failed VM instance uuids, this operation is    skipped.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_vm_group_migrate_post_migrate(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostVmGroupMigrationSpec body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_vm_group_migrate_post_migrate_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_vm_group_migrate_post_migrate_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_vm_group_migrate_post_migrate_with_http_info(self, body, **kwargs):  # noqa: E501
        """Perform steps required after migrating a VM group.  # noqa: E501

        For each VM group, the following three high level steps are performed in sequence. 1. Call pre VM group migrate API. 2. Migrate (by vmotion,in place, etc.,) VMs in the VM group. This step will be done by user independent of MC. 3. Call post VM group migrate API with the same VM group id used in the pre VM group migrate API. This API specifically deals with post VM group migrate API. When post VM group migrate API is invoked for a VM group id, MC performs following actions.  - Add security tags on the VMs migrated. For the VMs mentioned in the failed VM instance uuids, this operation is    skipped.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_vm_group_migrate_post_migrate_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostVmGroupMigrationSpec body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_vm_group_migrate_post_migrate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_vm_group_migrate_post_migrate`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/migration/vmgroup?action=post_migrate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pre_vm_group_migrate_pre_migrate(self, body, **kwargs):  # noqa: E501
        """Perform steps required before migrating a VM group.  # noqa: E501

        For each VM group, the following three high level steps are performed in sequence. 1. Call pre VM group migrate API. 2. Migrate (by vmotion,in place, etc.,) VMs in the VM group. This step will be done by user independent of MC. 3. Call post VM group migrate API with the same VM group id used in the pre VM group migrate API. This API specifically deals with pre VM group migrate API. When pre VM group migrate API is invoked for a VM group id, MC performs following actions.  - Checks segmentation realization state.  - Creates segment ports.  - Creates temporary security groups.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pre_vm_group_migrate_pre_migrate(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PreVmGroupMigrationSpec body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pre_vm_group_migrate_pre_migrate_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.pre_vm_group_migrate_pre_migrate_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def pre_vm_group_migrate_pre_migrate_with_http_info(self, body, **kwargs):  # noqa: E501
        """Perform steps required before migrating a VM group.  # noqa: E501

        For each VM group, the following three high level steps are performed in sequence. 1. Call pre VM group migrate API. 2. Migrate (by vmotion,in place, etc.,) VMs in the VM group. This step will be done by user independent of MC. 3. Call post VM group migrate API with the same VM group id used in the pre VM group migrate API. This API specifically deals with pre VM group migrate API. When pre VM group migrate API is invoked for a VM group id, MC performs following actions.  - Checks segmentation realization state.  - Creates segment ports.  - Creates temporary security groups.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pre_vm_group_migrate_pre_migrate_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PreVmGroupMigrationSpec body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pre_vm_group_migrate_pre_migrate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `pre_vm_group_migrate_pre_migrate`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/migration/vmgroup?action=pre_migrate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
