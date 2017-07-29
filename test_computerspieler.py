import unittest
import feld
import computerspieler

class TestZufallsspieler(unittest.TestCase):

    def test_ermittleZug(self):
        mein_feld = feld.Spielfeld()
        spieler = computerspieler.Zufallsspieler()

        zug = spieler.ermittle_zug(mein_feld)

        self.assertTrue(0 <= zug[0] <= 3)

class TestSchlauerspieler(unittest.TestCase):

    def test_ermittleGueltigeZuege(self):

        spieler = computerspieler.Schlauerspieler()

        # Startfeld, Spieler 1 am Zug
        mein_feld = feld.Spielfeld()
        zuege = spieler.ermittle_gueltige_zuge(mein_feld)
        self.assertEquals(len(zuege), 8)

        # Spieler 1 hat keinen Spezialstein
        mein_feld.sp_eins = 0
        zuege = spieler.ermittle_gueltige_zuge(mein_feld)
        self.assertEquals(len(zuege), 4)

    def test_ermittleZug(self):
        mein_feld = feld.Spielfeld()
        spieler = computerspieler.Schlauerspieler()

        zug = spieler.ermittle_zug(mein_feld)
        self.assertTrue(0 <= zug[0] <= 3)

    def test_gewinnzugmachen_spieler_1(self):
        mein_feld = feld.Spielfeld()
        spieler = computerspieler.Schlauerspieler()

        # 0123 (o am Zug)
        # xxox
        #   o
        #   o
        #
        mein_feld.neuer_stein(2, 1) # o in Spalte 2
        mein_feld.neuer_stein(0, 1) # x in Spalte 0
        mein_feld.neuer_stein(2, 1) # o in Spalte 2
        mein_feld.neuer_stein(1, 1) # x in Spalte 1
        mein_feld.neuer_stein(2, 1) # o in Spalte 2
        mein_feld.neuer_stein(3, 1) # x in Spalte 3

        zug = spieler.ermittle_zug(mein_feld)

        print("ZUG :",zug)
        self.assertTrue(zug[0] == 2)
        self.assertTrue(zug[1] == 2)


    def test_gewinnzugmachen_spieler_2(self):
        mein_feld = feld.Spielfeld()
        spieler = computerspieler.Schlauerspieler()

        # 0123 (o am Zug)
        # ooxo
        # o x
        #   x
        #
        mein_feld.neuer_stein(0, 1) # o in Spalte 2
        mein_feld.neuer_stein(2, 1) # o in Spalte 2
        mein_feld.neuer_stein(0, 1) # x in Spalte 0
        mein_feld.neuer_stein(2, 1) # o in Spalte 2
        mein_feld.neuer_stein(1, 1) # x in Spalte 1
        mein_feld.neuer_stein(2, 1) # o in Spalte 2
        mein_feld.neuer_stein(3, 1) # x in Spalte 3

        zug = spieler.ermittle_zug(mein_feld)

        print("ZUG :",zug)
        self.assertTrue(zug[0] == 2)
        self.assertTrue(zug[1] == 2)


    def test_gewinnzugmachen_spieler_3(self):  #Zwickmuehle
        mein_feld = feld.Spielfeld()
        spieler = computerspieler.Schlauerspieler()
        # 0123 (o am Zug)
        # xoxx
        # ooxo
        # oxox
        # ooxx


        # mein_feld.neuer_stein(0, 1) # o1
        # mein_feld.neuer_stein(3, 1) # x2
        # mein_feld.neuer_stein(0, 1) # o3
        # mein_feld.neuer_stein(3, 1) # x4
        # mein_feld.neuer_stein(0, 1) # o5
        # mein_feld.neuer_stein(2, 1) # x6
        # mein_feld.neuer_stein(3, 1) # o7
        # mein_feld.neuer_stein(0, 1) # x8
        # mein_feld.neuer_stein(3, 1) # o9
        # mein_feld.neuer_stein(1, 1) # x10
        # mein_feld.neuer_stein(1, 1) # o11
        # mein_feld.neuer_stein(3, 1) # x12
        # mein_feld.neuer_stein(2, 1) # o13
        # mein_feld.neuer_stein(2, 1) # x14
        # mein_feld.neuer_stein(1, 1) # o15
        # mein_feld.neuer_stein(2, 1) # x16

        mein_feld.feld_liste = [["x", "o", "o", "o"], ["o", "o", "x", "o"], ["x", "x", "o", "x"], ["x", "o", "x", "x"]]
        mein_feld.zeige_feld()
        spieler.maximale_tiefe = 4
        zug = spieler.ermittle_zug(mein_feld)


        print("ZUG :", zug)
        self.assertEqual(zug[0], 3)
        self.assertEqual(zug[1], 1)

        mein_feld.feld_liste = [["o", "x", "x", "x"], ["x", "x", "o", "x"], ["o", "o", "x", "o"], ["o", "x", "o", "o"]]
        mein_feld.zeige_feld()
        mein_feld.am_zug = 2
        spieler.maximale_tiefe = 4
        zug = spieler.ermittle_zug(mein_feld)


        print("ZUG :", zug)
        self.assertEqual(zug[0], 3)
        self.assertEqual(zug[1], 1)

