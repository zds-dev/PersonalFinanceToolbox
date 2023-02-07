from dateutil.relativedelta import relativedelta


def get_complete_periods_between(date1, date2, period):
    """
    Get the number of periods between two dates
    :param date1: the first date
    :param date2: the second date
    :param period: the period
    :return:
     period the number of periods and the relativedelta object in terms of periods from date1 to date2
     this will take you to the nearest period before date2.
    """
    conversion_period_to_attribute = {
        'yearly': 'years',
        'monthly': 'months',
        'weekly': 'weeks',
        'daily': 'days',
    }

    if period not in conversion_period_to_attribute:
        raise ValueError(f'Period {period} not supported')

    attribute = conversion_period_to_attribute[period]
    periods = getattr(relativedelta(date2, date1), attribute)
    return periods, relativedelta(**{attribute: periods})

