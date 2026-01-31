from ..backtrader import indicators
from . import testcommon

chkdatas = 2
chkvals = []

chkmin = 151  # because of the weekly data
chkind = [indicators.SMA]
chkargs = dict()


def test_run(main=False):
    datas = [testcommon.getdata(i) for i in range(chkdatas)]
    testcommon.runtest(datas,
                       testcommon.TestStrategy,
                       main=main,
                       plot=main,
                       chkind=chkind,
                       chkmin=chkmin,
                       chkvals=chkvals,
                       chkargs=chkargs)


if __name__ == '__main__':
    test_run(main=True)
