# Kirjoita postinumerot-moduulin testit tähän tiedostoon
#Testeissä varmista ainakin seuraavien tapausten toiminta:

#1. postitoimipaikan nimellä löytyy vain yksi postinumero
#2. postitoimipaikan nimellä löytyy useita postinumeroita
#3. postitoimipaikan nimellä ei löydy lainkaan postinumeroita.

from postinumerot import get_postal_codes 

def test_one_result():
    assert get_postal_codes("Kormu") == ["12520"]

def test_multiple_results():
    assert get_postal_codes("porvoo") == ["06100", "06101", "06150", "06151", "06200", "06400", "06401", "06450", "06500"]

def test_no_result():
    assert get_postal_codes("mutsis") == None

def test_all_smart_post():
    assert len(get_postal_codes("smart post")) == len(get_postal_codes("SMARTPOST"))