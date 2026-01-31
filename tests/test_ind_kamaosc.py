from ..backtrader import indicators
from . import testcommon

chkdatas = 1
chkvals = [
    ['65.752078', '78.911000', '39.950810']
]

chkmin = 31
chkind = indicators.KAMAOsc


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
