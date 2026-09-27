import pygame

SZEROKOSC, WYSOKOSC = 800, 600
FPS = 60
TLO = (28, 28, 40)
KOLOR_TEKSTU = (240, 240, 240)

pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("z54_licznik.py - Kliknięcia myszy")
clock = pygame.time.Clock()
czcionka = pygame.font.SysFont(None, 36)

licznik_lewy = 0
licznik_prawy = 0

dziala = True
while dziala:
    clock.tick(FPS)

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                dziala = False
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN:
            if zdarzenie.button == 1:  #Lewy
                licznik_lewy += 1
            elif zdarzenie.button == 3:  #Prawy
                licznik_prawy += 1

    ekran.fill(TLO)

    tekst_lewy = czcionka.render(f"Lewy przycisk: {licznik_lewy}", True, KOLOR_TEKSTU)
    tekst_prawy = czcionka.render(f"Prawy przycisk: {licznik_prawy}", True, KOLOR_TEKSTU)

    ekran.blit(tekst_lewy, (50, 50))
    ekran.blit(tekst_prawy, (50, 100))

    pygame.display.flip()

pygame.quit()