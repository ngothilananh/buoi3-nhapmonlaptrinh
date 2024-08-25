# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:26:59 2024

@author: Student
"""
import math 
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
so1=math.sqrt(a)-math.sqrt(b)
so2=a**(1/4)-b**(1/4)
so3=math.sqrt(a)+(a*b)**(1/4)
so4=a**(1/4)+b**(1/4)
ketqua=(so1/so2)-(so3/so4)
print("Giá trị của biểu thức là: ", ketqua)