from personalfinancetoolbox.models.ValueTimeseries import ValueTimeseries, ValueLimitedTimeseries
import datetime as dt


def test_value_timeseries():
    timeseries = ValueTimeseries({dt.datetime(2019, 1, 1): 1, dt.datetime(2019, 1, 2): 2, dt.datetime(2019, 1, 3): 3})
    assert timeseries[dt.datetime(2019, 1, 2)] == 2


def test_value_limited_timeseries():
    timeseries = ValueLimitedTimeseries({dt.datetime(2019, 1, 1): 2, dt.datetime(2019, 1, 2): 2, dt.datetime(2019, 1, 3): 3}, min_value=2, max_value=50)
    assert timeseries[dt.datetime(2019, 1, 1)] == 2


def test_value_limited_timeseries_errors():
    try:
        ValueLimitedTimeseries({dt.datetime(2019, 1, 1): 2, dt.datetime(2019, 1, 2): 2, dt.datetime(2019, 1, 3): 3},
                               min_value=5)
    except Exception as e:
        assert e.args[0] == 'Value cannot be less than 5'

    try:
        ValueLimitedTimeseries({dt.datetime(2019, 1, 1): -1000, dt.datetime(2019, 1, 2): 10, dt.datetime(2019, 1, 3): 3},
                               max_value=5)
    except Exception as e:
        assert e.args[0] == 'Value cannot be greater than 5'


