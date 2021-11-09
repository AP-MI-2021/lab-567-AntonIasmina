from Domain.obiect import get_locatie, get_pret_achizitie


def determina_pret_maxim_per_locatie(lista):
    """
    Determina cel mai mare pret pentru fiecare locatie.
    :param lista: lst
    :return:
    """
    rezultat = {}
    for obiect in lista:
        locatie = get_locatie(obiect)
        pret = get_pret_achizitie(obiect)
        if locatie in rezultat:
            if pret > rezultat[locatie]:
                rezultat[locatie] = pret
        else:
            rezultat[locatie] = pret
    return rezultat
