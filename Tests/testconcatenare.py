from Domain.obiect import get_descriere
from Logic.CRUD import adaugare_obiect, getById
from Logic.Concatenare import concatenare


def test_concatenare():
    lista = []
    lista = adaugare_obiect("111", "carte", "fictiune", 100, "2345", lista)
    lista = adaugare_obiect("112", "revista", "horror", 9, "2346", lista)

    lista=concatenare(lista, "copii", 10)

    assert get_descriere(getById("111", lista)) =="fictiunecopii"
    assert get_descriere(getById("112", lista)) == "horror"