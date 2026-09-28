import math
import pygame

SZEROKOSC, WYSOKOSC = 800, 600
FPS = 60
TLO = (28, 28, 40)
KOLOR_OKREGU = (100, 200, 255)
KOLOR_TEKSTU = (220, 220, 230)
PROMIEN_OKREGU = 25

pygame.init()
pygame.font.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Zarządzanie okręgami i licznik")
clock = pygame.time.Clock()
czcionka = pygame.font.Font(None, 32)

okregi = []

dziala = True
while dziala:
    dt = clock.tick(FPS) / 1000.0

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                dziala = False
            elif zdarzenie.key == pygame.K_c:
                okregi.clear()
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN:
            mysz_x, mysz_y = zdarzenie.pos
            if zdarzenie.button == 1:  
                okregi.append((mysz_x, mysz_y))
            elif zdarzenie.button == 3: 
                for okrag in okregi:
                    ox, oy = okrag
                    
                    if math.hypot(mysz_x - ox, mysz_y - oy) <= PROMIEN_OKREGU:
                        okregi.remove(okrag)
                        break  

    ekran.fill(TLO)

    # Rysowanie wszystkich okręgów
    for ox, oy in okregi:
        pygame.draw.circle(ekran, KOLOR_OKREGU, (ox, oy), PROMIEN_OKREGU)
        pygame.draw.circle(ekran, (40, 40, 60), (ox, oy), PROMIEN_OKREGU, 2)  

    # Wyświetlanie licznika okręgów w prawym rogu
    tekst_licznika = czcionka.render(f"Okręgi: {len(okregi)}", True, KOLOR_TEKSTU)
    tekst_prostokat = tekst_licznika.get_rect(topright=(SZEROKOSC - 20, 20))
    ekran.blit(tekst_licznika, tekst_prostokat)

    pygame.display.flip()

pygame.quit()