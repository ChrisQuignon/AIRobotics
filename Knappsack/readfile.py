#!/usr/bin/python
import sys

#for i in range(7):
#  #print str(i)
#  with open("data/knapsack" + str(i) + ".txt") as f:
#    for line in f.readlines():
#      int_list = [int(i) for i in line]
#      print type(line) 
#    #  print line,
for i in range(7):
  with open("data/knapsack" + str(i) + ".txt") as f:
    for line in f:
      int_list = [float(i) for i in line.split()]
      print int_list
