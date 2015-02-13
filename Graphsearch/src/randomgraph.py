#!/usr/bin/python

import igraph as ig
from math import sqrt
from random import *


f = ig.Graph()
f.add_vertices(3000)

l = ig.Layout([])
for v in f.vs:
  x = random()
  y = random()
  v['x'] = x
  v['y'] = y
  l.append((int(x*1200), int(y*1200)))
  #print v

#ly = ig.Layout(l)
#print type(ly)

edges = []
for start in range(3000):
  for con in range(int(expovariate(20)*40+2)):
    goal =  int(random()*300)
    edges.append((start, goal))
    print edges[len(edges)-1]
    #print 'edge: ' + str((start, goal))
#f.add_edges(edges)
#f.write_svg("graph.svg", layout=l,  width=1200, height=1200,  vertex_size=4)


#print f
