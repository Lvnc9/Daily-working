#!/usr/bin/python
# Start 
# Writing testis for cypher encode and decoding
# Moudles
from vigenereCipher import VigenereCipher



def test_encode():
    cipher = VigenereCipher("TRAIN")
    encoded = cipher.encode("ENCODEINPYTHON")
    assert encoded == "XECWQXUIVCRKHWA"

def test_encode_character():
    cipher = VigenereCipher("TRAIN")
    encoded = cipher.encode("E")
    assert encoded == "X"


# End