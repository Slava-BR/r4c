import re

REG = r'^[A-Z1-9]{2}$'


def data_is_valid(model, version, created) -> bool:
    if re.match(REG, model) and re.match(REG, version) and created:
        return True
    return False
