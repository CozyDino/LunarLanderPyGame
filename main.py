import pygame

class GameConfig:
    windowW = 800
    windowH = 500
    black = (0,0,0)
    white = (255,255,255)
class GameState:
    def __init__(self):
        self.fusee = Fusee()
    def advanceState(self):
        pass
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
        pass
    def tourner(self, angle):
        pass
    def update(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
    def Activerpropulser():
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
    def intersection(ligne): # retourne booléen, paramètre ligne
        pass
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
