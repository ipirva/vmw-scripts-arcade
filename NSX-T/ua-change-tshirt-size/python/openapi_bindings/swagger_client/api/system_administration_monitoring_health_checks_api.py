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


class SystemAdministrationMonitoringHealthChecksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_automatic_health_check(self, transport_zone_id, **kwargs):  # noqa: E501
        """Get an automatic health check  # noqa: E501

        Get health check performed by system automatically for specific transport zone.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_automatic_health_check(transport_zone_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transport_zone_id: (required)
        :return: AutomaticHealthCheck
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_automatic_health_check_with_http_info(transport_zone_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_automatic_health_check_with_http_info(transport_zone_id, **kwargs)  # noqa: E501
            return data

    def get_automatic_health_check_with_http_info(self, transport_zone_id, **kwargs):  # noqa: E501
        """Get an automatic health check  # noqa: E501

        Get health check performed by system automatically for specific transport zone.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_automatic_health_check_with_http_info(transport_zone_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transport_zone_id: (required)
        :return: AutomaticHealthCheck
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transport_zone_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_automatic_health_check" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transport_zone_id' is set
        if ('transport_zone_id' not in params or
                params['transport_zone_id'] is None):
            raise ValueError("Missing the required parameter `transport_zone_id` when calling `get_automatic_health_check`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transport_zone_id' in params:
            path_params['transport-zone-id'] = params['transport_zone_id']  # noqa: E501

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
            '/automatic-health-checks/transport-zones/{transport-zone-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutomaticHealthCheck',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_automatic_health_check_toggle(self, **kwargs):  # noqa: E501
        """Get automatic health check toggle  # noqa: E501

        Get detailed info for automatic health check toggle.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_automatic_health_check_toggle(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AutomaticHealthCheckToggle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_automatic_health_check_toggle_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_automatic_health_check_toggle_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_automatic_health_check_toggle_with_http_info(self, **kwargs):  # noqa: E501
        """Get automatic health check toggle  # noqa: E501

        Get detailed info for automatic health check toggle.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_automatic_health_check_toggle_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AutomaticHealthCheckToggle
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
                    " to method get_automatic_health_check_toggle" % key
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
            '/automatic-health-check-toggle', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutomaticHealthCheckToggle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_automatic_health_checks(self, **kwargs):  # noqa: E501
        """List automatic health checks  # noqa: E501

        Query automatic health checks with list parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_automatic_health_checks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: AutomaticHealthCheckListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_automatic_health_checks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_automatic_health_checks_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_automatic_health_checks_with_http_info(self, **kwargs):  # noqa: E501
        """List automatic health checks  # noqa: E501

        Query automatic health checks with list parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_automatic_health_checks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: AutomaticHealthCheckListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cursor', 'included_fields', 'page_size', 'sort_ascending', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_automatic_health_checks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'included_fields' in params:
            query_params.append(('included_fields', params['included_fields']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_ascending' in params:
            query_params.append(('sort_ascending', params['sort_ascending']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501

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
            '/automatic-health-checks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutomaticHealthCheckListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_automatic_health_check_toggle(self, body, **kwargs):  # noqa: E501
        """Update automatic health check toggle  # noqa: E501

        Change status of automatic health check toggle to enabled/disabled.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_automatic_health_check_toggle(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AutomaticHealthCheckToggle body: (required)
        :return: AutomaticHealthCheckToggle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_automatic_health_check_toggle_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_automatic_health_check_toggle_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_automatic_health_check_toggle_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update automatic health check toggle  # noqa: E501

        Change status of automatic health check toggle to enabled/disabled.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_automatic_health_check_toggle_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AutomaticHealthCheckToggle body: (required)
        :return: AutomaticHealthCheckToggle
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
                    " to method update_automatic_health_check_toggle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_automatic_health_check_toggle`")  # noqa: E501

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
            '/automatic-health-check-toggle', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutomaticHealthCheckToggle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
