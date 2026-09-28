1 zdarzenie KEYDOWN (generowane przy wciśnięciu klawisza), a get_pressed() zwróci True 120 razy (60 klatek na sekundę przez 2 sekundy).

Skok to akcja jednorazowa (ma się wykonać raz po kliknięciu), a bieg to stan ciągły, który trwa tak długo, jak trzymamy klawisz.

Zablokuje się ruch po przekątnej. elif sprawdza kolejny warunek tylko wtedy, gdy poprzedni był fałszywy, więc gra reagowałaby tylko na jeden klawisz naraz.

Użyto metody pygame.key.get_pressed(). Po przełączeniu okna (Alt+Tab) program gubi zdarzenie puszczenia klawisza (KEYUP). Naprawia się to przez zresetowanie prędkości/ruchu przy utracie fokusu okna.

zdarzenie.pos podaje współrzędne kursora z momentu wystąpienia konkretnego zdarzenia (np. kliknięcia), a pygame.mouse.get_pos() zwraca aktualną, bieżącą pozycję myszy w danej klatce gry.