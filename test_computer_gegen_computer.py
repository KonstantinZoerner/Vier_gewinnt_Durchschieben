import unittest
import feld
import computerspieler

class TestBegegnungen(unittest.TestCase):

    def test_unterschiedliche_tiefe(self):
        f = feld.Spielfeld()

        spieler1 = computerspieler.Schlauerspieler(tiefe=2)
        spieler2 = computerspieler.Schlauerspieler(tiefe=4)

        print(f.siegbedingungen_ueberpruefen())
        anzahl_zuege = 0

        while f.siegbedingungen_ueberpruefen() == [] and anzahl_zuege <= 10:
            if f.am_zug == 1:
                zug = spieler1.ermittle_zug(f)
                f.neuer_stein(zug[0], zug[1])
            else:
                zug = spieler2.ermittle_zug(f)
                f.neuer_stein(zug[0], zug[1])
            f.zeige_feld()
            print()
            anzahl_zuege += 1

        # TODO: Pruefen, dass Spieler 2 gewonnen hat

