# -*- coding: utf-8 -*-
"""
Created on Fri May 13 22:49:46 2022

@author: Vaibhav Tiwari
"""

while True:
    a=input("Enyer 1st no. : ")
    if(a=='q'):
        break
    b=int(input("Eneter 2nd no. : "))
    try:
        v=int(a+b)
    except:
        print("Can't be divisible by 0")
    else:
        print(v)
        
        