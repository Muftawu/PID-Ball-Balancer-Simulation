## PID ALGORITHM SIMULATION WITH PYGAME

- I have been fascinated with the PID algorithm used in many
modern and legacy control systems and how it makes everything look smooth and responsive particularly in robotics.

- I plan on building my own ball balancer robot someday but
before that I decided to implement a simulation of it in python using the pygame library.

# FILE STRUCTURE
    - ball.py file: contains the 'Ball' class with methods to draw the ball, calculate the error and contains the PID constants.

    - balancer.py file: entry point to the program/simulation. This is the file you run to start the simulation.

    - settings.py file: As the name suggests, it contains all the simulations constants, variables and values for the simulation.

    - utils.py file: contains helper functions for simulation

# HOW THE SYSTEM WORKS
- The simulation is a very simple one with two main component.
    - A display area acting as a Platform
    - A blue circle acting as a ball 

- The target position for the ball (blue circle) is the center of the display (platform) which is half the width of the display for the x-coordinate and half the height of the display area for the y-coordinate. 
Same as (x, y) -> (0.5*DISPLAY_WIDTH, 0.5*DISPLAY_HEIGHT)

- With the target position established, the error is calculated using the ##formula, distance between two points formula. Pretty simple 😊 

- Two PID algorithms are used. One for the X-axis and the other for the Y-axis. With some little tweaking, the Kp, Ki, and Kd values are calculated and voila 👻, we have smooth feedback and control.
PID values can be seen from the [ball.py] file in the 'Ball' class.

- You can also see the effect of the PID algorithm on multiple balls by changing the value of the NUM_BALLS in the [settings.py] file
