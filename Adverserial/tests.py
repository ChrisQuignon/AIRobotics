 #!/usr/bin/python
# -*- coding: utf-8 -*-

from random import shuffle
from ground import *

# SETUP
board = Board5)
max_turn = True
max_score = 0
min_score = 0

board.s(0, 0)
board.s(0, 2)
board.s(2, 0)
board.s(0, 4)
board.s(4, 0)
board.o(1, 0)
board.o(3, 0)
board.o(1, 2)
board.o(2, 1)

board.o(2, 2)
print board.val(2, 2)

print board