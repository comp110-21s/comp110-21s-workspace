"""Draw a black triangle with turtle graphics as a test of installation success."""

from turtle import Turtle, Screen

__author__ = "Kris Jordan <kris@cs.unc.edu>"

# Establish a window for our friend the turtle.
window: Screen = Screen()

# Construct a Turtle object and bind it to the name ertle.
ertle: Turtle = Turtle()

# Draw a black triangle.
ertle.begin_fill()
ertle.forward(100)
ertle.left(120)
ertle.forward(100)
ertle.left(120)
ertle.forward(100)
ertle.left(120)
ertle.end_fill()

# Don't quit the window until the user clicks on it.
window.exitonclick()