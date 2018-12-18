import pygame
import math

class GameConfig:
    windowW = 800
    windowH = 600
    black = (188,42,58)
    white = (255,255,255)
    gravity = 0.001
    imgFusee = pygame.image.load('rocketspritethumb.png')
class GameState:
    def __init__(self):
        self.fusee = Fusee()
        self.niveau = Niveau()
    def advanceState(self):
        self.fusee.update()
    def draw(self, window):
        window.fill(GameConfig.black)
        self.niveau.draw(window)
        self.fusee.draw(window)
    def eventHandle(self, valeur):
        print(pygame.K_UP)
        if(valeur == pygame.K_UP):
            self.fusee.propulser()
        if(valeur == pygame.K_RIGHT):
            self.fusee.tourner(2)
        if(valeur == pygame.K_LEFT):
            self.fusee.tourner(-2)


def main():
    pygame.init()
    window = pygame.display.set_mode((GameConfig.windowW, GameConfig.windowH))
    horloge = pygame.time.Clock()
    pygame.display.set_caption("Lunar_Lander")
    gameLoop(window, horloge)
    pygame.quit()
    quit()

class Fusee:
    def __init__(self):
        self.x = 0 # nombre à déterminer
        self.y = 0
        self.vx = 0
        self.vy = 0.0
        self.largeur = 0
<<<<<<< HEAD
        self.angle = 270 # de 0 à 360 degré
        self.forceReacteur = 0.004
=======
        self.angle = 0 # de 0 à 360 degré
        self.forceReacteur = 20
>>>>>>> f48af6edb16a178ac73f4371a6ad733c5f687496
    def collide(self, ligne): # retourne booléen, paramètre ligne
        lineH = Ligne(self.x, self.y, self.x+self.largeur, self.y)
        lineB = Ligne(self.x, self.y-self.largeur, self.x+self.largeur, self.y-self.largeur)
        lineG = Ligne(self.x, self.y, self.x, self.y-self.largeur)
        lineD = Ligne(self.x+self.largeur, self.y, self.x+self.largeur, self.y-self.largeur)
        if ((lineH.intersection(ligne) == True) or (lineB.intersection(ligne) == True)
        or (lineG.intersection(ligne) == True) or (lineD.intersection(ligne) == True)):
            return True
        else:
            return False
    def tourner(self, angle):
        self.angle = (self.angle + angle)%360
        # GameConfig.imgFusee = pygame.transform.rotate(GameConfig.imgFusee, angle)
    def update(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.vy += GameConfig.gravity
    def propulser(self):
        self.vy += math.sin(math.radians(self.angle)) * self.forceReacteur
        self.vx += math.cos(math.radians(self.angle)) * self.forceReacteur
    def draw(self, window):
        imgFusee = rot_center(GameConfig.imgFusee, 270 - self.angle)
        window.blit(imgFusee, (self.x, self.y))



class Niveau:
    def __init__(self):
<<<<<<< HEAD
        self.listeLigne = []
        self.listeLigne.append(Ligne(0,600,300,500))
        self.listeLigne.append(Ligne(300,500,400,500))
        self.listeLigne.append(Ligne(400,500,600,550))
        self.listeLigne.append(Ligne(600,550,800,200))
        # liste.append(valeur) # permet d'ajouter une valeur à la liste, 
    def collide(fusee): # boolean
        for line in self.listeLigne:
            if(fusee.collide(line) and line.gagnant == 0):
                return true
        return false
    def draw(self, window):
        for ligne in self.listeLigne:
            ligne.draw(window)
    
=======
        listeLigne = []
        # liste.append(valeur) # permet d'ajouter une valeur à la liste,
    def collide(fusee): # boolean
        pass

>>>>>>> f48af6edb16a178ac73f4371a6ad733c5f687496

class Ligne:
    def __init__(self, ax, ay, bx, by):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.gagnant = 0 # 0 = dangereux, 1 = gagnant
    def intersection(self, ligne): # retourne booléen, paramètre ligne
        x = 0 # coordonnée de l'intersection de deux droites
        y = 0 # coordonnées y de l'intersection des deux droites
    def pointSurSegment(self, x, y):
        return ((y - self.ay)*(self.bx - self.ax) == (self.by - self.ay)*(x-self.ax)) and (x >= self.ax and x <= self.bx) and (y >= self.ay, y <= self.by)
    def setGagnant(self, v):
        self.gagant = v
    def draw(self, window):
	    pygame.draw.line(window,GameConfig.white, (self.ax,self.ay), (self.bx, self.by),1)



def gameLoop(window, horloge):
    game_over = False
    propulser = False
    tournerGauche = False
    tournerDroite = False
    gameState = GameState()
    while not game_over:
        gameState.advanceState()
        horloge.tick(100)
        gameState.draw(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                propulser = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                tournerGauche = True
                tournerDroite = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                tournerDroite = True
                tournerGauche = False
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                propulser = False
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                tournerGauche = False
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                tournerDroite = False
        
        if(propulser):
            gameState.fusee.propulser() 
        if(tournerDroite):
            gameState.fusee.tourner(2)
        if(tournerGauche):
            gameState.fusee.tourner(-2)
        pygame.display.update()

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center  #rot_image is not defined 
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

main()
