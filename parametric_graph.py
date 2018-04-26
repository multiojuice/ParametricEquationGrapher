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
    end_theta =  10 * math.pi
    dx = .025
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
    """
    This draw function draws the simple graph by going up and down and makes it 
    look like a filled in picture!
    Uses polar coordinates to locate where to go. using the simple goto(radiuns, radius)
    """
    turtle.clear()
    turtle.pd()
    for point in points:
        turtle.goto(0,0)
        turtle.seth(0)
        turtle.left(int(point[0] * 180 / math.pi))
        turtle.forward(int(point[1] * 100))


def draw_graph_cont(points):
    """
    This function draws it in a continous line. This is the actual test version
    for the code that will go onto the arduino. Because the laser pointer will
        have to draw it in a continous line so it keeps the image.
    """
    coefficient = 50
    turtle.clear()
    turtle.pu()
    turtle.seth(0)
    turtle.goto(points[0][1] * math.cos(points[0][0]) * coefficient,points[0][1] * math.sin(points[0][0]) * coefficient)
    turtle.pd()
    for point in points:
        turtle.goto(point[1] * math.cos(point[0]) * coefficient,point[1] * math.sin(point[0]) * coefficient)

"""
These are all sample functions!
Check to see how they end up graphing out!
"""
def cosplusone(x):
    return (2* math.cos(x)) + 1

def rosegraph(x):
    return math.sin(8*x)

def archimedean_spiral(x):
    return 1 + (.3 * x)


"""
Main Commands
"""
turtle.speed(4)
draw_graph_cont(get_initial_points(archimedean_spiral))
turtle.done()


