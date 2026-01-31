from ..backtrader import indicators
from . import testcommon

chkdatas = 1
chkvals = [
    ['4070.115719', '3644.444667', '3581.728712'],
]

chkmin = 30
chkind = indicators.EMA


def test_run(main=False):
    datas = [testcommon.getdata(i) for i in range(chkdatas)]
    testcommon.runtest(datas,
                       testcommon.TestStrategy,
                       main=main,
                       plot=main,
                       chkind=chkind,
                       chkmin=chkmin,
                       chkvals=chkvals)


if __name__ == '__main__':
    test_run(main=True)
