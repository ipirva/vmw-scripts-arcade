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


class ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_bridge_cluster(self, body, **kwargs):  # noqa: E501
        """Create a Bridge Cluster  # noqa: E501

        Creates a bridge cluster. It is collection of transport nodes that will do the bridging for overlay network to vlan networks. Bridge cluster may have one or more transport nodes   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_bridge_cluster(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BridgeCluster body: (required)
        :return: BridgeCluster
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_bridge_cluster_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_bridge_cluster_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_bridge_cluster_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a Bridge Cluster  # noqa: E501

        Creates a bridge cluster. It is collection of transport nodes that will do the bridging for overlay network to vlan networks. Bridge cluster may have one or more transport nodes   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_bridge_cluster_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BridgeCluster body: (required)
        :return: BridgeCluster
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
                    " to method create_bridge_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_bridge_cluster`")  # noqa: E501

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
            '/bridge-clusters', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BridgeCluster',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_bridge_cluster(self, bridgecluster_id, **kwargs):  # noqa: E501
        """Delete a Bridge Cluster  # noqa: E501

        Removes the specified Bridge Cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bridge_cluster(bridgecluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bridgecluster_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_bridge_cluster_with_http_info(bridgecluster_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_bridge_cluster_with_http_info(bridgecluster_id, **kwargs)  # noqa: E501
            return data

    def delete_bridge_cluster_with_http_info(self, bridgecluster_id, **kwargs):  # noqa: E501
        """Delete a Bridge Cluster  # noqa: E501

        Removes the specified Bridge Cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bridge_cluster_with_http_info(bridgecluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bridgecluster_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bridgecluster_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bridge_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bridgecluster_id' is set
        if ('bridgecluster_id' not in params or
                params['bridgecluster_id'] is None):
            raise ValueError("Missing the required parameter `bridgecluster_id` when calling `delete_bridge_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bridgecluster_id' in params:
            path_params['bridgecluster-id'] = params['bridgecluster_id']  # noqa: E501

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
            '/bridge-clusters/{bridgecluster-id}', 'DELETE',
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

    def get_bridge_cluster(self, bridgecluster_id, **kwargs):  # noqa: E501
        """Get Information about a bridge cluster  # noqa: E501

        Returns information about a specified bridge cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bridge_cluster(bridgecluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bridgecluster_id: (required)
        :return: BridgeCluster
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bridge_cluster_with_http_info(bridgecluster_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bridge_cluster_with_http_info(bridgecluster_id, **kwargs)  # noqa: E501
            return data

    def get_bridge_cluster_with_http_info(self, bridgecluster_id, **kwargs):  # noqa: E501
        """Get Information about a bridge cluster  # noqa: E501

        Returns information about a specified bridge cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bridge_cluster_with_http_info(bridgecluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bridgecluster_id: (required)
        :return: BridgeCluster
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bridgecluster_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bridge_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bridgecluster_id' is set
        if ('bridgecluster_id' not in params or
                params['bridgecluster_id'] is None):
            raise ValueError("Missing the required parameter `bridgecluster_id` when calling `get_bridge_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bridgecluster_id' in params:
            path_params['bridgecluster-id'] = params['bridgecluster_id']  # noqa: E501

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
            '/bridge-clusters/{bridgecluster-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BridgeCluster',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bridge_cluster_status(self, cluster_id, **kwargs):  # noqa: E501
        """Returns status of a specified Bridge Cluster  # noqa: E501

        Get the status for the Bridge Cluster of the given cluster id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bridge_cluster_status(cluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_id: (required)
        :param str source: Data source type.
        :return: BridgeClusterStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bridge_cluster_status_with_http_info(cluster_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bridge_cluster_status_with_http_info(cluster_id, **kwargs)  # noqa: E501
            return data

    def get_bridge_cluster_status_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """Returns status of a specified Bridge Cluster  # noqa: E501

        Get the status for the Bridge Cluster of the given cluster id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bridge_cluster_status_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_id: (required)
        :param str source: Data source type.
        :return: BridgeClusterStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_id', 'source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bridge_cluster_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if ('cluster_id' not in params or
                params['cluster_id'] is None):
            raise ValueError("Missing the required parameter `cluster_id` when calling `get_bridge_cluster_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in params:
            path_params['cluster-id'] = params['cluster_id']  # noqa: E501

        query_params = []
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
            '/bridge-clusters/{cluster-id}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BridgeClusterStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_bridge_clusters(self, **kwargs):  # noqa: E501
        """List All Bridge Clusters  # noqa: E501

        Returns information about all configured bridge clusters   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_bridge_clusters(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: BridgeClusterListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_bridge_clusters_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_bridge_clusters_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_bridge_clusters_with_http_info(self, **kwargs):  # noqa: E501
        """List All Bridge Clusters  # noqa: E501

        Returns information about all configured bridge clusters   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_bridge_clusters_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: BridgeClusterListResult
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
                    " to method list_bridge_clusters" % key
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
            '/bridge-clusters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BridgeClusterListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_bridge_cluster(self, body, bridgecluster_id, **kwargs):  # noqa: E501
        """Update a Bridge Cluster  # noqa: E501

        Modifies a existing bridge cluster. One of more transport nodes can be added or removed from the bridge cluster using this API.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_bridge_cluster(body, bridgecluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BridgeCluster body: (required)
        :param str bridgecluster_id: (required)
        :return: BridgeCluster
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_bridge_cluster_with_http_info(body, bridgecluster_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_bridge_cluster_with_http_info(body, bridgecluster_id, **kwargs)  # noqa: E501
            return data

    def update_bridge_cluster_with_http_info(self, body, bridgecluster_id, **kwargs):  # noqa: E501
        """Update a Bridge Cluster  # noqa: E501

        Modifies a existing bridge cluster. One of more transport nodes can be added or removed from the bridge cluster using this API.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_bridge_cluster_with_http_info(body, bridgecluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BridgeCluster body: (required)
        :param str bridgecluster_id: (required)
        :return: BridgeCluster
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'bridgecluster_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_bridge_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_bridge_cluster`")  # noqa: E501
        # verify the required parameter 'bridgecluster_id' is set
        if ('bridgecluster_id' not in params or
                params['bridgecluster_id'] is None):
            raise ValueError("Missing the required parameter `bridgecluster_id` when calling `update_bridge_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bridgecluster_id' in params:
            path_params['bridgecluster-id'] = params['bridgecluster_id']  # noqa: E501

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
            '/bridge-clusters/{bridgecluster-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BridgeCluster',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
