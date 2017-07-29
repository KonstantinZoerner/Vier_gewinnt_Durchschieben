import random
import bewerten


class Computerspieler(object):

    def __init__(self):
        pass

    def ermittle_gueltige_zuge(self, spielfeld):
        """ liefert eine Liste mit den aktuell moeglichen Zuegen zurueck. """

        am_zug = spielfeld.am_zug

        hat_spezialstein_noch = False
        if am_zug == 1 and spielfeld.sp_eins == 1:
            hat_spezialstein_noch = True
        elif am_zug == 2 and spielfeld.sp_zwei == 1:
            hat_spezialstein_noch = True

        zuege = []
        for spalte in range(4):
            zuege.append((spalte, 1))
            if hat_spezialstein_noch:
                zuege.append((spalte, 2))

        return zuege

    def ermittle_zug(self, spielfeld):
        pass


class Zufallsspieler (Computerspieler):

    def __init__(self):
        Computerspieler.__init__(self)
        pass

    def ermittle_zug(self, spielfeld):
        zufalls_reihe = random.randint(0, 3)
        return zufalls_reihe, 1

class Schlauerspieler (Computerspieler):

    def __init__(self):
        Computerspieler.__init__(self)
        self.bewerter = bewerten.Bewertung()
        pass

    def ermittle_zug(self, spielfeld):

        # 1. Moegliche Zuege ermitteln

        kandidaten_zuege = self.ermittle_gueltige_zuge(spielfeld)
        random.shuffle(kandidaten_zuege)

        # Zuege ausprobieren und bewerten

        beste_bewertung = -1000
        bester_zug = kandidaten_zuege[0]

        for zug in kandidaten_zuege:
            bewertung = self.probiere_zug_aus(spielfeld, zug)
            if bewertung > beste_bewertung:
                beste_bewertung = bewertung
                bester_zug = zug

        # Zug zurueckliefern
        return bester_zug

    def probiere_zug_aus(self, spielfeld, zug):
        ich = spielfeld.am_zug
        spielfeld.neuer_stein(zug[0], zug[1])

        # bewerte neue Spielsituation
        bewertung = self.bewerter.bewerten_gewinnen(spielfeld, ich)

        # Zug zuruecknehmen
        spielfeld.neuer_stein_undo()

        return bewertung

