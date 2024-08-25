# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:04:18 2024

@author: Student
"""

chuoi = "Đại học quốc gia, Khu phố 6, P.Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings = chuoi.split (", ")
print (sub_strings)
chuoi = "Đại học quốc gia, Khu phố 6, P.Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings_2 = [chuoi.replace("P. ", "").replace("Q. ", "").replace("Tp. ", "") for part in sub_strings]
for chuoi in sub_strings_2:
    print(sub_strings_2)