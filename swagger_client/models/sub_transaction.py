# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SubTransaction(object):
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
        'id': 'str',
        'transaction_id': 'str',
        'amount': 'int',
        'memo': 'str',
        'payee_id': 'str',
        'category_id': 'str',
        'transfer_account_id': 'str',
        'deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'transaction_id': 'transaction_id',
        'amount': 'amount',
        'memo': 'memo',
        'payee_id': 'payee_id',
        'category_id': 'category_id',
        'transfer_account_id': 'transfer_account_id',
        'deleted': 'deleted'
    }

    def __init__(self, id=None, transaction_id=None, amount=None, memo=None, payee_id=None, category_id=None, transfer_account_id=None, deleted=None):  # noqa: E501
        """SubTransaction - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._transaction_id = None
        self._amount = None
        self._memo = None
        self._payee_id = None
        self._category_id = None
        self._transfer_account_id = None
        self._deleted = None
        self.discriminator = None

        self.id = id
        self.transaction_id = transaction_id
        self.amount = amount
        self.memo = memo
        self.payee_id = payee_id
        self.category_id = category_id
        self.transfer_account_id = transfer_account_id
        self.deleted = deleted

    @property
    def id(self):
        """Gets the id of this SubTransaction.  # noqa: E501


        :return: The id of this SubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubTransaction.


        :param id: The id of this SubTransaction.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def transaction_id(self):
        """Gets the transaction_id of this SubTransaction.  # noqa: E501


        :return: The transaction_id of this SubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this SubTransaction.


        :param transaction_id: The transaction_id of this SubTransaction.  # noqa: E501
        :type: str
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def amount(self):
        """Gets the amount of this SubTransaction.  # noqa: E501

        The subtransaction amount in milliunits format  # noqa: E501

        :return: The amount of this SubTransaction.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SubTransaction.

        The subtransaction amount in milliunits format  # noqa: E501

        :param amount: The amount of this SubTransaction.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def memo(self):
        """Gets the memo of this SubTransaction.  # noqa: E501


        :return: The memo of this SubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this SubTransaction.


        :param memo: The memo of this SubTransaction.  # noqa: E501
        :type: str
        """
        if memo is None:
            raise ValueError("Invalid value for `memo`, must not be `None`")  # noqa: E501

        self._memo = memo

    @property
    def payee_id(self):
        """Gets the payee_id of this SubTransaction.  # noqa: E501


        :return: The payee_id of this SubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this SubTransaction.


        :param payee_id: The payee_id of this SubTransaction.  # noqa: E501
        :type: str
        """
        if payee_id is None:
            raise ValueError("Invalid value for `payee_id`, must not be `None`")  # noqa: E501

        self._payee_id = payee_id

    @property
    def category_id(self):
        """Gets the category_id of this SubTransaction.  # noqa: E501


        :return: The category_id of this SubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this SubTransaction.


        :param category_id: The category_id of this SubTransaction.  # noqa: E501
        :type: str
        """
        if category_id is None:
            raise ValueError("Invalid value for `category_id`, must not be `None`")  # noqa: E501

        self._category_id = category_id

    @property
    def transfer_account_id(self):
        """Gets the transfer_account_id of this SubTransaction.  # noqa: E501

        If a transfer, the account_id which the subtransaction transfers to  # noqa: E501

        :return: The transfer_account_id of this SubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transfer_account_id

    @transfer_account_id.setter
    def transfer_account_id(self, transfer_account_id):
        """Sets the transfer_account_id of this SubTransaction.

        If a transfer, the account_id which the subtransaction transfers to  # noqa: E501

        :param transfer_account_id: The transfer_account_id of this SubTransaction.  # noqa: E501
        :type: str
        """
        if transfer_account_id is None:
            raise ValueError("Invalid value for `transfer_account_id`, must not be `None`")  # noqa: E501

        self._transfer_account_id = transfer_account_id

    @property
    def deleted(self):
        """Gets the deleted of this SubTransaction.  # noqa: E501

        Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be included in delta requests.  # noqa: E501

        :return: The deleted of this SubTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this SubTransaction.

        Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be included in delta requests.  # noqa: E501

        :param deleted: The deleted of this SubTransaction.  # noqa: E501
        :type: bool
        """
        if deleted is None:
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
