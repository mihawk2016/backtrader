from ..backtrader.indicators.accdecoscillator import AccelerationDecelerationOscillator
from . import testcommon


chkdatas = 1
chkvals = [
    ['-2.097441', '14.156647', '30.408335']
]

chkmin = 38
chkind = AccelerationDecelerationOscillator


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
