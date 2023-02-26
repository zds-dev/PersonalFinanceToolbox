from personalfinancetoolbox.models.InterestAccruingAsset import InterestAccruingAsset
from personalfinancetoolbox.models.Asset import Asset
class Bond(InterestAccruingAsset):
    def __init__(self, name, value, start_date, coupon_rate, maturity_date):
        super().__init__(name, value, start_date, coupon_rate)
        self.maturity_date = maturity_date
        self.coupon_rate = coupon_rate
        self.coupon_value_asset = Asset(name + ' coupon value', 0, start_date)
