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

class DirectoryDomain(ManagedResource):
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
        'ldap_servers': 'list[DirectoryLdapServer]',
        'name': 'str',
        'resource_type': 'str'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'ldap_servers': 'ldap_servers',
        'name': 'name',
        'resource_type': 'resource_type'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    discriminator_value_class_map = {
          'DirectoryAdDomain': 'DirectoryAdDomain'    }

    def __init__(self, ldap_servers=None, name=None, resource_type=None, *args, **kwargs):  # noqa: E501
        """DirectoryDomain - a model defined in Swagger"""  # noqa: E501
        self._ldap_servers = None
        self._name = None
        self._resource_type = None
        self.discriminator = 'resource_type'
        self.ldap_servers = ldap_servers
        self.name = name
        self.resource_type = resource_type
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def ldap_servers(self):
        """Gets the ldap_servers of this DirectoryDomain.  # noqa: E501

        Directory domain LDAP servers' information including host, name, port, protocol and so on.  # noqa: E501

        :return: The ldap_servers of this DirectoryDomain.  # noqa: E501
        :rtype: list[DirectoryLdapServer]
        """
        return self._ldap_servers

    @ldap_servers.setter
    def ldap_servers(self, ldap_servers):
        """Sets the ldap_servers of this DirectoryDomain.

        Directory domain LDAP servers' information including host, name, port, protocol and so on.  # noqa: E501

        :param ldap_servers: The ldap_servers of this DirectoryDomain.  # noqa: E501
        :type: list[DirectoryLdapServer]
        """
        if ldap_servers is None:
            raise ValueError("Invalid value for `ldap_servers`, must not be `None`")  # noqa: E501

        self._ldap_servers = ldap_servers

    @property
    def name(self):
        """Gets the name of this DirectoryDomain.  # noqa: E501

        Directory domain name which best describes the domain. It could be unique fqdn name or it could also be descriptive. There is no unique contraint for domain name among different domains.  # noqa: E501

        :return: The name of this DirectoryDomain.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DirectoryDomain.

        Directory domain name which best describes the domain. It could be unique fqdn name or it could also be descriptive. There is no unique contraint for domain name among different domains.  # noqa: E501

        :param name: The name of this DirectoryDomain.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def resource_type(self):
        """Gets the resource_type of this DirectoryDomain.  # noqa: E501

        Domain resource type comes from multiple sub-classes extending this base class. For example, DirectoryAdDomain is one accepted resource_type. If there are more sub-classes defined, they will also be accepted resource_type.  # noqa: E501

        :return: The resource_type of this DirectoryDomain.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this DirectoryDomain.

        Domain resource type comes from multiple sub-classes extending this base class. For example, DirectoryAdDomain is one accepted resource_type. If there are more sub-classes defined, they will also be accepted resource_type.  # noqa: E501

        :param resource_type: The resource_type of this DirectoryDomain.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DirectoryAdDomain"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(DirectoryDomain, dict):
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
        if not isinstance(other, DirectoryDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other