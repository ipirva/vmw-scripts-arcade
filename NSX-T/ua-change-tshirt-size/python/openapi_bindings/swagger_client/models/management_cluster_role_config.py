# coding: utf-8

"""
    NSX-T Manager API

    VMware NSX-T Manager REST API  # noqa: E501

    OpenAPI spec version: 3.1.0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.cluster_role_config import ClusterRoleConfig  # noqa: F401,E501

class ManagementClusterRoleConfig(ClusterRoleConfig):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mgmt_cluster_listen_addr': 'ServiceEndpoint',
        'mpa_msg_client_info': 'MsgClientInfo',
        'api_listen_addr': 'ServiceEndpoint',
        'appliance_connection_info': 'ServiceEndpoint',
        'mgmt_plane_listen_addr': 'ServiceEndpoint'
    }
    if hasattr(ClusterRoleConfig, "swagger_types"):
        swagger_types.update(ClusterRoleConfig.swagger_types)

    attribute_map = {
        'mgmt_cluster_listen_addr': 'mgmt_cluster_listen_addr',
        'mpa_msg_client_info': 'mpa_msg_client_info',
        'api_listen_addr': 'api_listen_addr',
        'appliance_connection_info': 'appliance_connection_info',
        'mgmt_plane_listen_addr': 'mgmt_plane_listen_addr'
    }
    if hasattr(ClusterRoleConfig, "attribute_map"):
        attribute_map.update(ClusterRoleConfig.attribute_map)

    def __init__(self, mgmt_cluster_listen_addr=None, mpa_msg_client_info=None, api_listen_addr=None, appliance_connection_info=None, mgmt_plane_listen_addr=None, *args, **kwargs):  # noqa: E501
        """ManagementClusterRoleConfig - a model defined in Swagger"""  # noqa: E501
        self._mgmt_cluster_listen_addr = None
        self._mpa_msg_client_info = None
        self._api_listen_addr = None
        self._appliance_connection_info = None
        self._mgmt_plane_listen_addr = None
        self.discriminator = None
        if mgmt_cluster_listen_addr is not None:
            self.mgmt_cluster_listen_addr = mgmt_cluster_listen_addr
        if mpa_msg_client_info is not None:
            self.mpa_msg_client_info = mpa_msg_client_info
        if api_listen_addr is not None:
            self.api_listen_addr = api_listen_addr
        if appliance_connection_info is not None:
            self.appliance_connection_info = appliance_connection_info
        if mgmt_plane_listen_addr is not None:
            self.mgmt_plane_listen_addr = mgmt_plane_listen_addr
        ClusterRoleConfig.__init__(self, *args, **kwargs)

    @property
    def mgmt_cluster_listen_addr(self):
        """Gets the mgmt_cluster_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501


        :return: The mgmt_cluster_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501
        :rtype: ServiceEndpoint
        """
        return self._mgmt_cluster_listen_addr

    @mgmt_cluster_listen_addr.setter
    def mgmt_cluster_listen_addr(self, mgmt_cluster_listen_addr):
        """Sets the mgmt_cluster_listen_addr of this ManagementClusterRoleConfig.


        :param mgmt_cluster_listen_addr: The mgmt_cluster_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501
        :type: ServiceEndpoint
        """

        self._mgmt_cluster_listen_addr = mgmt_cluster_listen_addr

    @property
    def mpa_msg_client_info(self):
        """Gets the mpa_msg_client_info of this ManagementClusterRoleConfig.  # noqa: E501


        :return: The mpa_msg_client_info of this ManagementClusterRoleConfig.  # noqa: E501
        :rtype: MsgClientInfo
        """
        return self._mpa_msg_client_info

    @mpa_msg_client_info.setter
    def mpa_msg_client_info(self, mpa_msg_client_info):
        """Sets the mpa_msg_client_info of this ManagementClusterRoleConfig.


        :param mpa_msg_client_info: The mpa_msg_client_info of this ManagementClusterRoleConfig.  # noqa: E501
        :type: MsgClientInfo
        """

        self._mpa_msg_client_info = mpa_msg_client_info

    @property
    def api_listen_addr(self):
        """Gets the api_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501


        :return: The api_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501
        :rtype: ServiceEndpoint
        """
        return self._api_listen_addr

    @api_listen_addr.setter
    def api_listen_addr(self, api_listen_addr):
        """Sets the api_listen_addr of this ManagementClusterRoleConfig.


        :param api_listen_addr: The api_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501
        :type: ServiceEndpoint
        """

        self._api_listen_addr = api_listen_addr

    @property
    def appliance_connection_info(self):
        """Gets the appliance_connection_info of this ManagementClusterRoleConfig.  # noqa: E501


        :return: The appliance_connection_info of this ManagementClusterRoleConfig.  # noqa: E501
        :rtype: ServiceEndpoint
        """
        return self._appliance_connection_info

    @appliance_connection_info.setter
    def appliance_connection_info(self, appliance_connection_info):
        """Sets the appliance_connection_info of this ManagementClusterRoleConfig.


        :param appliance_connection_info: The appliance_connection_info of this ManagementClusterRoleConfig.  # noqa: E501
        :type: ServiceEndpoint
        """

        self._appliance_connection_info = appliance_connection_info

    @property
    def mgmt_plane_listen_addr(self):
        """Gets the mgmt_plane_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501


        :return: The mgmt_plane_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501
        :rtype: ServiceEndpoint
        """
        return self._mgmt_plane_listen_addr

    @mgmt_plane_listen_addr.setter
    def mgmt_plane_listen_addr(self, mgmt_plane_listen_addr):
        """Sets the mgmt_plane_listen_addr of this ManagementClusterRoleConfig.


        :param mgmt_plane_listen_addr: The mgmt_plane_listen_addr of this ManagementClusterRoleConfig.  # noqa: E501
        :type: ServiceEndpoint
        """

        self._mgmt_plane_listen_addr = mgmt_plane_listen_addr

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ManagementClusterRoleConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ManagementClusterRoleConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other