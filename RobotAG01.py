from roboticstoolbox import DXform, Bicycle, RandomPath, VehicleIcon, RangeBearingSensor, LandmarkMap # initialise all packages

from math import pi, atan2

import matplotlib.pyplot as plt

import matplotlib.image as mpimg

import numpy as np

from scipy.io import loadmat

anim = VehicleIcon('robot', scale=5)  # give robot image

run = True

# view map first before inputs so user can get path, goal, starting coordinates
map = LandmarkMap(50, 50)  # set grid size
map.plot()  # plot obstacles

rectangle_1 = plt.Rectangle((-50, 47), 100, 3, fc='black', ec='black')
plt.gca().add_patch(rectangle_1)
rectangle_2 = plt.Rectangle((-50, -50), 3, 100, fc='black', ec='black')
plt.gca().add_patch(rectangle_2)
rectangle_3 = plt.Rectangle((-50, -47), 100, -3, fc='black', ec='black')
plt.gca().add_patch(rectangle_3)
rectangle_4 = plt.Rectangle((50, -50), 4, 100, fc='black', ec='black')
plt.gca().add_patch(rectangle_4)
rectangle_5 = plt.Rectangle((50, -50), -3, 100, fc='black', ec='black')
plt.gca().add_patch(rectangle_5)
rectangle_6 = plt.Rectangle((-19, 14), 37, 4, fc='black', ec='black')
plt.gca().add_patch(rectangle_6)
rectangle_7 = plt.Rectangle((-19, 18), 4, -35, fc='black', ec='black')
plt.gca().add_patch(rectangle_7)
rectangle_8 = plt.Rectangle((14, 50), 4, -34, fc='black', ec='black')
plt.gca().add_patch(rectangle_8)
rectangle_9 = plt.Rectangle((-19, -18), 45, 4, fc='black', ec='black')
plt.gca().add_patch(rectangle_9)

plt.show()


# Input for starting coordinates with value range check
X = int(input('Input starting X coordinate'))     # Checks if values are in range if they are run continues to equal True so code runs
if X > 50 or X < -50:                             # If not code stops running
    print('Value outside of mape range')
    run = False

while run != False:
    Y = int(input('Input starting Y coordinate'))
    if Y > 50 or Y < -50:
        print('Value outside of mape range')
        run = False

    while run != False:
        initial_pos = [X, Y, 1.5]                 # Add coordinates to array

        veh = Bicycle(  # assign vehicle type
            animation=anim,

            control=RandomPath,

            x0=((initial_pos[0], initial_pos[1], 0))
            )
        veh.init(plot=True)  # visualise vehicle on map

        # create target point and illustrate it

        X_ = int(input('Input goal X cooordinate'))  # input for goal coordinates with range checker that runs code if allowed and stop code if false
        if X_ > 50 or X_ <-50:
            print('Value outside of mape range')
            run = False
        while run != False:
            Y_ = int(input('Input goal Y coordinate'))
            if Y_ > 50 or Y_ < -50:
                print('Value outside of mape range')
                run = False

            goal = [X_, Y_];  # marker cooridinates  # assign variables to array
            goal_marker_style = {                 # designing goal marker
                'marker': 'o',  # marker style
                'markersize': 8,  # size
                'color': 'b',  # colour
            }
            plt.plot(goal[0], goal[1], **goal_marker_style) # plot goal marker

            map = LandmarkMap(50, 50)  # set grid size
            map.plot()  # plot obstacles
            
            # plot maze design
            rectangle_1 = plt.Rectangle((-50, 47), 100, 3, fc='black', ec='black')
            plt.gca().add_patch(rectangle_1)
            rectangle_2 = plt.Rectangle((-50, -50), 3, 100, fc='black', ec='black')
            plt.gca().add_patch(rectangle_2)
            rectangle_3 = plt.Rectangle((-50, -47), 100, -3, fc='black', ec='black')
            plt.gca().add_patch(rectangle_3)
            rectangle_4 = plt.Rectangle((50, -50), 4, 100, fc='black', ec='black')
            plt.gca().add_patch(rectangle_4)
            rectangle_5 = plt.Rectangle((50, -50), -3, 100, fc='black', ec='black')
            plt.gca().add_patch(rectangle_5)
            rectangle_6 = plt.Rectangle((-19, 14), 37, 4, fc='black', ec='black')
            plt.gca().add_patch(rectangle_6)
            rectangle_7 = plt.Rectangle((-19, 18), 4, -35, fc='black', ec='black')
            plt.gca().add_patch(rectangle_7)
            rectangle_8 = plt.Rectangle((14, 50), 4, -34, fc='black', ec='black')
            plt.gca().add_patch(rectangle_8)
            rectangle_9 = plt.Rectangle((-19, -18), 45, 4, fc='black', ec='black')
            plt.gca().add_patch(rectangle_9)

            # initialise sensor
            sensor = RangeBearingSensor(robot=veh, map=map, animate=True)
                
            # moving vehicle on path using checkpoint
            goal_arr = []  # create array with points free of obstacle
            
            turnN = int(input('Input number of checkpoints'))

            for i in range(turnN):
                turn_arr = [] # create array to assign single turning point coordinates in before being appended
                turnX = int(input('Input checkpoint X coordinate')) # input coordinates with value checker that will either end or continue code
                if turnX > 50 or turnX < -50:
                    print('Value outside of map range')
                    run = False
                    exit()
                else:
                    turnY = int(input('Input checkpoint Y coordinate'))
                    if turnY > 50 or turnY < -50:
                        print('Value outside of mape range')
                        run = False
                        exit()
                    else:
                        turn_arr.append(turnX)    # append inputted values to first array which is reset each time the for loop is looped (10 times), so user has 10 coordinates to input
                        turn_arr.append(turnY)
                        goal_arr.append(turn_arr) # append each X,Y array into larger goal array containing 10 turning points and the goal
            
            goal_arr.append(goal) # append goal point into array

            target = goal_arr
            goal_arr.insert(0, initial_pos)

            x_arr = [item[0] for item in goal_arr]  # split X & Y into diff arrays
            y_arr = [item[1] for item in goal_arr]  

            if run != False:
                for n in range(len(goal_arr)-1):
                    run = True
                    target = [x_arr[n+1], y_arr[n+1]]
                    while (run):  # continues to operate if False loop ends and goes back to check for next point and repeat...
                        goal_heading = atan2( 
                        target[1] - veh.x[1],
                        target[0] - veh.x[0]
                            )

                        for i in sensor.h(veh.x):
                            if (i[0] < 3):           # checks for obstacle if true move 90 degrees and continue
                                if(abs(i[1]) < pi/4):
                                    run = True
                                    veh.step(4,0.5)
                            else: 
                                run = True 

                        steer = goal_heading-veh.x[2] # sets robot on set path to check/turning points inputted by user in beggining
                        if steer>pi:
                            steer = steer-2*pi 
                        veh.step(4,steer)  
                        if( (abs(target[0]-veh.x[0]) >0.3) or (abs(target[1] -veh.x[1]) >0.3) ):
                            run=True
                        else:
                            run=False                # stops loop when robot reaches destination
                        veh._animation.update(veh.x)
                        plt.pause(0.0005)
                plt.pause(1000)
