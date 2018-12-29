import main
import pygame
import math

print("_____________TEST POINT SUR SEGMENT______________")


line = main.Ligne(0,0,3,3)

line2 = main.Ligne(0,1,3,0)

line3 = main.Ligne(2,3,5,3)

if(line.pointSurSegment(2.4545,2.45454) and line.pointSurSegment(2,2) and not line.pointSurSegment(2.4545,2)):
    print("OK !")

if(line2.pointSurSegment(0,1) and line2.pointSurSegment(3,0) and line2.pointSurSegment(2.1,0.3)):
    print("OK 2 !")


if(line.intersection(line2)):
    print("Collision des lignes 1 et 2")
if(line.intersection(line3)):
    print("Collision des lignes 1 et 3")
