import time
import os.path
import itertools
from random import randint
from asciimatics.screen import Screen


def read_frames(location='.frames'):
    path = os.path.abspath(location)
    if not os.path.exists(path):
        raise ValueError("DOESNT EXIST")
    fname = os.path.join(path, '0.txt')
    return os.path.exists(fname)


def main(screen):
    frames = read_frames()
    for frame in itertools.cycle(frames):
        color = randint(0, screen.colours - 1)
        for i, line in enumerate(frame.split('\n')):
            screen.paint(
                line, 0, i,
                colour=color)
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()
        time.sleep(0.3)
        screen.clear()

if __name__ == '__main__':
    # Screen.wrapper(main)
    print(read_frames())
