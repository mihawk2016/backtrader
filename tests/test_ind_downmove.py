from ..backtrader import indicators
from . import testcommon

chkdatas = 1
chkvals = [
    ['10.720000', '-10.010000', '-14.000000'],
]

chkmin = 2
chkind = indicators.DownMove


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
