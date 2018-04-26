"""
Author - Owen Sullivan
Email - multiojuice@gmail.com
desc - TBD
"""

import turtle
import math

def get_initial_points(function):
    """
    desc - Gets the x and y coordinates for a given point
    return - the array of points as [[x,y],[x,y],[x,y]] 
        sorted in ascending order of x.
    """
    start_theta = 0
    end_theta =  math.pi
    dx = .05
    points = []
    while start_theta <= end_theta:
        points.append([start_theta,function(start_theta)])
        start_theta += dx
    return points    


def make_points_continous(points):
    """
    desc - resorts array, see below.
    param - array of pointers sorted in ascending order by x
    return - the array of points as [[x,y],[x,y],[x,y]] 
        sorted in a "continous order". 
    """
    pass

def draw_graph(points):
    turtle.clear()
    turtle.pd()
    for point in points:
        turtle.goto(0,0)
        turtle.seth(0)
        turtle.left(int(point[0] * 180 / math.pi))
        turtle.forward(int(point[1] * 100))

def draw_graph_cont(points):
    turtle.clear()
    turtle.pu()

turtle.speed(9)
draw_graph(get_initial_points(math.sin))



