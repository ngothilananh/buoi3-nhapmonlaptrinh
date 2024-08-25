# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:57:57 2024

@author: Student
"""

chuoi = "i’m a cat"
ket_qua1 = chuoi.title()
print("I’m A Cat:", ket_qua1)
ket_qua2 = chuoi.upper()
print("I’M A CAT:", ket_qua2)
ket_qua3 = chuoi[0].lower() + chuoi[1].upper() + chuoi[2:6].lower() + chuoi[6].upper() + chuoi[7:10].lower() + chuoi[10:].upper()
print("i’M a cAT:", ket_qua3)
ket_qua4 = chuoi
print("I’m a cat:", ket_qua4)

