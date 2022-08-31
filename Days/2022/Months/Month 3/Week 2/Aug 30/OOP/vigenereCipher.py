#!/usr/bin/python
# Start
# Implementing Vigenere Cipher algorithm 


class VigenereCipher:
    
    def __init__(self, keyword):
        self.keyword = keyword
        
    def combine_character(plain, keyword):
        plain = plain.upper()
        keyword = keyword.upper()
        plain_num = ord(plain) - ord("A")
        keyword_num = ord(keyword) - ord("A")
        return chr(ord("A") + (plain_num + keyword_num) % 26)

    def extend_keyword(self, number):
        repeats = number // len(self.keywrod) + 1
        return (self.keyword * repeats) % 26
    
    def encode(self, plaintext:str):
        plaintext = plaintext.replace(" ", "")
        cipher = []
        keyword = self.extend_keyword(len(plaintext))
        for p, k in zip(plaintext, keyword):
            cipher.append(self.combine_character(p, k))
        return "".join(cipher)
    





# End