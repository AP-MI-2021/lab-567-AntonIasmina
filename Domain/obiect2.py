def creeaza_obiect(id_obiect, nume, descriere, pret_achizitie, locatie):
    """
    Creeaza o lista ce reprezinta un obiect
    :param id_:string
    :param nume:string
    :param descriere:string
    :param pret_achizitie:float
    :param locatie:string
    :return:o lista ce contine un obiect
    """
    lista_obiect = [id_obiect, nume, descriere, pret_achizitie, locatie]

    return lista_obiect


def get_id(lista_obiect):
    """
    Da id-ul unui obiect
    :param lista_obiect:lst
    :return:lst
    """
    return lista_obiect[0]


def get_nume(lista_obiect):
    """
    Da numele unui obiect
    :param lista_obiect:lst
    :return:lst
    """
    return lista_obiect[1]


def get_descriere(lista_obiect):
    """
    Da descrierea unui obiect
    :param lista_obiect:lst
    :return:lst
    """
    return lista_obiect[2]


def get_pret_achizitie(lista_obiect):
    """
    Da pretul de achizitie de achzitie al unui obiect
    :param lista_obiect:lst
    :return:lst
    """
    return lista_obiect[3]


def get_locatie(lista_obiect):
    """
    Da locatia unui obiect
    :param lista_obiect:lst
    :return:lst
    """
    return lista_obiect[4]


def to_string(obiect):
    return "id: {} ,nume: {}, descriere: {},pret achizitie: {},locatie: {}".format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret_achizitie(obiect),
        get_locatie(obiect)
    )
