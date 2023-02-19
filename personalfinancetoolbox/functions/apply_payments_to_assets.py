import numpy as np
from dateutil.relativedelta import relativedelta
from personalfinancetoolbox.helpers import date_range


def apply_payment_into_asset(asset, payoff_amount, payoff_date):
    if payoff_date in asset.value.keys():
        asset.value[payoff_date] += payoff_amount
    else:
        asset.value[payoff_date] = asset.get_value(payoff_date) + payoff_amount
    return asset


def apply_regular_payment_into_asset(asset, regular_amount, interval, from_date, to_date):
    # interval is a relative delta object
    # apply regular payments into asset from from_date to to_date
    for date in date_range(from_date, to_date, interval):
        asset = apply_payment_into_asset(asset, regular_amount, date)


def apply_regular_payment_into_debt(debt, regular_amount, interval, from_date, to_date):
    rem = 0
    for date in date_range(from_date, to_date, interval):
        try:
            apply_payment_into_asset(debt, regular_amount+rem, date)
            rem = 0
        except ValueError:
            val = debt.get_value(date)
            apply_payment_into_asset(debt, -val, date)
            print(rem)
            rem = regular_amount+rem+val
    return rem
