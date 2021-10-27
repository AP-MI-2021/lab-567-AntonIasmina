from Domain.obiect import creeaza_obiect, get_id, get_nume, get_descriere, get_pret_achizitie, get_locatie


def test_obiect():

    obiect= creeaza_obiect("111", "carte", "fictiune", 100, "2345")

    assert get_id(obiect)=="111"
    assert get_nume(obiect)=="carte"
    assert get_descriere(obiect)=="fictiune"
    assert get_pret_achizitie(obiect)==100
    assert get_locatie(obiect)=="2345"
