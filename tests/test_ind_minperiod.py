from ..backtrader import indicators
from . import testcommon

chkdatas = 1
chkvals = []

chkmin = 34  # from MACD
chkind = [indicators.SMA, indicators.Stochastic, indicators.MACD, indicators.Highest]
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
