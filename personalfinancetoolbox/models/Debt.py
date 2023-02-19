from personalfinancetoolbox.models.InterestAccruingAsset import InterestAccruingPeriodic
from personalfinancetoolbox.models.ValueTimeseries import ValueLimitedTimeseries


class Debt(InterestAccruingPeriodic):
    def __init__(self, name, value, interest, created_date, interest_period: str):
        super().__init__(name, value, interest, created_date, interest_period)
        self.value = ValueLimitedTimeseries({created_date: value}, max_value=0)



