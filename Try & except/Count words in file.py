# -*- coding: utf-8 -*-
"""
Created on Sat May 14 16:18:43 2022

@author: Vaibhav Tiwari
"""

try:
    a=open("D:\Python\File Handling\Text1.txt","r")
    r=a.read()
except:
    print("File not found")
else:
    a=input("Enter full name : ")
    q=a.split()
    print("Length og your name is : ",len(q))