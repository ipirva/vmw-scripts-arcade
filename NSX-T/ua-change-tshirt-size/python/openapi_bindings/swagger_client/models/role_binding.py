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

class RoleBinding(ManagedResource):
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
        'identity_source_type': 'str',
        'name': 'str',
        'roles': 'list[Role]',
        'type': 'str',
        'stale': 'str',
        'identity_source_id': 'str'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'identity_source_type': 'identity_source_type',
        'name': 'name',
        'roles': 'roles',
        'type': 'type',
        'stale': 'stale',
        'identity_source_id': 'identity_source_id'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, identity_source_type='VIDM', name=None, roles=None, type=None, stale=None, identity_source_id=None, *args, **kwargs):  # noqa: E501
        """RoleBinding - a model defined in Swagger"""  # noqa: E501
        self._identity_source_type = None
        self._name = None
        self._roles = None
        self._type = None
        self._stale = None
        self._identity_source_id = None
        self.discriminator = None
        if identity_source_type is not None:
            self.identity_source_type = identity_source_type
        if name is not None:
            self.name = name
        if roles is not None:
            self.roles = roles
        if type is not None:
            self.type = type
        if stale is not None:
            self.stale = stale
        if identity_source_id is not None:
            self.identity_source_id = identity_source_id
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def identity_source_type(self):
        """Gets the identity_source_type of this RoleBinding.  # noqa: E501

        Identity source type  # noqa: E501

        :return: The identity_source_type of this RoleBinding.  # noqa: E501
        :rtype: str
        """
        return self._identity_source_type

    @identity_source_type.setter
    def identity_source_type(self, identity_source_type):
        """Sets the identity_source_type of this RoleBinding.

        Identity source type  # noqa: E501

        :param identity_source_type: The identity_source_type of this RoleBinding.  # noqa: E501
        :type: str
        """
        allowed_values = ["VIDM", "LDAP", "OIDC"]  # noqa: E501
        if identity_source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `identity_source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(identity_source_type, allowed_values)
            )

        self._identity_source_type = identity_source_type

    @property
    def name(self):
        """Gets the name of this RoleBinding.  # noqa: E501

        User/Group's name  # noqa: E501

        :return: The name of this RoleBinding.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleBinding.

        User/Group's name  # noqa: E501

        :param name: The name of this RoleBinding.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def roles(self):
        """Gets the roles of this RoleBinding.  # noqa: E501

        Roles  # noqa: E501

        :return: The roles of this RoleBinding.  # noqa: E501
        :rtype: list[Role]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this RoleBinding.

        Roles  # noqa: E501

        :param roles: The roles of this RoleBinding.  # noqa: E501
        :type: list[Role]
        """

        self._roles = roles

    @property
    def type(self):
        """Gets the type of this RoleBinding.  # noqa: E501

        Type  # noqa: E501

        :return: The type of this RoleBinding.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RoleBinding.

        Type  # noqa: E501

        :param type: The type of this RoleBinding.  # noqa: E501
        :type: str
        """
        allowed_values = ["remote_user", "remote_group", "local_user", "principal_identity"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def stale(self):
        """Gets the stale of this RoleBinding.  # noqa: E501

        Property 'stale' can be considered to have these values - absent  - This type of rolebinding does not support stale property TRUE    - Rolebinding is stale in vIDM meaning the user is no longer present in vIDM FALSE   - Rolebinding is available in vIDM UNKNOWN - Rolebinding's state of staleness in unknown Once rolebindings become stale, they can be deleted using the API POST /aaa/role-bindings?action=delete_stale_bindings  # noqa: E501

        :return: The stale of this RoleBinding.  # noqa: E501
        :rtype: str
        """
        return self._stale

    @stale.setter
    def stale(self, stale):
        """Sets the stale of this RoleBinding.

        Property 'stale' can be considered to have these values - absent  - This type of rolebinding does not support stale property TRUE    - Rolebinding is stale in vIDM meaning the user is no longer present in vIDM FALSE   - Rolebinding is available in vIDM UNKNOWN - Rolebinding's state of staleness in unknown Once rolebindings become stale, they can be deleted using the API POST /aaa/role-bindings?action=delete_stale_bindings  # noqa: E501

        :param stale: The stale of this RoleBinding.  # noqa: E501
        :type: str
        """
        allowed_values = ["TRUE", "FALSE", "UNKNOWN"]  # noqa: E501
        if stale not in allowed_values:
            raise ValueError(
                "Invalid value for `stale` ({0}), must be one of {1}"  # noqa: E501
                .format(stale, allowed_values)
            )

        self._stale = stale

    @property
    def identity_source_id(self):
        """Gets the identity_source_id of this RoleBinding.  # noqa: E501

        The ID of the external identity source that holds the referenced external entity. Currently, only external LDAP and OIDC servers are allowed.  # noqa: E501

        :return: The identity_source_id of this RoleBinding.  # noqa: E501
        :rtype: str
        """
        return self._identity_source_id

    @identity_source_id.setter
    def identity_source_id(self, identity_source_id):
        """Sets the identity_source_id of this RoleBinding.

        The ID of the external identity source that holds the referenced external entity. Currently, only external LDAP and OIDC servers are allowed.  # noqa: E501

        :param identity_source_id: The identity_source_id of this RoleBinding.  # noqa: E501
        :type: str
        """

        self._identity_source_id = identity_source_id

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
        if issubclass(RoleBinding, dict):
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
        if not isinstance(other, RoleBinding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other