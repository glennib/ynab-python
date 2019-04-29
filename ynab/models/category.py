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


class Category(object):
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
        'category_group_id': 'str',
        'name': 'str',
        'hidden': 'bool',
        'original_category_group_id': 'str',
        'note': 'str',
        'budgeted': 'int',
        'activity': 'int',
        'balance': 'int',
        'goal_type': 'str',
        'goal_creation_month': 'date',
        'goal_target': 'int',
        'goal_target_month': 'date',
        'goal_percentage_complete': 'int',
        'deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'category_group_id': 'category_group_id',
        'name': 'name',
        'hidden': 'hidden',
        'original_category_group_id': 'original_category_group_id',
        'note': 'note',
        'budgeted': 'budgeted',
        'activity': 'activity',
        'balance': 'balance',
        'goal_type': 'goal_type',
        'goal_creation_month': 'goal_creation_month',
        'goal_target': 'goal_target',
        'goal_target_month': 'goal_target_month',
        'goal_percentage_complete': 'goal_percentage_complete',
        'deleted': 'deleted'
    }

    def __init__(self, id=None, category_group_id=None, name=None, hidden=None, original_category_group_id=None, note=None, budgeted=None, activity=None, balance=None, goal_type=None, goal_creation_month=None, goal_target=None, goal_target_month=None, goal_percentage_complete=None, deleted=None):  # noqa: E501
        """Category - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._category_group_id = None
        self._name = None
        self._hidden = None
        self._original_category_group_id = None
        self._note = None
        self._budgeted = None
        self._activity = None
        self._balance = None
        self._goal_type = None
        self._goal_creation_month = None
        self._goal_target = None
        self._goal_target_month = None
        self._goal_percentage_complete = None
        self._deleted = None
        self.discriminator = None
        self.id = id
        self.category_group_id = category_group_id
        self.name = name
        self.hidden = hidden
        if original_category_group_id is not None:
            self.original_category_group_id = original_category_group_id
        self.note = note
        self.budgeted = budgeted
        self.activity = activity
        self.balance = balance
        self.goal_type = goal_type
        self.goal_creation_month = goal_creation_month
        self.goal_target = goal_target
        self.goal_target_month = goal_target_month
        self.goal_percentage_complete = goal_percentage_complete
        self.deleted = deleted

    @property
    def id(self):
        """Gets the id of this Category.  # noqa: E501


        :return: The id of this Category.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Category.


        :param id: The id of this Category.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def category_group_id(self):
        """Gets the category_group_id of this Category.  # noqa: E501


        :return: The category_group_id of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_group_id

    @category_group_id.setter
    def category_group_id(self, category_group_id):
        """Sets the category_group_id of this Category.


        :param category_group_id: The category_group_id of this Category.  # noqa: E501
        :type: str
        """
        if category_group_id is None:
            raise ValueError("Invalid value for `category_group_id`, must not be `None`")  # noqa: E501

        self._category_group_id = category_group_id

    @property
    def name(self):
        """Gets the name of this Category.  # noqa: E501


        :return: The name of this Category.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Category.


        :param name: The name of this Category.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def hidden(self):
        """Gets the hidden of this Category.  # noqa: E501

        Whether or not the category is hidden  # noqa: E501

        :return: The hidden of this Category.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Category.

        Whether or not the category is hidden  # noqa: E501

        :param hidden: The hidden of this Category.  # noqa: E501
        :type: bool
        """
        if hidden is None:
            raise ValueError("Invalid value for `hidden`, must not be `None`")  # noqa: E501

        self._hidden = hidden

    @property
    def original_category_group_id(self):
        """Gets the original_category_group_id of this Category.  # noqa: E501

        If category is hidden this is the id of the category group it originally belonged to before it was hidden.  # noqa: E501

        :return: The original_category_group_id of this Category.  # noqa: E501
        :rtype: str
        """
        return self._original_category_group_id

    @original_category_group_id.setter
    def original_category_group_id(self, original_category_group_id):
        """Sets the original_category_group_id of this Category.

        If category is hidden this is the id of the category group it originally belonged to before it was hidden.  # noqa: E501

        :param original_category_group_id: The original_category_group_id of this Category.  # noqa: E501
        :type: str
        """

        self._original_category_group_id = original_category_group_id

    @property
    def note(self):
        """Gets the note of this Category.  # noqa: E501


        :return: The note of this Category.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Category.


        :param note: The note of this Category.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def budgeted(self):
        """Gets the budgeted of this Category.  # noqa: E501

        Budgeted amount in milliunits format  # noqa: E501

        :return: The budgeted of this Category.  # noqa: E501
        :rtype: int
        """
        return self._budgeted

    @budgeted.setter
    def budgeted(self, budgeted):
        """Sets the budgeted of this Category.

        Budgeted amount in milliunits format  # noqa: E501

        :param budgeted: The budgeted of this Category.  # noqa: E501
        :type: int
        """
        if budgeted is None:
            raise ValueError("Invalid value for `budgeted`, must not be `None`")  # noqa: E501

        self._budgeted = budgeted

    @property
    def activity(self):
        """Gets the activity of this Category.  # noqa: E501

        Activity amount in milliunits format  # noqa: E501

        :return: The activity of this Category.  # noqa: E501
        :rtype: int
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this Category.

        Activity amount in milliunits format  # noqa: E501

        :param activity: The activity of this Category.  # noqa: E501
        :type: int
        """
        if activity is None:
            raise ValueError("Invalid value for `activity`, must not be `None`")  # noqa: E501

        self._activity = activity

    @property
    def balance(self):
        """Gets the balance of this Category.  # noqa: E501

        Balance in milliunits format  # noqa: E501

        :return: The balance of this Category.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Category.

        Balance in milliunits format  # noqa: E501

        :param balance: The balance of this Category.  # noqa: E501
        :type: int
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def goal_type(self):
        """Gets the goal_type of this Category.  # noqa: E501

        The type of goal, if the cagegory has a goal (TB=Target Category Balance, TBD=Target Category Balance by Date, MF=Monthly Funding)  # noqa: E501

        :return: The goal_type of this Category.  # noqa: E501
        :rtype: str
        """
        return self._goal_type

    @goal_type.setter
    def goal_type(self, goal_type):
        """Sets the goal_type of this Category.

        The type of goal, if the cagegory has a goal (TB=Target Category Balance, TBD=Target Category Balance by Date, MF=Monthly Funding)  # noqa: E501

        :param goal_type: The goal_type of this Category.  # noqa: E501
        :type: str
        """
        if goal_type is None:
            raise ValueError("Invalid value for `goal_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TB", "TBD", "MF"]  # noqa: E501
        if goal_type not in allowed_values:
            raise ValueError(
                "Invalid value for `goal_type` ({0}), must be one of {1}"  # noqa: E501
                .format(goal_type, allowed_values)
            )

        self._goal_type = goal_type

    @property
    def goal_creation_month(self):
        """Gets the goal_creation_month of this Category.  # noqa: E501

        The month a goal was created  # noqa: E501

        :return: The goal_creation_month of this Category.  # noqa: E501
        :rtype: date
        """
        return self._goal_creation_month

    @goal_creation_month.setter
    def goal_creation_month(self, goal_creation_month):
        """Sets the goal_creation_month of this Category.

        The month a goal was created  # noqa: E501

        :param goal_creation_month: The goal_creation_month of this Category.  # noqa: E501
        :type: date
        """
        if goal_creation_month is None:
            raise ValueError("Invalid value for `goal_creation_month`, must not be `None`")  # noqa: E501

        self._goal_creation_month = goal_creation_month

    @property
    def goal_target(self):
        """Gets the goal_target of this Category.  # noqa: E501

        The goal target amount in milliunits  # noqa: E501

        :return: The goal_target of this Category.  # noqa: E501
        :rtype: int
        """
        return self._goal_target

    @goal_target.setter
    def goal_target(self, goal_target):
        """Sets the goal_target of this Category.

        The goal target amount in milliunits  # noqa: E501

        :param goal_target: The goal_target of this Category.  # noqa: E501
        :type: int
        """
        if goal_target is None:
            raise ValueError("Invalid value for `goal_target`, must not be `None`")  # noqa: E501

        self._goal_target = goal_target

    @property
    def goal_target_month(self):
        """Gets the goal_target_month of this Category.  # noqa: E501

        If the goal type is 'TBD' (Target Category Balance by Date), this is the target month for the goal to be completed  # noqa: E501

        :return: The goal_target_month of this Category.  # noqa: E501
        :rtype: date
        """
        return self._goal_target_month

    @goal_target_month.setter
    def goal_target_month(self, goal_target_month):
        """Sets the goal_target_month of this Category.

        If the goal type is 'TBD' (Target Category Balance by Date), this is the target month for the goal to be completed  # noqa: E501

        :param goal_target_month: The goal_target_month of this Category.  # noqa: E501
        :type: date
        """
        if goal_target_month is None:
            raise ValueError("Invalid value for `goal_target_month`, must not be `None`")  # noqa: E501

        self._goal_target_month = goal_target_month

    @property
    def goal_percentage_complete(self):
        """Gets the goal_percentage_complete of this Category.  # noqa: E501

        The percentage completion of the goal  # noqa: E501

        :return: The goal_percentage_complete of this Category.  # noqa: E501
        :rtype: int
        """
        return self._goal_percentage_complete

    @goal_percentage_complete.setter
    def goal_percentage_complete(self, goal_percentage_complete):
        """Sets the goal_percentage_complete of this Category.

        The percentage completion of the goal  # noqa: E501

        :param goal_percentage_complete: The goal_percentage_complete of this Category.  # noqa: E501
        :type: int
        """
        if goal_percentage_complete is None:
            raise ValueError("Invalid value for `goal_percentage_complete`, must not be `None`")  # noqa: E501

        self._goal_percentage_complete = goal_percentage_complete

    @property
    def deleted(self):
        """Gets the deleted of this Category.  # noqa: E501

        Whether or not the category has been deleted.  Deleted categories will only be included in delta requests.  # noqa: E501

        :return: The deleted of this Category.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Category.

        Whether or not the category has been deleted.  Deleted categories will only be included in delta requests.  # noqa: E501

        :param deleted: The deleted of this Category.  # noqa: E501
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
        if issubclass(Category, dict):
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
        if not isinstance(other, Category):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
