import gym
import numpy as np

class SimpleCarEnv(gym.Env):
    def __init__(self):
        super(SimpleCarEnv, self).__init__()
        
        # Observation → distance from obstacle (dummy)
        self.observation_space = gym.spaces.Box(low=0, high=100, shape=(1,), dtype=np.float32)
        
        # Action → steer left (0), right (1), straight (2)
        self.action_space = gym.spaces.Discrete(3)

        self.state = 50  # midpoint
        self.done = False
    
    def step(self, action):
        if action == 0:
            self.state -= 10
        elif action == 1:
            self.state += 10
        
        reward = 1 if 30 < self.state < 70 else -10
        self.done = reward == -10

        return np.array([self.state]), reward, self.done, {}
    
    def reset(self):
        self.state = 50
        self.done = False
        return np.array([self.state])
