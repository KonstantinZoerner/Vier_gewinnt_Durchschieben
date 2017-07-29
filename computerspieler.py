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
        self.maximale_tiefe = 4
        pass

    def ermittle_zug(self, spielfeld):

        # 1. Moegliche Zuege ermitteln

        kandidaten_zuege = self.ermittle_gueltige_zuge(spielfeld)

        # Zuege ausprobieren und bewerten

        beste_bewertung = -1000
        bester_zug = kandidaten_zuege[0]

        for zug in kandidaten_zuege:
            bewertung = self.probiere_zug_aus(spielfeld.am_zug, spielfeld, zug, 1)
            if bewertung > beste_bewertung:
                beste_bewertung = bewertung
                bester_zug = zug

        # Zug zurueckliefern
        return bester_zug

    def probiere_zug_aus(self, spieler_am_zug, spielfeld, zug, tiefe):


        spielfeld.neuer_stein(zug[0], zug[1])

        print("tiefe=" , tiefe, " zug=", zug)
        spielfeld.zeige_feld()

        (punkte1, punkte2), umwichtig = spielfeld.neue_siegesbedingungen()
        if punkte1 != 0 or punkte2 != 0:
            if spieler_am_zug == 1:
                bewertung = (punkte1 - punkte2) * 1000
                print("Bewertung",bewertung)
            else:
                bewertung = (punkte2 - punkte1) * 1000
                print("Bewertung", bewertung)

        elif tiefe == self.maximale_tiefe:
            # Position bewerten und zurueckliefern
            bewertung = self.bewerter.bewerten(spielfeld, spieler_am_zug)
            print("Bewertung bei maximaler Tiefe", tiefe, " :", bewertung)
            print()
        else:
            # tiefer rechnen
            kandidaten_zuege = self.ermittle_gueltige_zuge(spielfeld)

            if tiefe % 2 == 0:
                bester_wert = -1000
                for zug in kandidaten_zuege:
                    wert = self.probiere_zug_aus(spieler_am_zug, spielfeld, zug, tiefe + 1)
                    if wert > bester_wert:
                        bester_wert = wert
                bewertung = bester_wert
                print("Bewertung (Maximum)", tiefe, " :", bewertung)
            else:
                bester_wert = 1000
                for zug in kandidaten_zuege:
                    wert = self.probiere_zug_aus(spieler_am_zug, spielfeld, zug, tiefe + 1)
                    if wert < bester_wert:
                        bester_wert = wert
                bewertung = bester_wert
            print("Bewertung (Minimum)", tiefe, " :", bewertung)

        # Zug zuruecknehmen
        spielfeld.neuer_stein_undo()

        return bewertung
