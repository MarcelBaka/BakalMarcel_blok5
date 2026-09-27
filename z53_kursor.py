import pygame

SZERKOSC, WYSOKOSC = 800, 600
FPS = 60
TLO = (28, 28, 40)

pygame.init()
ekran = pygame.display.set_mode((SZERKOSC, WYSOKOSC))
pygame.display.set_caption("Kursor")
zegar = pygame.time.Clock()
dziala = True
while dziala:
    dt = zegar.tick(FPS) / 1000.0

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                dziala = False

    rect = pygame.Rect(0, 0, 40, 40)
    rect.center = pygame.mouse.get_pos()

    ekran.fill(TLO)
    pygame.draw.rect(ekran, (255, 100, 100), rect)

    pygame.display.flip()
    zegar.tick(FPS)
pygame.quit()