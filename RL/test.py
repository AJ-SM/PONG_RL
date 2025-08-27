import os
from stable_baselines3 import PPO
from env import PongSand

models_dir = "MODELS/PPO"
logdir = "logs"


os.makedirs(models_dir, exist_ok=True)
os.makedirs(logdir, exist_ok=True)

env = PongSand()


# Initialize the model


# Training parameters
TIMESTEPS = 10000
steps = 300
model = PPO.load("E:\\Storage\\Codes\\PYTHON\\PONG\\game2\\MODELS\\PPO\\1000000.zip")

obs = self.reset()  # Reset the environment once at the beginning
done = False

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
                return  # Exit the game loop

            # Predict the action using the trained model
        action, _ = model.predict(obs)

            # Take a step in the environment
        obs, reward, done, _ = self.step(action)

            # Render the environment
        self.render()

            # Reset the environment if done
        if done:
            obs = self.reset()
env.close()
