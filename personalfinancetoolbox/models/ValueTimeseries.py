from collections import UserDict
from datetime import datetime


class ValueTimeseries(UserDict):
    def __setitem__(self, key, value):
        # Assert key is datetime and value is number
        if not isinstance(key, datetime):
            raise TypeError('Key must be a datetime')
        if not isinstance(value, (int, float)):
            raise TypeError('Value must be a number')
        super().__setitem__(key, value)


class ValueLimitedTimeseries(ValueTimeseries):
    def __init__(self, *args, min_value=None, max_value=None, **kwargs):
        if min_value is None:
            min_value = -float('inf')
        if max_value is None:
            max_value = float('inf')
        self._min_value = min_value
        self._max_value = max_value

        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if value > self._max_value:
            raise ValueError('Value cannot be greater than {}'.format(self._max_value))
        if value < self._min_value:
            raise ValueError('Value cannot be less than {}'.format(self._min_value))
        super().__setitem__(key, value)

