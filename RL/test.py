import os
from stable_baselines3 import PPO
from env import PongSand

models_dir = "MODELS/PPO"
logdir = "logs"


os.makedirs(models_dir, exist_ok=True)
os.makedirs(logdir, exist_ok=True)

env = PongSand()


# Initialize the model
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=logdir)

# Training parameters
TIMESTEPS = 10000
steps = 300

# Training loop
for step in range(1, steps + 1):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"{models_dir}/{TIMESTEPS * step}")

    # Run the environment to visualize the current model
    if step % 10 == 0: 
        print(f"Running the environment after step {step}")

env.close()
