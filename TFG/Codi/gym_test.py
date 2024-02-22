import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import pickle
import random

env = gym.make('FrozenLake-v1', map_name="4x4", is_slippery=False, render_mode='human')

q = np.zeros((env.observation_space.n, env.action_space.n)) # init a 64 x 4 array
action_list = []
won = False
terminated = False      
truncated = False 
while won==False:
    if(terminated):
        action_list[-1] = (action_list[-1]+1)%4
    else:
        action_list.append(env.action_space.sample())
    state = env.reset()[0]
    terminated = False      
    truncated = False       
    a=0
    while(not terminated and not truncated and a < len(action_list)):
        action = action_list[a] # actions: 0=left,1=down,2=right,3=up
        new_state,reward,terminated,truncated,_ = env.step(action)
        if(state == new_state):
            terminated = True
        state = new_state        
        print(action_list)
        if(state == 15):
            won=True
        else:
            a=a+1

env.close()

#action_list = [2,2,1,1,1,2]