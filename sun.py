from vpython import *

p = vector(0.6, 0, 0)
b = sphere(pos=vector(5,0,0),color=color.blue,redius=.25,make_trail=True)
w = sphere(pos=b.pos+p,redius=0.1)
r = sphere(color=color.red,redius=0.9)
while True:
    rate(50)
    b.pos = rotate(b.pos, angle=0.001,axis=vector(0,2,1))
    p = rotate(p, angle=0.013,axis=vector(0,5,5))
    w.pos = b.pos + p