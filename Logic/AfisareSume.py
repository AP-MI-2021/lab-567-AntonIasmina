from Domain.obiect import get_pret_achizitie, get_locatie


def suma_pret_locatie(lista):
    """
    Determina suma preturilor pentru fiecare locatie.
    :param lista: lista obiecte
    :return: un dictionar
    """
    rezultat = {}
    for obiect in lista:
        pret = get_pret_achizitie(obiect)
        nume = get_locatie(obiect)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + pret
        else:
            rezultat[nume] = pret
    return rezultat