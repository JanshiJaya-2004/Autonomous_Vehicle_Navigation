from stable_baselines3 import PPO
from env.simple_env import SimpleCarEnv

env = SimpleCarEnv()
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=20000)

model.save("model/car_model")
print("Training completed")
