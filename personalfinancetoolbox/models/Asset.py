from personalfinancetoolbox.models.CombinedAsset import CombinedAsset
from personalfinancetoolbox.models.ValueHolding import ValueHolding
from personalfinancetoolbox.models.ValueTimeseries import ValueTimeseries


class Asset(ValueHolding):
    _id = 1

    def __init__(self, name, value, created_date):
        self.name = name
        self.value = ValueTimeseries({created_date: value})
        self.id = self.__class__.assign_id()

    @classmethod
    def assign_id(cls):
        cls._id += 1
        return cls._id

    def get_value(self, at_datetime):
        if at_datetime < min(self.value.keys()):
            return 0
        # return minimum value at a datetime after at_datetime
        return self.get_value_before(at_datetime)[0]

    def get_value_before(self, at_datetime):
        # exclusive of at datetime
        if at_datetime <= min(self.value.keys()):
            return 0, at_datetime
        # return maximum value at a datetime before at_datetime and the datetime
        nearest_datetime = max([datetime for datetime in self.value.keys() if datetime < at_datetime])
        return self.value[nearest_datetime], nearest_datetime

    def get_value_after(self, at_datetime):
        # inclusive of at datetime
        if at_datetime > max(self.value.keys()):
            return False, at_datetime
        # return minimum value at a datetime after at_datetime and the datetime
        nearest_datetime = min([datetime for datetime in self.value.keys() if datetime >= at_datetime])
        return self.value[nearest_datetime], nearest_datetime

    def __add__(self, other):
        if type(other) == CombinedAsset:
            return CombinedAsset([self] + other.assets)
        elif issubclass(type(other), Asset):
            return CombinedAsset([self, other])
        else:
            raise NotImplementedError

    __radd__ = __add__
