import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(10000)
        self.kortti2 = Maksukortti(0)

    def test_konstruktori_asettaa_kassapaatteen_oikein(self):
        self.assertEqual(str(self.kassapaate), "Kassapäätteessä on rahaa 100000, edulliset = 0, maukkaat = 0")

        
    def test_kateisosto_edullinen_toimii_kun_rahaa_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(str(self.kassapaate), "Kassapäätteessä on rahaa 100240, edulliset = 1, maukkaat = 0")
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250),10)

    
    def test_kateisosto_edullinen_toimii_kun_rahaa_ei_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kateisella(230)

        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230),230)
        self.assertEqual(str(self.kassapaate), "Kassapäätteessä on rahaa 100000, edulliset = 0, maukkaat = 0")

        
    def test_kateisosto_maukas_toimii_kun_rahaa_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)

        self.assertEqual(str(self.kassapaate), "Kassapäätteessä on rahaa 100400, edulliset = 0, maukkaat = 1")
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250),10)

    
    def test_kateisosto_maukas_toimii_kun_rahaa_ei_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kateisella(230)

        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230),230)
        self.assertEqual(str(self.kassapaate), "Kassapäätteessä on rahaa 100000, edulliset = 0, maukkaat = 0")

    
    def test_korttiosto_edullinen_toimii_kun_rahaa_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(str(self.kassapaate), "Kassapäätteessä on rahaa 100000, edulliset = 1, maukkaat = 0")
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti),True)

    
    def test_korttiosto_edullinen_toimii_kun_rahaa_ei_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti2)

        self.assertEqual(str(self.kassapaate), "Kassapäätteessä on rahaa 100000, edulliset = 0, maukkaat = 0")
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti2),False)
        
    def test_korttiosto_maukas_toimii_kun_rahaa_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(str(self.kassapaate), "Kassapäätteessä on rahaa 100000, edulliset = 0, maukkaat = 1")
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti),True)

    
    def test_korttiosto_maukkaasti_toimii_kun_rahaa_ei_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti2)

        self.assertEqual(str(self.kassapaate), "Kassapäätteessä on rahaa 100000, edulliset = 0, maukkaat = 0")
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti2),False)

    def test_kortin_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti2,200)

        self.assertEqual(str(self.kortti2), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(str(self.kassapaate), "Kassapäätteessä on rahaa 100200, edulliset = 0, maukkaat = 0")
    
    def test_kortin_lataus_tyhjalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti2,0)

        self.assertEqual(str(self.kortti2), "Kortilla on rahaa 0.00 euroa")
        self.assertEqual(str(self.kassapaate), "Kassapäätteessä on rahaa 100000, edulliset = 0, maukkaat = 0")

    def test_kortin_lataus_negatiivisella(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti2,-100)

        self.assertEqual(str(self.kortti2), "Kortilla on rahaa 0.00 euroa")
        self.assertEqual(str(self.kassapaate), "Kassapäätteessä on rahaa 100000, edulliset = 0, maukkaat = 0")