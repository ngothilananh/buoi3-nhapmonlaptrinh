# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:27:40 2024

@author: Student
"""

N=int(input("Nhập N: "))
chu_so_1= N//10
chu_so_2= N%10 
tong= chu_so_1 + chu_so_2
if 10 <= N<=99:
    print(" Tổng là ", tong)
else:
    print(" Không hợp lệ ")