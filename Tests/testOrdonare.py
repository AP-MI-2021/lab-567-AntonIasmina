from Domain.obiect import get_id
from Logic.CRUD import adaugare_obiect
from Logic.Ordonare import ordoneaza_obiecte


def test_ordoneaza_obiecte():
    lista = []
    lista = adaugare_obiect("111", "carte", "fictiune", 100, "2345", lista)
    lista = adaugare_obiect("112", "revista", "horror", 200, "2346", lista)

    rezultat=ordoneaza_obiecte(lista)

    assert get_id(rezultat[0]) == "111"
    assert get_id(rezultat[1]) == "112"
