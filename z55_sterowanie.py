import pygame

SZEROKOSC, WYSOKOSC = 800, 600
FPS = 60
PREDKOSC = 300
TLO = (28, 28, 40)
KOLOR = (100, 200, 255)

pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Ruch w 8 kierunkach")
clock = pygame.time.Clock()

kwadrat = pygame.Rect(375, 275, 50, 50)
x, y = float(kwadrat.x), float(kwadrat.y)

dziala = True
while dziala:
    dt = clock.tick(FPS) / 1000.0

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_ESCAPE:
            dziala = False

    klawisze = pygame.key.get_pressed()
    dx, dy = 0, 0
    if klawisze[pygame.K_LEFT]:
        dx -= 1
    if klawisze[pygame.K_RIGHT]:
        dx += 1
    if klawisze[pygame.K_UP]:
        dy -= 1
    if klawisze[pygame.K_DOWN]:
        dy += 1


    if dx != 0 and dy != 0:
        dx *= 0.7071
        dy *= 0.7071

    x += dx * PREDKOSC * dt
    y += dy * PREDKOSC * dt

    x = max(0.0, min(x, float(SZEROKOSC - kwadrat.width)))
    y = max(0.0, min(y, float(WYSOKOSC - kwadrat.height)))

    kwadrat.x = int(x)
    kwadrat.y = int(y)

    ekran.fill(TLO)
    pygame.draw.rect(ekran, KOLOR, kwadrat)
    pygame.display.flip()

pygame.quit()