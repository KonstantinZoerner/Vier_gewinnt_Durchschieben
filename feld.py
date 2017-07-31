
class Spielfeld:

    def __init__(self, groesse=(4, 4)):  # groesse = breite, hoehe
        self.breite, self.hoehe = groesse
        self.am_zug = 1
        self.sp_zwei = 1
        self.sp_eins = 1
        self.ziel = 3
        self.punkte = [0, 0]

        self.feld_liste = []
        for spalte in range(self.breite):
            self.feld_liste.append([])
            for reihe in range(self.hoehe):
                self.feld_liste[-1].append("-")

        self.historie = []

    def zeige_feld(self):
        for reihe in range(self.hoehe):
            linie = ""
            for spalte in range(self.breite):
                linie += self.feld_liste[spalte][reihe] + " "
            print(linie)


    def aendere_feld(self, position, symbol):
        x, y = position
        if x < self.breite and y < self.hoehe:
            self.feld_liste[x][y] = symbol
        else:
            print("Diese Koordinate exestiert nicht")

    def stein_verschieben(self, position):
        x, y = position
        if x < self.breite and y < self.hoehe:
            stein = self.feld_liste[x][y]
            self.feld_liste[x][y] = "-"
            if y + 1 < self.hoehe:
                self.feld_liste[x][y + 1] = stein
            else:
                pass
        else:
            print("Diese Koordinate exestiert nicht")

    def neuer_stein(self, spalte, art):
        if self.am_zug == 1:
            if art == 1:
                symbol = "o"
            else:
                symbol = "O"
                self.sp_eins = 0
        else:
            if art == 1:
                symbol = "x"
            else:
                symbol = "X"
                self.sp_zwei = 0

        stein_der_rausfaellt = self.feld_liste[spalte][self.hoehe - 1]

        if stein_der_rausfaellt == "X":
            self.sp_zwei = 1
        if stein_der_rausfaellt == "O":
            self.sp_eins = 1

        historien_eintrag = (spalte, stein_der_rausfaellt)
        self.historie.append(historien_eintrag)

        for zeile in range(self.hoehe):
            self.stein_verschieben((spalte, self.hoehe - 1 - zeile))
        self.aendere_feld((spalte, 0), symbol)
        self.anderer_spieler_dran()

    def neuer_stein_undo(self):

        eintrag = self.historie.pop()
        spalte = eintrag[0]
        stein = eintrag[1]

        alte_spalte = self.feld_liste[spalte]

        oberster_stein = alte_spalte[0]

        # spezialstein wiederherstellen

        if oberster_stein == "O":
            self.sp_eins = 1
        elif oberster_stein == "X":
            self.sp_zwei = 1

        # spieler aendern
        self.anderer_spieler_dran()

        for feld in range(3):
            self.feld_liste[spalte][feld] = alte_spalte[feld+1]

        self.feld_liste[spalte][3] = stein
        if stein == "X":
            self.sp_zwei = 0
        if stein == "O":
            self.sp_eins = 0

    def aktuelles_symbol(self):
        if self.am_zug == 1:
            return 'o'
        else:
            return 'x'

    def siegbedingungen_ueberpruefen(self):
        sieger = []
        for spalte in range(self.breite):
            if self.feld_liste[spalte][0] == self.feld_liste[spalte][1] == self.feld_liste[spalte][2] == self.feld_liste[spalte][3] and self.feld_liste[spalte][0] != "-":
                sieger.append(self.feld_liste[spalte][0])
        for reihe in range(self.hoehe):
            if self.feld_liste[0][reihe] == self.feld_liste[1][reihe] == self.feld_liste[2][reihe] == self.feld_liste[3][reihe] and self.feld_liste[0][reihe] != "-":
                sieger.append(self.feld_liste[0][reihe])
        if self.feld_liste[0][0] == self.feld_liste[1][1] == self.feld_liste[2][2] == self.feld_liste[3][3] and self.feld_liste[0][0] != "-":
            sieger.append(self.feld_liste[0][0])
        if self.feld_liste[0][3] == self.feld_liste[1][2] == self.feld_liste[2][1] == self.feld_liste[3][0] and self.feld_liste[0][3] != "-":
            sieger.append(self.feld_liste[0][3])
        return sieger

    def neue_siegesbedingungen(self):
        positionen = [["-", "-", "-", "-"], ["-", "-", "-", "-"], ["-", "-", "-", "-"], ["-", "-", "-", "-"]]
        punkte = [0, 0]

        for spalte in range(self.breite):
            if self.feld_liste[spalte][0].lower() == self.feld_liste[spalte][1].lower() == self.feld_liste[spalte][2].lower() == self.feld_liste[spalte][3].lower() and self.feld_liste[spalte][0].lower() != "-":
                if self.feld_liste[spalte][0].isupper() or self.feld_liste[spalte][1].isupper() or self.feld_liste[spalte][2].isupper() or self.feld_liste[spalte][3].isupper():
                    if self.feld_liste[spalte][0].lower() == "x":
                        punkte[1] += 2
                    elif self.feld_liste[spalte][0].lower() == "o":
                        punkte[0] += 2
                else:
                    if self.feld_liste[spalte][0].lower() == "x":
                        punkte[1] += 1
                    elif self.feld_liste[spalte][0].lower() == "o":
                        punkte[0] += 1
                positionen[spalte] = ["+", "+", "+", "+"]
                #print("1")

        for reihe in range(self.hoehe):
            if self.feld_liste[0][reihe].lower() == self.feld_liste[1][reihe].lower() == self.feld_liste[2][reihe].lower() == self.feld_liste[3][reihe].lower() and self.feld_liste[0][reihe].lower() != "-":
                if self.feld_liste[0][reihe].isupper() or self.feld_liste[1][reihe].isupper() or self.feld_liste[2][reihe].isupper() or self.feld_liste[3][reihe].isupper():
                    if self.feld_liste[0][reihe].lower() == "x":
                        punkte[1] += 2
                    elif self.feld_liste[0][reihe].lower() == "o":
                        punkte[0] += 2
                else:
                    if self.feld_liste[0][reihe].lower() == "x":
                        punkte[1] += 1
                    elif self.feld_liste[0][reihe].lower() == "o":
                        punkte[0] += 1

                for s, spalte in enumerate(self.feld_liste):
                    positionen[s][reihe] = "+"
                    #print("2")

        if self.feld_liste[0][3].lower() == self.feld_liste[1][2].lower() == self.feld_liste[2][1].lower() == self.feld_liste[3][0].lower() and self.feld_liste[0][3].lower() != "-":
            if self.feld_liste[0][3].isupper() or self.feld_liste[1][2].isupper() or self.feld_liste[2][1].isupper() or self.feld_liste[3][0].isupper():
                if self.feld_liste[0][3].lower() == "x":
                    punkte[1] += 2
                elif self.feld_liste[0][3].lower() == "o":
                    punkte[0] += 2
            else:
                if self.feld_liste[0][3].lower() == "x":
                    punkte[1] += 1
                elif self.feld_liste[0][3].lower() == "o":
                    punkte[0] += 1

            for i in range(4):
                positionen[i][3 - i] = "+"
                #print("3")

        if self.feld_liste[0][0].lower() == self.feld_liste[1][1].lower() == self.feld_liste[2][2].lower() == self.feld_liste[3][3].lower() and self.feld_liste[0][0].lower() != "-":
            if self.feld_liste[0][0].isupper() or self.feld_liste[1][1].isupper() or self.feld_liste[2][2].isupper() or self.feld_liste[3][3].isupper():
                if self.feld_liste[0][0].lower() == "x":
                    punkte[1] += 2
                elif self.feld_liste[0][0].lower() == "o":
                    punkte[0] += 2
            else:
                if self.feld_liste[0][0].lower() == "x":
                    punkte[1] += 1
                elif self.feld_liste[0][0].lower() == "o":
                    punkte[0] += 1

            for i in range(4):
                positionen[i][i] = "+"
                #print("4")

        return punkte, positionen

    def anderer_spieler_dran(self):
        if self.am_zug == 1:
            self.am_zug = 2
        else:
            self.am_zug = 1

    def spielablauf(self):
        self.zeige_feld()
        gewonnwn = False
        s1 = None
        s2 = None
        while not gewonnwn:
            if self.am_zug == 1:
                print("Spieler 1 am Zug")
                korrekt = False
                while not korrekt:
                    s1 = int(input()) - 1
                    if {s1} <= {0, 1, 2, 3}:
                        korrekt = True
                    else:
                        print("Bitte antworten Sie mt der Zeilen Nummer (1 - 4)")
                self.neuer_stein(s1, "o")
                self.am_zug = 2
            elif self.am_zug == 2:
                print("Spieler 2 am Zug")
                korrekt = False
                while not korrekt:
                    s2 = int(input()) - 1
                    if {s2} <= {0, 1, 2, 3}:
                        korrekt = True
                    else:
                        print("Bitte antworten Sie mt der Zeilen Nummer (1 - 4)")
                self.neuer_stein(s2, "x")
                self.am_zug = 1
            self.zeige_feld()
            if len(self.siegbedingungen_ueberpruefen()) != 0:
                print(self.siegbedingungen_ueberpruefen())
                gewonnwn = True

def erzeuge_spielfeld_aus_zeilen(zeilen, am_zug = 1):
    spielfeld = Spielfeld()

    spielfeld.am_zug = am_zug
    spielfeld.sp_eins = 1
    spielfeld.sp_zwei = 1
    x = 0
    y = 0
    for zeile in zeilen:
        for zeichen in zeile:
            spielfeld.aendere_feld((x, y), zeichen)
            if zeichen == 'O':
                spielfeld.sp_eins = 0
            if zeichen == 'X':
                spielfeld.sp_zwei = 0
            x += 1
        y += 1
        x = 0

    return spielfeld

if __name__ == "__main__":
    spielfeld = Spielfeld((4, 4))
    spielfeld.spielablauf()
