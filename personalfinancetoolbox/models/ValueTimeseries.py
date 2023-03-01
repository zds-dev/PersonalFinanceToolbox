from collections import UserDict
from datetime import datetime


class ValueTimeseries(UserDict):
    """
    A dictionary of datetime keys and number values - the number values represent the value of the
    timeseries at this point. Best practice is to use a secondary value i.e [main_value, delta_value]
    where delta_value is the change from the natural value of the timeseries at this point. This is
    defined independently of the main value and is unaware of any value dynamics that apply to the main
    value. This is important for recalculating the main value of the timeseries at any point in time.

    Since the main_value and delta_value are not aware of outside dynamics, when a delta_value is inserted
    into the timeseries, before a time already in the timeseries, a callback is applied which notifies or
    causes a calling or holding class to repropogate the timeseries from the new point onwards.

    This uses the delta_values and recalculates the main values allowing for the outer class to be able to
    use the main values as if they were the natural values of the timeseries.
    """

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
    """
    A modified ValueTimeseries with a minimum and maximum value.
    """
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

