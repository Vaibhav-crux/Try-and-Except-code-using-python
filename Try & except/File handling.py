# -*- coding: utf-8 -*-
"""
Created on Fri May 13 23:30:20 2022

@author: Vaibhav Tiwari
"""

try:
    a=open("D:\Python\File Handling\Text1.txt","r")
    r=a.read()
    print(r)
except:
    print("File not found")

############################################################

try:
    a=open("D:\Python\File Handling\Text2.txt","r")
    r=a.read()
except:
    pass
else:
    print(r)