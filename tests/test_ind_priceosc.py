from ..backtrader import indicators
from . import testcommon
chkdatas = 1
chkvals = [
    ['25.821368', '23.202675', '-9.927422']
]

chkmin = 26
chkind = indicators.PriceOsc


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
