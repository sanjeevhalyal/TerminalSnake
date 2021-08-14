import enum
import numpy as np
from gamedomain.gameentity import SnakeEntity
import random


class GameStatus(enum.Enum):
    Next = "Next"
    Lost = "Lost"
    EndGame = "End"


class GameGround:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self._gamestatus = GameStatus.Next
        self._score = 0
        self._treat = [int(col/2), int(row/2)+5]
        # self._treat = [random.randrange(1, col-1), random.randrange(1, row-1)]
        self._snake = SnakeEntity(col, row)
        self.printstring(head=self._snake.head, snake=self._snake.snakebody)

    @property
    def score(self):
        return self._score

    def matrix(self):
        return self._matrix, self.col, self.row

    def printstring(self, head, snake):
        output = ""
        for r in range(self.row):
            for c in range(self.col):
                if c in [0, self.col - 1] or r in [0, self.row - 1]:
                    output += "#"
                elif any(c == i[0] and r == i[1] for i in snake):
                    output += "@" if c == head[0] and r == head[1] else "+"
                elif c == self._treat[0] and r == self._treat[1]:
                    output += "$"
                else:
                    output += " "
            output += "\n"
        print(output)


    def scored(self, by=1):
        self._score += by

    def step(self, direction):

        response = self._snake.move(direction, self._treat)
        if response == SnakeEntity.HITME:
            return GameStatus.Lost

        if response == SnakeEntity.TREATED:
            self._treat = [random.randrange(1, self.col-1), random.randrange(1, self.row-1)]
            self.scored(100)
        self.printstring(head=self._snake.head, snake=self._snake.snakebody)
        self.scored()

        return GameStatus.Next,

    def reset(self):
        self._snake.reset()
        self._gamestatus = GameStatus.Next
        self._score = 0
        self.resetmatrix()





