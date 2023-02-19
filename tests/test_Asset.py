from personalfinancetoolbox.models import Asset
from personalfinancetoolbox.models import ValueTimeseries
import datetime as dt

def test_Asset():
    asset = Asset('new_asset', 1000, dt.datetime(year=2021, month=1, day=10))
    assert asset.name == 'new_asset'
    assert dict(asset.value) == {dt.datetime(year=2021, month=1, day=10): 1000}
    assert asset.get_value(dt.datetime(year=2024, month=2, day=21)) == 1000
    assert asset.get_value(dt.datetime(year=2020, month=2, day=5)) == 0

