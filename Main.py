import pygame as p
import Engine

p.init()
WIDTH = HEIGHT = 512  # 400 is another option

DIMENSION = 8  # dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations later on
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main. 
'''


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'WB', 'WK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bk', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


# Note: we can access an image by saying "IMAGES['wp']"

def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = Engine.GameState()
    loadImages()  # only do this once before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        clock.tick(MAX_FPS)
        p.display.flip()


if __name__ == '__main__':
    main()
