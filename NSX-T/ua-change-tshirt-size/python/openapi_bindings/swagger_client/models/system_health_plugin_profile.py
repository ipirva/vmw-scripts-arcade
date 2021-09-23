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
from swagger_client.models.managed_resource import ManagedResource  # noqa: F401,E501

class SystemHealthPluginProfile(ManagedResource):
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
        'node_types': 'list[str]',
        'publisher': 'str',
        'config': 'SHAPredefinedPluginProfileData',
        'enabled': 'bool',
        'type': 'str'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'node_types': 'node_types',
        'publisher': 'publisher',
        'config': 'config',
        'enabled': 'enabled',
        'type': 'type'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, node_types=None, publisher=None, config=None, enabled=None, type='NETWORK', *args, **kwargs):  # noqa: E501
        """SystemHealthPluginProfile - a model defined in Swagger"""  # noqa: E501
        self._node_types = None
        self._publisher = None
        self._config = None
        self._enabled = None
        self._type = None
        self.discriminator = None
        if node_types is not None:
            self.node_types = node_types
        if publisher is not None:
            self.publisher = publisher
        if config is not None:
            self.config = config
        if enabled is not None:
            self.enabled = enabled
        if type is not None:
            self.type = type
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def node_types(self):
        """Gets the node_types of this SystemHealthPluginProfile.  # noqa: E501

        Display the running node types of pre-defined plugin. The config can be changed by API /systemhealth/profiles. To see the effective status on given node, use the status API per node /systemhealth/plugins/status/<node-id>.   # noqa: E501

        :return: The node_types of this SystemHealthPluginProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._node_types

    @node_types.setter
    def node_types(self, node_types):
        """Sets the node_types of this SystemHealthPluginProfile.

        Display the running node types of pre-defined plugin. The config can be changed by API /systemhealth/profiles. To see the effective status on given node, use the status API per node /systemhealth/plugins/status/<node-id>.   # noqa: E501

        :param node_types: The node_types of this SystemHealthPluginProfile.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["NSX_ESX", "NSX_KVM", "NSX_BAREMETAL_SERVER", "NSX_EDGE", "NSX_PUBLIC_CLOUD_GATEWAY", "NSX_MANAGER", "NSX_POLICY_MANAGER", "NSX_CONTROLLER", "GLOBAL_MANAGER"]  # noqa: E501
        if not set(node_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `node_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(node_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._node_types = node_types

    @property
    def publisher(self):
        """Gets the publisher of this SystemHealthPluginProfile.  # noqa: E501

        The publisher of System Health Agent plugin  # noqa: E501

        :return: The publisher of this SystemHealthPluginProfile.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this SystemHealthPluginProfile.

        The publisher of System Health Agent plugin  # noqa: E501

        :param publisher: The publisher of this SystemHealthPluginProfile.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def config(self):
        """Gets the config of this SystemHealthPluginProfile.  # noqa: E501


        :return: The config of this SystemHealthPluginProfile.  # noqa: E501
        :rtype: SHAPredefinedPluginProfileData
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this SystemHealthPluginProfile.


        :param config: The config of this SystemHealthPluginProfile.  # noqa: E501
        :type: SHAPredefinedPluginProfileData
        """

        self._config = config

    @property
    def enabled(self):
        """Gets the enabled of this SystemHealthPluginProfile.  # noqa: E501

        Display the default on-off switch of pre defined plugin. The config can be changed by API /systemhealth/profiles. To see the effective status on given node, use the status API per node /systemhealth/plugins/status/<node-id>.   # noqa: E501

        :return: The enabled of this SystemHealthPluginProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SystemHealthPluginProfile.

        Display the default on-off switch of pre defined plugin. The config can be changed by API /systemhealth/profiles. To see the effective status on given node, use the status API per node /systemhealth/plugins/status/<node-id>.   # noqa: E501

        :param enabled: The enabled of this SystemHealthPluginProfile.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def type(self):
        """Gets the type of this SystemHealthPluginProfile.  # noqa: E501

        The type of System Health Agent plugin  # noqa: E501

        :return: The type of this SystemHealthPluginProfile.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemHealthPluginProfile.

        The type of System Health Agent plugin  # noqa: E501

        :param type: The type of this SystemHealthPluginProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["COMPUTE", "STORAGE", "NETWORK", "HYPERBUS", "NCP", "NODEAGENT", "VSAN", "TNAGENT", "UPLINK"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(SystemHealthPluginProfile, dict):
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
        if not isinstance(other, SystemHealthPluginProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other