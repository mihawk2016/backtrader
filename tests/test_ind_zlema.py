from ..backtrader import indicators
from . import testcommon

chkdatas = 1
chkvals = [
    ['4125.487746', '3778.694000', '3620.284712']
]

chkmin = 44
chkind = indicators.ZLEMA


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
