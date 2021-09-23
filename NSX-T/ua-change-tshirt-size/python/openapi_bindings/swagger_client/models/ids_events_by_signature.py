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
from swagger_client.models.resource import Resource  # noqa: F401,E501

class IDSEventsBySignature(Resource):
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
        'count': 'int',
        'first_occurence': 'int',
        'severity': 'str',
        'signature_name': 'str',
        'is_ongoing': 'bool',
        'signature_id': 'int',
        'resource_type': 'str'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        'count': 'count',
        'first_occurence': 'first_occurence',
        'severity': 'severity',
        'signature_name': 'signature_name',
        'is_ongoing': 'is_ongoing',
        'signature_id': 'signature_id',
        'resource_type': 'resource_type'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, count=None, first_occurence=None, severity=None, signature_name=None, is_ongoing=None, signature_id=None, resource_type=None, *args, **kwargs):  # noqa: E501
        """IDSEventsBySignature - a model defined in Swagger"""  # noqa: E501
        self._count = None
        self._first_occurence = None
        self._severity = None
        self._signature_name = None
        self._is_ongoing = None
        self._signature_id = None
        self._resource_type = None
        self.discriminator = None
        if count is not None:
            self.count = count
        if first_occurence is not None:
            self.first_occurence = first_occurence
        if severity is not None:
            self.severity = severity
        if signature_name is not None:
            self.signature_name = signature_name
        if is_ongoing is not None:
            self.is_ongoing = is_ongoing
        if signature_id is not None:
            self.signature_id = signature_id
        if resource_type is not None:
            self.resource_type = resource_type
        Resource.__init__(self, *args, **kwargs)

    @property
    def count(self):
        """Gets the count of this IDSEventsBySignature.  # noqa: E501

        Number of times this particular signature was detected.  # noqa: E501

        :return: The count of this IDSEventsBySignature.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this IDSEventsBySignature.

        Number of times this particular signature was detected.  # noqa: E501

        :param count: The count of this IDSEventsBySignature.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def first_occurence(self):
        """Gets the first_occurence of this IDSEventsBySignature.  # noqa: E501

        First occurence of the intrusion, in epoch milliseconds.  # noqa: E501

        :return: The first_occurence of this IDSEventsBySignature.  # noqa: E501
        :rtype: int
        """
        return self._first_occurence

    @first_occurence.setter
    def first_occurence(self, first_occurence):
        """Sets the first_occurence of this IDSEventsBySignature.

        First occurence of the intrusion, in epoch milliseconds.  # noqa: E501

        :param first_occurence: The first_occurence of this IDSEventsBySignature.  # noqa: E501
        :type: int
        """

        self._first_occurence = first_occurence

    @property
    def severity(self):
        """Gets the severity of this IDSEventsBySignature.  # noqa: E501

        Severity of the threat covered by the signature, can be Critical, High, Medium, or Low.  # noqa: E501

        :return: The severity of this IDSEventsBySignature.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this IDSEventsBySignature.

        Severity of the threat covered by the signature, can be Critical, High, Medium, or Low.  # noqa: E501

        :param severity: The severity of this IDSEventsBySignature.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def signature_name(self):
        """Gets the signature_name of this IDSEventsBySignature.  # noqa: E501

        Name of the signature pertaining to the detected intrusion.  # noqa: E501

        :return: The signature_name of this IDSEventsBySignature.  # noqa: E501
        :rtype: str
        """
        return self._signature_name

    @signature_name.setter
    def signature_name(self, signature_name):
        """Sets the signature_name of this IDSEventsBySignature.

        Name of the signature pertaining to the detected intrusion.  # noqa: E501

        :param signature_name: The signature_name of this IDSEventsBySignature.  # noqa: E501
        :type: str
        """

        self._signature_name = signature_name

    @property
    def is_ongoing(self):
        """Gets the is_ongoing of this IDSEventsBySignature.  # noqa: E501

        Flag indicating an ongoing intrusion.  # noqa: E501

        :return: The is_ongoing of this IDSEventsBySignature.  # noqa: E501
        :rtype: bool
        """
        return self._is_ongoing

    @is_ongoing.setter
    def is_ongoing(self, is_ongoing):
        """Sets the is_ongoing of this IDSEventsBySignature.

        Flag indicating an ongoing intrusion.  # noqa: E501

        :param is_ongoing: The is_ongoing of this IDSEventsBySignature.  # noqa: E501
        :type: bool
        """

        self._is_ongoing = is_ongoing

    @property
    def signature_id(self):
        """Gets the signature_id of this IDSEventsBySignature.  # noqa: E501

        Signature ID pertaining to the detected intrusion.  # noqa: E501

        :return: The signature_id of this IDSEventsBySignature.  # noqa: E501
        :rtype: int
        """
        return self._signature_id

    @signature_id.setter
    def signature_id(self, signature_id):
        """Sets the signature_id of this IDSEventsBySignature.

        Signature ID pertaining to the detected intrusion.  # noqa: E501

        :param signature_id: The signature_id of this IDSEventsBySignature.  # noqa: E501
        :type: int
        """

        self._signature_id = signature_id

    @property
    def resource_type(self):
        """Gets the resource_type of this IDSEventsBySignature.  # noqa: E501

        IDSEvent resource type.  # noqa: E501

        :return: The resource_type of this IDSEventsBySignature.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this IDSEventsBySignature.

        IDSEvent resource type.  # noqa: E501

        :param resource_type: The resource_type of this IDSEventsBySignature.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

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
        if issubclass(IDSEventsBySignature, dict):
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
        if not isinstance(other, IDSEventsBySignature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other