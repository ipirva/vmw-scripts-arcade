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


class SystemAdministrationMonitoringSystemHealthContainerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_container_cluster_status(self, body, **kwargs):  # noqa: E501
        """Create container cluster status list  # noqa: E501

        Create container cluster status list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_container_cluster_status(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContainerClusterStatus body: (required)
        :return: ContainerClusterStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_container_cluster_status_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_container_cluster_status_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_container_cluster_status_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create container cluster status list  # noqa: E501

        Create container cluster status list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_container_cluster_status_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContainerClusterStatus body: (required)
        :return: ContainerClusterStatus
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
                    " to method create_container_cluster_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_container_cluster_status`")  # noqa: E501

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
            '/systemhealth/container-cluster/ncp/status', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContainerClusterStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_container_cluster_summary(self, cluster_id, **kwargs):  # noqa: E501
        """Create container cluster status list  # noqa: E501

        Create container cluster status list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_container_cluster_summary(cluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_container_cluster_summary_with_http_info(cluster_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_container_cluster_summary_with_http_info(cluster_id, **kwargs)  # noqa: E501
            return data

    def delete_container_cluster_summary_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """Create container cluster status list  # noqa: E501

        Create container cluster status list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_container_cluster_summary_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_container_cluster_summary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if ('cluster_id' not in params or
                params['cluster_id'] is None):
            raise ValueError("Missing the required parameter `cluster_id` when calling `delete_container_cluster_summary`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in params:
            path_params['cluster-id'] = params['cluster_id']  # noqa: E501

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
            '/systemhealth/container-cluster/{cluster-id}/ncp/status', 'DELETE',
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

    def read_container_cluster_status(self, cluster_id, **kwargs):  # noqa: E501
        """Get the container cluster status by given id  # noqa: E501

        Get the container cluster status by given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_container_cluster_status(cluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_id: (required)
        :return: ContainerClusterSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_container_cluster_status_with_http_info(cluster_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_container_cluster_status_with_http_info(cluster_id, **kwargs)  # noqa: E501
            return data

    def read_container_cluster_status_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """Get the container cluster status by given id  # noqa: E501

        Get the container cluster status by given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_container_cluster_status_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_id: (required)
        :return: ContainerClusterSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_container_cluster_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if ('cluster_id' not in params or
                params['cluster_id'] is None):
            raise ValueError("Missing the required parameter `cluster_id` when calling `read_container_cluster_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in params:
            path_params['cluster-id'] = params['cluster_id']  # noqa: E501

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
            '/systemhealth/container-cluster/{cluster-id}/ncp/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContainerClusterSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_container_cluster_status_list(self, **kwargs):  # noqa: E501
        """Get all the container cluster status  # noqa: E501

        Get all the container cluster status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_container_cluster_status_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: ContainerClusterStatusList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_container_cluster_status_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.read_container_cluster_status_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def read_container_cluster_status_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get all the container cluster status  # noqa: E501

        Get all the container cluster status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_container_cluster_status_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: ContainerClusterStatusList
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
                    " to method read_container_cluster_status_list" % key
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
            '/systemhealth/container-cluster/ncp/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContainerClusterStatusList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_tn_container_agent_status(self, node_id, **kwargs):  # noqa: E501
        """Get the containter status on given node  # noqa: E501

        Get the containter status on given node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_tn_container_agent_status(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: (required)
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: TnNodeAgentStatusListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_tn_container_agent_status_with_http_info(node_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_tn_container_agent_status_with_http_info(node_id, **kwargs)  # noqa: E501
            return data

    def read_tn_container_agent_status_with_http_info(self, node_id, **kwargs):  # noqa: E501
        """Get the containter status on given node  # noqa: E501

        Get the containter status on given node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_tn_container_agent_status_with_http_info(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: (required)
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: TnNodeAgentStatusListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node_id', 'cursor', 'included_fields', 'page_size', 'sort_ascending', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_tn_container_agent_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in params or
                params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `read_tn_container_agent_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'node_id' in params:
            path_params['node-id'] = params['node_id']  # noqa: E501

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
            '/systemhealth/transport-nodes/{node-id}/container/agent/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TnNodeAgentStatusListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_tn_hyperbus_status(self, node_id, **kwargs):  # noqa: E501
        """Get the containter hyperbus status on given node  # noqa: E501

        Get the containter hyperbus status on given node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_tn_hyperbus_status(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: (required)
        :return: TnHyperbusStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_tn_hyperbus_status_with_http_info(node_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_tn_hyperbus_status_with_http_info(node_id, **kwargs)  # noqa: E501
            return data

    def read_tn_hyperbus_status_with_http_info(self, node_id, **kwargs):  # noqa: E501
        """Get the containter hyperbus status on given node  # noqa: E501

        Get the containter hyperbus status on given node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_tn_hyperbus_status_with_http_info(node_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str node_id: (required)
        :return: TnHyperbusStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_tn_hyperbus_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in params or
                params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `read_tn_hyperbus_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'node_id' in params:
            path_params['node-id'] = params['node_id']  # noqa: E501

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
            '/systemhealth/transport-nodes/{node-id}/container/hyperbus/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TnHyperbusStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)