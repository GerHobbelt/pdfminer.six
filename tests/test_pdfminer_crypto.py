
# test of various compression/encoding modules (previously in doctests):
from pdfminer3.ascii85 import *
from pdfminer3.crypto import encrypt_arc4
from pdfminer3.lzw import *
from pdfminer3.runlength import *


def test_ascii85decode():
    # The sample string is taken from: http://en.wikipedia.org/w/index.php?title=Ascii85
    assert ascii85decode(b'9jqo^BlbD-BleB1DJ+*+F(f,q') == b'Man is distinguished'

    assert ascii85decode(b'E,9)oF*2M7/c~>') == b'pleasure.'


def test_asciihexdecode():
    assert asciihexdecode(b'61 62 2e6364   65') == b'ab.cde'
    assert asciihexdecode(b'61 62 2e6364   657>') == b'ab.cdep'
    assert asciihexdecode(b'7>') == b'p'


def test_arcfour():
    assert encrypt_arc4(b'Key', b'Plaintext').hex() == 'bbf316e8d940af0ad3'
    assert encrypt_arc4(b'Wiki', b'pedia').hex() == '1021bf0420'
    assert (
        encrypt_arc4(b'Secret', b'Attack at dawn').hex()
        == '45a01f645fc35b383552544b9bf5'
    )


def test_lzwdecode():
    assert (
        lzwdecode(b'\x80\x0b\x60\x50\x22\x0c\x0c\x85\x01')
        == b'\x2d\x2d\x2d\x2d\x2d\x41\x2d\x2d\x2d\x42'
    )


def test_rldecode():
    assert rldecode(b'\x05123456\xfa7\x04abcde\x80junk') == b'1234567777777abcde'
