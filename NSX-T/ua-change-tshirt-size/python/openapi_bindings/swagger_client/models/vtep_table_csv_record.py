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
from swagger_client.models.csv_record import CsvRecord  # noqa: F401,E501

class VtepTableCsvRecord(CsvRecord):
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
        'vtep_label': 'int',
        'vtep_mac_address': 'str',
        'vtep_ip': 'str',
        'segment_id': 'str'
    }
    if hasattr(CsvRecord, "swagger_types"):
        swagger_types.update(CsvRecord.swagger_types)

    attribute_map = {
        'vtep_label': 'vtep_label',
        'vtep_mac_address': 'vtep_mac_address',
        'vtep_ip': 'vtep_ip',
        'segment_id': 'segment_id'
    }
    if hasattr(CsvRecord, "attribute_map"):
        attribute_map.update(CsvRecord.attribute_map)

    def __init__(self, vtep_label=None, vtep_mac_address=None, vtep_ip=None, segment_id=None, *args, **kwargs):  # noqa: E501
        """VtepTableCsvRecord - a model defined in Swagger"""  # noqa: E501
        self._vtep_label = None
        self._vtep_mac_address = None
        self._vtep_ip = None
        self._segment_id = None
        self.discriminator = None
        self.vtep_label = vtep_label
        self.vtep_mac_address = vtep_mac_address
        if vtep_ip is not None:
            self.vtep_ip = vtep_ip
        if segment_id is not None:
            self.segment_id = segment_id
        CsvRecord.__init__(self, *args, **kwargs)

    @property
    def vtep_label(self):
        """Gets the vtep_label of this VtepTableCsvRecord.  # noqa: E501

        The virtual tunnel endpoint label  # noqa: E501

        :return: The vtep_label of this VtepTableCsvRecord.  # noqa: E501
        :rtype: int
        """
        return self._vtep_label

    @vtep_label.setter
    def vtep_label(self, vtep_label):
        """Sets the vtep_label of this VtepTableCsvRecord.

        The virtual tunnel endpoint label  # noqa: E501

        :param vtep_label: The vtep_label of this VtepTableCsvRecord.  # noqa: E501
        :type: int
        """
        if vtep_label is None:
            raise ValueError("Invalid value for `vtep_label`, must not be `None`")  # noqa: E501

        self._vtep_label = vtep_label

    @property
    def vtep_mac_address(self):
        """Gets the vtep_mac_address of this VtepTableCsvRecord.  # noqa: E501

        The virtual tunnel endpoint MAC address  # noqa: E501

        :return: The vtep_mac_address of this VtepTableCsvRecord.  # noqa: E501
        :rtype: str
        """
        return self._vtep_mac_address

    @vtep_mac_address.setter
    def vtep_mac_address(self, vtep_mac_address):
        """Sets the vtep_mac_address of this VtepTableCsvRecord.

        The virtual tunnel endpoint MAC address  # noqa: E501

        :param vtep_mac_address: The vtep_mac_address of this VtepTableCsvRecord.  # noqa: E501
        :type: str
        """
        if vtep_mac_address is None:
            raise ValueError("Invalid value for `vtep_mac_address`, must not be `None`")  # noqa: E501

        self._vtep_mac_address = vtep_mac_address

    @property
    def vtep_ip(self):
        """Gets the vtep_ip of this VtepTableCsvRecord.  # noqa: E501

        The virtual tunnel endpoint IP address  # noqa: E501

        :return: The vtep_ip of this VtepTableCsvRecord.  # noqa: E501
        :rtype: str
        """
        return self._vtep_ip

    @vtep_ip.setter
    def vtep_ip(self, vtep_ip):
        """Sets the vtep_ip of this VtepTableCsvRecord.

        The virtual tunnel endpoint IP address  # noqa: E501

        :param vtep_ip: The vtep_ip of this VtepTableCsvRecord.  # noqa: E501
        :type: str
        """

        self._vtep_ip = vtep_ip

    @property
    def segment_id(self):
        """Gets the segment_id of this VtepTableCsvRecord.  # noqa: E501

        The segment Id  # noqa: E501

        :return: The segment_id of this VtepTableCsvRecord.  # noqa: E501
        :rtype: str
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this VtepTableCsvRecord.

        The segment Id  # noqa: E501

        :param segment_id: The segment_id of this VtepTableCsvRecord.  # noqa: E501
        :type: str
        """

        self._segment_id = segment_id

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
        if issubclass(VtepTableCsvRecord, dict):
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
        if not isinstance(other, VtepTableCsvRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other