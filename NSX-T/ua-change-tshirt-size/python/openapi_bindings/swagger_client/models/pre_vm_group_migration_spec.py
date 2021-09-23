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

class PreVmGroupMigrationSpec(object):
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
        'allow_override': 'bool',
        'group_id': 'str',
        'vm_instance_ids': 'list[str]'
    }

    attribute_map = {
        'allow_override': 'allow_override',
        'group_id': 'group_id',
        'vm_instance_ids': 'vm_instance_ids'
    }

    def __init__(self, allow_override=False, group_id=None, vm_instance_ids=None):  # noqa: E501
        """PreVmGroupMigrationSpec - a model defined in Swagger"""  # noqa: E501
        self._allow_override = None
        self._group_id = None
        self._vm_instance_ids = None
        self.discriminator = None
        if allow_override is not None:
            self.allow_override = allow_override
        self.group_id = group_id
        self.vm_instance_ids = vm_instance_ids

    @property
    def allow_override(self):
        """Gets the allow_override of this PreVmGroupMigrationSpec.  # noqa: E501

        Flag to indicate whether to re-run the pre migrate steps for the VM group if they are already run before.  # noqa: E501

        :return: The allow_override of this PreVmGroupMigrationSpec.  # noqa: E501
        :rtype: bool
        """
        return self._allow_override

    @allow_override.setter
    def allow_override(self, allow_override):
        """Sets the allow_override of this PreVmGroupMigrationSpec.

        Flag to indicate whether to re-run the pre migrate steps for the VM group if they are already run before.  # noqa: E501

        :param allow_override: The allow_override of this PreVmGroupMigrationSpec.  # noqa: E501
        :type: bool
        """

        self._allow_override = allow_override

    @property
    def group_id(self):
        """Gets the group_id of this PreVmGroupMigrationSpec.  # noqa: E501

        User defined VM group id that must be unique among all VM groups ids.  # noqa: E501

        :return: The group_id of this PreVmGroupMigrationSpec.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this PreVmGroupMigrationSpec.

        User defined VM group id that must be unique among all VM groups ids.  # noqa: E501

        :param group_id: The group_id of this PreVmGroupMigrationSpec.  # noqa: E501
        :type: str
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")  # noqa: E501

        self._group_id = group_id

    @property
    def vm_instance_ids(self):
        """Gets the vm_instance_ids of this PreVmGroupMigrationSpec.  # noqa: E501

        List of VM instance uuids that can be found in VC inventory.  # noqa: E501

        :return: The vm_instance_ids of this PreVmGroupMigrationSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._vm_instance_ids

    @vm_instance_ids.setter
    def vm_instance_ids(self, vm_instance_ids):
        """Sets the vm_instance_ids of this PreVmGroupMigrationSpec.

        List of VM instance uuids that can be found in VC inventory.  # noqa: E501

        :param vm_instance_ids: The vm_instance_ids of this PreVmGroupMigrationSpec.  # noqa: E501
        :type: list[str]
        """
        if vm_instance_ids is None:
            raise ValueError("Invalid value for `vm_instance_ids`, must not be `None`")  # noqa: E501

        self._vm_instance_ids = vm_instance_ids

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
        if issubclass(PreVmGroupMigrationSpec, dict):
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
        if not isinstance(other, PreVmGroupMigrationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
