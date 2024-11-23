import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        
        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0 
            return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "banaani", 3)
            if tuote_id == 3:
                return Tuote(3, "mansikka", 8)
            return None

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kaksi_eri_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        self.kauppa.lisaa_koriin(2)  
        self.kauppa.tilimaksu("kalle", "11111")

        self.pankki_mock.tilisiirto.assert_called_with("kalle", 42, "11111", "33333-44455", 8)

    def test_kaksi_samaa_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)  
        self.kauppa.lisaa_koriin(1)  
        self.kauppa.tilimaksu("elina", "222222")

        self.pankki_mock.tilisiirto.assert_called_with("elina", 42, "222222", "33333-44455", 10)

    def test_loppunut_tuote_ei_nosta_summaa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)  
        self.kauppa.lisaa_koriin(3)  
        self.kauppa.tilimaksu("maria", "333333")

        self.pankki_mock.tilisiirto.assert_called_with("maria", 42, "333333", "33333-44455", 5)

    def test_aloita_asiointi_nollaa_ostokset(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)  
        self.kauppa.aloita_asiointi() 
        self.kauppa.tilimaksu("pasi", "44444")

        self.pankki_mock.tilisiirto.assert_called_with("pasi", 42, "44444", "33333-44455", 0)

    def test_uusi_viitenumero_jokaiselle_maksulle(self):
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2] 
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("olli", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("olli", 1, "12345", "33333-44455", 5)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("kalle", "67890")

        self.pankki_mock.tilisiirto.assert_called_with("kalle", 2, "67890", "33333-44455", 3)