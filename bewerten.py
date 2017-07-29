

class Bewertung(object):

    def bewerten(self, spielfeld, aus_sicht):

        wert_steine1 = 0
        wert_steine2 = 0

        for spalte in spielfeld.feld_liste:
            for stein in spalte:
                if stein == 'o':
                    wert_steine1 += 1
                elif stein == 'x':
                    wert_steine2 += 1
                elif stein == 'O':
                    wert_steine1 += 5
                elif stein == 'X':
                    wert_steine2 += 5

        bewertung = wert_steine1 - wert_steine2
        if aus_sicht == 2:
            bewertung *= -1

        return bewertung

    def bewerten_gewinnen(self, spielfeld, aus_sicht):

        (punkte1, punkte2), umwichtig = spielfeld.neue_siegesbedingungen()

        bewertung = punkte1 - punkte2
        if aus_sicht == 2:
            bewertung *= -1

        return bewertung
