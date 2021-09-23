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

class X509Crl(object):
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
        'next_update': 'str',
        'version': 'str',
        'crl_entries': 'list[X509CrlEntry]',
        'issuer': 'str'
    }

    attribute_map = {
        'next_update': 'next_update',
        'version': 'version',
        'crl_entries': 'crl_entries',
        'issuer': 'issuer'
    }

    def __init__(self, next_update=None, version=None, crl_entries=None, issuer=None):  # noqa: E501
        """X509Crl - a model defined in Swagger"""  # noqa: E501
        self._next_update = None
        self._version = None
        self._crl_entries = None
        self._issuer = None
        self.discriminator = None
        if next_update is not None:
            self.next_update = next_update
        if version is not None:
            self.version = version
        if crl_entries is not None:
            self.crl_entries = crl_entries
        if issuer is not None:
            self.issuer = issuer

    @property
    def next_update(self):
        """Gets the next_update of this X509Crl.  # noqa: E501

        Next update time for the CRL.  # noqa: E501

        :return: The next_update of this X509Crl.  # noqa: E501
        :rtype: str
        """
        return self._next_update

    @next_update.setter
    def next_update(self, next_update):
        """Sets the next_update of this X509Crl.

        Next update time for the CRL.  # noqa: E501

        :param next_update: The next_update of this X509Crl.  # noqa: E501
        :type: str
        """

        self._next_update = next_update

    @property
    def version(self):
        """Gets the version of this X509Crl.  # noqa: E501

        CRL's version number either 1 or 2.  # noqa: E501

        :return: The version of this X509Crl.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this X509Crl.

        CRL's version number either 1 or 2.  # noqa: E501

        :param version: The version of this X509Crl.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def crl_entries(self):
        """Gets the crl_entries of this X509Crl.  # noqa: E501

        List of X509CrlEntry.  # noqa: E501

        :return: The crl_entries of this X509Crl.  # noqa: E501
        :rtype: list[X509CrlEntry]
        """
        return self._crl_entries

    @crl_entries.setter
    def crl_entries(self, crl_entries):
        """Sets the crl_entries of this X509Crl.

        List of X509CrlEntry.  # noqa: E501

        :param crl_entries: The crl_entries of this X509Crl.  # noqa: E501
        :type: list[X509CrlEntry]
        """

        self._crl_entries = crl_entries

    @property
    def issuer(self):
        """Gets the issuer of this X509Crl.  # noqa: E501

        Issuer's distinguished name. (DN)  # noqa: E501

        :return: The issuer of this X509Crl.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this X509Crl.

        Issuer's distinguished name. (DN)  # noqa: E501

        :param issuer: The issuer of this X509Crl.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

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
        if issubclass(X509Crl, dict):
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
        if not isinstance(other, X509Crl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
