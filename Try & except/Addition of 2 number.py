# -*- coding: utf-8 -*-
"""
Created on Fri May 13 22:36:49 2022

@author: Vaibhav Tiwari
"""

a=True    
while a==True: 
    try:
        f=int(input("First number :"))
        a=False    
    except ValueError:
        print("Give integer value in a")
        a=True
a=True        
while a==True:   
    try:
        s=int(input("Second number :"))
        a=False
        
    except ValueError:
        print("Give integer value in b")
        a=True
print("Sum of number is:",f+s)
