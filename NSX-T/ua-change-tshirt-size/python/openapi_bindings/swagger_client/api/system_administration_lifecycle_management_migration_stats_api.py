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


class SystemAdministrationLifecycleManagementMigrationStatsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def download_migration_data(self, file_type, **kwargs):  # noqa: E501
        """Download migration data  # noqa: E501

        Download the data needed for migration. The call returns after Download is completed.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_migration_data(file_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_type: Type of the Migration data file that needs to be downloaded. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_migration_data_with_http_info(file_type, **kwargs)  # noqa: E501
        else:
            (data) = self.download_migration_data_with_http_info(file_type, **kwargs)  # noqa: E501
            return data

    def download_migration_data_with_http_info(self, file_type, **kwargs):  # noqa: E501
        """Download migration data  # noqa: E501

        Download the data needed for migration. The call returns after Download is completed.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_migration_data_with_http_info(file_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_type: Type of the Migration data file that needs to be downloaded. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_migration_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_type' is set
        if ('file_type' not in params or
                params['file_type'] is None):
            raise ValueError("Missing the required parameter `file_type` when calling `download_migration_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_type' in params:
            query_params.append(('file_type', params['file_type']))  # noqa: E501

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
            '/migration/data/download', 'GET',
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

    def get_logical_construct_migration_stats(self, **kwargs):  # noqa: E501
        """Get migration stats for logical constructs phase  # noqa: E501

        Get migration stats for logical constructs phase. This API can be polled for getting runtime progress of the migration from source to target.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_logical_construct_migration_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: LogicalConstructMigrationStatsListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_logical_construct_migration_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_logical_construct_migration_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_logical_construct_migration_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Get migration stats for logical constructs phase  # noqa: E501

        Get migration stats for logical constructs phase. This API can be polled for getting runtime progress of the migration from source to target.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_logical_construct_migration_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: LogicalConstructMigrationStatsListResult
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
                    " to method get_logical_construct_migration_stats" % key
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
            '/migration/logical-constructs/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LogicalConstructMigrationStatsListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_migration_data_info(self, file_type, **kwargs):  # noqa: E501
        """Get Migration Data Info.  # noqa: E501

        Get information about the requested Migration Data file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_migration_data_info(file_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_type: Type of the Migration data file for which info is needed. (required)
        :return: MigrationDataInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_migration_data_info_with_http_info(file_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_migration_data_info_with_http_info(file_type, **kwargs)  # noqa: E501
            return data

    def get_migration_data_info_with_http_info(self, file_type, **kwargs):  # noqa: E501
        """Get Migration Data Info.  # noqa: E501

        Get information about the requested Migration Data file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_migration_data_info_with_http_info(file_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_type: Type of the Migration data file for which info is needed. (required)
        :return: MigrationDataInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_migration_data_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_type' is set
        if ('file_type' not in params or
                params['file_type'] is None):
            raise ValueError("Missing the required parameter `file_type` when calling `get_migration_data_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_type' in params:
            query_params.append(('file_type', params['file_type']))  # noqa: E501

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
            '/migration/data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MigrationDataInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)