import os

import pytest
import tools.pdf2txt as pdf2txt

path = os.path.dirname(os.path.abspath(__file__)) + '/'


@pytest.mark.parametrize(
    'datapath,filename,options',
    [
        ('../samples/', 'jo', None),
        ('../samples/', 'simple1', None),
        ('../samples/', 'simple2', None),
        ('../samples/', 'simple3', None),
        ('../samples/nonfree/', 'dmca', None),
        ('../samples/nonfree/', 'f1040nr', None),
        ('../samples/nonfree/', 'i1040nr', None),
        ('../samples/nonfree/', 'kampo', None),
        ('../samples/nonfree/', 'naacl06-shinyama', None),
        # this test works on Windows but on Linux & Travis-CI it says
        # PDFSyntaxError: No /Root object! - Is this really a PDF?
        # TODO: Find why
        # ('../samples/contrib/','stamp-no'),
        ('../samples/contrib/', '2b', '-A -t xml'),
        (
            '../samples/nonfree/',
            '175',
            None,
        ),  # https://github.com/pdfminer/pdfminer.six/issues/65
        (
            '../samples/scancode/',
            'patchelf',
            None,
        ),  # https://github.com/euske/pdfminer/issues/96
    ],
)
def test_tools_pdf2txt(datapath, filename, options):
    i = path + datapath + filename + '.pdf'
    o = path + filename + '.txt'
    if options:
        s = 'pdf2txt -o%s %s %s' % (o, options, i)
    else:
        s = 'pdf2txt -o%s %s' % (o, i)
    pdf2txt.main(s.split(' ')[1:])
