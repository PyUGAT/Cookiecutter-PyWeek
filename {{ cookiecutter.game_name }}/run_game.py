#
# {{ cookiecutter.game_name }}
# {{ cookiecutter.pyweek_link }} | {{ cookiecutter.github_link }}
# Copyright (c) 2022 {{ cookiecutter.contributors }}
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
import argparse
import logging

import pygame as pg


parser = argparse.ArgumentParser()
parser.add_argument(
    "--debug",
    action="store_true",
    help="Show debug info",
)
cliargs = parser.parse_args()

logging.basicConfig(
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.DEBUG if cliargs.debug else logging.WARNING,
)


def main():
    SCREEN_WIDTH = 300
    SCREEN_HEIGHT = 100
    PINK = (255, 20, 147)

    pg.init()
    pg.display.set_caption('Hi there =)')
    display = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display.fill(PINK)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

    pg.quit()
    logging.info('Goodbye!')



if __name__ == "__main__":
    main()
