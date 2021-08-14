import numpy as np
from copy import deepcopy
from keyinput import Direction

direction_mapping = {
    Direction.UP: np.array([0,-1]),
    Direction.DOWN: np.array([0,1]),
    Direction.LEFT: np.array([-1,0]),
    Direction.RIGHT: np.array([1,0]),
}


class SnakeEntity:

    TREATED = "treated"
    HITME = "hitme"
    WHATNEXT = "whatnext"

    def __init__(self, col, row):
        self._border = np.array([col, row])
        self._s_col, self._s_row = int(col/2), int(row/2)
        self.reset()

    @property
    def snakebody(self):
        return self._snakebody

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def reset(self):
        self._head = [self._s_col, self._s_row]
        self._tail = [self._s_col-2, self._s_row]
        self._snakebody = np.array([self._head,
                                    [self._s_col-1, self._s_row],
                                    self._tail])

    def move(self, direction, treat):
        if direction:
            next = np.mod(self._snakebody[0] + direction_mapping[direction], self._border)

        else:

            next = np.mod(self._snakebody[0] +
                                (self._snakebody[0] - self._snakebody[1]),
                                self._border)

        if next[0] == self._snakebody[1][0] and next[1] == self._snakebody[1][1]:
            return


        self._tail = deepcopy(self._snakebody[-1])

        for i in range(len(self._snakebody)-1, 0, -1):
            self._snakebody[i] = self._snakebody[i-1]
            self._snakebody[i] = np.mod(self._snakebody[i], self._border)
        self._snakebody[0] = self._head = next
        if treat and next[0] == treat[0] and next[1] == treat[1]:
            self._snakebody = np.append(self._snakebody, [self._tail], axis=0)
            return self.TREATED




        if any(next[0] == i[0] and next[1] == i[1] for i in self._snakebody[2:]):
            return self.HITME
        return self.WHATNEXT






