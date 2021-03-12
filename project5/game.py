import pygame
import random

pygame.init()

background = pygame.image.load("/home/niccolo/projects/projects_python/project5/image/background.png")
bird = pygame.image.load("/home/niccolo/projects/projects_python/project5/image/bird.png")
game_over = pygame.image.load("/home/niccolo/projects/projects_python/project5/image/game_over.png")
base = pygame.image.load("/home/niccolo/projects/projects_python/project5/image/base.png")
tube_below = pygame.image.load("/home/niccolo/projects/projects_python/project5/image/tube.png")
tube_above = pygame.transform.flip(tube_below, False, True)

screen = pygame.display.set_mode((288,512))
FPS = 50
forward_speed = 3
font = pygame.font.SysFont("Comic Sans MS", 50, bold=False)
class input_tube:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75,150)
    def forward_tube(self):
        self.x -= forward_speed
        screen.blit(tube_below, (self.x,self.y+210))
        screen.blit(tube_above, (self.x,self.y-210))
    def crash(self, bird, birdx, birdy):
        tolerance = 5
        bird_side_dx = birdx+bird.get_width()-tolerance
        bird_side_sx = birdx+tolerance
        tube_side_dx = self.x + tube_above.get_width()
        tube_side_sx = self.x
        bird_side_below = birdy+tolerance
        bird_side_above = birdy+bird.get_height()-tolerance
        tube_side_below = self.y+110
        tube_side_above = self.y+210
        if bird_side_dx > tube_side_sx and bird_side_sx < tube_side_dx:
            if bird_side_below < tube_side_below or bird_side_above > tube_side_above:
                gameover()
    def overtaking_tube(self, bird, birdx):
        tolerance = 5
        bird_side_dx = birdx+bird.get_width()-tolerance
        bird_side_sx = birdx+tolerance
        tube_side_dx = self.x + tube_above.get_width()
        tube_side_sx = self.x
        if bird_side_dx > tube_side_sx and bird_side_sx < tube_side_dx:
            return True
def input(): #Variable initialization
    global birdx, birdy, bird_vely
    global basex
    global tube
    birdx, birdy = 60, 150
    bird_vely = 0
    global score
    score = 0
    basex = 0
    global overtaking_tube
    overtaking_tube = False
    tube = []
    tube.append(input_tube())
def image():
    screen.blit(background, (0,0))
    for x in tube:
        x.forward_tube()
    screen.blit(bird, (birdx,birdy))
    screen.blit(base, (basex,400))
    score_render = font.render(str(score), 1, (255,255,255))
    screen.blit(score_render, (5,0))
def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
def gameover():
    screen.blit(game_over, (50,180))
    update()
    restart = False
    while not restart:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                input()
                restart = True
            if event.type == pygame.QUIT:
                pygame.quit()
input()
while True:
    #To move the base to the left 
    basex -= forward_speed
    if basex < -45: 
        basex = 0
    #Gravity in the game
    bird_vely += 1
    birdy += bird_vely
    #We initialize the up key to make the bird go up and stop it falling 
    for event in pygame.event.get():
        if( event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
         bird_vely = -10  
        if event.type == pygame.QUIT:
            pygame.quit()
    if tube[-1].x < 150:
        tube.append(input_tube())
    for x in tube:
        x.crash(bird, birdx, birdy)
    if not overtaking_tube:
        for x in tube:
            if x.overtaking_tube(bird, birdx):
                overtaking_tube = True
                break
    if overtaking_tube:
        overtaking_tube = False
        for x in tube:
            if x.overtaking_tube(bird, birdx):
                overtaking_tube = True
                break
        if not overtaking_tube:
            score += 1 
    if birdy > 380:
        gameover()
    #Screen update
    image()
    update()