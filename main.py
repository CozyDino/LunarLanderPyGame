import pygame
import math
import time

class GameConfig:
    windowW = 800
    windowH = 600
    black = (188,42,58)
    white = (255,255,255)
    green = (0,255,0)
    gravity = 0.001

    pygame.font.init()
    imgFusee = pygame.image.load('rocketspritethumb.png')
    fontFin = pygame.font.Font("BradBunR.ttf", 24)
    imageBackground = pygame.image.load('starbackground')
class GameState:
    def __init__(self):
        self.fusee = Fusee()
        self.niveau = Niveau()
    def advanceState(self):
        self.fusee.update()
    def draw(self, window):
        # window.fill(GameConfig.black)
        window.blit(GameConfig.imageBackground, (0,0))
        self.niveau.draw(window)
        self.fusee.draw(window)
        getIACommand(self)
    def isOver(self, window):
        LigneCollision = self.niveau.collide(self.fusee)
        if(LigneCollision):
            if(self.fusee.angle <= 270 + 20 and self.fusee.angle >= 270-20 and abs(self.fusee.vy) < 2 and LigneCollision.gagnant == 1):
                displayMessage(window, "Gagné !", GameConfig.windowW/2, GameConfig.windowW/2)
            else:
                displayMessage(window, "Perdu !", GameConfig.windowW/2, GameConfig.windowW/2)
            return True
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
        lineB = Ligne(self.x, self.y+self.largeur, self.x+self.largeur, self.y + self.largeur)
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
        #print(self.angle)
        print("Vitesse courante en X : ", self.vx)



class Niveau:
    def __init__(self):
        self.listeLigne = []
        self.listeLigne.append(Ligne(0,600,300,500))
        self.winLine = Ligne(300,500,400,500)
        self.winLine.setGagnant(1)
        self.listeLigne.append(self.winLine)
        self.listeLigne.append(Ligne(400,500,600,550))
        self.listeLigne.append(Ligne(600,550,800,200))
        # liste.append(valeur) # permet d'ajouter une valeur à la liste, 
    def collide(self, fusee): # boolean
        for line in self.listeLigne:
            if(fusee.collide(line)):
                return line
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

        #print("Ix : ", Ix," Iy : ", Iy)
        if(ligne.pointSurSegment(Ix,Iy) and self.pointSurSegment(Ix, Iy)):
            #print("chancla")
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
        self.gagnant = v
    def draw(self, window):
        if(self.gagnant == 0):
            couleur = GameConfig.white
        else:
            couleur = GameConfig.green
        pygame.draw.line(window,couleur, (self.ax,self.ay), (self.bx, self.by),1)



def gameLoop(window, horloge):
    game_over = False
    propulser = False
    tournerGauche = False
    tournerDroite = False
    IA = True
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
        
        if(IA):
            if(getIACommand(gameState) == "droite"):
                propulser = False
                tournerGauche = False
                tournerDroite = True
            elif(getIACommand(gameState) == "gauche"):
                tournerGauche = True
                propulse = False
                tournerDroite = False
            elif(getIACommand(gameState) == "propulse"):
                propulser = True
                tournerGauche = False
                tournerDroite = False


        if(propulser):
            gameState.fusee.propulser() 
        if(tournerDroite):
            gameState.fusee.tourner(2)
        if(tournerGauche):
            gameState.fusee.tourner(-2)
        if(gameState.isOver(window)):
            game_over = True
        pygame.display.update()
    if(playAgain()):
        main()
        

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center  #rot_image is not defined 
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

def playAgain():
    time.sleep(2)
    while True:
        for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                return True
        time.sleep(0.5)

def displayMessage(window, text, x, y):
    img = GameConfig.fontFin.render(text, True, GameConfig.white)
    displayRect = img.get_rect()
    displayRect.center = (x,y)
    window.blit(img, displayRect)


def getIACommand(GameState): 
    Ox = (GameState.niveau.winLine.ax + GameState.niveau.winLine.bx)/2
    Oy = (GameState.niveau.winLine.ay + GameState.niveau.winLine.by)/2 # Le point O représente le point à atteindre
    vitesseAAtteindre = (Ox - GameState.fusee.x) / ((-GameState.fusee.vy + math.sqrt(math.pow(GameState.fusee.vy, 2 ) - 2 * (GameState.fusee.y - Oy) * GameConfig.gravity)) / GameConfig.gravity)
    print("vitesse à atteindre en X : ",vitesseAAtteindre)
    if((vitesseAAtteindre >= GameState.fusee.vx - 0.01 and vitesseAAtteindre <= GameState.fusee.vx + 0.01) or abs(GameState.fusee.y - Oy) < 30):
        if(GameState.fusee.angle > 270 and GameState.fusee.angle < 360 or GameState.fusee.angle == 0):
            return "gauche"
        if(GameState.fusee.angle > 180 and GameState.fusee.angle < 270):
            return "droite"
    
    if(vitesseAAtteindre > GameState.fusee.vx and GameState.fusee.angle != 0):
        return "droite"
    
    if(vitesseAAtteindre > GameState.fusee.vx and GameState.fusee.angle == 0):
        return "propulse"
    if(vitesseAAtteindre < GameState.fusee.vx and GameState.fusee.angle == 180):
        return "propulse"
    if(vitesseAAtteindre < GameState.fusee.vx and GameState.fusee.angle != 180):
        return "gauche"