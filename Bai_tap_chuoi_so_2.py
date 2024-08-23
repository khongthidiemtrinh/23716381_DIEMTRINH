# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:13:32 2024

@author: diemtrinh
"""
txt= "i'm a cat"
print(" chuyển lệnh i'm a cat")
# 1. Chuyển thành "I’m A Cat"
print(txt.title())
# 2. Chuyển thành "I’M A CAT"
print(txt.upper())
# 3. Chuyển thành "i’M a cAT"
print(txt[0]+txt[1:3].upper()+txt[3:7]+txt[7:9].upper())
# 4. Chuyển thành "I’m a cat"
print(txt.capitalize())