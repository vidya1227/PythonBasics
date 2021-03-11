def __init__(self, iWeight):
    self.iWeight = iWeight


def lbs_to_kg(iWeight):
    return iWeight * 0.45


def kg_to_lbs(iWeight):
    return iWeight / 0.45


print(lbs_to_kg(34))
print(kg_to_lbs(32))
