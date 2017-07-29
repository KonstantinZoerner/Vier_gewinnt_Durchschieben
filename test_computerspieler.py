import unittest
import feld
import computerspieler

class TestZufallsspieler(unittest.TestCase):

    def test_ermittleZug(self):
        mein_feld = feld.Spielfeld()
        spieler = computerspieler.Zufallsspieler()

        zug = spieler.ermittleZug(mein_feld)

        self.assertTrue(0 <= zug[0] <= 3)

class TestSchlauerspieler(unittest.TestCase):

    def test_ermittleGueltigeZuege(self):

        spieler = computerspieler.Schlauerspieler()

        # Startfeld, Spieler 1 am Zug
        mein_feld = feld.Spielfeld()
        zuege = spieler.ermittleGueltigeZuge(mein_feld)
        self.assertEquals(len(zuege), 8)

        # Spieler 1 hat keinen Spezialstein
        mein_feld.sp_eins = 0
        zuege = spieler.ermittleGueltigeZuge(mein_feld)
        self.assertEquals(len(zuege), 4)

    def test_ermittleZug(self):
        mein_feld = feld.Spielfeld()
        spieler = computerspieler.Schlauerspieler()

        zug = spieler.ermittleZug(mein_feld)
        self.assertTrue(0 <= zug[0] <= 3)
