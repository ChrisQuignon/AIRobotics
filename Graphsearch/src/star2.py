#!/usr/bin/python

import igraph as ig
from math import sqrt
from random import *

def dist (a, b):
  d = sqrt((b.attributes()['x'] - a.attributes()['x'])**2 + (b.attributes()['y'] - a.attributes()['y'])**2)
  return d

#g = ig.Graph.Erdos_Renyi(3000, p=0.002, directed=False, loops=True)
#print g

N = 3000
R = 0.025

#N = 10
#R = 0.3

#f = ig.Graph.GRG(n=N, radius=R, torus=True)

f = ig.Graph()
f.add_vertices(3000)

for v in f.vs:
  v['x']=random()
  v['y']=random()
  print v

edges = []
for start in range(3000):
  for con in range(int(expovariate(20)*40+2)):
    goal =  int(random()*300)
    edges.append((start, goal))
    #print 'edge: ' + str((start, goal))
f.add_edges(edges)
 

s = f.vs[0]
g = f.vs[N-1]

#propagate heuristic
for n in f.vs:
  #n["g"] = 0
  n["h"] = dist(g, n)
  #n["f"] = 0

def a_star(start, goal):
  closed_list = []
  open_list = [(start, 0.0)]
  #print type(open_list[0][1])

  while(open_list):
    n = open_list.pop(0)

    #print str(current_node.index) + ' -> ' + str(current_node['f']) #+ ' | ' + str(len(current_node.successors()))
    #print min
    print str(n[0].index) + ': f = ' + str(n[1])
    if n[0].index == goal.index:
      return True
    closed_list.insert(0, n[0].index)
    
    for v in n[0].successors():
      if (not v.index in closed_list):# and not v in open_list):
        suc_g = dist(v, n[0]) #+ n[1]
        suc_f = suc_g + v['h']
        open_list.insert(0, (v, suc_f))
    #order List by f - very ineffective
    open_list = sorted(open_list, key=lambda x: x[1])
    open_list_string = 'open: '
    #for v in open_list:
    #  open_list_string = open_list_string + ' ' + str(v[1])
      #open_list_string = open_list_string +'|' + str(v['f'])
    #print open_list[0][1]
    #print 'closed: ' + str(closed_list)
    #print ''
    #print len(closed_list[:1])
    #print len(open_list)
    #print ''
  return False

print 'Start is: ' + str(f.vs[0]['x']) + '/' + str(f.vs[0]['y'])
print 'Goal is: ' + str(f.vs[N-1]['x']) + '/' + str(f.vs[N-1]['y'])
print 'Distance is: ' + str(dist(f.vs[0], f.vs[N-1]))
print f.shortest_paths(source=f.vs[0], target=f.vs[N-1], weights=None)
a_star(f.vs[0], f.vs[N-1])
f.write_lgl('graph.lgl') 
f.write_svg("graph.svg", layout=f.layout("grid_fr"),  width=1200, height=1200,  vertex_size=4)



