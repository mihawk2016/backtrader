from ..backtrader import indicators
from . import testcommon

chkdatas = 1
chkvals = [
    ['4054.187922', '3648.549000', '3592.979190'],
]

chkmin = 31
chkind = indicators.KAMA


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
