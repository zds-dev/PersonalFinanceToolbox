from collections import UserDict
from datetime import datetime


class ValueTimeseries(UserDict):
    """A dictionary of datetime keys and number values.

    Also contains a secondary data structure with the same keys as the main data structure
    that stores the change in natural value from the previous datetime key - this may not be
    the same as the change in value from the previous datetime key as it is determined by the
    value dynamics defined by the object using this class."""
    def __init__(self, *args, repropogate_callback=lambda x: None, **kwargs):
        self.delta_value = {}
        self.recreate_timeseries_callback = repropogate_callback
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if type(value) == list and len(value) == 2:
            self.delta_value[key] = value[1]
            value = value[0]
        else:
            self.delta_value[key] = 0
        self.update_value(key, value)
        if len(self.data.keys()) > 1:
            if key < max(self.data.keys()):
                self.recreate_timeseries_callback(key)

    def update_value(self, key, value):
        # Assert key is datetime and value is number
        if not isinstance(key, datetime):
            raise TypeError('Key must be a datetime')
        if not isinstance(value, (int, float)):
            raise TypeError('Value must be a number')
        self.data[key] = value


class ValueLimitedTimeseries(ValueTimeseries):
    """A ValueTimeseries with a minimum and maximum value."""
    def __init__(self, *args, min_value=None, max_value=None, **kwargs):
        if min_value is None:
            min_value = -float('inf')
        if max_value is None:
            max_value = float('inf')
        self._min_value = min_value
        self._max_value = max_value

        super().__init__(*args, **kwargs)

    def update_value(self, key, value):
        if value > self._max_value:
            raise ValueError('Value cannot be greater than {}'.format(self._max_value))
        if value < self._min_value:
            raise ValueError('Value cannot be less than {}'.format(self._min_value))
        super().update_value(key, value)

