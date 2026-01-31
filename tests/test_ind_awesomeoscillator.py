from ..backtrader.indicators.awesomeoscillator import AO
from ..backtrader import indicators
from ..backtrader.dataseries import TimeFrame
from . import testcommon


chkdatas = 1
chkvals = [
    ['50.804206', '72.983735', '33.655941']
]

chkmin = 34
chkind = AO


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
