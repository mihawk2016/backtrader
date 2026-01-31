from ..backtrader import indicators
from . import testcommon

chkdatas = 1
chkvals = [
    ['0.900000', '0.880000', '0.980000'],
]

chkmin = 50
chkind = indicators.PercentRank


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
