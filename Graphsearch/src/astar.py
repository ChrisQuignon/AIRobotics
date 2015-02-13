#!/usr/bin/python

import igraph as ig
from math import sqrt
from random import *

def dist (a, b):
  d = sqrt((b.attributes()['x'] - a.attributes()['x'])**2 + (b.attributes()['y'] - a.attributes()['y'])**2)
  return d

#CREATE RANDOM MAP 
N = 3000
R = 0.022
f = ig.Graph.GRG(n=N, radius=R, torus=True)
"""
###ALTERNATIVE GRAPH

f = ig.Graph()
f.add_vertices(N)

for v in f.vs:
  v['x']=random()
  v['y']=random()
  #print v

edges = []
for start in range(N):
  for con in range(int(expovariate(20)*40+2)):
    goal =  int(random()*300)
    edges.append((start, goal))
    #print 'edge: ' + str((start, goal))
f.add_edges(edges)"""

#START WITHOUT TRAINSTATION
#create vertex with starting point coordinates
f.add_vertex(name='start', x=0, y=0)
start = f.vs.find(name='start')
#find closest vertex
closest=sorted(f.vs, key=lambda x: dist(x, start))[1]
#connect them
f.add_edges([(start.index, closest.index)])


#DEFINE HEURISTIC
for n in f.vs:
  n['g'] = 0
  n['h'] = dist(f.vs[N-1], n)
  n['f'] = 0

#IMPLEMENT A STAR
def a_star(start, goal):
  closed_set = set()
  open_set = set()
  open_set.add(start)

  while(open_set):
    current_node = min(open_set, key=lambda x: x.attributes()['f'])
    open_set.remove(current_node)
    print str(current_node.index) + ' ' + str(current_node['f'])
    if current_node.index == goal.index:
      return 'goal found'
    closed_set.add(current_node.index)
    for v in current_node.successors():
      if (not v.index in closed_set):
        v['g'] = current_node['g'] + dist(v, current_node)
        v['f'] = v['g'] + v['h']
        open_set.add(v)
  return 'goal not found'

print 'Visited nodes including their f:'
print a_star(start, f.vs[N-1]) 

#print 'Start is: ' + str(f.vs[0]['x']) + '/' + str(f.vs[0]['y'])
#print 'Goal is: ' + str(f.vs[N-1]['x']) + '/' + str(f.vs[N-1]['y'])
#print 'Distance was: ' + str(dist(f.vs[0], f.vs[N-1]))
#print 'shortest path is:'
#shortest =  f.shortest_paths(source=f.vs[0], target=f.vs[N-1], weights=None)
#print shortest

#f.write_edgelist("graph.el") 
#f.write_svg("graph.svg", layout=f.layout("grid_fr"),  width=1200, height=1200,  vertex_size=4)



