import numpy as np
import math as m
import matplotlib.pyplot as plt
import os #these last 3 used to open the file
import platform
import subprocess

def plot_trajectory(r,label = "Projectile trajectory"):
    plt.clf() #clears previous line
    plt.plot(r[:,0],r[:,1],linewidth=2, label=label) #plots y coordinates against the x
    plt.xlabel("x (m)") # labels the axis
    plt.ylabel("y (m)")
    plt.title(label)
    plt.tight_layout()
    plt.axhline(0, linestyle="--")
    plt.grid(True) # enables a grid
    plt.legend() # displays name of line on graph
    plt.savefig("trajectory.png")
    if platform.system() == "Windows":
        os.startfile("trajectory.png")
    elif platform.system() == "Darwin":
        subprocess.call(["open","trajectory.png"])
    else:
        subprocess.call(["xdg-open","trajectory.png"])
def find_max_height(r):
    return r[:,1].max()

def find_height_increase(r):
    return find_max_height(r)-r[:,1].min()

def find_distance_travelled(r):
    x0 = r[0,0]
    for i in range(1, len(r)):
        if r[i,1] <= 0:
            return r[i,0] - x0
    return None

def find_flight_time(t, r):
    for i in range(1, len(r)):
        if r[i,1] <= 0:
            return t[i]

    
