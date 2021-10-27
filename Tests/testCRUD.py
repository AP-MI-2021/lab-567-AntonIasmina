from Domain.obiect2 import get_nume, get_descriere, get_pret_achizitie, get_locatie, creeaza_obiect, get_id
from Logic.CRUD import getById, adaugare_obiect, modifica_obiect, stergere_obiect


def test_adaugare_obiect():
    lista = []
    lista = adaugare_obiect("111", "carte", "fictiune", 100, "2345", lista)

    assert len(lista) == 1
    assert get_id(getById("111", lista)) == "111"
    assert get_nume(getById("111", lista)) == "carte"
    assert get_descriere(getById("111", lista)) == "fictiune"
    assert get_pret_achizitie(getById("111", lista)) == 100
    assert get_locatie(getById("111", lista)) == "2345"

def test_stergere_obiect():
    lista=[]
    lista = adaugare_obiect("111", "carte", "fictiune", 100, "2345", lista)
    lista = adaugare_obiect("112", "revista", "horror", 200, "2346", lista)

    lista = stergere_obiect("112", lista)
    assert len(lista) ==1
    assert getById("112", lista) is None
    assert getById("111", lista) is not None

def test_modifica_obiect():
    lista=[]
    lista = adaugare_obiect("111", "carte", "fictiune", 100, "2345", lista)
    lista = adaugare_obiect("112", "revista", "horror", 200, "2346", lista)

    lista=modifica_obiect("111", "manual", "scolar", 300, "2347", lista)

    obiectUpdate= getById("111", lista)
    assert get_id(obiectUpdate) == "111"
    assert get_nume(obiectUpdate) == "manual"
    assert get_descriere(obiectUpdate) == "scolar"
    assert get_pret_achizitie(obiectUpdate) == 300
    assert get_locatie(obiectUpdate) == "2347"

    obiectNonupdate= getById("112", lista)

    assert get_id(obiectNonupdate) == "112"
    assert get_nume(obiectNonupdate) == "revista"
    assert get_descriere(obiectNonupdate) =="horror"
    assert get_pret_achizitie(obiectNonupdate) == 200
    assert get_locatie(obiectNonupdate) =="2346"
