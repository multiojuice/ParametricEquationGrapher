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
    end_theta =  2 * math.pi
    dx = .01
    points = []
    while start_theta <= end_theta:
        points.append([int(start_theta * 180 / math.pi),int(function(start_theta) * 100)])
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
        turtle.left(point[0])
        turtle.forward(point[1])



def draw_graph_cont(points):
    turtle.clear()
    turtle.pu()


def cosplusone(x):
    return math.cos(x) + 1


def rosegraph(x):
    return math.sin(2*x)


turtle.speed(0)
draw_graph(get_initial_points(cosplusone))
turtle.done()


