# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Product(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, title: str=None, description: str=None, procedures: List[str]=None, feature_of_interest: List[str]=None, pds4_label_url: str=None, properties: Dict[str, List[str]]=None):  # noqa: E501
        """Product - a model defined in Swagger

        :param id: The id of this Product.  # noqa: E501
        :type id: str
        :param title: The title of this Product.  # noqa: E501
        :type title: str
        :param description: The description of this Product.  # noqa: E501
        :type description: str
        :param procedures: The procedures of this Product.  # noqa: E501
        :type procedures: List[str]
        :param feature_of_interest: The feature_of_interest of this Product.  # noqa: E501
        :type feature_of_interest: List[str]
        :param pds4_label_url: The pds4_label_url of this Product.  # noqa: E501
        :type pds4_label_url: str
        :param properties: The properties of this Product.  # noqa: E501
        :type properties: Dict[str, List[str]]
        """
        self.swagger_types = {
            'id': str,
            'title': str,
            'description': str,
            'procedures': List[str],
            'feature_of_interest': List[str],
            'pds4_label_url': str,
            'properties': Dict[str, List[str]]
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'description': 'description',
            'procedures': 'procedures',
            'feature_of_interest': 'feature_of_interest',
            'pds4_label_url': 'pds4_label_url',
            'properties': 'properties'
        }
        self._id = id
        self._title = title
        self._description = description
        self._procedures = procedures
        self._feature_of_interest = feature_of_interest
        self._pds4_label_url = pds4_label_url
        self._properties = properties

    @classmethod
    def from_dict(cls, dikt) -> 'Product':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product of this Product.  # noqa: E501
        :rtype: Product
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Product.

        identifier lidvid of the collection  # noqa: E501

        :return: The id of this Product.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Product.

        identifier lidvid of the collection  # noqa: E501

        :param id: The id of this Product.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self) -> str:
        """Gets the title of this Product.


        :return: The title of this Product.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Product.


        :param title: The title of this Product.
        :type title: str
        """

        self._title = title

    @property
    def description(self) -> str:
        """Gets the description of this Product.


        :return: The description of this Product.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Product.


        :param description: The description of this Product.
        :type description: str
        """

        self._description = description

    @property
    def procedures(self) -> List[str]:
        """Gets the procedures of this Product.

        identifier lidvid of the instrument or procedure generating the data (for concept see https://en.wikipedia.org/wiki/Observations_and_Measurements)  # noqa: E501

        :return: The procedures of this Product.
        :rtype: List[str]
        """
        return self._procedures

    @procedures.setter
    def procedures(self, procedures: List[str]):
        """Sets the procedures of this Product.

        identifier lidvid of the instrument or procedure generating the data (for concept see https://en.wikipedia.org/wiki/Observations_and_Measurements)  # noqa: E501

        :param procedures: The procedures of this Product.
        :type procedures: List[str]
        """

        self._procedures = procedures

    @property
    def feature_of_interest(self) -> List[str]:
        """Gets the feature_of_interest of this Product.

        identifier lidvid of the target of or feature of interest the observation (for concept see https://en.wikipedia.org/wiki/Observations_and_Measurements)  # noqa: E501

        :return: The feature_of_interest of this Product.
        :rtype: List[str]
        """
        return self._feature_of_interest

    @feature_of_interest.setter
    def feature_of_interest(self, feature_of_interest: List[str]):
        """Sets the feature_of_interest of this Product.

        identifier lidvid of the target of or feature of interest the observation (for concept see https://en.wikipedia.org/wiki/Observations_and_Measurements)  # noqa: E501

        :param feature_of_interest: The feature_of_interest of this Product.
        :type feature_of_interest: List[str]
        """

        self._feature_of_interest = feature_of_interest

    @property
    def pds4_label_url(self) -> str:
        """Gets the pds4_label_url of this Product.


        :return: The pds4_label_url of this Product.
        :rtype: str
        """
        return self._pds4_label_url

    @pds4_label_url.setter
    def pds4_label_url(self, pds4_label_url: str):
        """Sets the pds4_label_url of this Product.


        :param pds4_label_url: The pds4_label_url of this Product.
        :type pds4_label_url: str
        """

        self._pds4_label_url = pds4_label_url

    @property
    def properties(self) -> Dict[str, List[str]]:
        """Gets the properties of this Product.


        :return: The properties of this Product.
        :rtype: Dict[str, List[str]]
        """
        return self._properties

    @properties.setter
    def properties(self, properties: Dict[str, List[str]]):
        """Sets the properties of this Product.


        :param properties: The properties of this Product.
        :type properties: Dict[str, List[str]]
        """

        self._properties = properties
