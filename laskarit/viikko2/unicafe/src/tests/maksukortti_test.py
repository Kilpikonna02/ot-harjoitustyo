import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        if self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa"):
            return True
        else:
            return False
    
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)

        if self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa"):
            return True
        else:
            return False
        
    def test_saldo_vahenee_oikein_jos_ei_ole_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1500)

        if self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa"):
            return True
        else:
            return False
        
    def test_saldo_latautuu_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        if self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa"):
            return True
        else:
            return False

