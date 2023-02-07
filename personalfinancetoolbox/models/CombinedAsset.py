from personalfinancetoolbox.models.ValueHolding import ValueHolding


class CombinedAsset(ValueHolding):
    def __init__(self, assets):
        self.assets = assets

    def get_value(self, at_datetime):
        return sum([asset.get_value(at_datetime) for asset in self.assets])

    def __radd__(self, other):
        if type(other) == CombinedAsset:
            return CombinedAsset(self.assets + other.assets)
        else:
            return NotImplemented

    def __add__(self, other):
        return self.__radd__(other)

