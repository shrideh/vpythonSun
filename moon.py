from vpython import *
import numpy as np
from math import sin,cos

a = 5
b = 3.5
ball = sphere(radius=0.2, color=color.blue, pos=vector(-a,0,0),make_trail=True)
ball2 = sphere(radius=0.08, color=color.yellow, pos=vector(-a,0,0))
sun = sphere(radius=0.37,pos=vector((a**2-b**2)**0.5, 0, 0), color=color.red)
def y(x):
    return b * (1 - (x/a)**2)**0.5
while True:
    for n in np.linspace(-5,5,num=1000):
        t += 0.01
        rate(30)
        ball.pos.x = n
        ball.pos.y = y(n)
        ball2.pos.x = n + 0.5*cos(t)
        ball2.pos.y = y(n) + 0.5*sin(t)
    for n in np.linspace(5, -5, num=1000):
        t += 0.01
        rate(30)
        ball.pos.x = n
        ball.pos.y = -y(n)
        ball2.pos.x = n + 0.5*cos(t)
        ball2.pos.y = -y(n) + 0.5*sin(t)
