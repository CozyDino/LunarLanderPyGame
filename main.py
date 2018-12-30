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
    def isOver(self):
        if(self.niveau.collide(self.fusee)):
            return False
        else:
            return False


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
        self.largeur = 20
        self.angle = 270 # de 0 à 360 degré
        self.forceReacteur = 0.004
    def collide(self, ligne): # retourne booléen, paramètre ligne
        lineH = Ligne(self.x, self.y, self.x+self.largeur, self.y)
        lineB = Ligne(self.x, self.y+self.largeur, self.x+self.largeur, self.y+self.largeur)
        lineG = Ligne(self.x, self.y, self.x, self.y+self.largeur)
        lineD = Ligne(self.x+self.largeur, self.y, self.x+self.largeur, self.y+self.largeur)
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
        self.listeLigne = []
        self.listeLigne.append(Ligne(0,600,300,500))
        self.listeLigne.append(Ligne(300,500,400,500))
        self.listeLigne.append(Ligne(400,500,600,550))
        self.listeLigne.append(Ligne(600,550,800,200))
        # liste.append(valeur) # permet d'ajouter une valeur à la liste, 
    def collide(self, fusee): # boolean
        for line in self.listeLigne:
            if(fusee.collide(line)):
                return True
        return False
    def draw(self, window):
        for ligne in self.listeLigne:
            ligne.draw(window)

class Ligne:
    def __init__(self, ax, ay, bx, by):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.gagnant = 0 # 0 = dangereux, 1 = gagnant
    def intersection(self, ligne): # retourne booléen, paramètre ligne Attention ! Probleme collision axe horizontal
        Ix = 0 # coordonnée de l'intersection de deux droites
        Iy = 0 # coordonnées y de l'intersection des deux droites
        aVertical =  False
        if(self.bx - self.ax == 0 and ligne.bx - ligne.ax == 0): # Ici, c'est lorsqu'on a deux ligne verticales, donc parallèle
            return False

        if(self.bx - self.ax != 0):
            coefDirecteur = ((self.by - self.ay)/(self.bx - self.ax))
            ordonneOrigine = (self.ay - coefDirecteur* self.ax)
        else:
            coefDirecteur = float("inf")
            ordonneOrigine = 0
            aVertical = True
        
        if(ligne.bx - ligne.ax != 0):
            coefDirecteur2 = ((ligne.by - ligne.ay)/(ligne.bx - ligne.ax))
            ordonneOrigine2 = (ligne.ay - coefDirecteur2* ligne.ax)
        else:
            coefDirecteur = float("inf")
            ordonneOrigine = 0
            aVertical = True
        
        if(coefDirecteur == coefDirecteur2):
            return False


        if(aVertical):
            if(self.bx - self.ax == 0):
                Ix = self.bx
                Iy = (Ix* coefDirecteur2 + ordonneOrigine2)
            else:
                Ix = ligne.bx
                Iy = (Ix* coefDirecteur + ordonneOrigine)
        else:
            Ix = ((ordonneOrigine2 - ordonneOrigine) / (coefDirecteur - coefDirecteur2))
            Iy = (Ix* coefDirecteur + ordonneOrigine)

        print("Ix : ", Ix," Iy : ", Iy)
        if(ligne.pointSurSegment(Ix,Iy) and self.pointSurSegment(Ix, Iy)):
            print("chancla")
            return True
        else:
            return False
            
    def pointSurSegment(self, x, y):
        """ print("X : ",x," Y : ",y)
        print("left :", y * (self.bx - self.ax), "right : ", (self.by-self.ay)*(x-self.bx)+ self.by * (self.bx-self.ax)) """
        if((y * (self.bx - self.ax) <= (self.by-self.ay)*(x-self.bx)+ self.by * (self.bx-self.ax) + 0.5)
        and (y * (self.bx - self.ax) >= (self.by-self.ay)*(x-self.bx)+ self.by * (self.bx-self.ax) - 0.5)):
            """ print("Appartient à la droite ok")
            print("x : ",x," max x : ",max([self.ax, self.bx]))
            print("x : ",x," min x : ",min([self.ax, self.bx])) """
            if((x <= max([self.ax, self.bx]) and x >= min([self.ax, self.bx]))
            and (y <= max([self.ay, self.by]) and y >= min([self.ay, self.by]))):
                #print("Appartient au segment ok")
                return True
        return False
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
        print(1)
        game_over = gameState.isOver()

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center  #rot_image is not defined 
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite


