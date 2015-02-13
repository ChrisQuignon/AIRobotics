#!/usr/bin/python
import sys
import copy
import time

#distance between two points
def dist(a, b):
  xa = a[0]
  ya = a[1]
  xb = b[0]
  yb = b[1]
  return pow((pow(xa-xb,2) + pow(ya-yb,2)), 0.5)

#Number of evaluations for performance analysis
EVALS = 0

#DFS WITH BACKTRACKING
def recursive_backtracking(assign, goals):
  global EVALS
  gs = copy.deepcopy(goals)
  #gs = goals
  if len(assign) == len(goals):
    #print 'DONE:', assign
    return assign
  #All nodes that are not assigned
  succs = filter((lambda x : x not in assign),gs)
  for head in succs:
    #print 'TEST: ',  assign[-1], '->', head
    new_time = dist(assign[-1], head) + assign[-1][3]
    # number of evalulations for performance measurment
    EVALS = EVALS +1
    if new_time < head[2]:
      #print 'NEW:', new_time
      if len(head) < 4:
        head.append(new_time)
      else:
        head[3] = new_time
      assign.append(head)
      result = recursive_backtracking(assign, gs)
      if result:
        return result
      else:
        #print 'REMOVE:', head
        assign.remove(head)
  return False

#READ FILES
for i in range(1, 6):
  print ''
  print 'File: scenarios/scenario' + str(i) + '.txt'
  goals = []
  with open("scenarios/scenario" + str(i) + ".txt") as f:
    for line in f:
      goals.append([float(n) for n in line.split()])
  
  #SETUP
  #Start point has no deadline
  goals[0].append(0.0)
  #start time is zero
  goals[0].append(0.0)
  
  #the three sortings: as given, by deadline, goal distance
  sorts = [lambda x : x, lambda x: x[2], lambda x: dist(x, goals[0])]

  for sort in sorts:
    g = sorted(goals[1:], key = sort)
    g.insert(0, goals[0])
    
    #FUNCTION CALL
    EVALS = 0
    timeElapsed=time.time()
    d =  recursive_backtracking([goals[0]], sorted(goals[1:], key = sort))
    timeElapsed= time.time() - timeElapsed
    
    #OUTPUT
    print '---next sorting---'
    print 'Time taken:', timeElapsed, 'ms'
    print 'Evaluations: ', EVALS
    if not d:
      print 'no solution'
    else:
      for p in d:
        print 'X:', p[0], 'Y:', p[1], 'Deadline:', p[2], 'Reached at:', p[3]
    EVALS = 0
