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


class SystemAdministrationConfigurationFabricNodesLogsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_node_logs(self, **kwargs):  # noqa: E501
        """List available node logs  # noqa: E501

        Returns the number of log files and lists the log files that reside on the NSX virtual appliance. The list includes the filename, file size, and last-modified time in milliseconds since epoch (1 January 1970) for each log file. Knowing the last-modified time with millisecond accuracy since epoch is helpful when you are comparing two times, such as the time of a POST request and the end time on a server.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_node_logs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeLogPropertiesListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_node_logs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_node_logs_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_node_logs_with_http_info(self, **kwargs):  # noqa: E501
        """List available node logs  # noqa: E501

        Returns the number of log files and lists the log files that reside on the NSX virtual appliance. The list includes the filename, file size, and last-modified time in milliseconds since epoch (1 January 1970) for each log file. Knowing the last-modified time with millisecond accuracy since epoch is helpful when you are comparing two times, such as the time of a POST request and the end time on a server.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_node_logs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeLogPropertiesListResult
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
                    " to method list_node_logs" % key
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
            '/node/logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeLogPropertiesListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_node_log(self, log_name, **kwargs):  # noqa: E501
        """Read node log properties  # noqa: E501

        For a single specified log file, lists the filename, file size, and last-modified time.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_node_log(log_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str log_name: Name of log file to read properties (required)
        :return: NodeLogProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_node_log_with_http_info(log_name, **kwargs)  # noqa: E501
        else:
            (data) = self.read_node_log_with_http_info(log_name, **kwargs)  # noqa: E501
            return data

    def read_node_log_with_http_info(self, log_name, **kwargs):  # noqa: E501
        """Read node log properties  # noqa: E501

        For a single specified log file, lists the filename, file size, and last-modified time.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_node_log_with_http_info(log_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str log_name: Name of log file to read properties (required)
        :return: NodeLogProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['log_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_node_log" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'log_name' is set
        if ('log_name' not in params or
                params['log_name'] is None):
            raise ValueError("Missing the required parameter `log_name` when calling `read_node_log`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'log_name' in params:
            path_params['log-name'] = params['log_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/node/logs/{log-name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeLogProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_node_log_data(self, log_name, **kwargs):  # noqa: E501
        """Read node log contents  # noqa: E501

        For a single specified log file, returns the content of the log file. This method supports byte-range requests. To request just a portion of a log file, supply an HTTP Range header, e.g. \"Range: bytes=<start>-<end>\". <end> is optional, and, if omitted, the file contents from start to the end of the file are returned.'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_node_log_data(log_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str log_name: Name of log to read (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_node_log_data_with_http_info(log_name, **kwargs)  # noqa: E501
        else:
            (data) = self.read_node_log_data_with_http_info(log_name, **kwargs)  # noqa: E501
            return data

    def read_node_log_data_with_http_info(self, log_name, **kwargs):  # noqa: E501
        """Read node log contents  # noqa: E501

        For a single specified log file, returns the content of the log file. This method supports byte-range requests. To request just a portion of a log file, supply an HTTP Range header, e.g. \"Range: bytes=<start>-<end>\". <end> is optional, and, if omitted, the file contents from start to the end of the file are returned.'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_node_log_data_with_http_info(log_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str log_name: Name of log to read (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['log_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_node_log_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'log_name' is set
        if ('log_name' not in params or
                params['log_name'] is None):
            raise ValueError("Missing the required parameter `log_name` when calling `read_node_log_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'log_name' in params:
            path_params['log-name'] = params['log_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/node/logs/{log-name}/data', 'GET',
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
