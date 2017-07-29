import feld
import fenster_klasse
import pygame
import sys
import kontrollstrukturen

# sp1 = o
# sp2 = x
bild = fenster_klasse.Fenster()
daten = feld.Spielfeld()

strich0 = bild.aussenrand + bild.zwischen_rand_gitter
strich1, strich2, strich3, strich4 = strich0 + 100, strich0 + 200, strich0 + 300, strich0 + 400
alt_bereich = 4

bild.startbildschirm()
bild.stand_bild(daten)

gewonnen = False
while not gewonnen:
    print("am_zug:", daten.am_zug, "sp_eins:", daten.sp_eins, "sp_zwei:", daten.sp_zwei)

    auswahl_erfolgt = False
    while not auswahl_erfolgt:

        # reihenauswahl mit stein anzeigen
        maus_position = pygame.mouse.get_pos()
        if strich0 <= maus_position[0] < strich1:
            bereich = 0
        elif strich1 <= maus_position[0] < strich2:
            bereich = 1
        elif strich2 <= maus_position[0] < strich3:
            bereich = 2
        elif strich3 <= maus_position[0] < strich4:
            bereich = 3
        else:
            bereich = 4
        if bereich != alt_bereich:

            bild.zeige_auswahl(bereich, daten.feld_liste, daten)
            alt_bereich = bereich

        for event in pygame.event.get():
            # fenster schliessen optionen
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            # (spezial-)stein auswaehlen
            if event.type == pygame.MOUSEBUTTONDOWN and bereich == 4:
                if daten.am_zug == 2:
                    if daten.sp_zwei == 1:
                        if bild.hoehe / 2 + 80 <= pygame.mouse.get_pos()[1] <= bild.hoehe / 2 + 100:
                            if 2 * bild.aussenrand + 400 + 10 + 2 * bild.zwischen_rand_gitter + 80 <= pygame.mouse.get_pos()[0] <= 2 * bild.aussenrand + 400 + 10 + 2 * bild.zwischen_rand_gitter + 100:
                                bild.stein_ausgewaehlt = 1
                            elif 2 * bild.aussenrand + 420 + 10 + 2 * bild.zwischen_rand_gitter + 80 <= pygame.mouse.get_pos()[0] <= 2 * bild.aussenrand + 420 + 10 + 2 * bild.zwischen_rand_gitter + 100:
                                bild.stein_ausgewaehlt = 2

                elif daten.am_zug == 1:
                    if daten.sp_eins == 1:
                        if bild.aussenrand + 80 <= pygame.mouse.get_pos()[1] <= bild.aussenrand + 100:
                            if 2 * bild.aussenrand + 400 + 10 + 2 * bild.zwischen_rand_gitter + 80 <= pygame.mouse.get_pos()[0] <= 2 * bild.aussenrand + 400 + 10 + 2 * bild.zwischen_rand_gitter + 100:
                                bild.stein_ausgewaehlt = 1
                            elif 2 * bild.aussenrand + 420 + 10 + 2 * bild.zwischen_rand_gitter + 80 <= pygame.mouse.get_pos()[0] <= 2 * bild.aussenrand + 420 + 10 + 2 * bild.zwischen_rand_gitter + 100:
                                bild.stein_ausgewaehlt = 2

                bild.stand_bild(daten)

            # stein in reihe setzen
            if event.type == pygame.MOUSEBUTTONDOWN and bereich != 4:
                bild.animation_Reihe(bereich, daten)
                if bild.stein_ausgewaehlt == 1:
                    daten.neuer_stein(bereich, 1)
                if bild.stein_ausgewaehlt == 2:
                    daten.neuer_stein(bereich, 2)
                bild.zeige_position(daten.feld_liste)
                alt_bereich = 5
                auswahl_erfolgt = True
                bild.stein_ausgewaehlt = 1

                # siegebedingungen fuer einzelnes spiel ueberpruefen
                punkte, positionen = daten.neue_siegesbedingungen()
                if punkte != [0, 0]:
                    daten.punkte[1] += punkte[1]
                    daten.punkte[0] += punkte[0]
                    bild.umkreisen_animation(positionen, daten)
                    bild.animation_leren(daten)
                    daten.feld_liste = [["-", "-", "-", "-"], ["-", "-", "-", "-"],
                                        ["-", "-", "-", "-"], ["-", "-", "-", "-"]]
                    daten.sp_zwei = 1
                    daten.sp_eins = 1

    # siegbedingungen fuer gesamtes spiel ueberpruefen
    if daten.punkte[0] >= daten.ziel and daten.punkte[1] >= daten.ziel:
        if daten.punkte[0] > daten.punkte[1]:
            bild.nachricht("Spieler 1 hat gewonnen", (150, 150, 150), 60, (100, 530), bild.rot_gewinnt)
            daten.punkte = [0, 0]
        elif daten.punkte[0] < daten.punkte[1]:
            bild.nachricht("Spieler 2 hat gewonnen", (150, 150, 150), 60, (100, 530), bild.blau_gewinnt)
        else:
            bild.nachricht("Entscheidungsspiel", (100, 100, 100), 60, (150, 100), bild.beide_aliens)
            daten.punkte = [0, 0]
            daten.ziel = daten.punkte[0] + 1
    elif daten.punkte[0] >= daten.ziel:
        bild.nachricht("Spieler 1 hat gewonnen", (150, 150, 150), 60, (100, 530), bild.rot_gewinnt)
        daten.punkte = [0, 0]
    elif daten.punkte[1] >= daten.ziel:
        bild.nachricht("Spieler 2 hat gewonnen", (150, 150, 150), 60, (100, 530), bild.blau_gewinnt)
        daten.punkte = [0, 0]

    kontrollstrukturen.aus_schalten_pruefen()
