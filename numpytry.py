#!usr/bin/python3


import os
import pip
import numpy

loc =  input("Enter the locaiton of the file to store output : ")

namefile  =  input("Enter the name of the file with extension : ")

os.system("touch " + loc + '/' + namefile)
os.system("echo Enter Row and Column")
row =  input("Enter Row")
col =  input("Enter Column")

ar1 = numpy.zeroes((i,j))

  for i in row:
    for j in column:
       
      ar1[i,j] = input("Enter the value at "+ i + "row " + j +" column") 
      i++
      j++


