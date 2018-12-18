import pygame

class GameConfig:
    windowW = 800
    windowH = 500
    black = (0,0,0)
    white = (255,255,255)
    imgFusee = pygame.image.load('rocketsprite.png')
class GameState:
    def __init__(self):
        self.fusee = Fusee()
        self.niveau = Niveau()
    def advanceState(self):
        self.fusee.update()
    def draw(self, window):
        window.fill(GameConfig.black)


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
        self.vy = 0
        self.largeur = 0
        self.angle = 0 # de 0 à 360 degré
        self.forceReacteur = 20
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
        pass
    def update(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
    def propulser():
        pass
    def draw(window):
        pass



class Niveau:
    def __init__(self):
        listeLigne = []
        # liste.append(valeur) # permet d'ajouter une valeur à la liste,
    def collide(fusee): # boolean
        pass


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
    def draw(window):
	    window.draw.line(window,GameConfig.white, (ax,ay), (bx, by),1)



def gameLoop(window, horloge):
    game_over = False
    gameState = GameState()
    while not game_over:
        gameState.advanceState()
        horloge.tick(100)
        gameState.draw(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        pygame.display.update()
 main()
