import atexit
import enum
from pynput.keyboard import Key, Listener, KeyCode


class Direction(enum.Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    NONE = 'none'
    QUIT = 'quit'
    RESET = 'reset'
    

key_mapping = {
    Direction.UP: [Key.up, "w", "W"],
    Direction.DOWN: [Key.down, "s", "S"],
    Direction.LEFT: [Key.left, "a", "A"],
    Direction.RIGHT: [Key.right, "d", "D"],
    Direction.QUIT: [Key.esc, "q", "Q"],
    Direction.RESET: ["r", "R"],
}


class KeyBuffer:
    _buffer = []

    @classmethod
    def append(cls, key):
        for cmd, value in key_mapping.items():
            # TODO: char detect doesn't work
            if key in value:
                cls._buffer.append(cmd)


    @classmethod
    def __next__(cls):
        if cls._buffer:
            return cls._buffer.pop(0)
        return None


_listener = Listener(on_press=KeyBuffer.append)
_listener.start()

def stopl():
    _listener.stop()

atexit.register(stopl)

