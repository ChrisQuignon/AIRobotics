#!/usr/bin/python

#coordinates of all SOS relative to (0, 0)
sos_pos =[#INNER 9
          #[(-1,1), (0,1), (1,1)],#horizontal
          [(-1,0), (0,0), (1,0)],
          #[(-1,-1), (0,-1), (1,-1)],
          #[(-1,1), (-1,0), (-1,-1)],#vertical
          [(0,1), (0,0), (0,-1)],
          #[(1,1), (1,0), (1,-1)],
          [(-1,1), (0,0), (1,-1)],#diagonal
          [(-1,-1), (0,0), (1,1)],
          #OUTER 25
          [(-2,0), (-1,0), (0,0)],#horizontal
          [(0,0), (1,0), (2,0)],
          [(0,2), (0,1), (0,0)],#vertical
          [(0,0), (0,-1), (0,-2)],
          [(-2,2), (-1,1), (0,0)],#diagonal\
          [(0,0), (1,-1), (2,-2)],
          [(2,2), (1,1), (0,0)],#diagonal/
          [(0,0), (-1,-1), (-2,-2)]]



class Board(list):

    self = []

    def __init__(self, n):
        for i in range(n):
            self.append([' '] * n)
            self.x = n
            self.y = n

    def what(self, x, y):
        _max = len(self)
        if 0 <= x < _max and 0 <= y < _max:
            return self[len(self) - 1 - y][x]
        else:
            return False

    def s(self, x, y):
        if self[len(self) - 1 - y][x] == 'O':
            return False
        self[len(self) - 1 - y][x] = 'S'
        return True

    def o(self, x, y):
        if self[len(self) - 1 - y][x] == 'S':
            return False
        self[len(self) - 1 - y][x] = 'O'
        return True

    def rev(self, x, y):
        self[len(self) - 1 - y][x] = ' '

    def is_sos(
        self,
        (x1, y1),
        (x2, y2),
        (x3, y3),
        ):
        return (self.what(x1, y1) == 'S' and
                self.what(x2, y2) == 'O' and
                self.what(x3, y3) == 'S')

    def val(self, x, y):
        v = 0
        for ((s1x, s1y), (ox, oy), (s2x, s2y)) in sos_pos:
            if (self.what(x + s1x, y + s1y) == 'S' and
                self.what(x + ox,  y + oy)  == 'O' and
                self.what(x + s2x, y + s2y) == 'S'):
                v = v + 1
        return v

    def has_free(self):
        for i in self:
            if ' ' in i:
                return True
        return False

    def __str__(self):
        s = ''
        for (y, row) in enumerate(self):
            s += '-' * (2 * self.x + 1)
            s += '\n'
            for (y, cell) in enumerate(row):
                s += '|'
                s += cell
            s += '|\n'
        s += '-' * (2 * self.x + 1)
        return s