from personalfinancetoolbox.models.InterestAccruingAsset import InterestAccruingPeriodic
import datetime as dt


def test_repropagate_timeseries():
    asset = InterestAccruingPeriodic('test',  [100, 0], 1.05, dt.datetime(2019, 1, 1), 'monthly')
    asset.value[dt.datetime(2019, 2, 1)] = [200, 0]
    asset.repropagate_timeseries(dt.datetime(2019, 1, 1))
    assert asset.value[dt.datetime(2019, 2, 1)] == 105
    assert asset.value.delta_value[dt.datetime(2019, 2, 1)] == 0


def test_repropagate_timeseries_with_payment():
    asset = InterestAccruingPeriodic('test',  [100, 0], 1.05, dt.datetime(2019, 1, 1), 'monthly')
    asset.value[dt.datetime(2019, 2, 1)] = [200, 100]
    asset.repropagate_timeseries(dt.datetime(2019, 1, 1))
    assert asset.value[dt.datetime(2019, 2, 1)] == 205
    assert asset.value.delta_value[dt.datetime(2019, 2, 1)] == 100
