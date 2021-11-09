from Logic.CRUD import adaugare_obiect
from Logic.PretMaximLocatie import determina_pret_maxim_per_locatie


def test_determina_pret_maxim_per_locatie():
    lista = []
    lista = adaugare_obiect("111", "carte", "fictiune", 200, "2345", lista)
    lista = adaugare_obiect("112", "revista", "horror", 150, "2346", lista)

    rezultat = determina_pret_maxim_per_locatie(lista)

    assert len(rezultat) == 2
    print(rezultat["2345"])
    assert rezultat["2345"] == 200
    assert rezultat["2346"] == 150
