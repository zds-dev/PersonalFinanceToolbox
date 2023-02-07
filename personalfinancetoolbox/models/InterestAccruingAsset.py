from personalfinancetoolbox.models.Asset import Asset
from personalfinancetoolbox.helpers import get_complete_periods_between


class InterestAccruingPeriodic(Asset):
    def __init__(self, name, value, interest, created_date, interest_period: str):
        super().__init__(name, value, created_date)
        self.interest_period = interest_period
        self.interest = interest
        self.interest_apply_from = created_date

    def get_interest_date(self, at_datetime):
        periods, relative = get_complete_periods_between(self.interest_apply_from, at_datetime, self.interest_period)
        return self.interest_apply_from + relative

    def calculate_interest(self, at_datetime):
        interest_date_before_current = self.get_interest_date(at_datetime)
        interest_date_before_previous = self.get_interest_date(self.get_value_before(at_datetime)[1])
        periods_between_interest_dates = get_complete_periods_between(interest_date_before_previous,
                                                                      interest_date_before_current,
                                                                      self.interest_period)[0]

        value_interest, df = self.get_value_after(interest_date_before_previous)

        interest_produced = value_interest*self.interest**periods_between_interest_dates-value_interest
        return interest_produced

    def get_value(self, at_datetime):
        if at_datetime < min(self.value.keys()):
            return 0
        return self.get_value_before(at_datetime)[0]+self.calculate_interest(at_datetime)


class YearlyInterestAccruing(InterestAccruingPeriodic):
    """
    Interest is accrued yearly
    """
    def __init__(self, name, value, interest, created_date):
        super().__init__(name, value, interest, created_date, 'yearly')