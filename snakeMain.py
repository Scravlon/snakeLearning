# import pygame, random, sys
import random
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

    def neightborAction(self,s,a):
        r, c = self.stateTocoo(s)
        if a == 'U':
            return self.cooTostate((r-1, c))
        elif a == 'D':
            return self.cooTostate((r+1, c))
        elif a == 'L':
            return self.cooTostate((r, c-1))
        elif a == 'R':
            return self.cooTostate((r, c+1))

    def generate_food(self):
        x = self.world
        food = 0
        i = random.randint(0, len(x))
        j = random.randint(0, len(x))
        while food == 0:
            x[i][j] = 1
            food += 1

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
        self.body_state = [60,71]
        self.current_action = 'U'
        self.actions = {'U', 'D', 'L', 'R'}
        self.maze = maze

    def increase_length(self):
        self.body_length = self.body_length + 1

    '''
    Move the snake to a new state with the current action
    '''
    def moveSnake(self):
        for i in range(1,len(self.body_state)):
            length = len(self.body_state)-i
            self.body_state[length] = self.body_state[length-1]
        self.body_state[0] = self.maze.neightborAction(self.body_state[0], self.current_action)

        #update state too

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
    snakePlayer = SnakePlayer(snakeMaze)
    print(snakePlayer.body_state)

    snakePlayer.moveSnake()
    print(snakePlayer.body_state)
    snakePlayer.moveSnake()
    print(snakePlayer.body_state)
    snakePlayer.moveSnake()
    print(snakePlayer.body_state)
    snakePlayer.current_action = 'L'
    snakePlayer.moveSnake()
    print(snakePlayer.body_state)
    snakePlayer.generate_food()
