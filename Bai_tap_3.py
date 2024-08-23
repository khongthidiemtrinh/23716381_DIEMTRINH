# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:27:31 2024

@author: diemtrinh
"""
n=int(input(" Nhập số nguyên N= "))
a=n//10
b=n%10
if 10 <= n <= 99: print("Tổng các chữ số của số nguyên là:", a+b)
else: print(" Không hợp lệ")
