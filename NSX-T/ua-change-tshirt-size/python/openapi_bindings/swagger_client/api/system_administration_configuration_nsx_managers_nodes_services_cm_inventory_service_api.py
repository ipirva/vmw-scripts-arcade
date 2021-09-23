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


class SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_cminventory_service_action_restart(self, **kwargs):  # noqa: E501
        """Restart, start or stop the manager service  # noqa: E501

        Restart, start or stop the manager service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cminventory_service_action_restart(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeServiceStatusProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_cminventory_service_action_restart_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_cminventory_service_action_restart_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_cminventory_service_action_restart_with_http_info(self, **kwargs):  # noqa: E501
        """Restart, start or stop the manager service  # noqa: E501

        Restart, start or stop the manager service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cminventory_service_action_restart_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeServiceStatusProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_cminventory_service_action_restart" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/node/services/cm-inventory?action=restart', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeServiceStatusProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_cminventory_service_action_start(self, **kwargs):  # noqa: E501
        """Restart, start or stop the manager service  # noqa: E501

        Restart, start or stop the manager service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cminventory_service_action_start(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeServiceStatusProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_cminventory_service_action_start_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_cminventory_service_action_start_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_cminventory_service_action_start_with_http_info(self, **kwargs):  # noqa: E501
        """Restart, start or stop the manager service  # noqa: E501

        Restart, start or stop the manager service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cminventory_service_action_start_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeServiceStatusProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_cminventory_service_action_start" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/node/services/cm-inventory?action=start', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeServiceStatusProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_cminventory_service_action_stop(self, **kwargs):  # noqa: E501
        """Restart, start or stop the manager service  # noqa: E501

        Restart, start or stop the manager service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cminventory_service_action_stop(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeServiceStatusProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_cminventory_service_action_stop_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_cminventory_service_action_stop_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_cminventory_service_action_stop_with_http_info(self, **kwargs):  # noqa: E501
        """Restart, start or stop the manager service  # noqa: E501

        Restart, start or stop the manager service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cminventory_service_action_stop_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeServiceStatusProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_cminventory_service_action_stop" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/node/services/cm-inventory?action=stop', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeServiceStatusProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_cminventory_service(self, **kwargs):  # noqa: E501
        """Read cm inventory service properties  # noqa: E501

        Read cm inventory service properties  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_cminventory_service(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeServiceProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_cminventory_service_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.read_cminventory_service_with_http_info(**kwargs)  # noqa: E501
            return data

    def read_cminventory_service_with_http_info(self, **kwargs):  # noqa: E501
        """Read cm inventory service properties  # noqa: E501

        Read cm inventory service properties  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_cminventory_service_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeServiceProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_cminventory_service" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/node/services/cm-inventory', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeServiceProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_cminventory_service_status(self, **kwargs):  # noqa: E501
        """Read manager service status  # noqa: E501

        Read manager service status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_cminventory_service_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeServiceStatusProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_cminventory_service_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.read_cminventory_service_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def read_cminventory_service_status_with_http_info(self, **kwargs):  # noqa: E501
        """Read manager service status  # noqa: E501

        Read manager service status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_cminventory_service_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeServiceStatusProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_cminventory_service_status" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/node/services/cm-inventory/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeServiceStatusProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
