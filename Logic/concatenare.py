from Domain.obiect import get_pret_achizitie, creeaza_obiect, get_id, get_nume, get_descriere, get_locatie


def concatenare(lista,sir_caractere,valoare):
    """
    Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
    :param lista:lst
    :param sir_caractere:string
    :param valoare: int
    :return:
    """
    listaNoua=[]
    for obiect in lista :
        if get_pret_achizitie(obiect) > valoare :
            obiectNou=creeaza_obiect(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect)+sir_caractere,
                get_pret_achizitie(obiect),
                get_locatie(obiect)
            )
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua




