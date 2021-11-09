from Logic.AfisareSume import suma_pret_locatie
from Logic.CRUD import adaugare_obiect


def test_afisare_sume():
    lista = []
    lista = adaugare_obiect("111", "carte", "fictiune", 100, "2345", lista)
    lista = adaugare_obiect("112", "revista", "horror", 200, "2346", lista)
    lista = adaugare_obiect("113", "manual", "scolar", 300, "2345", lista)

    rezultat= suma_pret_locatie(lista)

    assert len(rezultat) == 2
    assert rezultat["2345"] == 400
    assert rezultat["2346"] == 200