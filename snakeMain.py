import pygame, random, sys
import numpy as np


class maze:
    def __init__(self, world):
        self.world = world
        self.worldShape = world.shape
        self.stateSize = self.worldShape[0] * self.worldShape[1]
        self.endGame = False
        self.reward = self.makereward()

        self.mapSize = 100
        self.actions = {'U', 'D', 'L', 'R'}

    # Functions for going between the two representations
    def state2coord(self, s):
        # transfer state to grid world coordinate (x,y)
        row = int(s / self.worldShape[1])
        col = np.mod(s, self.worldShape[1])
        return row, col

    def coord2state(self, c):
        # transfer grid world coordinate (x,y) to state
        return c[0] * self.worldShape[1] + c[1]

    def numNbrs(self, s):
        nbrs = 0
        r, c = self.state2coord(s)
        if r > 0 and self.world[r - 1, c] == 0:
            nbrs += 1
        if r < self.worldShape[0] - 1 and self.world[r + 1, c] == 0:
            nbrs += 1
        if c > 0 and self.world[r, c - 1] == 0:
            nbrs += 1
        if c < self.worldShape[1] - 1 and self.world[r, c + 1] == 0:
            nbrs += 1
        return nbrs

    def nbrList(self, s):
        # returns neighbors index of a given state (0-79)
        nbrs = []
        r, c = self.state2coord(s)
        if r > 0 and self.world[r - 1, c] == 0:
            nbrs.append(self.coord2state((r - 1, c)))
        if r < self.worldShape[0] - 1 and self.world[r + 1, c] == 0:
            nbrs.append(self.coord2state((r + 1, c)))
        if c > 0 and self.world[r, c - 1] == 0:
            nbrs.append(self.coord2state((r, c - 1)))
        if c < self.worldShape[1] - 1 and self.world[r, c + 1] == 0:
            nbrs.append(self.coord2state((r, c + 1)))
        return nbrs

    def actionList(self, s):
        nbrs = []
        r, c = self.state2coord(s)
        if r > 0 and self.world[r - 1, c] == 0:
            nbrs.append('U')
        if r < self.worldShape[0] - 1 and self.world[r + 1, c] == 0:
            nbrs.append('D')
        if c > 0 and self.world[r, c - 1] == 0:
            nbrs.append('L')
        if c < self.worldShape[1] - 1 and self.world[r, c + 1] == 0:
            nbrs.append('R')
        return nbrs



    def makereward(self):
        print("Reward")
        return np.array([
        [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]])


if __name__=="__main__":

    iniState = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    snakeMaze = maze(np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
    print(snakeMaze.actionList(0))
    print("Done")