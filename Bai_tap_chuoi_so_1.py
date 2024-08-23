# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:35:33 2024

@author: diemtrinh
"""
txt = " Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM "
print("   NUMBER 1")      
print(txt.replace(",","\n"))
print("   NUMBER 2")
print(txt.replace(",","\n").replace("P. ","").replace("Q. ","").replace("Tp. ",""))
