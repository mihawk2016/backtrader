from ..backtrader import indicators
from . import testcommon
chkdatas = 1
chkvals = [
    ['4113.721705', '3862.386854', '3832.691054']
]

chkmin = 88
chkind = indicators.TEMA


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
