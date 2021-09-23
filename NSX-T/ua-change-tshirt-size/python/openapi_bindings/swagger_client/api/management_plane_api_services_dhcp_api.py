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


class ManagementPlaneAPIServicesDHCPApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_dhcp_lease_info(self, server_id, **kwargs):  # noqa: E501
        """Get specific leases of a given dhcp server  # noqa: E501

        Get specific leases of a given dhcp server. As a dhcp server could manage millions of leases, the API has to limit the number of the returned leases via two mutually-excluded request parameters, i.e. \"pool_id\" and \"address\". Either a \"pool_id\" or an \"address\" can be provided, but not both in a same call.  If a \"pool_id\" is specified, the leases of the specific pool are returned. If an \"address\" is specified, only the lease(s) represented y this address is(are) returned. The \"address\" can be a single IP, an ip-range, or a mac address.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dhcp_lease_info(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: (required)
        :param str address: can be an ip address, or an ip range, or a mac address
        :param str pool_id: The uuid of dhcp ip pool
        :param str source: Data source type.
        :return: DhcpLeases
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dhcp_lease_info_with_http_info(server_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dhcp_lease_info_with_http_info(server_id, **kwargs)  # noqa: E501
            return data

    def get_dhcp_lease_info_with_http_info(self, server_id, **kwargs):  # noqa: E501
        """Get specific leases of a given dhcp server  # noqa: E501

        Get specific leases of a given dhcp server. As a dhcp server could manage millions of leases, the API has to limit the number of the returned leases via two mutually-excluded request parameters, i.e. \"pool_id\" and \"address\". Either a \"pool_id\" or an \"address\" can be provided, but not both in a same call.  If a \"pool_id\" is specified, the leases of the specific pool are returned. If an \"address\" is specified, only the lease(s) represented y this address is(are) returned. The \"address\" can be a single IP, an ip-range, or a mac address.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dhcp_lease_info_with_http_info(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: (required)
        :param str address: can be an ip address, or an ip range, or a mac address
        :param str pool_id: The uuid of dhcp ip pool
        :param str source: Data source type.
        :return: DhcpLeases
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'address', 'pool_id', 'source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dhcp_lease_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `get_dhcp_lease_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server-id'] = params['server_id']  # noqa: E501

        query_params = []
        if 'address' in params:
            query_params.append(('address', params['address']))  # noqa: E501
        if 'pool_id' in params:
            query_params.append(('pool_id', params['pool_id']))  # noqa: E501
        if 'source' in params:
            query_params.append(('source', params['source']))  # noqa: E501

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
            '/dhcp/servers/{server-id}/leases', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DhcpLeases',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dhcp_statistics(self, server_id, **kwargs):  # noqa: E501
        """Get DHCP statistics with given dhcp server id  # noqa: E501

        Returns the statistics of the given dhcp server.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dhcp_statistics(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: (required)
        :return: DhcpStatistics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dhcp_statistics_with_http_info(server_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dhcp_statistics_with_http_info(server_id, **kwargs)  # noqa: E501
            return data

    def get_dhcp_statistics_with_http_info(self, server_id, **kwargs):  # noqa: E501
        """Get DHCP statistics with given dhcp server id  # noqa: E501

        Returns the statistics of the given dhcp server.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dhcp_statistics_with_http_info(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: (required)
        :return: DhcpStatistics
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dhcp_statistics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `get_dhcp_statistics`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server-id'] = params['server_id']  # noqa: E501

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
            '/dhcp/servers/{server-id}/statistics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DhcpStatistics',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)