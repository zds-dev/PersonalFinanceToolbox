from abc import ABC, abstractmethod
from .helpers import date_range
import numpy as np
from dateutil.relativedelta import relativedelta


class ValueHolding(ABC):
    """
    Abstract class for a value holding object.

    A value holding object is an object that holds a value at a given date.
    This class is used to represent assets, liabilities and other value holding objects through
    subclasses.

    All value holding objects must implement the get_value method which returns the value of the
    object at a given date.

    The generate_timeseries method is a convenience method that returns a numpy array of values
    for a given date range.
    """

    @abstractmethod
    def get_value(self, date):
        raise NotImplementedError

    def generate_timeseries(self, to_datetime, from_datetime, discretization: relativedelta = relativedelta(years=1)):
        return np.array([self.get_value(date) for date in date_range(from_datetime, to_datetime, discretization)])

