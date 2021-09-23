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

class Footer(object):
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
        'condition': 'str',
        'actions': 'list[FooterAction]'
    }

    attribute_map = {
        'condition': 'condition',
        'actions': 'actions'
    }

    def __init__(self, condition=None, actions=None):  # noqa: E501
        """Footer - a model defined in Swagger"""  # noqa: E501
        self._condition = None
        self._actions = None
        self.discriminator = None
        if condition is not None:
            self.condition = condition
        if actions is not None:
            self.actions = actions

    @property
    def condition(self):
        """Gets the condition of this Footer.  # noqa: E501

        If the condition is met then the footer will be applied. Examples of expression syntax are provided under 'example_request' section of 'CreateWidgetConfiguration' API.  # noqa: E501

        :return: The condition of this Footer.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this Footer.

        If the condition is met then the footer will be applied. Examples of expression syntax are provided under 'example_request' section of 'CreateWidgetConfiguration' API.  # noqa: E501

        :param condition: The condition of this Footer.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def actions(self):
        """Gets the actions of this Footer.  # noqa: E501

        Action to be performed at the footer of a widget. An action at the footer can be simple text description or a hyperlink to a UI page. Action allows a clickable url for navigation. An example usage of footer action is provided under 'example_request' section of 'CreateWidgetConfiguration' API.  # noqa: E501

        :return: The actions of this Footer.  # noqa: E501
        :rtype: list[FooterAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Footer.

        Action to be performed at the footer of a widget. An action at the footer can be simple text description or a hyperlink to a UI page. Action allows a clickable url for navigation. An example usage of footer action is provided under 'example_request' section of 'CreateWidgetConfiguration' API.  # noqa: E501

        :param actions: The actions of this Footer.  # noqa: E501
        :type: list[FooterAction]
        """

        self._actions = actions

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
        if issubclass(Footer, dict):
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
        if not isinstance(other, Footer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
