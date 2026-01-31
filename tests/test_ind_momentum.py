from ..backtrader import indicators
from . import testcommon

chkdatas = 1
chkvals = [
    ['67.050000', '-34.160000', '67.630000'],
]

chkmin = 13
chkind = indicators.Momentum


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
