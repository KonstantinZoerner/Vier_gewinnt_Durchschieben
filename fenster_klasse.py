import pygame
import kontrollstrukturen
import sys


class Fenster:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.zwischen_rand_rand = 80
        self.aussenrand = 12
        self.spielfeldrand = 20
        self.zwischen_rand_gitter = self.spielfeldrand + self.zwischen_rand_rand
        self.fenster_groesse = self.breite, self.hoehe = 700 + 3 * self.aussenrand + 2 * self.zwischen_rand_gitter, 400 + 2 * self.aussenrand + 2 * self.zwischen_rand_gitter
        self.hintergrund = (100, 100, 100)
        self.screen = pygame.display.set_mode(self.fenster_groesse)
        pygame.display.set_caption("Vier Gewinnt ", " Tolles Spiel")
        self.stein_blau1 = pygame.image.load("Grafiken/Steine/Stein1.png")
        self.stein_rot1 = pygame.image.load("Grafiken/Steine/Stein2.png")
        self.stein_blau2 = pygame.image.load("Grafiken/Steine/Stein3.png")
        self.stein_rot2 = pygame.image.load("Grafiken/Steine/Stein4.png")
        self.stein2klein = pygame.image.load("Grafiken/Steine/Stein1klein.png")
        self.stein1klein = pygame.image.load("Grafiken/Steine/Stein2klein.png")
        self.stein4klein = pygame.image.load("Grafiken/Steine/Stein3klein.png")
        self.stein3klein = pygame.image.load("Grafiken/Steine/Stein4klein.png")
        self.grausteinklein = pygame.image.load("Grafiken/Steine/grauSteinklein.png")
        self.hintergrund_bild = pygame.image.load("Grafiken/Hintergrund/hintergrund (936, 702).png")
        self.hintergrund_bild_quadrat = pygame.image.load("Grafiken/Hintergrund/hintergrund (600, 600).png")
        self.blau_gewinnt = pygame.image.load("Grafiken/Hintergrund/blaugewinnt (936, 702).png")
        self.rot_gewinnt = pygame.image.load("Grafiken/Hintergrund/rotgewinnt (936, 702).png")
        self.beide_aliens = pygame.image.load("Grafiken/Hintergrund/beidealliens (936, 702).png")
        self.kreis = pygame.image.load("Grafiken/Steine/sieger_mantel.png")
        self.keinstein = pygame.image.load("Grafiken/Steine/keinStein.png")
        self.gitter = pygame.image.load("Grafiken/Gitter/Gitter2.png")
        self.icon = pygame.image.load("Grafiken/Icon/Icon2.png")
        pygame.display.set_icon(self.icon)
        self.screen.fill(self.hintergrund)
        self.farbe1 = (229, 0, 0)
        self.farbe2 = (0, 149, 199)
        self.stein_ausgewaehlt = 1
        print(self.zwischen_rand_gitter * 2 + 400)

    def animation_reihe_symbol(self, spalte, daten, neu):
        for i in range(20):
            self.screen.fill(self.hintergrund)
            self.screen.blit(self.hintergrund_bild_quadrat, (self.aussenrand, self.aussenrand))
            for j in range(4):
                if daten.feld_liste[spalte][j] == "-":
                    self.screen.blit(self.keinstein, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 + j * 100 + 5 + self.zwischen_rand_gitter))
                if daten.feld_liste[spalte][j] == "x":
                    self.screen.blit(self.stein_blau1, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 + j * 100 + 5 + self.zwischen_rand_gitter))
                if daten.feld_liste[spalte][j] == "o":
                    self.screen.blit(self.stein_rot1, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 + j * 100 + 5 + self.zwischen_rand_gitter))
                if daten.feld_liste[spalte][j] == "X":
                    self.screen.blit(self.stein_blau2, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 + j * 100 + 5 + self.zwischen_rand_gitter))
                if daten.feld_liste[spalte][j] == "O":
                    self.screen.blit(self.stein_rot2, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 + j * 100 + 5 + self.zwischen_rand_gitter))

            if neu == "-":
                self.screen.blit(self.keinstein, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 - 100 + 5 + self.zwischen_rand_gitter))
            if neu == "x":
                self.screen.blit(self.stein_blau1, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 - 100 + 5 + self.zwischen_rand_gitter))
            if neu == "o":
                self.screen.blit(self.stein_rot1, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 - 100 + 5 + self.zwischen_rand_gitter))
            if neu == "X":
                self.screen.blit(self.stein_blau2, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 - 100 + 5 + self.zwischen_rand_gitter))
            if neu == "O":
                self.screen.blit(self.stein_rot2, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 - 100 + 5 + self.zwischen_rand_gitter))
            kontrollstrukturen.aus_schalten_pruefen()
            extra_liste = daten.feld_liste[:]
            extra_liste[spalte] = ["-", "-", "-", "-"]
            self.zeige_position(extra_liste)
            self.wiederkehrende_blider(daten)
            pygame.display.flip()
            self.clock.tick(30)

        for i in range(7):
            self.screen.fill(self.hintergrund)
            self.screen.blit(self.hintergrund_bild_quadrat, (self.aussenrand, self.aussenrand))
            if daten.feld_liste[spalte][3] == "-":
                self.screen.blit(self.keinstein, (
                    self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 10 + 400 + 10 + self.zwischen_rand_gitter))
            if daten.feld_liste[spalte][j] == "x":
                self.screen.blit(self.stein_blau1, (
                    self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 10 + 400 + 10 + self.zwischen_rand_gitter))
            if daten.feld_liste[spalte][j] == "o":
                self.screen.blit(self.stein_rot1, (
                    self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 10 + 400 + 10 + self.zwischen_rand_gitter))
            if daten.feld_liste[spalte][j] == "X":
                self.screen.blit(self.stein_blau2, (
                    self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 10 + 400 + 10 + self.zwischen_rand_gitter))
            if daten.feld_liste[spalte][j] == "O":
                self.screen.blit(self.stein_rot2, (
                    self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 10 + 400 + 10 + self.zwischen_rand_gitter))
            kontrollstrukturen.aus_schalten_pruefen()

            extra_liste = daten.feld_liste[:]
            extra_liste[spalte] = [neu, daten.feld_liste[spalte][0], daten.feld_liste[spalte][1], daten.feld_liste[spalte][2]]
            self.zeige_position(extra_liste)
            self.wiederkehrende_blider(daten)
            pygame.display.flip()
            self.clock.tick(30)

    def animation_reihe(self, spalte, daten, neu=None):
        if neu is None:
            if daten.am_zug == 1 and self.stein_ausgewaehlt == 1:
                neu = "o"
            if daten.am_zug == 2 and self.stein_ausgewaehlt == 1:
                neu = "x"
            if daten.am_zug == 1 and self.stein_ausgewaehlt == 2:
                neu = "O"
            if daten.am_zug == 2 and self.stein_ausgewaehlt == 2:
                neu = "X"

        for i in range(20):
            self.screen.fill(self.hintergrund)
            self.screen.blit(self.hintergrund_bild_quadrat, (self.aussenrand, self.aussenrand))
            for j in range(4):
                if daten.feld_liste[spalte][j] == "-":
                    self.screen.blit(self.keinstein, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 + j * 100 + 5 + self.zwischen_rand_gitter))
                if daten.feld_liste[spalte][j] == "x":
                    self.screen.blit(self.stein_blau1, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 + j * 100 + 5 + self.zwischen_rand_gitter))
                if daten.feld_liste[spalte][j] == "o":
                    self.screen.blit(self.stein_rot1, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 + j * 100 + 5 + self.zwischen_rand_gitter))
                if daten.feld_liste[spalte][j] == "X":
                    self.screen.blit(self.stein_blau2, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 + j * 100 + 5 + self.zwischen_rand_gitter))
                if daten.feld_liste[spalte][j] == "O":
                    self.screen.blit(self.stein_rot2, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 + j * 100 + 5 + self.zwischen_rand_gitter))

            if neu == "-":
                self.screen.blit(self.keinstein, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 - 100 + 5 + self.zwischen_rand_gitter))
            if neu == "x":
                self.screen.blit(self.stein_blau1, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 - 100 + 5 + self.zwischen_rand_gitter))
            if neu == "o":
                self.screen.blit(self.stein_rot1, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 - 100 + 5 + self.zwischen_rand_gitter))
            if neu == "X":
                self.screen.blit(self.stein_blau2, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 - 100 + 5 + self.zwischen_rand_gitter))
            if neu == "O":
                self.screen.blit(self.stein_rot2, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 5 - 100 + 5 + self.zwischen_rand_gitter))
            kontrollstrukturen.aus_schalten_pruefen()
            extra_liste = daten.feld_liste[:]
            extra_liste[spalte] = ["-", "-" ,"-" ,"-"]
            self.zeige_position(extra_liste)
            self.wiederkehrende_blider(daten)
            pygame.display.flip()
            self.clock.tick(30)

        for i in range(7):
            self.screen.fill(self.hintergrund)
            self.screen.blit(self.hintergrund_bild_quadrat, (self.aussenrand, self.aussenrand))
            if daten.feld_liste[spalte][3] == "-":
                self.screen.blit(self.keinstein, (
                    self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 10 + 400 + 10 + self.zwischen_rand_gitter))
            if daten.feld_liste[spalte][j] == "x":
                self.screen.blit(self.stein_blau1, (
                    self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 10 + 400 + 10 + self.zwischen_rand_gitter))
            if daten.feld_liste[spalte][j] == "o":
                self.screen.blit(self.stein_rot1, (
                    self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 10 + 400 + 10 + self.zwischen_rand_gitter))
            if daten.feld_liste[spalte][j] == "X":
                self.screen.blit(self.stein_blau2, (
                    self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 10 + 400 + 10 + self.zwischen_rand_gitter))
            if daten.feld_liste[spalte][j] == "O":
                self.screen.blit(self.stein_rot2, (
                    self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 10 + 400 + 10 + self.zwischen_rand_gitter))
            kontrollstrukturen.aus_schalten_pruefen()

            extra_liste = daten.feld_liste[:]
            if neu is not None:
                extra_liste[spalte] = [neu, daten.feld_liste[spalte][0], daten.feld_liste[spalte][1], daten.feld_liste[spalte][2]]
            self.zeige_position(extra_liste)
            self.wiederkehrende_blider(daten)
            pygame.display.flip()
            self.clock.tick(30)

    def animation_leren(self, daten):
        for i in range(35):
            self.screen.fill(self.hintergrund)
            self.screen.blit(self.hintergrund_bild_quadrat, (self.aussenrand, self.aussenrand))
            for j in range(4):
                for k in range(4):

                    if daten.feld_liste[k][j] == "-":
                        self.screen.blit(self.keinstein, (self.aussenrand + k * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 15 + j * 100 + 5 + self.zwischen_rand_gitter))
                    if daten.feld_liste[k][j] == "x":
                        self.screen.blit(self.stein_blau1, (self.aussenrand + k * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 15 + j * 100 + 5 + self.zwischen_rand_gitter))
                    if daten.feld_liste[k][j] == "o":
                        self.screen.blit(self.stein_rot1, (self.aussenrand + k * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 15 + j * 100 + 5 + self.zwischen_rand_gitter))
                    if daten.feld_liste[k][j] == "X":
                        self.screen.blit(self.stein_blau2, (self.aussenrand + k * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 15 + j * 100 + 5 + self.zwischen_rand_gitter))
                    if daten.feld_liste[k][j] == "O":
                        self.screen.blit(self.stein_rot2, (self.aussenrand + k * 100 + self.zwischen_rand_gitter, self.aussenrand + i * 15 + j * 100 + 5 + self.zwischen_rand_gitter))


            kontrollstrukturen.aus_schalten_pruefen()
            self.wiederkehrende_blider(daten)
            pygame.display.flip()
            self.clock.tick(30)

    def aussenrand_malen(self):
        st_farbe = 100
        ent_farbe = 50
        farbspanne = ent_farbe - st_farbe
        intervall = farbspanne / self.aussenrand
        r, g, b = ent_farbe, ent_farbe, ent_farbe
        for i in range(self.aussenrand):
            pygame.draw.line(self.screen, (r, g, b), (400 - 1 + i + self.aussenrand + 2 * self.zwischen_rand_gitter, 0), (400 - 1 + i + self.aussenrand + 2 * self.zwischen_rand_gitter, self.hoehe - 1))
            if i <= (self.aussenrand / 2):
                r -= intervall
                g -= intervall
                b -= intervall
            else:
                r += intervall
                g += intervall
                b += intervall

        r, g, b = st_farbe, st_farbe, st_farbe
        for i in range(self.aussenrand):
            pygame.draw.line(self.screen, (r, g, b), (0 + i, 0 + i), (self.breite - 1 - i, 0 + i))
            pygame.draw.line(self.screen, (r, g, b), (self.breite - 1 - i, 0 + i), (self.breite - 1 - i, self.hoehe - 1 - i))
            pygame.draw.line(self.screen, (r, g, b), (0 + i, 0 + i), (0 + i, self.hoehe - 1 - i))
            pygame.draw.line(self.screen, (r, g, b), (self.breite - 1 - i, self.hoehe - 1 - i), (0 + i, self.hoehe - 1 - i))

            r += intervall
            g += intervall
            b += intervall

    def spielfeldrand_malen(self):
        st_farbe = 50
        ent_farbe = 0
        farbspanne = ent_farbe - st_farbe
        intervall = farbspanne / self.spielfeldrand
        r, g, b = st_farbe, st_farbe, st_farbe


        for i in range(self.spielfeldrand):
            pygame.draw.line(self.screen, (r, g, b), (self.aussenrand + self.zwischen_rand_rand + i, self.aussenrand + self.zwischen_rand_rand + i), (self.aussenrand + self.zwischen_rand_gitter + 400 + self.spielfeldrand - i - 1, self.aussenrand + self.zwischen_rand_rand + i ))
            pygame.draw.line(self.screen, (r, g, b), (self.aussenrand + self.zwischen_rand_rand + i, self.aussenrand + self.zwischen_rand_rand + i), (self.aussenrand + self.zwischen_rand_rand + i, self.hoehe - self.aussenrand -self.zwischen_rand_rand - 1 - i))
            pygame.draw.line(self.screen, (r, g, b), (self.aussenrand + self.zwischen_rand_gitter + 400 + self.spielfeldrand - i - 1, self.aussenrand + self.zwischen_rand_rand + i), (self.aussenrand + self.zwischen_rand_gitter + 400 + self.spielfeldrand - i - 1, self.hoehe - self.aussenrand -self.zwischen_rand_rand - 1 - i))
            pygame.draw.line(self.screen, (r, g, b), (self.aussenrand + self.zwischen_rand_rand + i, self.hoehe - self.aussenrand -self.zwischen_rand_rand - 1 - i), (self.aussenrand + self.zwischen_rand_gitter + 400 + self.spielfeldrand - i - 1, self.hoehe - self.aussenrand -self.zwischen_rand_rand - 1 - i))

            r += intervall
            g += intervall
            b += intervall

    def text_auf_bildschirm(self, text, farbe, groese, position):
        text_groesse = pygame.font.Font("freesansbold.ttf", groese)
        text_oberflaeche, text_rect = self.ermittle_textobjekte(text, text_groesse, farbe)
        self.screen.blit(text_oberflaeche, position)

    def ermittle_textobjekte(self, text, text_groesse, farbe):
        text_oberflaeche = text_groesse.render(text, True, farbe)
        return text_oberflaeche, text_oberflaeche.get_rect

    def wiederkehrende_blider(self, daten):
        x = self.aussenrand * 2 + self.zwischen_rand_gitter * 2 + 399
        y = self.aussenrand
        pygame.draw.rect(self.screen, (20, 20, 20), (x, y, self.breite - x, self.hoehe - y))
        if daten.am_zug == 1:
            self.text_auf_bildschirm("(am Zug)", self.farbe1, 20, (2 * self.aussenrand + 550 + 10 + 2 * self.zwischen_rand_gitter, self.aussenrand + 15))
        elif daten.am_zug == 2:
            self.text_auf_bildschirm("(am Zug)", self.farbe2, 20, (2 * self.aussenrand + 550 + 10 + 2 * self.zwischen_rand_gitter, self.hoehe / 2 + 15))
        self.text_auf_bildschirm("Steine:", self.farbe1, 20, (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter, self.aussenrand + 80))
        self.text_auf_bildschirm("Steine:", self.farbe2, 20, (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter, self.hoehe / 2 + 80))

        if daten.am_zug == 1:
            if self.stein_ausgewaehlt == 1:
                pygame.draw.rect(self.screen, self.farbe1, (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter + 80, self.aussenrand + 80, 20, 20))
                pygame.draw.rect(self.screen, (20, 20, 20), (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter + 81, self.aussenrand + 81, 18, 18))
            else:
                pygame.draw.rect(self.screen, (255, 146, 0), (2 * self.aussenrand + 420 + 10 + 2 * self.zwischen_rand_gitter + 80, self.aussenrand + 80, 20, 20))
                pygame.draw.rect(self.screen, (20, 20, 20), (2 * self.aussenrand + 420 + 10 + 2 * self.zwischen_rand_gitter + 81, self.aussenrand + 81, 18, 18))
        if daten.am_zug == 2:
            if self.stein_ausgewaehlt == 1:
                pygame.draw.rect(self.screen, self.farbe2, (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter + 80, self.hoehe / 2 + 80, 20, 20))
                pygame.draw.rect(self.screen, (20, 20, 20), (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter + 81, self.hoehe / 2 + 81, 18, 18))
            else:
                pygame.draw.rect(self.screen, (0, 255, 255), (2 * self.aussenrand + 420 + 10 + 2 * self.zwischen_rand_gitter + 80, self.hoehe / 2 + 80, 20, 20))
                pygame.draw.rect(self.screen, (20, 20, 20), (2 * self.aussenrand + 420 + 10 + 2 * self.zwischen_rand_gitter + 81, self.hoehe / 2 + 81, 18, 18))
        if daten.sp_eins == 1:

            self.screen.blit(self.stein3klein, (2 * self.aussenrand + 420 + 10 + 2 * self.zwischen_rand_gitter + 80, self.aussenrand + 80))

        else:
            self.screen.blit(self.grausteinklein, (2 * self.aussenrand + 420 + 10 + 2 * self.zwischen_rand_gitter + 80, self.aussenrand + 80))

        if daten.sp_zwei == 1:
            self.screen.blit(self.stein4klein,(2 * self.aussenrand + 420 + 10 + 2 * self.zwischen_rand_gitter + 80, self.hoehe / 2 + 80))

        else:
            self.screen.blit(self.grausteinklein,(2 * self.aussenrand + 420 + 10 + 2 * self.zwischen_rand_gitter + 80, self.hoehe / 2 + 80))

        self.screen.blit(self.stein1klein, (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter + 80, self.aussenrand + 80))
        self.screen.blit(self.stein2klein, (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter + 80, self.hoehe / 2 + 80))
        self.screen.blit(self.gitter, (self.aussenrand + self.zwischen_rand_gitter, self.aussenrand + self.zwischen_rand_gitter))
        self.aussenrand_malen()
        self.spielfeldrand_malen()
        self.text_auf_bildschirm("Spieler 1", self.farbe1, 30, (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter, self.aussenrand + 10))
        self.text_auf_bildschirm("Spieler 2", self.farbe2, 30, (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter, self.hoehe / 2 + 10))
        self.zeige_punkte(daten.punkte)

    def zeige_position(self, feld_liste):
        for s, spalte in enumerate(feld_liste):
            for f, feld in enumerate(spalte):
                if feld == "x":
                    self.screen.blit(self.stein_blau1, (self.aussenrand + s * 100 + self.zwischen_rand_gitter, self.aussenrand + f * 100 + self.zwischen_rand_gitter))
                elif feld == "o":
                    self.screen.blit(self.stein_rot1, (self.aussenrand + s * 100 + self.zwischen_rand_gitter, self.aussenrand + f * 100 + self.zwischen_rand_gitter))
                if feld == "X":
                    self.screen.blit(self.stein_blau2, (self.aussenrand + s * 100 + self.zwischen_rand_gitter, self.aussenrand + f * 100 + self.zwischen_rand_gitter))
                elif feld == "O":
                    self.screen.blit(self.stein_rot2, (self.aussenrand + s * 100 + self.zwischen_rand_gitter, self.aussenrand + f * 100 + self.zwischen_rand_gitter))

    def umkreisen_animation(self, kreisliste, daten):
        an = False
        for i in range(90):
            if i % 10 == 0 and not an:
                an = True
            elif i % 10 == 0 and  an:
                an = False


            self.screen.fill(self.hintergrund)
            self.screen.blit(self.hintergrund_bild_quadrat, (self.aussenrand, self.aussenrand))
            self.zeige_position(daten.feld_liste)
            self.wiederkehrende_blider(daten)

            for s, spalte in enumerate(kreisliste):
                for f, feld in enumerate(spalte):
                    if feld == "+" and an:

                        self.screen.blit(self.kreis, (self.aussenrand + s * 100 + self.zwischen_rand_gitter, self.aussenrand + f * 100 + self.zwischen_rand_gitter))


            pygame.display.flip()
            kontrollstrukturen.aus_schalten_pruefen()
            self.clock.tick(30)

    def zeige_auswahl(self, spalte, feldliste, daten, neu = None):
        if neu is None:
            if daten.am_zug == 1 and self.stein_ausgewaehlt == 1:
                neu = "o"
            if daten.am_zug == 2 and self.stein_ausgewaehlt == 1:
                neu = "x"
            if daten.am_zug == 1 and self.stein_ausgewaehlt == 2:
                neu = "O"
            if daten.am_zug == 2 and self.stein_ausgewaehlt == 2:
                neu = "X"
        self.screen.fill(self.hintergrund)
        self.screen.blit(self.hintergrund_bild_quadrat, (self.aussenrand, self.aussenrand))
        if spalte != 4:

            if neu == "-":
                self.screen.blit(self.keinstein, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand - 100  + self.zwischen_rand_gitter))
            elif neu == "x":
                self.screen.blit(self.stein_blau1, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand - 100 + self.zwischen_rand_gitter))
            elif neu == "o":
                self.screen.blit(self.stein_rot1, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand - 100 + self.zwischen_rand_gitter))
            elif neu == "X":
                self.screen.blit(self.stein_blau2, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand - 100 + self.zwischen_rand_gitter))
            elif neu == "O":
                self.screen.blit(self.stein_rot2, (self.aussenrand + spalte * 100 + self.zwischen_rand_gitter, self.aussenrand - 100 + self.zwischen_rand_gitter))




        self.zeige_position(feldliste)
        self.wiederkehrende_blider(daten)
        pygame.display.flip()

    def zeige_punkte(self, punkte):
        if punkte[0] == 1:
            self.text_auf_bildschirm("1 Punkt", self.farbe1, 20, (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter, self.aussenrand + 50))
        else:
            self.text_auf_bildschirm((str(punkte[0]) + " Punkte"), self.farbe1, 20, (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter, self.aussenrand + 50))

        if punkte[1] == 1:
            self.text_auf_bildschirm("1 Punkt", self.farbe2, 20, (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter, self.hoehe / 2 + 50))
        else:
            self.text_auf_bildschirm((str(punkte[1]) + " Punkte"), self.farbe2, 20, (2 * self.aussenrand + 400 + 10 + 2 * self.zwischen_rand_gitter, self.hoehe / 2 + 50))

    def startbildschirm(self):
        self.screen.fill((20, 20, 20))
        self.screen.blit(self.beide_aliens,(0,0))

        self.text_auf_bildschirm("Wilkommen bei Vier-Gewinnt", (200, 200, 200), 60, (30, 100))
        pygame.display.flip()
        geklickt = False
        while not geklickt:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    geklickt = True

    def nachricht(self, nachricht, farbe, groesse, position, bild):
        self.screen.fill((20, 20, 20))
        if bild is not None:
            self.screen.blit(bild, (0,0))
        self.text_auf_bildschirm(nachricht, farbe, groesse, position)
        pygame.display.flip()
        geklickt = False
        while not geklickt:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    geklickt = True

    def stand_bild(self, daten):
        self.screen.fill(self.hintergrund)
        self.screen.blit(self.hintergrund_bild_quadrat, (self.aussenrand, self.aussenrand))
        self.zeige_position(daten.feld_liste)
        self.wiederkehrende_blider(daten)
        pygame.display.flip()

if __name__ == "__main__":
    fenster = Fenster()
    pygame.display.flip()


    while True:
        kontrollstrukturen.aus_schalten_pruefen()

        pygame.display.flip()
