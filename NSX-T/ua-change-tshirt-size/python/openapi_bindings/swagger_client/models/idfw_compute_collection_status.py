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

class IdfwComputeCollectionStatus(object):
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
        'compute_collection_status': 'list[IdfwComputeCollectionCondition]',
        'compute_collection_id': 'str'
    }

    attribute_map = {
        'compute_collection_status': 'compute_collection_status',
        'compute_collection_id': 'compute_collection_id'
    }

    def __init__(self, compute_collection_status=None, compute_collection_id=None):  # noqa: E501
        """IdfwComputeCollectionStatus - a model defined in Swagger"""  # noqa: E501
        self._compute_collection_status = None
        self._compute_collection_id = None
        self.discriminator = None
        if compute_collection_status is not None:
            self.compute_collection_status = compute_collection_status
        self.compute_collection_id = compute_collection_id

    @property
    def compute_collection_status(self):
        """Gets the compute_collection_status of this IdfwComputeCollectionStatus.  # noqa: E501

        IDFW enabled compute collection status.  # noqa: E501

        :return: The compute_collection_status of this IdfwComputeCollectionStatus.  # noqa: E501
        :rtype: list[IdfwComputeCollectionCondition]
        """
        return self._compute_collection_status

    @compute_collection_status.setter
    def compute_collection_status(self, compute_collection_status):
        """Sets the compute_collection_status of this IdfwComputeCollectionStatus.

        IDFW enabled compute collection status.  # noqa: E501

        :param compute_collection_status: The compute_collection_status of this IdfwComputeCollectionStatus.  # noqa: E501
        :type: list[IdfwComputeCollectionCondition]
        """

        self._compute_collection_status = compute_collection_status

    @property
    def compute_collection_id(self):
        """Gets the compute_collection_id of this IdfwComputeCollectionStatus.  # noqa: E501

        IDFW compute collection ID connected to VC.  # noqa: E501

        :return: The compute_collection_id of this IdfwComputeCollectionStatus.  # noqa: E501
        :rtype: str
        """
        return self._compute_collection_id

    @compute_collection_id.setter
    def compute_collection_id(self, compute_collection_id):
        """Sets the compute_collection_id of this IdfwComputeCollectionStatus.

        IDFW compute collection ID connected to VC.  # noqa: E501

        :param compute_collection_id: The compute_collection_id of this IdfwComputeCollectionStatus.  # noqa: E501
        :type: str
        """
        if compute_collection_id is None:
            raise ValueError("Invalid value for `compute_collection_id`, must not be `None`")  # noqa: E501

        self._compute_collection_id = compute_collection_id

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
        if issubclass(IdfwComputeCollectionStatus, dict):
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
        if not isinstance(other, IdfwComputeCollectionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other