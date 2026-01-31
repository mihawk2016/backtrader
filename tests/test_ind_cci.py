from ..backtrader import indicators
from . import testcommon

chkdatas = 1
chkvals = [
    ['69.574287', '91.196363', '82.175663'],
]

chkmin = 39
chkind = indicators.CCI


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
