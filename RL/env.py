import os
import numpy as np
import gym
import pygame
import random
from gym import spaces
from stable_baselines3 import PPO

class PongSand(gym.Env):
    """Custom Environment that follows the Gymnasium interface."""

    def __init__(self):
        super(PongSand, self).__init__()
        pygame.init()

        # Game Screen Setup
        self.screen_width = 1280
        self.no_of_plays = 0 
        self.screen_height = 720
        self.rect_1_posi_y = 300
        
        self.ball_posi = [640, 360]
        self.velo_x, self.velo_y = -10, -2

        # Scores
        self.score_p1 = 0

        # Define the Action and Observation Space
        self.action_space = spaces.Discrete(2)  # Number of actions: 0 = Up, 1 = Down

        # Observations: [ball_x, ball_y, velo_x, velo_y, paddle_y]
        self.observation_space = spaces.Box(
            low=np.array([0, 0, -15, -15, 0]),  # Minimum values
            high=np.array([self.screen_width, self.screen_height, 15, 15, self.screen_height - 100]),  # Maximum values
            dtype=np.float32,
        )

        self.clock = pygame.time.Clock()

    def step(self, action):
        """Update game state based on an action."""
        done = False
        reward = 0  # Reward initialization

        # Action logic for paddle movement
        if action == 0 and self.rect_1_posi_y > 0:  # Up
            self.rect_1_posi_y -= 20
        if action == 1 and self.rect_1_posi_y < 620:  # Down
            self.rect_1_posi_y += 20

        # Ball Movement
        self.ball_posi[0] += self.velo_x
        self.ball_posi[1] += self.velo_y

        # Ball collision with screen edges (top/bottom)
        if self.ball_posi[1] - 15 <= 0 or self.ball_posi[1] + 15 >= self.screen_height:
            self.velo_y = -self.velo_y







        # Ball collision with player paddle and scoring
        if self.ball_posi[0] - 15 <= 55:
            if self.rect_1_posi_y < self.ball_posi[1] < self.rect_1_posi_y + 100:
                  # Reward for hitting the paddle
                self.velo_x = -self.velo_x  # Reverse X direction on paddle collision
            

        # Ball out of bounds on the right side
        if self.ball_posi[0] + 15 >= self.screen_width:
            self.velo_x = -self.velo_x
            self.score_p1 += 5

        # Check if the ball goes out of bounds on the left (lose condition)
        if self.ball_posi[0] - 15 <= 0:
            self.no_of_plays+=1
            self.score_p1 -= 2  # Penalty for missing the ball
            self.ball_posi = np.array([640, random.randint(100,700)])
        

        if self.rect_1_posi_y - self.ball_posi[1] <-4 and self.rect_1_posi_y - self.ball_posi[1]> -76  and self.ball_posi[0]<60:
            self.score_p1 += 1
            # print("done")


        if self.rect_1_posi_y >550 or self.rect_1_posi_y < 25:
            self.score_p1 -=2
        

        # Set episode termination condition based on the player's score
        if self.score_p1 < -10 or self.no_of_plays==700:
            done = True
        reward = self.score_p1

        return np.array(self._get_obs()), reward, done, False, {}

    def reset(self, seed=None, **kwargs):
        """Reset the game state for a new episode."""
        super().reset(seed=seed, **kwargs)
        self.rect_1_posi_y = 300
        self.ball_posi = np.array([640, 360])
        self.velo_x, self.velo_y = -10, -2
        self.score_p1 = 0
        return np.array(self._get_obs()), {}

    def _get_obs(self):
       return np.array([self.ball_posi[0], self.ball_posi[1], self.velo_x, self.velo_y, self.rect_1_posi_y], dtype=np.float32)


    def close(self):
        """Close the game and quit Pygame."""
        pygame.quit()
