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

class SolutionConfig(ManagedResource):
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
        'service_id': 'str',
        'solution_id': 'str',
        'listen_port': 'int',
        'control_ip': 'str'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'service_id': 'service_id',
        'solution_id': 'solution_id',
        'listen_port': 'listen_port',
        'control_ip': 'control_ip'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, service_id=None, solution_id=None, listen_port=None, control_ip=None, *args, **kwargs):  # noqa: E501
        """SolutionConfig - a model defined in Swagger"""  # noqa: E501
        self._service_id = None
        self._solution_id = None
        self._listen_port = None
        self._control_ip = None
        self.discriminator = None
        if service_id is not None:
            self.service_id = service_id
        self.solution_id = solution_id
        self.listen_port = listen_port
        self.control_ip = control_ip
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def service_id(self):
        """Gets the service_id of this SolutionConfig.  # noqa: E501

        The service to which the service profile belongs.  # noqa: E501

        :return: The service_id of this SolutionConfig.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this SolutionConfig.

        The service to which the service profile belongs.  # noqa: E501

        :param service_id: The service_id of this SolutionConfig.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def solution_id(self):
        """Gets the solution_id of this SolutionConfig.  # noqa: E501

        Partner needs to specify Solution Id assigned by VMware.  # noqa: E501

        :return: The solution_id of this SolutionConfig.  # noqa: E501
        :rtype: str
        """
        return self._solution_id

    @solution_id.setter
    def solution_id(self, solution_id):
        """Sets the solution_id of this SolutionConfig.

        Partner needs to specify Solution Id assigned by VMware.  # noqa: E501

        :param solution_id: The solution_id of this SolutionConfig.  # noqa: E501
        :type: str
        """
        if solution_id is None:
            raise ValueError("Invalid value for `solution_id`, must not be `None`")  # noqa: E501

        self._solution_id = solution_id

    @property
    def listen_port(self):
        """Gets the listen_port of this SolutionConfig.  # noqa: E501

        Partner needs to specify their port on which their solution application which consumes NXGI EPSec library listens.  # noqa: E501

        :return: The listen_port of this SolutionConfig.  # noqa: E501
        :rtype: int
        """
        return self._listen_port

    @listen_port.setter
    def listen_port(self, listen_port):
        """Sets the listen_port of this SolutionConfig.

        Partner needs to specify their port on which their solution application which consumes NXGI EPSec library listens.  # noqa: E501

        :param listen_port: The listen_port of this SolutionConfig.  # noqa: E501
        :type: int
        """
        if listen_port is None:
            raise ValueError("Invalid value for `listen_port`, must not be `None`")  # noqa: E501

        self._listen_port = listen_port

    @property
    def control_ip(self):
        """Gets the control_ip of this SolutionConfig.  # noqa: E501

        Partner needs to specify their assigned control IP with which they have configured their OVFs.  # noqa: E501

        :return: The control_ip of this SolutionConfig.  # noqa: E501
        :rtype: str
        """
        return self._control_ip

    @control_ip.setter
    def control_ip(self, control_ip):
        """Sets the control_ip of this SolutionConfig.

        Partner needs to specify their assigned control IP with which they have configured their OVFs.  # noqa: E501

        :param control_ip: The control_ip of this SolutionConfig.  # noqa: E501
        :type: str
        """
        if control_ip is None:
            raise ValueError("Invalid value for `control_ip`, must not be `None`")  # noqa: E501

        self._control_ip = control_ip

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
        if issubclass(SolutionConfig, dict):
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
        if not isinstance(other, SolutionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
