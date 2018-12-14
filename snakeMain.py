import pygame, random, sys
import numpy as np

class snakeMaze:
    def __init__(self):
        self.endGame = False
        self.reward = self.makereward()

        self.mapSize = 100
        self.actions = {'U', 'D', 'L', 'R'}


    def makereward(self):
        print("Reward")
        return np.zeros(80)

