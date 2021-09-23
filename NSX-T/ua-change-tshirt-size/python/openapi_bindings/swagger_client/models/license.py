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

class License(Resource):
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
        'features': 'str',
        'description': 'str',
        'product_version': 'str',
        'expiry': 'int',
        'is_eval': 'bool',
        'is_mh': 'bool',
        'license_key': 'str',
        'is_expired': 'bool',
        'product_name': 'str',
        'capacity_type': 'str',
        'quantity': 'int'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        'features': 'features',
        'description': 'description',
        'product_version': 'product_version',
        'expiry': 'expiry',
        'is_eval': 'is_eval',
        'is_mh': 'is_mh',
        'license_key': 'license_key',
        'is_expired': 'is_expired',
        'product_name': 'product_name',
        'capacity_type': 'capacity_type',
        'quantity': 'quantity'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, features=None, description=None, product_version=None, expiry=None, is_eval=None, is_mh=None, license_key=None, is_expired=None, product_name=None, capacity_type=None, quantity=None, *args, **kwargs):  # noqa: E501
        """License - a model defined in Swagger"""  # noqa: E501
        self._features = None
        self._description = None
        self._product_version = None
        self._expiry = None
        self._is_eval = None
        self._is_mh = None
        self._license_key = None
        self._is_expired = None
        self._product_name = None
        self._capacity_type = None
        self._quantity = None
        self.discriminator = None
        if features is not None:
            self.features = features
        if description is not None:
            self.description = description
        if product_version is not None:
            self.product_version = product_version
        if expiry is not None:
            self.expiry = expiry
        if is_eval is not None:
            self.is_eval = is_eval
        if is_mh is not None:
            self.is_mh = is_mh
        if license_key is not None:
            self.license_key = license_key
        if is_expired is not None:
            self.is_expired = is_expired
        if product_name is not None:
            self.product_name = product_name
        if capacity_type is not None:
            self.capacity_type = capacity_type
        if quantity is not None:
            self.quantity = quantity
        Resource.__init__(self, *args, **kwargs)

    @property
    def features(self):
        """Gets the features of this License.  # noqa: E501

        semicolon delimited feature list  # noqa: E501

        :return: The features of this License.  # noqa: E501
        :rtype: str
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this License.

        semicolon delimited feature list  # noqa: E501

        :param features: The features of this License.  # noqa: E501
        :type: str
        """

        self._features = features

    @property
    def description(self):
        """Gets the description of this License.  # noqa: E501

        license edition  # noqa: E501

        :return: The description of this License.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this License.

        license edition  # noqa: E501

        :param description: The description of this License.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def product_version(self):
        """Gets the product_version of this License.  # noqa: E501

        product version  # noqa: E501

        :return: The product_version of this License.  # noqa: E501
        :rtype: str
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """Sets the product_version of this License.

        product version  # noqa: E501

        :param product_version: The product_version of this License.  # noqa: E501
        :type: str
        """

        self._product_version = product_version

    @property
    def expiry(self):
        """Gets the expiry of this License.  # noqa: E501

        date that license expires  # noqa: E501

        :return: The expiry of this License.  # noqa: E501
        :rtype: int
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this License.

        date that license expires  # noqa: E501

        :param expiry: The expiry of this License.  # noqa: E501
        :type: int
        """

        self._expiry = expiry

    @property
    def is_eval(self):
        """Gets the is_eval of this License.  # noqa: E501

        true for evalution license  # noqa: E501

        :return: The is_eval of this License.  # noqa: E501
        :rtype: bool
        """
        return self._is_eval

    @is_eval.setter
    def is_eval(self, is_eval):
        """Sets the is_eval of this License.

        true for evalution license  # noqa: E501

        :param is_eval: The is_eval of this License.  # noqa: E501
        :type: bool
        """

        self._is_eval = is_eval

    @property
    def is_mh(self):
        """Gets the is_mh of this License.  # noqa: E501

        multi-hypervisor support  # noqa: E501

        :return: The is_mh of this License.  # noqa: E501
        :rtype: bool
        """
        return self._is_mh

    @is_mh.setter
    def is_mh(self, is_mh):
        """Sets the is_mh of this License.

        multi-hypervisor support  # noqa: E501

        :param is_mh: The is_mh of this License.  # noqa: E501
        :type: bool
        """

        self._is_mh = is_mh

    @property
    def license_key(self):
        """Gets the license_key of this License.  # noqa: E501

        license key  # noqa: E501

        :return: The license_key of this License.  # noqa: E501
        :rtype: str
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """Sets the license_key of this License.

        license key  # noqa: E501

        :param license_key: The license_key of this License.  # noqa: E501
        :type: str
        """

        self._license_key = license_key

    @property
    def is_expired(self):
        """Gets the is_expired of this License.  # noqa: E501

        whether the license has expired  # noqa: E501

        :return: The is_expired of this License.  # noqa: E501
        :rtype: bool
        """
        return self._is_expired

    @is_expired.setter
    def is_expired(self, is_expired):
        """Sets the is_expired of this License.

        whether the license has expired  # noqa: E501

        :param is_expired: The is_expired of this License.  # noqa: E501
        :type: bool
        """

        self._is_expired = is_expired

    @property
    def product_name(self):
        """Gets the product_name of this License.  # noqa: E501

        product name  # noqa: E501

        :return: The product_name of this License.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this License.

        product name  # noqa: E501

        :param product_name: The product_name of this License.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def capacity_type(self):
        """Gets the capacity_type of this License.  # noqa: E501

        License metrics specifying the capacity type of license key. Types are: - VM - CPU - USER(Concurrent User) - CORE - HOST   # noqa: E501

        :return: The capacity_type of this License.  # noqa: E501
        :rtype: str
        """
        return self._capacity_type

    @capacity_type.setter
    def capacity_type(self, capacity_type):
        """Sets the capacity_type of this License.

        License metrics specifying the capacity type of license key. Types are: - VM - CPU - USER(Concurrent User) - CORE - HOST   # noqa: E501

        :param capacity_type: The capacity_type of this License.  # noqa: E501
        :type: str
        """
        allowed_values = ["VM", "CPU", "USER", "CORE", "HOST"]  # noqa: E501
        if capacity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `capacity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(capacity_type, allowed_values)
            )

        self._capacity_type = capacity_type

    @property
    def quantity(self):
        """Gets the quantity of this License.  # noqa: E501

        license capacity; 0 for unlimited  # noqa: E501

        :return: The quantity of this License.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this License.

        license capacity; 0 for unlimited  # noqa: E501

        :param quantity: The quantity of this License.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if issubclass(License, dict):
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
        if not isinstance(other, License):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
