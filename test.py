import main
import pygame
import math

print("_____________TEST POINT SUR SEGMENT______________")


line = main.Ligne(0,0,3,3)

line2 = main.Ligne(0,1,3,0)

line3 = main.Ligne(300,519,310,499)

if(line.pointSurSegment(2.4545,2.45454) and line.pointSurSegment(2,2) and not line.pointSurSegment(2.4545,2)):
    print("OK !")

if(line2.pointSurSegment(0,1) and line2.pointSurSegment(3,0) and line2.pointSurSegment(2.1,0.3)):
    print("OK 2 !")


lineHorizontal = main.Ligne(100,100, 600, 100)
if(lineHorizontal.pointSurSegment(120,100) and lineHorizontal.pointSurSegment(140,100) and lineHorizontal.pointSurSegment(500,100) and  not lineHorizontal.pointSurSegment(120,110)):
    print("OMG OK")

# la fonction point sur Segment semble fonctionner pour les lignes horizontales, il faut donc aller voir du côté de la fonction intersection

if(line.intersection(line2)):
    print("Collision des lignes 1 et 2")
if(line.intersection(line3)):
    print("Collision des lignes 1 et 3")

if(line3.intersection(lineHorizontal)): # détermine les bonnes coordonnées d'intersection
    print("Collision ligne 1 et horizontal")

lineBug = main.Ligne(300,500,400,500)

if(line3.intersection(lineBug)):
    print("collision good ")