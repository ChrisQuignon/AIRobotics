#!/usr/bin/python
import sys
from random import shuffle

#HILLCLIMBING
def hillclimb(cap, weights): 
  weight = 0
  sack = list()
  profit = 0
  while weights:
    rnd = weights.pop()
    if rnd[1] < cap:
      sack.append(rnd)
      cap = cap - rnd[0]
      weight = weight + rnd[0]
      profit = profit + rnd[1]
      weights.append(rnd)
      # weights get shuffled so the outcompe of pop will be random
      shuffle(weights) 
  return (profit, sack)
  
#READ FILES
for i in range(8):
  int_file = list()
  with open("data/knapsack" + str(i) + ".txt") as f:
    for line in f:
      int_file.append([float(n) for n in line.split()])
  cap = int_file[0][0]
  obj_line = int_file[1:]
  weight = [w[1] for w in obj_line]
  capacities = [c[2] for c in obj_line]
  weights = zip(weight, capacities)
  
  #FUNCTION CALL  
  (profit, weights) = hillclimb(cap, weights)
  
  #OUTPUT
  print ''
  print 'Knappsack number',
  print i,
  print ':'
  
  print 'Profit:',
  print profit

  print 'Weight:',
  print sum([s[0] for s in weights])

  print 'Weightlist:',
  print weights