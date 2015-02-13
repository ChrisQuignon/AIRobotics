 #!/usr/bin/python
# -*- coding: utf-8 -*-

from random import shuffle
from ground import *

# SETUP
board = Board(3)
max_turn = True
max_score = 0
min_score = 0

def operators():
    ops = []
    for x in range(len(board)):
        for y in range(len(board)):
            if board.what(x, y) == ' ':
                board.s(x, y)
                ops.append({
                    'x': x,
                    'y': y,
                    'value': board.val(x, y),
                    'entry': board.what(x, y),
                    })
                board.rev(x, y)

                board.o(x, y)
                ops.append({
                    'x': x,
                    'y': y,
                    'value': board.val(x, y),
                    'entry': board.what(x, y),
                    })
                board.rev(x, y)

  #  uncomment if you are for MAX
  #  and/or you do not like deterministic games
  #  shuffle(ops)
    return ops


def minimax_decision():
    vs = []
    for op in operators():
        vs.append(minimax_value(op))
        #do recursion to eval whole tree
    return max(vs, key=lambda x: x['value'])


def minimax_value(op):
    succs = operators()
    if not board.has_free():
        return board.val(op)
    elif max_turn:
      r = max(succs, key=lambda x: x['value'])
    else:
      r =  min(succs, key=lambda x: x['value'])
    return r


# GAME WITH MINIMAX
while board.has_free():
    if max_turn:
        print 'next: MAX'
    else:
        print 'next: MIN'

  # decide what to do
    o = minimax_decision()
    print o['entry'], 'at', o['x'], '/', o['y']

  # Set stone
    if o['entry'] == 'S':
        board.s(o['x'], o['y'])
    else:
        board.o(o['x'], o['y'])

    print board

  # RULE: Whover scores takes another turn
  # MIN can not win because it will not score

  #  if max_turn and board.val(o['x'], o['y']) > 0:
  #    max_score = max_score +1
  #    print "MAX scored:", max_score
  #  elif board.val(o['x'], o['y']) > 0:
  #    min_score = min_score +1
  #    print "MIN scored:", min_score
  #  else:
  #    max_turn = not max_turn
  #  print ''

  # RULE: Both plazers take turns
  # second player wins

    if max_turn:
      if board.val(o['x'], o['y'])>0:
        max_score = max_score + 1
        print 'MAX scored:', max_score
    else:
      if board.val(o['x'], o['y'])>0:
        min_score = min_score + 1
        print 'MIN scored:', min_score
    print ''
    max_turn = not max_turn
    

# Game Over
print 'AAAAnd the winner is:'
if min_score > max_score:
    print 'MIN WINS with', min_score, 'points!'
    print 'MAX has only', max_score, 'points!'
elif max_score > min_score:

    print 'MAX WINSwith', max_score, 'points!'
    print 'MIN has only', min_score, 'points!'
else:
    print 'NOBODY!'
    print 'Both opponents have', min_score, 'points!'
    print 'Deterministic games are booring...'

			