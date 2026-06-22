import model 
import analysis as a
import numpy as np
import math as m
def main():
    initialxpos = float(input("enter starting x coordinate: "))
    initialypos = float(input("enter starting y coordinate: "))
    initialpos = np.array([initialxpos,initialypos])

    mass1 = float(input("enter mass of object (kg): "))
    angle = float(input("enter angle in degrees of launch in relation to x axis: "))
    speed = float(input("enter speed in m/s: "))

    angleradians = angle*m.pi/180 # converts to radians
    xvelocity = speed*m.cos(angleradians) # turns into 2 vectors 1 on x and 1 on y axis
    yvelocity = speed*m.sin(angleradians) 
    initial_velocity1 = np.array([xvelocity,yvelocity])
    if abs(xvelocity) < 1e-10:
        initial_velocity1[0] = 0.0
    if abs(yvelocity) < 1e-10:
        initial_velocity1[1] = 0.0
    

    dt1 = float(input("enter length of time increments (s): "))
    total_time1 = float(input("enter total amound of time for simulation (s): "))
    drag_coefficient1 = float(input("enter drag coefficient (usually between 0-2 squere is 0.47): "))
    
    output = model.simulate(initialpos,initial_velocity1,dt1,total_time1,mass1,drag_coefficient1) #calls the function
    r = output["r"]
    t = output["t"]
    max_height = a.find_max_height(r)
    distance_travelled = a.find_distance_travelled(r)
    flight_time = a.find_flight_time(t,r)
    print("the max height reached was:", max_height,"m")
    print("the distance travelled was: ", distance_travelled,"m")
    print("the flight time was:",flight_time,"s")
    label = "Trajectory (v=",speed,"m/s, theta =",angle,"degrees)"
    a.plot_trajectory(r,label=label)
b = True
while b:
    main()





