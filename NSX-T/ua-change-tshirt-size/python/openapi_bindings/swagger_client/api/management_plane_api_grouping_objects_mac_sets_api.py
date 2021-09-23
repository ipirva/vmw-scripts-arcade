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


class ManagementPlaneAPIGroupingObjectsMACSetsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_mac_address(self, body, mac_set_id, **kwargs):  # noqa: E501
        """Add a MAC address to a MACSet  # noqa: E501

        Add an individual MAC address to a MACSet   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_mac_address(body, mac_set_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MACAddressElement body: (required)
        :param str mac_set_id: MAC Set Id (required)
        :return: MACAddressElement
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_mac_address_with_http_info(body, mac_set_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_mac_address_with_http_info(body, mac_set_id, **kwargs)  # noqa: E501
            return data

    def add_mac_address_with_http_info(self, body, mac_set_id, **kwargs):  # noqa: E501
        """Add a MAC address to a MACSet  # noqa: E501

        Add an individual MAC address to a MACSet   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_mac_address_with_http_info(body, mac_set_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MACAddressElement body: (required)
        :param str mac_set_id: MAC Set Id (required)
        :return: MACAddressElement
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'mac_set_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_mac_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_mac_address`")  # noqa: E501
        # verify the required parameter 'mac_set_id' is set
        if ('mac_set_id' not in params or
                params['mac_set_id'] is None):
            raise ValueError("Missing the required parameter `mac_set_id` when calling `add_mac_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'mac_set_id' in params:
            path_params['mac-set-id'] = params['mac_set_id']  # noqa: E501

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
            '/mac-sets/{mac-set-id}/members', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MACAddressElement',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_mac_set(self, mac_set_id, **kwargs):  # noqa: E501
        """Delete MACSet  # noqa: E501

        Deletes the specified MACSet. By default, if the MACSet is added to an NSGroup, it won't be deleted. In such situations, pass \"force=true\" as query param to force delete the MACSet.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_mac_set(mac_set_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mac_set_id: MACSet Id (required)
        :param bool force: Force delete the resource even if it is being used somewhere 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_mac_set_with_http_info(mac_set_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_mac_set_with_http_info(mac_set_id, **kwargs)  # noqa: E501
            return data

    def delete_mac_set_with_http_info(self, mac_set_id, **kwargs):  # noqa: E501
        """Delete MACSet  # noqa: E501

        Deletes the specified MACSet. By default, if the MACSet is added to an NSGroup, it won't be deleted. In such situations, pass \"force=true\" as query param to force delete the MACSet.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_mac_set_with_http_info(mac_set_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mac_set_id: MACSet Id (required)
        :param bool force: Force delete the resource even if it is being used somewhere 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mac_set_id', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_mac_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mac_set_id' is set
        if ('mac_set_id' not in params or
                params['mac_set_id'] is None):
            raise ValueError("Missing the required parameter `mac_set_id` when calling `delete_mac_set`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'mac_set_id' in params:
            path_params['mac-set-id'] = params['mac_set_id']  # noqa: E501

        query_params = []
        if 'force' in params:
            query_params.append(('force', params['force']))  # noqa: E501

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
            '/mac-sets/{mac-set-id}', 'DELETE',
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

    def get_mac_addresses(self, mac_set_id, **kwargs):  # noqa: E501
        """Get all MACAddresses in a MACSet  # noqa: E501

        List all MAC addresses in a MACSet   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mac_addresses(mac_set_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mac_set_id: MAC Set Id (required)
        :return: MACAddressElementListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_mac_addresses_with_http_info(mac_set_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_mac_addresses_with_http_info(mac_set_id, **kwargs)  # noqa: E501
            return data

    def get_mac_addresses_with_http_info(self, mac_set_id, **kwargs):  # noqa: E501
        """Get all MACAddresses in a MACSet  # noqa: E501

        List all MAC addresses in a MACSet   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mac_addresses_with_http_info(mac_set_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mac_set_id: MAC Set Id (required)
        :return: MACAddressElementListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mac_set_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mac_addresses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mac_set_id' is set
        if ('mac_set_id' not in params or
                params['mac_set_id'] is None):
            raise ValueError("Missing the required parameter `mac_set_id` when calling `get_mac_addresses`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'mac_set_id' in params:
            path_params['mac-set-id'] = params['mac_set_id']  # noqa: E501

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
            '/mac-sets/{mac-set-id}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MACAddressElementListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_mac_sets(self, **kwargs):  # noqa: E501
        """List MACSets  # noqa: E501

        Returns paginated list of MACSets   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_mac_sets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: MACSetListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_mac_sets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_mac_sets_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_mac_sets_with_http_info(self, **kwargs):  # noqa: E501
        """List MACSets  # noqa: E501

        Returns paginated list of MACSets   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_mac_sets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: MACSetListResult
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
                    " to method list_mac_sets" % key
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
            '/mac-sets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MACSetListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_mac_set(self, mac_set_id, **kwargs):  # noqa: E501
        """Read MACSet  # noqa: E501

        Returns information about the specified MACSet   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_mac_set(mac_set_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mac_set_id: MACSet Id (required)
        :return: MACSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_mac_set_with_http_info(mac_set_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_mac_set_with_http_info(mac_set_id, **kwargs)  # noqa: E501
            return data

    def read_mac_set_with_http_info(self, mac_set_id, **kwargs):  # noqa: E501
        """Read MACSet  # noqa: E501

        Returns information about the specified MACSet   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_mac_set_with_http_info(mac_set_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mac_set_id: MACSet Id (required)
        :return: MACSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mac_set_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_mac_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mac_set_id' is set
        if ('mac_set_id' not in params or
                params['mac_set_id'] is None):
            raise ValueError("Missing the required parameter `mac_set_id` when calling `read_mac_set`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'mac_set_id' in params:
            path_params['mac-set-id'] = params['mac_set_id']  # noqa: E501

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
            '/mac-sets/{mac-set-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MACSet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_mac_address(self, mac_set_id, mac_address, **kwargs):  # noqa: E501
        """Remove a MAC address from given MACSet  # noqa: E501

        Remove an individual MAC address from a MACSet   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_mac_address(mac_set_id, mac_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mac_set_id: MACSet Id (required)
        :param str mac_address: MAC address to be removed (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_mac_address_with_http_info(mac_set_id, mac_address, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_mac_address_with_http_info(mac_set_id, mac_address, **kwargs)  # noqa: E501
            return data

    def remove_mac_address_with_http_info(self, mac_set_id, mac_address, **kwargs):  # noqa: E501
        """Remove a MAC address from given MACSet  # noqa: E501

        Remove an individual MAC address from a MACSet   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_mac_address_with_http_info(mac_set_id, mac_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mac_set_id: MACSet Id (required)
        :param str mac_address: MAC address to be removed (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mac_set_id', 'mac_address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_mac_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mac_set_id' is set
        if ('mac_set_id' not in params or
                params['mac_set_id'] is None):
            raise ValueError("Missing the required parameter `mac_set_id` when calling `remove_mac_address`")  # noqa: E501
        # verify the required parameter 'mac_address' is set
        if ('mac_address' not in params or
                params['mac_address'] is None):
            raise ValueError("Missing the required parameter `mac_address` when calling `remove_mac_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'mac_set_id' in params:
            path_params['mac-set-id'] = params['mac_set_id']  # noqa: E501
        if 'mac_address' in params:
            path_params['mac-address'] = params['mac_address']  # noqa: E501

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
            '/mac-sets/{mac-set-id}/members/{mac-address}', 'DELETE',
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

    def update_mac_set(self, body, mac_set_id, **kwargs):  # noqa: E501
        """Update MACSet  # noqa: E501

        Updates the specified MACSet. Modifiable parameters include the description, display_name and mac_addresses.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_mac_set(body, mac_set_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MACSet body: (required)
        :param str mac_set_id: MACSet Id (required)
        :return: MACSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_mac_set_with_http_info(body, mac_set_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_mac_set_with_http_info(body, mac_set_id, **kwargs)  # noqa: E501
            return data

    def update_mac_set_with_http_info(self, body, mac_set_id, **kwargs):  # noqa: E501
        """Update MACSet  # noqa: E501

        Updates the specified MACSet. Modifiable parameters include the description, display_name and mac_addresses.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_mac_set_with_http_info(body, mac_set_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MACSet body: (required)
        :param str mac_set_id: MACSet Id (required)
        :return: MACSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'mac_set_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_mac_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_mac_set`")  # noqa: E501
        # verify the required parameter 'mac_set_id' is set
        if ('mac_set_id' not in params or
                params['mac_set_id'] is None):
            raise ValueError("Missing the required parameter `mac_set_id` when calling `update_mac_set`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'mac_set_id' in params:
            path_params['mac-set-id'] = params['mac_set_id']  # noqa: E501

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
            '/mac-sets/{mac-set-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MACSet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
