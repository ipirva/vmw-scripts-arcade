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

class RenderConfiguration(object):
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
        'color': 'str',
        'condition': 'str',
        'display_value': 'str',
        'tooltip': 'list[Tooltip]',
        'icons': 'list[Icon]'
    }

    attribute_map = {
        'color': 'color',
        'condition': 'condition',
        'display_value': 'display_value',
        'tooltip': 'tooltip',
        'icons': 'icons'
    }

    def __init__(self, color=None, condition=None, display_value=None, tooltip=None, icons=None):  # noqa: E501
        """RenderConfiguration - a model defined in Swagger"""  # noqa: E501
        self._color = None
        self._condition = None
        self._display_value = None
        self._tooltip = None
        self._icons = None
        self.discriminator = None
        if color is not None:
            self.color = color
        if condition is not None:
            self.condition = condition
        if display_value is not None:
            self.display_value = display_value
        if tooltip is not None:
            self.tooltip = tooltip
        if icons is not None:
            self.icons = icons

    @property
    def color(self):
        """Gets the color of this RenderConfiguration.  # noqa: E501

        The color to use when rendering an entity. For example, set color as 'RED' to render a portion of donut in red.  # noqa: E501

        :return: The color of this RenderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this RenderConfiguration.

        The color to use when rendering an entity. For example, set color as 'RED' to render a portion of donut in red.  # noqa: E501

        :param color: The color of this RenderConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["GREY", "DARK_GREY", "LIGHT_GREY", "SKY_BLUE", "BLUE", "GREEN", "YELLOW", "RED", "DARK_RED"]  # noqa: E501
        if color not in allowed_values:
            raise ValueError(
                "Invalid value for `color` ({0}), must be one of {1}"  # noqa: E501
                .format(color, allowed_values)
            )

        self._color = color

    @property
    def condition(self):
        """Gets the condition of this RenderConfiguration.  # noqa: E501

        If the condition is met then the rendering specified for the condition will be applied. Examples of expression syntax are provided under 'example_request' section of 'CreateWidgetConfiguration' API.  # noqa: E501

        :return: The condition of this RenderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this RenderConfiguration.

        If the condition is met then the rendering specified for the condition will be applied. Examples of expression syntax are provided under 'example_request' section of 'CreateWidgetConfiguration' API.  # noqa: E501

        :param condition: The condition of this RenderConfiguration.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def display_value(self):
        """Gets the display_value of this RenderConfiguration.  # noqa: E501

        If specified, overrides the field value. This can be used to display a meaningful value in situations where field value is not available or not configured.  # noqa: E501

        :return: The display_value of this RenderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        """Sets the display_value of this RenderConfiguration.

        If specified, overrides the field value. This can be used to display a meaningful value in situations where field value is not available or not configured.  # noqa: E501

        :param display_value: The display_value of this RenderConfiguration.  # noqa: E501
        :type: str
        """

        self._display_value = display_value

    @property
    def tooltip(self):
        """Gets the tooltip of this RenderConfiguration.  # noqa: E501

        Multi-line text to be shown on tooltip while hovering over the UI element if the condition is met.  # noqa: E501

        :return: The tooltip of this RenderConfiguration.  # noqa: E501
        :rtype: list[Tooltip]
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this RenderConfiguration.

        Multi-line text to be shown on tooltip while hovering over the UI element if the condition is met.  # noqa: E501

        :param tooltip: The tooltip of this RenderConfiguration.  # noqa: E501
        :type: list[Tooltip]
        """

        self._tooltip = tooltip

    @property
    def icons(self):
        """Gets the icons of this RenderConfiguration.  # noqa: E501

        Icons to be applied at dashboard for widgets and UI elements.  # noqa: E501

        :return: The icons of this RenderConfiguration.  # noqa: E501
        :rtype: list[Icon]
        """
        return self._icons

    @icons.setter
    def icons(self, icons):
        """Sets the icons of this RenderConfiguration.

        Icons to be applied at dashboard for widgets and UI elements.  # noqa: E501

        :param icons: The icons of this RenderConfiguration.  # noqa: E501
        :type: list[Icon]
        """

        self._icons = icons

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
        if issubclass(RenderConfiguration, dict):
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
        if not isinstance(other, RenderConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other