import feld
import fenster_klasse
import pygame
import sys
import kontrollstrukturen
import  computerspieler

def sieg_ueberpruefen():
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

# sp1 = o
# sp2 = x
bild = fenster_klasse.Fenster()
daten = feld.Spielfeld()
computerspieler = computerspieler.Schlauerspieler()

computer = True

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

        if daten.am_zug == 1 or not computer:
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
            if daten.am_zug == 1 or not computer:
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

            if daten.am_zug == 1 or not computer:
                # stein in reihe setzen
                if event.type == pygame.MOUSEBUTTONDOWN and bereich != 4:
                    bild.animation_reihe(bereich, daten)
                    daten.neuer_stein(bereich, bild.stein_ausgewaehlt)
                    bild.zeige_position(daten.feld_liste)
                    alt_bereich = 5
                    auswahl_erfolgt = True
                    bild.stein_ausgewaehlt = 1

                    # siegebedingungen fuer einzelnes spiel ueberpruefen
                    sieg_ueberpruefen()

        if daten.am_zug == 2 and computer and not auswahl_erfolgt:
            gewaehlte_spalte, gewaehlter_stein = computerspieler.ermittle_zug(daten)
            bild.stein_ausgewaehlt = gewaehlter_stein
            bild.animation_reihe(gewaehlte_spalte, daten)
            daten.neuer_stein(gewaehlte_spalte, bild.stein_ausgewaehlt)
            bild.zeige_position(daten.feld_liste)
            alt_bereich = 5
            auswahl_erfolgt = True
            bild.stein_ausgewaehlt = 1
            sieg_ueberpruefen()

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

