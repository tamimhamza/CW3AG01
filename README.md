# CW3AG01 
Autonomous Robot Navigation,
 Python ver. 3.10.6,
 RoboticsToolBox ver. 0.10.0

# Goals Of Code:
a) Allow user input to initialise the robot’s start and target coordinates, as well as loading a generated map to be navigated autonomously.

b) Calculate and continue to update the position of the robot within the map using simulated robot encoders and distance sensors.

c) Define the logic required to reach the target as fast as possible without any collision with the walls using sensory feedback.

d) Display a plot showing the robot, map, target, and any additional useful outputs, in order to visualise the robot’s locomotion towards its target.

# Importing Packages & Tools
Packages used: RoboticsToolBox, Math, MatPlotLib, Numpy, SciPi.

RoboticsToolBox is the backbone of this program, it's used to add the range sensor for the autonomous navigation and obstacle evasion and is also used to assign the bicycle vehicle type for all this to work. It's also used to add the random generated obstacles on the map which are plotted using MatplotLib.

MatplotLib is used for plotting the maze, goal marker and for making and generating the map.

# Functions of the code
The code starts by showing the user the map before the prompts so the user can choose their starting point, goal point, turning points and how many turning points there are.  

Each point is run through a checking process to make sure values inputted are suitable according to the maps dimensions. If values are not in range "Value outside of map range" is printed and program closes. If inputted points are in range the program conintinues to run. The robot starts at the starting point and continues to move to each checkpoint inputted, any obstacles in the way of the robot are automatically avoided and the robot continues on its set path to the goal point. Once the robot reaches the goal the program ends.

# Difficulties & Limitations
The main limitation was the lack of an auto generated path for the robot to move on. The issue was when curve fitting was used the curve would pass through the walls and wouldn't be suitable. That's why I designed a way for the user to input a path at the start of the program after a view of the map.

A limitation to do with the walls is that the sensor does not detect them so it was impossible to have complete autonomous navigation. There was no way that I was capable of in the timeframe of the deadline to get this completed. 

Another limitation is the degree of steering and obstacle avoidance threshold as when I increased it the vehicle would steer and then would pass through the obstacles.

These limitations aswell as an error checking system for inputted coordinates to not allow values in the maps walls are the only improvements I believe I could've made.

I had great difficulty coding this as at the start I had a set path I made which I later updated to a user inputted path. The error checking was also very difficult as the amount of loops I had to create for this to work and loops within loops caused me to have lots of errors and issues with indenting and logic it took a long time to fix. I also had an issue implementing the obstacle avoidance at the start at the same time as the set path movement.





