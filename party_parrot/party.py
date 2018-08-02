import time
import os.path
import itertools
from random import randint, choice
from asciimatics.screen import Screen

AVAILABLE_COLORS = [
    'COLOUR_RED',
    'COLOUR_GREEN',
    'COLOUR_YELLOW',
    'COLOUR_BLUE',
    'COLOUR_MAGENTA',
    'COLOUR_CYAN',
    'COLOUR_WHITE',
]


def read_frames(location='./frames'):
    frames = []
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), location))
    if not os.path.exists(path):
        raise ValueError("Frames path doesn't exist")
    for i in itertools.count():
        fname = os.path.join(path, '{}.txt'.format(i))
        if os.path.exists(fname):
            with open(fname, 'r') as fp:
                frames.append(fp.read().rstrip())
        else:
            return frames


def main(screen):
    frames = read_frames()
    for frame in itertools.cycle(frames):
        color_attr = choice(AVAILABLE_COLORS)
        color = getattr(Screen, color_attr)
        for i, line in enumerate(frame.split('\n')):
            screen.paint(
                line, 0, i,
                colour=color)
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()
        screen.clear()


def party():
    Screen.wrapper(main)

if __name__ == '__main__':
    party()
