
import os

import pytest

from tools import dumppdf

path = os.path.dirname(os.path.abspath(__file__)) + '/'


@pytest.mark.parametrize(
    'datapath,filename,options',
    [
        ('../samples/', 'jo', '-t -a'),
        ('../samples/', 'simple1', '-t -a'),
        ('../samples/', 'simple2', '-t -a'),
        ('../samples/', 'simple3', '-t -a'),
        ('../samples/nonfree/', 'dmca', '-t -a'),
        ('../samples/nonfree/', 'f1040nr', None),
        ('../samples/nonfree/', 'i1040nr', None),
        ('../samples/nonfree/', 'kampo', '-t -a'),
        ('../samples/nonfree/', 'naacl06-shinyama', '-t -a'),
    ],
)
def test_dumppdf(datapath, filename, options):
    i = path + datapath + filename + '.pdf'
    o = path + filename + '.xml'
    if options:
        s = 'dumppdf -o%s %s %s' % (o, options, i)
    else:
        s = 'dumppdf -o%s %s' % (o, i)
    dumppdf.main(s.split(' '))
