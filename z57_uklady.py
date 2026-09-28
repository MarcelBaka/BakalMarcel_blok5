import pygame

SZEROKOSC, WYSOKOSC = 800, 600
FPS = 60
PREDKOSC = 300
TLO = (28, 28, 40)
KOLOR = (100, 200, 255)
KOLOR_MRUGANIA = (255, 255, 255)

pygame.init()
pygame.font.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Ruch w 8 kierunkach + układy sterowania")
clock = pygame.time.Clock()
czcionka = pygame.font.Font(None, 28)

kwadrat = pygame.Rect(375, 275, 50, 50)
x, y = float(kwadrat.x), float(kwadrat.y)
czas_mrugania = 0.0

uklady = {
    1: {"lewo": pygame.K_LEFT, "prawo": pygame.K_RIGHT, "gora": pygame.K_UP, "dol": pygame.K_DOWN, "nazwa": "Strzałki"},
    2: {"lewo": pygame.K_a, "prawo": pygame.K_d, "gora": pygame.K_w, "dol": pygame.K_s, "nazwa": "WSAD"},
    3: {"lewo": pygame.K_j, "prawo": pygame.K_l, "gora": pygame.K_i, "dol": pygame.K_k, "nazwa": "IJKL"}
}
wybrany_uklad = 1

dziala = True
while dziala:
    dt = clock.tick(FPS) / 1000.0

    if czas_mrugania > 0:
        czas_mrugania -= dt

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                dziala = False
            elif zdarzenie.key == pygame.K_SPACE:
                czas_mrugania = 0.2
            elif zdarzenie.key == pygame.K_r:
                kwadrat.center = (SZEROKOSC // 2, WYSOKOSC // 2)
                x, y = float(kwadrat.x), float(kwadrat.y)
            elif zdarzenie.key in (pygame.K_EQUALS, pygame.K_PLUS):
                srodek = kwadrat.center
                nowy_rozmiar = min(150, kwadrat.width + 10)
                kwadrat.size = (nowy_rozmiar, nowy_rozmiar)
                kwadrat.center = srodek
                x, y = float(kwadrat.x), float(kwadrat.y)
            elif zdarzenie.key == pygame.K_MINUS:
                srodek = kwadrat.center
                nowy_rozmiar = max(20, kwadrat.width - 10)
                kwadrat.size = (nowy_rozmiar, nowy_rozmiar)
                kwadrat.center = srodek
                x, y = float(kwadrat.x), float(kwadrat.y)
            elif zdarzenie.key == pygame.K_1:
                wybrany_uklad = 1
            elif zdarzenie.key == pygame.K_2:
                wybrany_uklad = 2
            elif zdarzenie.key == pygame.K_3:
                wybrany_uklad = 3

    klawisze = pygame.key.get_pressed()
    sterowanie = uklady[wybrany_uklad]
    dx, dy = 0, 0
    if klawisze[sterowanie["lewo"]]:
        dx -= 1
    if klawisze[sterowanie["prawo"]]:
        dx += 1
    if klawisze[sterowanie["gora"]]:
        dy -= 1
    if klawisze[sterowanie["dol"]]:
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
    aktualny_kolor = KOLOR_MRUGANIA if czas_mrugania > 0 else KOLOR
    pygame.draw.rect(ekran, aktualny_kolor, kwadrat)

    tekst_ukladu = czcionka.render(f"Aktywny uklad ({wybrany_uklad}): {sterowanie['nazwa']}", True, (200, 200, 200))
    ekran.blit(tekst_ukladu, (15, 15))

    pygame.display.flip()

pygame.quit()