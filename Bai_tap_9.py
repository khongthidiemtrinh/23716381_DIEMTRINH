# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 01:02:31 2024

@author: diemtrinh
"""
import math
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
phan_so_1= (math.sqrt(a) - math.sqrt(b))/(math.pow(a, 0.25) - math.pow(b, 0.25))
phan_so_2= (math.sqrt(a) + math.pow(a*b,0.25))/(math.pow(a, 0.25) + math.pow(b, 0.25))
if a < 0 or b < 0:
   print("a và b phải là số không âm") 
else:
    print("Kết quả của biểu thức là:",phan_so_1 - phan_so_2)