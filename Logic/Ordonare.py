from Domain.obiect import get_pret_achizitie


def ordoneaza_obiecte(lista):
    """
    Ordoneaza crescator obiectele dupa pretul de achizitie
    :param lista: lst de obiecte
    :return: lst cu obiectele sortate dupa pret
    """
    #return sorted(lista, key=get_pret_achizitie)
    return sorted(lista, key=lambda obiect: get_pret_achizitie(obiect))
