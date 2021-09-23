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


class SystemAdministrationLifecycleManagementUpgradeNodesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def execute_upgrade_task_(self, body, **kwargs):  # noqa: E501
        """Execute upgrade task  # noqa: E501

        Execute upgrade task.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execute_upgrade_task_(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpgradeTaskProperties body: (required)
        :return: UpgradeTaskProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.execute_upgrade_task__with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.execute_upgrade_task__with_http_info(body, **kwargs)  # noqa: E501
            return data

    def execute_upgrade_task__with_http_info(self, body, **kwargs):  # noqa: E501
        """Execute upgrade task  # noqa: E501

        Execute upgrade task.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.execute_upgrade_task__with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpgradeTaskProperties body: (required)
        :return: UpgradeTaskProperties
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
                    " to method execute_upgrade_task_" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `execute_upgrade_task_`")  # noqa: E501

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
            '/node/upgrade/performtask?action=[^/]+', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpgradeTaskProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_node_upgrade_status_summary(self, **kwargs):  # noqa: E501
        """Get upgrade status summary  # noqa: E501

        Get status summary of node upgrade, if upgrade bundle is present.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_node_upgrade_status_summary(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UpgradeStatusSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_node_upgrade_status_summary_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_node_upgrade_status_summary_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_node_upgrade_status_summary_with_http_info(self, **kwargs):  # noqa: E501
        """Get upgrade status summary  # noqa: E501

        Get status summary of node upgrade, if upgrade bundle is present.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_node_upgrade_status_summary_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UpgradeStatusSummary
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
                    " to method get_node_upgrade_status_summary" % key
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
            '/node/upgrade/status-summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpgradeStatusSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_nodes(self, **kwargs):  # noqa: E501
        """Get list of nodes across all types  # noqa: E501

        Get list of nodes. If request parameter component type is specified, then all nodes for that component will be returned. If request parameter component version is specified, then all nodes at that version will be returned.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nodes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: Component type based on which nodes will be filtered
        :param str component_version: Component version based on which nodes will be filtered
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: NodeInfoListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_nodes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_nodes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_nodes_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of nodes across all types  # noqa: E501

        Get list of nodes. If request parameter component type is specified, then all nodes for that component will be returned. If request parameter component version is specified, then all nodes at that version will be returned.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nodes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: Component type based on which nodes will be filtered
        :param str component_version: Component version based on which nodes will be filtered
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included in query result
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :return: NodeInfoListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_type', 'component_version', 'cursor', 'included_fields', 'page_size', 'sort_ascending', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_nodes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'component_type' in params:
            query_params.append(('component_type', params['component_type']))  # noqa: E501
        if 'component_version' in params:
            query_params.append(('component_version', params['component_version']))  # noqa: E501
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
            '/upgrade/nodes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeInfoListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_nodes_summary(self, **kwargs):  # noqa: E501
        """Get summary of nodes  # noqa: E501

        Get summary of nodes, which includes node count for each type and component version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nodes_summary(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeSummaryList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_nodes_summary_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_nodes_summary_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_nodes_summary_with_http_info(self, **kwargs):  # noqa: E501
        """Get summary of nodes  # noqa: E501

        Get summary of nodes, which includes node count for each type and component version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nodes_summary_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NodeSummaryList
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
                    " to method get_nodes_summary" % key
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
            '/upgrade/nodes-summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeSummaryList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_upgrade_progress_status(self, **kwargs):  # noqa: E501
        """Get upgrade progress status  # noqa: E501

        Get progress status of last upgrade step, if upgrade bundle is present.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_upgrade_progress_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UpgradeProgressStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_upgrade_progress_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_upgrade_progress_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_upgrade_progress_status_with_http_info(self, **kwargs):  # noqa: E501
        """Get upgrade progress status  # noqa: E501

        Get progress status of last upgrade step, if upgrade bundle is present.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_upgrade_progress_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UpgradeProgressStatus
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
                    " to method get_upgrade_progress_status" % key
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
            '/node/upgrade/progress-status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpgradeProgressStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_upgrade_task_status(self, **kwargs):  # noqa: E501
        """Get upgrade task status  # noqa: E501

        Get upgrade task status for the given task of the given bundle. Both bundle_name and task_id must be provided, otherwise you will receive a 404 NOT FOUND response.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_upgrade_task_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bundle_name: Bundle Name
        :param str upgrade_task_id: Upgrade Task ID
        :return: UpgradeTaskProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_upgrade_task_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_upgrade_task_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_upgrade_task_status_with_http_info(self, **kwargs):  # noqa: E501
        """Get upgrade task status  # noqa: E501

        Get upgrade task status for the given task of the given bundle. Both bundle_name and task_id must be provided, otherwise you will receive a 404 NOT FOUND response.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_upgrade_task_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bundle_name: Bundle Name
        :param str upgrade_task_id: Upgrade Task ID
        :return: UpgradeTaskProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bundle_name', 'upgrade_task_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_upgrade_task_status" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bundle_name' in params:
            query_params.append(('bundle_name', params['bundle_name']))  # noqa: E501
        if 'upgrade_task_id' in params:
            query_params.append(('upgrade_task_id', params['upgrade_task_id']))  # noqa: E501

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
            '/node/upgrade', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpgradeTaskProperties',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_version_whitelist(self, **kwargs):  # noqa: E501
        """Get the version whitelist  # noqa: E501

        Get whitelist of versions for different components  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_version_whitelist(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AcceptableComponentVersionList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_version_whitelist_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_version_whitelist_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_version_whitelist_with_http_info(self, **kwargs):  # noqa: E501
        """Get the version whitelist  # noqa: E501

        Get whitelist of versions for different components  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_version_whitelist_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AcceptableComponentVersionList
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
                    " to method get_version_whitelist" % key
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
            '/upgrade/version-whitelist', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AcceptableComponentVersionList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_version_whitelist_by_component(self, component_type, **kwargs):  # noqa: E501
        """Get the version whitelist for the specified component  # noqa: E501

        Get whitelist of versions for a component. Component can include HOST, EDGE, CCP, MP  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_version_whitelist_by_component(component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: (required)
        :return: AcceptableComponentVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_version_whitelist_by_component_with_http_info(component_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_version_whitelist_by_component_with_http_info(component_type, **kwargs)  # noqa: E501
            return data

    def get_version_whitelist_by_component_with_http_info(self, component_type, **kwargs):  # noqa: E501
        """Get the version whitelist for the specified component  # noqa: E501

        Get whitelist of versions for a component. Component can include HOST, EDGE, CCP, MP  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_version_whitelist_by_component_with_http_info(component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: (required)
        :return: AcceptableComponentVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_version_whitelist_by_component" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'component_type' is set
        if ('component_type' not in params or
                params['component_type'] is None):
            raise ValueError("Missing the required parameter `component_type` when calling `get_version_whitelist_by_component`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'component_type' in params:
            path_params['component_type'] = params['component_type']  # noqa: E501

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
            '/upgrade/version-whitelist/{component_type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AcceptableComponentVersion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_version_whitelist(self, body, component_type, **kwargs):  # noqa: E501
        """Update the version whitelist for the specified component type  # noqa: E501

        Update the version whitelist for the specified component type (HOST, EDGE, CCP, MP).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_version_whitelist(body, component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VersionList body: (required)
        :param str component_type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_version_whitelist_with_http_info(body, component_type, **kwargs)  # noqa: E501
        else:
            (data) = self.update_version_whitelist_with_http_info(body, component_type, **kwargs)  # noqa: E501
            return data

    def update_version_whitelist_with_http_info(self, body, component_type, **kwargs):  # noqa: E501
        """Update the version whitelist for the specified component type  # noqa: E501

        Update the version whitelist for the specified component type (HOST, EDGE, CCP, MP).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_version_whitelist_with_http_info(body, component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VersionList body: (required)
        :param str component_type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'component_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_version_whitelist" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_version_whitelist`")  # noqa: E501
        # verify the required parameter 'component_type' is set
        if ('component_type' not in params or
                params['component_type'] is None):
            raise ValueError("Missing the required parameter `component_type` when calling `update_version_whitelist`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'component_type' in params:
            path_params['component_type'] = params['component_type']  # noqa: E501

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
            '/upgrade/version-whitelist/{component_type}', 'PUT',
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