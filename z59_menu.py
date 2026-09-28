import pygame

SZEROKOSC, WYSOKOSC = 700, 460
FPS = 60
TLO = (28, 28, 40)
ZWYKLY = (60, 90, 150)
NAJECHANY = (85, 125, 200)
WCISNIETY = (40, 62, 105)
NAPIS = (240, 240, 245)
OBWODKA_WYBRANA = (255, 215, 0)

pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Menu główne")
zegar = pygame.time.Clock()
czcionka = pygame.font.Font(None, 30)
male = pygame.font.Font(None, 24)

PRZYCISKI = [
    (pygame.Rect(0, 0, 240, 54), "Nowa gra"),
    (pygame.Rect(0, 0, 240, 54), "Opcje"),
    (pygame.Rect(0, 0, 240, 54), "Wyniki"),
    (pygame.Rect(0, 0, 240, 54), "Wyjscie"),
]

for i, (prostokat, _) in enumerate(PRZYCISKI):
    prostokat.center = (SZEROKOSC // 2, 100 + i * 80)

wybrany_indeks = 0
komunikat = "Wybierz opcję strzałkami lub myszą"


def aktywuj_opcje(napis):
    global dziala, komunikat
    komunikat = f"Kliknięto / Wybrano: {napis}"
    if napis == "Wyjscie":
        dziala = False


def rysuj_przycisk(ekran, prostokat, napis, aktywny, wcisniety):
    if wcisniety:
        kolor, przesun = WCISNIETY, 2
    elif aktywny:
        kolor, przesun = NAJECHANY, 0
    else:
        kolor, przesun = ZWYKLY, 0

    pygame.draw.rect(ekran, kolor, prostokat, 0, 10)

    if aktywny:
        pygame.draw.rect(ekran, OBWODKA_WYBRANA, prostokat, 3, 10)

    tekst = czcionka.render(napis, True, NAPIS)
    ekran.blit(
        tekst,
        tekst.get_rect(center=(prostokat.centerx, prostokat.centery + przesun)),
    )


dziala = True
while dziala:
    zegar.tick(FPS)
    mysz = pygame.mouse.get_pos()
    lewy_wcisniety = pygame.mouse.get_pressed()[0]

    for i, (prostokat, _) in enumerate(PRZYCISKI):
        if prostokat.collidepoint(mysz):
            wybrany_indeks = i

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                dziala = False
            elif zdarzenie.key == pygame.K_UP:
                wybrany_indeks = (wybrany_indeks - 1) % len(PRZYCISKI)
            elif zdarzenie.key == pygame.K_DOWN:
                wybrany_indeks = (wybrany_indeks + 1) % len(PRZYCISKI)
            elif zdarzenie.key in (pygame.K_RETURN, pygame.K_SPACE):
                _, napis = PRZYCISKI[wybrany_indeks]
                aktywuj_opcje(napis)
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
            for prostokat, napis in PRZYCISKI:
                if prostokat.collidepoint(zdarzenie.pos):
                    aktywuj_opcje(napis)

    ekran.fill(TLO)

    for i, (prostokat, napis) in enumerate(PRZYCISKI):
        aktywny = i == wybrany_indeks
        wcisniety = aktywny and lewy_wcisniety and prostokat.collidepoint(mysz)
        rysuj_przycisk(ekran, prostokat, napis, aktywny, wcisniety)

    ekran.blit(
        male.render(f"Komunikat: {komunikat}", True, (200, 200, 215)),
        (20, WYSOKOSC - 40),
    )

    pygame.display.flip()

pygame.quit()