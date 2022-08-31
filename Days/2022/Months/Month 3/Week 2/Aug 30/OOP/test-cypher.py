#!/usr/bin/python
# Start 
# Writing tests for cypher encode and decoding
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

def test_extend():
    cipher = VigenereCipher
    extended = cipher.extend_keyword(16)
    assert extended == "TRAINTRAINTRAINT"




# End