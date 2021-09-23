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

class CertificateKeyPair(object):
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
        'rsa_private_key': 'str',
        'certificate': 'SecurityCertificate'
    }

    attribute_map = {
        'rsa_private_key': 'rsa_private_key',
        'certificate': 'certificate'
    }

    def __init__(self, rsa_private_key=None, certificate=None):  # noqa: E501
        """CertificateKeyPair - a model defined in Swagger"""  # noqa: E501
        self._rsa_private_key = None
        self._certificate = None
        self.discriminator = None
        if rsa_private_key is not None:
            self.rsa_private_key = rsa_private_key
        self.certificate = certificate

    @property
    def rsa_private_key(self):
        """Gets the rsa_private_key of this CertificateKeyPair.  # noqa: E501

        The private key must include the enclosing \"-----BEGIN RSA PRIVATE KEY-----\" and \"-----END RSA PRIVATE KEY-----\". An empty string is returned in read responses.  # noqa: E501

        :return: The rsa_private_key of this CertificateKeyPair.  # noqa: E501
        :rtype: str
        """
        return self._rsa_private_key

    @rsa_private_key.setter
    def rsa_private_key(self, rsa_private_key):
        """Sets the rsa_private_key of this CertificateKeyPair.

        The private key must include the enclosing \"-----BEGIN RSA PRIVATE KEY-----\" and \"-----END RSA PRIVATE KEY-----\". An empty string is returned in read responses.  # noqa: E501

        :param rsa_private_key: The rsa_private_key of this CertificateKeyPair.  # noqa: E501
        :type: str
        """

        self._rsa_private_key = rsa_private_key

    @property
    def certificate(self):
        """Gets the certificate of this CertificateKeyPair.  # noqa: E501


        :return: The certificate of this CertificateKeyPair.  # noqa: E501
        :rtype: SecurityCertificate
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this CertificateKeyPair.


        :param certificate: The certificate of this CertificateKeyPair.  # noqa: E501
        :type: SecurityCertificate
        """
        if certificate is None:
            raise ValueError("Invalid value for `certificate`, must not be `None`")  # noqa: E501

        self._certificate = certificate

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
        if issubclass(CertificateKeyPair, dict):
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
        if not isinstance(other, CertificateKeyPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
