import pygame

SZEROKOSC, WYSOKOSC = 800, 600
FPS = 60
PREDKOSC = 250
TLO = (28, 28, 40)
KOLOR_KWADRATU = (100, 200, 255)

pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Poruszanie się")
clock = pygame.time.Clock()

dobry = pygame.Rect(100, 250, 40, 40)
dobry_x = float(dobry.x)

dziala = True
while dziala:
    dt = clock.tick(FPS) / 1000.0

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                dziala = False

    klawisze = pygame.key.get_pressed()
    if klawisze[pygame.K_LEFT]:
        dobry_x -= PREDKOSC * dt
    if klawisze[pygame.K_RIGHT]:
        dobry_x += PREDKOSC * dt

    dobry_x = max(0.0, min(dobry_x, float(SZEROKOSC - dobry.width)))
    dobry.x = int(dobry_x)

    ekran.fill(TLO)
    pygame.draw.rect(ekran, KOLOR_KWADRATU, dobry)
    pygame.display.flip()

pygame.quit()