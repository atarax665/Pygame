import random
import pygame
 
infec = 5 # number between 0 and 1 :infectability
travel = 10   #  n in a 10000
speed = 10  #miliseconds
deadr = 10    # n in 10000
recovr = 10   # n in 10000
vls = [speed,infec,deadr,recovr,travel]
vls0 = [speed,infec,deadr,recovr,travel]
dots =[ 0  for x in range(100*100)]
historyStats = []
def infect(b):
    dots[b] = 1
 
print "https://www.youtube.com/watch?v=2cCBbcPLg4A&feature=youtu.be"
 
pygame.init()
 
size = [1710, 1010]
screen = pygame.display.set_mode(size)
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
GREY =  (200, 200, 200)
 
 
class Slider():
    def __init__(self, txt, location,whome, action, bg=WHITE, fg=BLACK, size=(2, 20), font_name="Segoe Print", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size
        self.whome = whome 
        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])
 
        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)
 
        self.call_back_ = action
    def draw(self):
        self.mouseover()
 
        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)
 
    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREY  # mouseover color
 
    def call_back(self):
        self.call_back_(self.whome)
 
 
class Button():
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(500, 50), font_name="freesansbold.ttf", font_size=52):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size
        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])
 
        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)
 
        self.call_back_ = action
 
    def draw(self):
        self.mouseover()
 
        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)
 
    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREEN # mouseover color
 
    def call_back(self):
        self.call_back_()
 
def infect_first():
 
    for x in range(len(dots)):  # set all the values to 0 = healty 
        dots[x] = 0
 
    for x in range(102): # draw the lines
        pygame.draw.line(screen, GREY, [x*10, 0], [x*10,1010], 1)
    for y in range(102):
        pygame.draw.line(screen, GREY, [0, y*10], [1010,y*10], 1)
 
    # add boarders 
    razp = [0,5,10,15,25,35,50,70]
    for y in razp:
        for x in range(100):
            dots[x+y*100] = -1 
    for x in razp:
        for y in range(100):
            dots[x+y*100] = -1
 
    #infect the first dot
    while True:
        i = random.randint(0,len(dots)-1); 
        if dots[i] == 0:
            infect(i)
            break
def reset():
    infect_first()
 
 
    for i in range(len(vls)):
        vls[i]=vls0[i] #this should reset all the values
        #se izpis
        slid([i,vls0[i]])
 
def restart():
    #infect the first dot
    infect_first()
 
 
def slid(t):
    vls[t[0]]=t[1] # updates values for parameters
 
    if t[0]==0:
        besedilo = "Time speed: "
    elif t[0]==1:
        besedilo = "Infectivity: "
    elif t[0]==2:
        besedilo = "Lethality: "
    elif t[0]==3:
        besedilo = "Recovery rate:"
    elif t[0]==4:
        besedilo = "Travel rate: "
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render(besedilo+str(t[1]), True, BLACK, WHITE)
    textRect = text.get_rect()
    textRect.center= (1220,(t[0]+2)*70)
    pygame.draw.line(screen, WHITE, [1012, (t[0]+2)*70],  [1395, (t[0]+2)*70], 50)
    screen.blit(text, textRect)
 
 
 
def mousebuttondown():
    pos = pygame.mouse.get_pos()
    for button in buttons:
        if button.rect.collidepoint(pos):
            button.call_back()
    for slider in sliders:
        if slider.rect.collidepoint(pos):
            slider.call_back()
 
screen.fill(WHITE)
reset()
 
pygame.display.set_caption("Disease Spread Simulation!")
 
done = False
clock = pygame.time.Clock()
 
#buttons
button_01 = Button("Reset!", (1350,570), reset,bg= (150,150,150))
button_02 = Button("Restart!", (1350,500), restart,bg= GREY)
button_03 = Button("Disease Spread Simulation!", (1350,50), reset,bg= (250,50,50))
buttons = [button_01,button_02,button_03]
 
#sliders
sliders = []
for n in range(5):
    for x in range(100):
        sliders.append(Slider("", (1400+x*2, (n+2)*70),[n,x], slid, bg=(2*x+50, 250-x,20)))
 
 
while not done:
    if vls[0] == 0:
        pygame.time.wait(1000)
    elif vls[0] != 99:
        pygame.time.wait(100/vls[0]) 
 
 
    for i in range(100*100): 
        if dots[i] == 1: # 1 means that the dot is ifected
            #infect those around him
            for n in [1,-1, 100,-100, 101,99, -101, -99]: #all the naighbors
                if (i+n > 0) and (i+n < 100*100):
                    if dots[i+n] == 0:
                        if random.randint(0,100) < vls[1]: #he did not wash hands... 
                            infect(i+n)
 
            if random.randint(0,10000) < vls[2]: #die
                dots[i] = 2 #dead
            if random.randint(0,10000) < vls[3]: #recover
                dots[i] = 3 # recovered and immune
 
    #travel
    for i in range(100*100):
         if (dots[i] != -1) and (dots[i] != 2): #must be alive to travel
            if random.randint(0,100000) < vls[4]: 
                ni = random.randint(0,len(dots)-1)
                if (dots[ni] != -1) and (dots[ni] != 2):
                    op = dots[ni]   #switch the two dots
                    dots[ni] = dots[i]
                    dots[i]  = op
 
    # draw and get stats for a graph
    #0 healthyDots 1 infectedDots   2  deadDots  3 recoveredDots
    stats = [0,0,0,0]
    color = [GREEN, RED, BLACK, BLUE]
    for i in range(len(dots)):
        y = i//100
        x = i - (i//100)*100
 
        if dots[i] == 0:
            stats[0] += 1
            pygame.draw.circle(screen, GREEN, [5+x*10, 5+y*10], 4)
        elif dots[i] == 1:
            stats[1] += 1
            pygame.draw.circle(screen, RED, [5+x*10, 5+y*10], 4)
        elif dots[i] == 2:
            stats[2] += 1
            pygame.draw.circle(screen,  BLACK, [5+x*10, 5+y*10], 4)
        elif dots[i] == 3:
            stats[3] += 1
            pygame.draw.circle(screen,  BLUE, [5+x*10, 5+y*10], 4)
    # draw graph
    dotsum = sum(stats)
    print dotsum
    historyStats.append(stats)
    for n in range(len(historyStats)):
        x = n*2+1014 # graph is on the right side of the main thing
        y = 0
        hy = 0
        for v in range(4):
            y += (historyStats[n][v]*400)/dotsum
            pygame.draw.line(screen, color[v], [x,hy+600], [x,y+600], 4)
            hy = y
    if len(historyStats) > 350:
        historyStats.pop(0)
 
 
 
 
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousebuttondown()
 
    for button in buttons:
        button.draw()
    for slider in sliders:
        slider.draw()
    pygame.display.flip()
 
pygame.quit()
