from gamedomain.gameground import GameGround, GameStatus
from keyinput import KeyBuffer, Direction
import time
from random import randint
from asciimatics.screen import Screen

BASIC = "basic"
ADVANCED = "advanced"
class GamePlay:
    def __init__(self, col, row, displaymode=BASIC):
        self._displaymode = displaymode
        self._gameground = GameGround(col, row)

    def advancedgameplay(self, screen):
        raise Exception("Asciimatics display not implemented, use basic displaymode")
        # screen.print_at('Hello world!',
        #                 randint(0, screen.width), randint(0, screen.height),
        #                 colour=randint(0, screen.colours - 1),
        #                 bg=randint(0, screen.colours - 1))
        # data, c, r = self._gameground.matrix()
        # for i in range(c):
        #     for j in range(r):
        #         screen.print_at(data[i][j], i, j)

    def basicgameplay(self):
        # TODO: does not ignore click is same direction as snake is moving
        status = GameStatus.Next
        while(status == GameStatus.Next):
            key = KeyBuffer.__next__()
            if key == Direction.QUIT:
                status = GameStatus.EndGame
                continue
            status = self._gameground.step(key)
            time.sleep(0.5)

        if status == GameStatus.Lost:
            return self._gameground.score, "You lost the game, Better luck next time"
        if status == GameStatus.EndGame:
            return self._gameground.score, "Thanks for playing"

    def start(self):
        if self._displaymode == BASIC:
            return self.basicgameplay()
        elif self._displaymode == ADVANCED:
            Screen.wrapper(self.advancedgameplay)

