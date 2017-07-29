class Bewertung( object ):

    def bewerten(self, spielfeld, ausSicht):

        wertSteine1 = 0
        wertSteine2 = 0

        for spalte in spielfeld.feld_liste:
            for stein in spalte:
                if stein == 'o':
                    wertSteine1 += 1
                elif stein == 'x':
                    wertSteine2 += 1
                elif stein == 'O':
                    wertSteine1 += 5
                elif stein == 'X':
                    wertSteine2 += 5

        bewertung = wertSteine1 - wertSteine2
        if ausSicht == 2:
            bewertung *= -1

        return bewertung
