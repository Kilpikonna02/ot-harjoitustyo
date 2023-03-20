import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)
        self.kortti2 = Maksukortti(200)

    def test_konstruktori_asettaa_saldon_oikein(self):
        if self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa"):
            return True
        else:
            return False

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        if self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.50 euroa"):
            return True
        else:
            return False

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        if self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa"):
            return True
        else:
            return False

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti2 = Maksukortti(200)
        kortti2.syo_edullisesti()

        if self.assertEqual(str(kortti2), "Kortilla on rahaa 2.00 euroa"):
            return True
        else:
            return False

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        if self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa"):
            return True
        else:
            return False

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        if self.assertEqual(str(self.kortti), "Kortilla on rahaa 150.00 euroa"):
            return True
        else:
            return False
    
    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti2 = Maksukortti(200)
        kortti2.syo_maukkaasti()

        if self.assertEqual(str(self.kortti2), "Kortilla on rahaa 2.00 euroa"):
            return True
        else:
            return False
    
    def test_negatiivisen_summan_lataus_ei_muuta_arvoa(self):
        self.kortti.lataa_rahaa(-500)

        if self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa"):
            return True
        else:
            return False

    def test_syo_edullisesti_tasarahalla(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()

        if self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa"):
            return True
        else:
            return False

    def test_syo_maukkaasti_tasarahalla(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()

        if self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa"):
            return True
        else:
            return False






