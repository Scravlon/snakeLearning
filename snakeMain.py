import pygame, random, sys
import numpy as np


class Maze:
    def __init__(self, world):
        self.world = world
        self.worldShape = world.shape
        self.stateSize = self.worldShape[0] * self.worldShape[1]
        self.gameRunning = True
        self.reward = self.makereward()

        self.mapSize = 100
        self.actions = {'U', 'D', 'L', 'R'}

    # Functions for going between the two representations
    def stateTocoo(self, s):
        # transfer state to grid world coordinate (x,y)
        r = int(s / self.worldShape[1])
        c = np.mod(s, self.worldShape[1])
        return r, c

    def cooTostate(self, c):
        # transfer grid world coordinate (x,y) to state
        return c[0] * self.worldShape[1] + c[1]

    def neighborsList(self, s):
        # returns neighbors index of a given state (0-79)
        nbrs = []
        r, c = self.stateTocoo(s)
        if r > 0:
            nbrs.append(self.cooTostate((r - 1, c)))
        if r < self.worldShape[0] - 1:
            nbrs.append(self.cooTostate((r + 1, c)))
        if c > 0:
            nbrs.append(self.cooTostate((r, c - 1)))
        if c < self.worldShape[1] - 1:
            nbrs.append(self.cooTostate((r, c + 1)))
        return nbrs



    '''
    Reward with only maze
    '''
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


class SnakePlayer:
    def __init__(self, maze):
        self.body_length = 2
        self.tail_state = 71
        self.body_state = {60,71}
        self.current_action = 'U'
        self.actions = {'U', 'D', 'L', 'R'}
        self.maze = maze

    def increase_length(self):
        self.body_length = self.body_length + 1


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
    snakeMaze = Maze(np.array([
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
    r,c = snakeMaze.stateTocoo(60)
    print(iniState[r][c])
