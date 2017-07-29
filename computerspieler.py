import random
import bewerten


class Computerspieler(object):

    def __init__(self):
        pass

    def ermittle_gueltige_zuge(self, spielfeld):
        """ liefert eine Liste mit den aktuell moeglichen Zuegen zurueck. """

        amZug = spielfeld.am_zug

        hatSpezialsteinNoch = False
        if amZug == 1 and spielfeld.sp_eins == 1:
            hatSpezialsteinNoch = True
        elif amZug == 2 and spielfeld.sp_zwei == 1:
            hatSpezialsteinNoch = True

        zuege = []
        for spalte in range(4):
            zuege.append((spalte, 1))
            if hatSpezialsteinNoch:
                zuege.append((spalte, 2))

        return zuege

    def ermittleZug (self, spielfeld):
        pass


class Zufallsspieler ( Computerspieler ):

    def __init__(self):
        Computerspieler.__init__(self)
        pass

    def ermittleZug(self, spielfeld):
        zufalls_reihe = random.randint(0, 3)
        return zufalls_reihe, 1

class Schlauerspieler ( Computerspieler ):

    def __init__(self):
        Computerspieler.__init__(self)
        self.bewerter = bewerten.Bewertung()
        pass

    def ermittleZug(self, spielfeld):

        # 1. Moegliche Zuege ermitteln

        amZug = spielfeld.am_zug
        kandidatenZuege = self.ermittle_gueltige_zuge(spielfeld)
        random.shuffle(kandidatenZuege)

        # Zuege ausprobieren und bewerten

        besteBewertung = -1000
        besterZug = kandidatenZuege[0]

        for zug in kandidatenZuege:
            bewertung = self.probiereZugAus(spielfeld, zug)
            if bewertung > besteBewertung:
                besteBewertung = bewertung
                besterZug = zug
                #print("Neuer Bester Zug", besteBewertung, besterZug)

        # Zug zurueckliefern
        return besterZug

    def probiereZugAus (self, spielfeld, zug):

        ich = spielfeld.am_zug
        spielfeld.neuer_stein(zug[0], zug[1])

        # bewerte neue Spielsituation
        bewertung = self.bewerter.bewerten_gewinnen(spielfeld, ich)

        # Zug zuruecknehmen
        spielfeld.neuer_stein_undo()

        return bewertung

