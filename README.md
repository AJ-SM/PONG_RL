# Deep Reinforcement Learning on Custom Game : using PPO 

![PyTorch](https://img.shields.io/badge/PyTorch-2.0.0-%23EE4C2C?logo=pytorch)
![Stable-Baselines3](https://img.shields.io/badge/Stable--Baselines3-2.0.0-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.5.2-green?logo=pygame)

# Introduction: 
Pong is a custom made environment made to demonstrate the application of DRL Algorithm(here PPO) using StableBaseline3.

# Problem Statement:
The environment classic Pong game, with 2 paddle and one ball , paddles are restricted on X-axis and can move along Y-axis only,
where as the ball is allowed to all freedome to both of the axis. The ball will spwan on randomly on Y-axis form center of screen and move toward the player/agent with randome X and Y velocities.
The palyer/agent will score if the ball touches the opposite end.
On scoring 10 point the game end with the victory of scoring party. The palyer/Agent has to adjust the paddle position according the the poistion of ball.

# Apporach:
The agent has been trained on another custom sandbox environment. Where the game environment is specifically designed to push the agent 
to score more against the opponent. The Sandbox environment has the reward system optimized, for relative poistion of the paddle and ball. The Sparse reward of 
winning the game after securing 10 point is borken down in Dense Reward of score each time. For time optimization instead of giving when the ball hits the opposite end
the reward was given every thing the agent hits the ball successfull/ This reduces the waste of time ball traveling to another end, and doing randome movement of paddle initially.

# Implementation Included:
- PyGame to create the Pong Environment form scratch.
- Proximal Policy Optimization(PPO) using StableBaseline3.


## Algorithm: Proximal Policy Optimization (PPO)

1. **Initialize** policy parameters θ and value function parameters φ.  
2. **Repeat until convergence**:  
   - Collect trajectories by running the current policy πθ in the environment:  
     - Store states (s), actions (a), rewards (r), next states (s′), and log-probabilities logπθ(a|s).  
   - Compute **returns** (R) and **advantages** (A) using GAE:  
     - δt = rt + γ Vφ(st+1) − Vφ(st)  
     - At = ∑ (γλ)^l δt+l  
   - Normalize advantages to have zero mean and unit variance.  
   - For **K epochs**, repeat:  
     - Divide data into mini-batches.  
     - Compute probability ratio:  
       r(θ) = πθ(a|s) / πθ_old(a|s)  
     - Compute surrogate objective:  
       Lclip(θ) = E[min(r(θ)·A, clip(r(θ), 1−ε, 1+ε)·A)]  
     - Compute value loss: (Vφ(s) − R)^2  
     - Add entropy bonus to encourage exploration.  
     - Update θ and φ by minimizing total loss:  
       Loss = −Lclip(θ) + c_v·ValueLoss − c_e·Entropy  
   - Update old policy parameters: θ_old ← θ.  




# 🔹 Training Process:



## After 10K Episodes:

<p align="center">
  <img width="700" height="500" alt="mean_Epi_Length" 
       src="https://github.com/user-attachments/assets/29567cda-bba2-4a23-94de-c9ac82f37e8a" />
</p>



## After 20K Episodes:


<p align="center">
  <img width="700" height="500" alt="mean_Epi_Length" 
       src="https://github.com/user-attachments/assets/fcd5b912-15ad-4e65-b404-e292e4b608f2" />
</p>



## After 200K Episodes:

<p align="center">
  <img width="700" height="500" alt="mean_Epi_Length" 
       src="https://github.com/user-attachments/assets/9531a74d-e29a-4326-95a6-de7f3b7fb14e" />
</p>



# 📈 Results:
### Mean Episode Rewards: 

<p align="center">
  <img width="700" height="500" alt="ew_rew_mean" 
       src="https://github.com/user-attachments/assets/0370f8a4-8604-4091-83d5-d15d1eed92ee" />
</p>


### Mean Episode Length:

<p align="center">
  <img width="700" height="500" alt="mean_Epi_Length" 
       src="https://github.com/user-attachments/assets/70d2a0a1-cc5f-4f7e-ad22-a0064fd0d098" />
</p>

## 📉Losses:

### Training Loss: 

<p align="center">
  <img width="700" height="500" alt="mean_Epi_Length" 
       src="https://github.com/user-attachments/assets/41f421cd-c30b-437e-b577-f731c5055696" />
</p>

### Value Loss:
<p align="center">
  <img width="700" height="500" alt="mean_Epi_Length" 
       src="https://github.com/user-attachments/assets/7facefe5-315f-4700-9d6a-35bfe901fdec" />
</p>

### Entropy Loss:

<p align="center">
  <img width="700" height="500" alt="mean_Epi_Length" 
       src="https://github.com/user-attachments/assets/dbe2bfd0-7e05-4e0f-97ef-1766bb88a7c4" />
</p>



# 🔄 Planned Updates
- Implement the and testing multiple DRL algorithms to test the precisoin and speed of resolving the problem.
- Implement RL algorithms using discretization of state space.
- Implementation using CNNPolicy.

