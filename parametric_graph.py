"""
Author - Owen Sullivan
Email - multiojuice@gmail.com
desc - TBD
"""

import turtle
import math

def get_initial_points():
    """
    desc - Gets the x and y coordinates for a given point
    return - the array of points as [[x,y],[x,y],[x,y]] 
        sorted in ascending order of x.
    """
    start_x = -1
    end_x = 1
    dx = .1
    points = []
    for i in range(start_x,end_x+1,dx):
        temp = []
        temp[0] = math.sin(math.pi * 2 * i)
        temp[1] = math.cos(math.pi * 2 * i)
        points.append(temp)
    # Still being worked on





def make_points_continous(points):
    """
    desc - resorts array, see below.
    param - array of pointers sorted in ascending order by x
    return - the array of points as [[x,y],[x,y],[x,y]] 
        sorted in a "continous order". 
    """



