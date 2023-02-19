from personalfinancetoolbox.models.Asset import Asset
from personalfinancetoolbox.models.ValueTimeseries import ValueLimitedTimeseries


class Debt(Asset):
    def __init__(self, name, value, created_date):
        super().__init__(name, value, created_date)
        self.value = ValueLimitedTimeseries({created_date: value}, max_value=0)

