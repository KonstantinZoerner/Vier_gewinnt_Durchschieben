import unittest
import feld


class TestSpielfeld(unittest.TestCase):

    def test_spielfeld_erzeugen(self):
        mein_feld = feld.Spielfeld()
        self.assertEqual(mein_feld.breite, 4)
        self.assertEqual(mein_feld.hoehe, 4)

        self.assertEqual(mein_feld.am_zug, 1)
        self.assertEqual(mein_feld.aktuelles_symbol(), 'o')

    def test_stein_setzen(self):
        mein_feld = feld.Spielfeld()

        self.assertEqual(mein_feld.am_zug, 1)
        mein_feld.neuer_stein(0, 1)
        self.assertEqual(mein_feld.feld_liste[0][0], 'o')
        self.assertEqual(mein_feld.am_zug, 2)  # anderer Spieler dran


        mein_feld.neuer_stein(0, 2)
        self.assertEqual(mein_feld.feld_liste[0][0], 'X')
        self.assertEqual(mein_feld.feld_liste[0][1], 'o')
        self.assertEqual(mein_feld.am_zug, 1)  # anderer Spieler dran

    def test_stein_zurueck_nehmen1(self):
        mein_feld = feld.Spielfeld()

        start_liste = mein_feld.feld_liste[:]

        self.assertEqual(mein_feld.am_zug, 1)
        mein_feld.neuer_stein(0, 1)
        self.assertEqual(mein_feld.feld_liste[0][0], 'o')
        self.assertEqual(mein_feld.am_zug, 2)

        mein_feld.neuer_stein_undo()
        self.assertEqual(mein_feld.am_zug, 1)
        self.assertEqual(mein_feld.feld_liste, start_liste)

    def test_stein_zurueck_nehmen2(self):
        mein_feld = feld.Spielfeld()
        mein_feld.neuer_stein(1, 1)
        mein_feld.neuer_stein(1, 2)
        mein_feld.neuer_stein(1, 2)
        mein_feld.neuer_stein(1, 1)
        mein_feld.neuer_stein(1, 1)


        mein_feld.zeige_feld()

        mein_feld.neuer_stein_undo()
        mein_feld.zeige_feld()








if __name__ == '__main__':
    unittest.main()
