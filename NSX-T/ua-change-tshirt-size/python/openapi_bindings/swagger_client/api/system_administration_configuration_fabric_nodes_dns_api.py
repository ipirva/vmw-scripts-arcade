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


class SystemAdministrationConfigurationFabricNodesDNSApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def read_node_name_servers(self, **kwargs):  # noqa: E501
        """Read the Node's Name Servers  # noqa: E501

        Returns the list of servers that the node uses to look up IP addresses associated with given domain names.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_node_name_servers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeNameServersProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_node_name_servers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.read_node_name_servers_with_http_info(**kwargs)  # noqa: E501
            return data

    def read_node_name_servers_with_http_info(self, **kwargs):  # noqa: E501
        """Read the Node's Name Servers  # noqa: E501

        Returns the list of servers that the node uses to look up IP addresses associated with given domain names.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_node_name_servers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeNameServersProperties
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
                    " to method read_node_name_servers" % key
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
            '/node/network/name-servers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeNameServersProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_node_search_domains(self, **kwargs):  # noqa: E501
        """Read the Node's Search Domains  # noqa: E501

        Returns the domain list that the node uses to complete unqualified host names. When a host name does not include a fully qualified domain name (FQDN), the NSX Management node appends the first-listed domain name to the host name before the host name is looked up. The NSX Management node continues this for each entry in the domain list until it finds a match.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_node_search_domains(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeSearchDomainsProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_node_search_domains_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.read_node_search_domains_with_http_info(**kwargs)  # noqa: E501
            return data

    def read_node_search_domains_with_http_info(self, **kwargs):  # noqa: E501
        """Read the Node's Search Domains  # noqa: E501

        Returns the domain list that the node uses to complete unqualified host names. When a host name does not include a fully qualified domain name (FQDN), the NSX Management node appends the first-listed domain name to the host name before the host name is looked up. The NSX Management node continues this for each entry in the domain list until it finds a match.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_node_search_domains_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeSearchDomainsProperties
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
                    " to method read_node_search_domains" % key
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
            '/node/network/search-domains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeSearchDomainsProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_node_name_servers(self, body, **kwargs):  # noqa: E501
        """Update the Node's Name Servers  # noqa: E501

        Modifies the list of servers that the node uses to look up IP addresses associated with given domain names. If DHCP is configured, this method returns a 409 CONFLICT error, because DHCP manages the list of name servers.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_node_name_servers(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NodeNameServersProperties body: (required)
        :return: NodeNameServersProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_node_name_servers_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_node_name_servers_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_node_name_servers_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update the Node's Name Servers  # noqa: E501

        Modifies the list of servers that the node uses to look up IP addresses associated with given domain names. If DHCP is configured, this method returns a 409 CONFLICT error, because DHCP manages the list of name servers.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_node_name_servers_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NodeNameServersProperties body: (required)
        :return: NodeNameServersProperties
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
                    " to method update_node_name_servers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_node_name_servers`")  # noqa: E501

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
            '/node/network/name-servers', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeNameServersProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_node_search_domains(self, body, **kwargs):  # noqa: E501
        """Update the Node's Search Domains  # noqa: E501

        Modifies the list of domain names that the node uses to complete unqualified host names. If DHCP is configured, this method returns a 409 CONFLICT error, because DHCP manages the list of name servers.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_node_search_domains(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NodeSearchDomainsProperties body: (required)
        :return: NodeSearchDomainsProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_node_search_domains_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_node_search_domains_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_node_search_domains_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update the Node's Search Domains  # noqa: E501

        Modifies the list of domain names that the node uses to complete unqualified host names. If DHCP is configured, this method returns a 409 CONFLICT error, because DHCP manages the list of name servers.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_node_search_domains_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NodeSearchDomainsProperties body: (required)
        :return: NodeSearchDomainsProperties
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
                    " to method update_node_search_domains" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_node_search_domains`")  # noqa: E501

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
            '/node/network/search-domains', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeSearchDomainsProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
