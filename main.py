#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import math

errorPercision = 5

def findY(angle, x, v, g=9.8):
    return x*math.tan(angle) - (g*x*x)/(2*v*v*math.cos(angle)*math.cos(angle))

def findAngle(x, y, v, g):
    if(x == 0):
        return "x cannot be 0"
    elif(v == 0):
        return "Velocity cannot be 0"
    
    a = (-g*x) / (2*v*v)
    b = 1
    c = a - y/x
    
    discrim = b - 4*a*c
    
    if(discrim < 0):
        return "Insufficient Velocity"
    
    return math.degrees(math.atan((-b - math.sqrt(discrim)) / (2*a)))
    
def findMinVelocity(x, y, g=9.8):
    increment = .1
    v = increment
    while True:
        if(findAngle(x,y,v,g) == "Insufficient Velocity"):
            v += increment
        else:
            return v

if(__name__ == '__main__'):    
    x = float(raw_input("x = "))
    g=9.8
    y=2.5
    v=findMinVelocity(x, y, g)
    increment = .1
    
    print("")
    
    print("y = " + str(y))
    print("v = " + str(v))
    print("θ = " + str(findAngle(x, y, v, g)))
    
    print("")
    
    y=1.5
    v=findMinVelocity(x, y, g)
    print("y = " + str(y))
    print("v = " + str(v))
    print("θ = " + str(findAngle(x, y, v, g)))

