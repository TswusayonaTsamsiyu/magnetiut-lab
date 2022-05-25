import pandas as pd

from mgnt.common.utils import cached

from .fs import IV_TABLE


@cached
def get_iv_table():
    df = pd.read_excel(IV_TABLE)
    return dict(zip(*map(lambda i: df[i].to_numpy(), df.columns)))


def get_current(voltage):
    return get_iv_table()[abs(voltage)]