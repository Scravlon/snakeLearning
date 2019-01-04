# import pygame, random, sys
import random
import numpy as np


class Maze:
    def __init__(self, world):
        self.world = world
        self.worldShape = world.shape
        self.stateSize = self.worldShape[0] * self.worldShape[1]
        self.gameRunning = True
        self.reward = self.defReward()

        # self.mapSize = 100
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

    def generate_food(self, body_state):

        i = random.randint(1, 10)
        j = random.randint(1, 10)
        c = [i,j]
        foodState = self.cooTostate(c)
        while foodState in body_state:
            i = random.randint(1, 10)
            j = random.randint(1, 10)
            c = [i, j]
            foodState = self.cooTostate(c)
        return foodState

    '''
    Default reward all edge -2
    '''
    def defReward(self):
        return np.array([
        [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]])

    '''
    Reward with maze, food location (+5). body state (-2), border state (-2)
    '''
    def makereward(self, body_state, food_state):
        r = np.array([
        [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2],
        [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]])

        for a in body_state:
            i,j = self.stateTocoo(a)
            r[i][j] = r[i][j] - 2
        i,j = self.stateTocoo(food_state)
        r[i][j] = r[i][j] + 5
        return r


class SnakePlayer:
    def __init__(self, maze):
        self.food_state = -1
        self.body_length = 2
        self.tail_state = 71
        self.body_state = [65, 77]
        self.current_action = 'U'
        self.actions = {'U', 'D', 'L', 'R'}
        self.maze = maze
        self.generate_food_maze()
        self.Q = np.zeros((144,4))

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

    def generate_food_maze(self):
        retVal = self.maze.generate_food(self.body_state)
        self.food_state = retVal
        return retVal

    '''
    Game over
    '''
    def wall_state(self):
        maze = self.maze.world
        snake_head = self.maze.stateTocoo(self.body_state[0])
        for i in range(len(self.maze.world)):
            for j in range(len(self.maze.world)):
                if i == 0 or i == len(self.maze.world) - 1 or j == 0 or j == len(self.maze.world) - 1:
                    maze[i][j] = -1
        return maze

    def snake_die(self):
        live = True
        snake_head = self.maze.stateTocoo(self.body_state[0])
        maze = self.wall_state()
        # print(maze)
        for i in range(len(maze)):
            for j in range(len(maze)):
                if self.maze.cooTostate(snake_head) == -1:
                    live = False
        return 'game over'


    '''
    Visualize body location return matrix
    '''
    def body_np(self):
        retVal = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        for a in self.body_state:
            r,c = self.maze.stateTocoo(a)
            retVal[r][c] = 1
        return retVal

    def epsG(self, ep : float = 0.3):
        if random.uniform(0,1) < ep:
            return self.actions[random.randrange(0,len(self.actions))]
        else:
            return self.bestAction()

    def bestAction(self):
        retVal= self.actions[np.argmax(self.Q[self.body_state[0],:],axis=0)]
        self.current_action = retVal
        return retVal

    def qstep(self):
        action = self.epsG(0.3)
        # nextS, reward = self.
        return ''
if __name__=="__main__":

    snakeMaze = Maze(np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
    # r,c = snakeMaze.stateTocoo(60)
    # print(iniState[r][c])

    snakePlayer = SnakePlayer(snakeMaze)
    # print(snakePlayer.body_state)
    #
    # print(snakePlayer.body_np())
    #
    # snakePlayer.moveSnake()
    # print(snakePlayer.body_state)
    # print(snakePlayer.body_np())
    # snakePlayer.moveSnake()
    # print(snakePlayer.body_state)
    # print(snakePlayer.body_np())
    #
    # snakePlayer.moveSnake()
    # print(snakePlayer.body_state)
    # print(snakePlayer.body_np())
    #
    # snakePlayer.current_action = 'L'
    # snakePlayer.moveSnake()
    # print(snakePlayer.body_state)
    # print(snakePlayer.body_np())
    #
    # print(snakePlayer.maze.makereward(snakePlayer.body_state,snakePlayer.food_state))
    snakePlayer.snake_die()
    # snakePlayer.maze.generate_food()
