from turtle import goto, penup
from MyModule import *
import turtle as t
def dentiton(l,c="#000000"):
    t.color(c)
    t.penup
    t.forward((-l*14)/2)
    t.pendown
    for i in range(3):
        for e in range(4):
            trianglehaut(l)
            espace(l)
        espace(l)