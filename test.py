import main
import pygame

line = main.Ligne(-1, -1, 2, 2)

print(line.pointSurSegment(2, -1))

if(line.pointSurSegment(1,0)):
    print("nice")