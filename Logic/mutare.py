from Domain.obiect import get_locatie, get_id, get_nume, get_descriere, get_pret_achizitie, creeaza_obiect


def mutare_obiect(lista, locatiedata, locatieschimbata):
    """
    Muta un obiect dintr-o locatie in alta:
    :param lista:lst
    :param locatiedata:locatia initiala
    :param locatieschimbata:locatia noua
    :return:lst
    """
    if not (len(locatieschimbata) == 4) :
        raise ValueError("Locatia trebuie sa aiba exact 4 caractere.")

    if not (len(locatiedata)) == 4 :
        raise ValueError("Locatia trebuie sa aiba exact 4 caractere.")

    ok = 0
    for obiect in lista:
        if get_locatie(obiect) == locatiedata:
            ok = 1
            break
    if ok == 0:
        raise ValueError("Locatia data nu exista in lista.")

    listaNoua = []
    for obiect in lista:
        if get_locatie(obiect) == locatiedata:
            obiectNou = creeaza_obiect(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect),
                get_pret_achizitie(obiect),
                locatieschimbata
            )
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua

