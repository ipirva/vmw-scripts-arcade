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

class Csr(ManagedResource):
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
        'key_size': 'int',
        'pem_encoded': 'str',
        'algorithm': 'str',
        'subject': 'Principal'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'key_size': 'key_size',
        'pem_encoded': 'pem_encoded',
        'algorithm': 'algorithm',
        'subject': 'subject'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, key_size=None, pem_encoded=None, algorithm=None, subject=None, *args, **kwargs):  # noqa: E501
        """Csr - a model defined in Swagger"""  # noqa: E501
        self._key_size = None
        self._pem_encoded = None
        self._algorithm = None
        self._subject = None
        self.discriminator = None
        self.key_size = key_size
        if pem_encoded is not None:
            self.pem_encoded = pem_encoded
        self.algorithm = algorithm
        self.subject = subject
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def key_size(self):
        """Gets the key_size of this Csr.  # noqa: E501

        Size measured in bits of the public key used in a cryptographic algorithm.  # noqa: E501

        :return: The key_size of this Csr.  # noqa: E501
        :rtype: int
        """
        return self._key_size

    @key_size.setter
    def key_size(self, key_size):
        """Sets the key_size of this Csr.

        Size measured in bits of the public key used in a cryptographic algorithm.  # noqa: E501

        :param key_size: The key_size of this Csr.  # noqa: E501
        :type: int
        """
        if key_size is None:
            raise ValueError("Invalid value for `key_size`, must not be `None`")  # noqa: E501

        self._key_size = key_size

    @property
    def pem_encoded(self):
        """Gets the pem_encoded of this Csr.  # noqa: E501

        PEM encoded certificate data.  # noqa: E501

        :return: The pem_encoded of this Csr.  # noqa: E501
        :rtype: str
        """
        return self._pem_encoded

    @pem_encoded.setter
    def pem_encoded(self, pem_encoded):
        """Sets the pem_encoded of this Csr.

        PEM encoded certificate data.  # noqa: E501

        :param pem_encoded: The pem_encoded of this Csr.  # noqa: E501
        :type: str
        """

        self._pem_encoded = pem_encoded

    @property
    def algorithm(self):
        """Gets the algorithm of this Csr.  # noqa: E501

        Cryptographic algorithm(asymmetric ) used by the public key for data encryption.  # noqa: E501

        :return: The algorithm of this Csr.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this Csr.

        Cryptographic algorithm(asymmetric ) used by the public key for data encryption.  # noqa: E501

        :param algorithm: The algorithm of this Csr.  # noqa: E501
        :type: str
        """
        if algorithm is None:
            raise ValueError("Invalid value for `algorithm`, must not be `None`")  # noqa: E501
        allowed_values = ["RSA"]  # noqa: E501
        if algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(algorithm, allowed_values)
            )

        self._algorithm = algorithm

    @property
    def subject(self):
        """Gets the subject of this Csr.  # noqa: E501


        :return: The subject of this Csr.  # noqa: E501
        :rtype: Principal
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Csr.


        :param subject: The subject of this Csr.  # noqa: E501
        :type: Principal
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

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
        if issubclass(Csr, dict):
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
        if not isinstance(other, Csr):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other