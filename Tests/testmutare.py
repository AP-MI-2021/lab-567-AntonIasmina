from Domain.obiect import get_locatie
from Logic.CRUD import adaugare_obiect, getById
from Logic.Mutare import mutare_obiect


def test_mutare_obiect():
    lista = []
    lista = adaugare_obiect("111", "carte", "fictiune", 100, "2345", lista)
    lista = adaugare_obiect("112", "revista", "horror", 200, "2346", lista)

    lista = mutare_obiect(lista, "2345", "2347")

    assert get_locatie(getById("111", lista)) == "2347"
    assert get_locatie(getById("112", lista)) == "2346"

