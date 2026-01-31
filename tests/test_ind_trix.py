from ..backtrader import indicators
from . import testcommon

chkdatas = 1
chkvals = [
    ['0.071304', '0.181480', '0.050954']
]

chkmin = 44
chkind = indicators.Trix


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
