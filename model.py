#assumptions -object movement is in the 2D plane, linear air resistance, constant time step and Euler integration
#units = metres,seconds,kg,gravity = 9.81 m/s^2, x is right y is up
import numpy as np
import math as m
import matplotlib.pyplot as plt
gravity = np.array([0,-9.81])
def simulate(initial_position,initial_velocity,dt,total_time,mass,drag_coefficient):
    n_steps = int(total_time/dt)+1 #creates number of calculations
    final_index = n_steps-1 # creates final index value for culling of excess values in array if necessary
    t = np.zeros((n_steps)) # time at each step
    r = np.zeros((n_steps,2)) #2D array for postions each row is a step column 0 = x 1 = y
    v = np.zeros((n_steps,2)) 
    a = np.zeros((n_steps,2)) 
    r[0] = initial_position 
    v[0] = initial_velocity
    for i in range(1, n_steps): # starts at 1 as 0 is initial condition
        
        speed = np.linalg.norm([v[i-1]])
        drag = -drag_coefficient * speed * v[i-1] / mass
        a[i] = gravity+drag
        v[i] = v[i-1] + a[i] * dt #semi implict euler integration as it is more stable than standard
        r[i] = r[i-1]+v[i]*dt
        t[i] = t[i-1] + dt
        if r[i,1] <= 0 and i>1:
            y1 = r[i-1,1]
            y2 = r[i,1]
            frac = y1/(y1-y2) #fraction of the timestep until y = 0

            r[i] = r[i-1]+frac * (r[i]-r[i-1])
            v[i] = v[i-1]+frac * (v[i]-v[i-1])

            r[i,1] = 0.0
        

            t[i] = t[i-1] +frac*dt
            
            final_index = i
            break

    return{"t":t[:final_index+1],"r":r[:final_index+1],"v":v[:final_index+1],"a":a[:final_index+1]}
