import pygame

class GameConfig:
    windowW = 800
    windowH = 500
    black = (0,0,0)
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
    gameState = GameState()
    pygame.display.set_caption("Lunar_Lander")
    gameLoop()
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
    def collide(ligne) # retourne booléen, paramètre ligne
        pass


class Niveau:


class Ligne:
    def __init__(self, ax, ay, bx, by):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.gagnant = 0 # 0 = dangereux, 1 = gagnant
    def intersection(ligne): # retourne booléen, paramètre ligne
        pass
    def setGagnant(self, v)





def gameLoop():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
    
main()