from personalfinancetoolbox.models.InterestAccruingAsset import InterestAccruingPeriodic
import datetime as dt

asset = InterestAccruingPeriodic('test',  [100,100], 1.05, dt.datetime(2019, 1, 1), 'monthly')

asset.value[dt.datetime(2019, 2, 1)] = [200, 100]
asset.repropagate_timeseries(dt.datetime(2019, 1, 1))

