from dateutil.relativedelta import relativedelta


def date_range(start_date, end_date, interval=relativedelta(years=1)):
    while start_date < end_date:
        yield start_date
        start_date += interval
