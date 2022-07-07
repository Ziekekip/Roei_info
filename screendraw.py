import pygame

pygame.init()
pygame.font.init()


display_width = 1200
display_height = 1600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Baan 1')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
background_img = pygame.image.load('background.png')
print(pygame.font.get_fonts())

font = "arial"

def draw_background():
    gameDisplay.blit(pygame.image.load('background.png'), (0, 0))

def draw_ploegheader():
    gameDisplay.blit(pygame.image.load('Ploegheader.png'), (0, 50))

    gameDisplay.blit(pygame.image.load('bladen/Proteus.png'), (860, 70))

    ploegnaamfont = pygame.font.SysFont(font, 60)
    ploegnaamsurface = ploegnaamfont.render('Steen Papier Bier', False, (0, 0, 0))
    gameDisplay.blit(ploegnaamsurface, (50, 80))

    verenigingenfont = pygame.font.SysFont(font, 30)
    verenigingensurface = verenigingenfont.render('LAG-SKA-PRO', False, (0, 0, 0))
    gameDisplay.blit(verenigingensurface, (600, 100))

def draw_roeierheader(nummer):
    gameDisplay.blit(pygame.image.load('Roeierheader.png'), (0, (240 + 120*(nummer-1))))
    roeiernaamfont = pygame.font.SysFont(font, 50)

    roeiernaamsurface = roeiernaamfont.render(str(nummer) + ": " + 'Jasper Coppen', False, (0, 0, 0))
    gameDisplay.blit(roeiernaamsurface, (100, 255 + 120*(nummer-1)))

    verenigingenfont = pygame.font.SysFont(font, 30)
    verenigingensurface = verenigingenfont.render('PRO', False, (0, 0, 0))
    gameDisplay.blit(verenigingensurface, (860, 265 + 120*(nummer-1)))




draw_background()
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    draw_background()
    draw_ploegheader()
    for i in range(1,9):
        draw_roeierheader(i)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()