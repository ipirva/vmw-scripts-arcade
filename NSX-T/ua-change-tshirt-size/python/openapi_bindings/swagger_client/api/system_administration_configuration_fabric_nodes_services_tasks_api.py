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


class SystemAdministrationConfigurationFabricNodesServicesTasksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_appliance_management_task_cancel(self, task_id, **kwargs):  # noqa: E501
        """Cancel specified task  # noqa: E501

        Cancel specified task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_appliance_management_task_cancel(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_id: ID of task to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_appliance_management_task_cancel_with_http_info(task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_appliance_management_task_cancel_with_http_info(task_id, **kwargs)  # noqa: E501
            return data

    def cancel_appliance_management_task_cancel_with_http_info(self, task_id, **kwargs):  # noqa: E501
        """Cancel specified task  # noqa: E501

        Cancel specified task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_appliance_management_task_cancel_with_http_info(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_id: ID of task to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_appliance_management_task_cancel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `cancel_appliance_management_task_cancel`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in params:
            path_params['task-id'] = params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/node/tasks/{task-id}?action=cancel', 'POST',
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

    def delete_appliance_management_task(self, task_id, **kwargs):  # noqa: E501
        """Delete task  # noqa: E501

        Delete task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_appliance_management_task(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_id: ID of task to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_appliance_management_task_with_http_info(task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_appliance_management_task_with_http_info(task_id, **kwargs)  # noqa: E501
            return data

    def delete_appliance_management_task_with_http_info(self, task_id, **kwargs):  # noqa: E501
        """Delete task  # noqa: E501

        Delete task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_appliance_management_task_with_http_info(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_id: ID of task to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_appliance_management_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `delete_appliance_management_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in params:
            path_params['task-id'] = params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/node/tasks/{task-id}', 'DELETE',
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

    def list_appliance_management_tasks(self, **kwargs):  # noqa: E501
        """List appliance management tasks  # noqa: E501

        List appliance management tasks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_appliance_management_tasks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fields: Fields to include in query results
        :param str request_method: Request method(s) to include in query result
        :param str request_path: Request URI path(s) to include in query result
        :param str request_uri: Request URI(s) to include in query result
        :param str status: Status(es) to include in query result
        :param str user: Names of users to include in query result
        :return: ApplianceManagementTaskListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_appliance_management_tasks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_appliance_management_tasks_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_appliance_management_tasks_with_http_info(self, **kwargs):  # noqa: E501
        """List appliance management tasks  # noqa: E501

        List appliance management tasks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_appliance_management_tasks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fields: Fields to include in query results
        :param str request_method: Request method(s) to include in query result
        :param str request_path: Request URI path(s) to include in query result
        :param str request_uri: Request URI(s) to include in query result
        :param str status: Status(es) to include in query result
        :param str user: Names of users to include in query result
        :return: ApplianceManagementTaskListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'request_method', 'request_path', 'request_uri', 'status', 'user']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_appliance_management_tasks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'request_method' in params:
            query_params.append(('request_method', params['request_method']))  # noqa: E501
        if 'request_path' in params:
            query_params.append(('request_path', params['request_path']))  # noqa: E501
        if 'request_uri' in params:
            query_params.append(('request_uri', params['request_uri']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'user' in params:
            query_params.append(('user', params['user']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/node/tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplianceManagementTaskListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_appliance_management_task_properties(self, task_id, **kwargs):  # noqa: E501
        """Read task properties  # noqa: E501

        Read task properties  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_appliance_management_task_properties(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_id: ID of task to read (required)
        :param bool suppress_redirect: Suppress redirect status if applicable
        :return: ApplianceManagementTaskProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_appliance_management_task_properties_with_http_info(task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_appliance_management_task_properties_with_http_info(task_id, **kwargs)  # noqa: E501
            return data

    def read_appliance_management_task_properties_with_http_info(self, task_id, **kwargs):  # noqa: E501
        """Read task properties  # noqa: E501

        Read task properties  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_appliance_management_task_properties_with_http_info(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_id: ID of task to read (required)
        :param bool suppress_redirect: Suppress redirect status if applicable
        :return: ApplianceManagementTaskProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id', 'suppress_redirect']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_appliance_management_task_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `read_appliance_management_task_properties`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in params:
            path_params['task-id'] = params['task_id']  # noqa: E501

        query_params = []
        if 'suppress_redirect' in params:
            query_params.append(('suppress_redirect', params['suppress_redirect']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/node/tasks/{task-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplianceManagementTaskProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_async_appliance_management_task_response(self, task_id, **kwargs):  # noqa: E501
        """Read asynchronous task response  # noqa: E501

        Read asynchronous task response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_async_appliance_management_task_response(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_id: ID of task to read (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_async_appliance_management_task_response_with_http_info(task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_async_appliance_management_task_response_with_http_info(task_id, **kwargs)  # noqa: E501
            return data

    def read_async_appliance_management_task_response_with_http_info(self, task_id, **kwargs):  # noqa: E501
        """Read asynchronous task response  # noqa: E501

        Read asynchronous task response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_async_appliance_management_task_response_with_http_info(task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_id: ID of task to read (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_async_appliance_management_task_response" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `read_async_appliance_management_task_response`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in params:
            path_params['task-id'] = params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/node/tasks/{task-id}/response', 'GET',
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
