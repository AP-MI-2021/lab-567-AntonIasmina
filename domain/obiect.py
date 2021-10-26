def creeaza_obiect(id, nume, descriere, pret_achizitie, locatie):
    """
    Creaza un dictionar ce reprezinta un obiect
    :param lista:
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return: un dictionar ce contine un obiect
    """
    return {
        "id":id,
        "nume":nume,
        "descriere":descriere,
        "pret_achizitie":pret_achizitie,
        "locatie":locatie
    }

def get_id(obiect):
    """
    Da id-ul unui obiect
    :param obiect: string
    :return: id obiect
    """
    return obiect["id"]

def get_nume(obiect):
    """
    Da numele obiectului
    :param nume: string
    :return: nume obiect
    """
    return obiect["nume"]

def get_descriere(obiect):
    """
    Da descrierea unui obiect
    :param obiect: string
    :return: descrierea obiectului
    """
    return obiect["descriere"]

def get_pret_achizitie(obiect):
    """
    Da pretul de achizitie al obiectului
    :param obiect: string
    :return: pret obiect
    """
    return obiect["pret_achizitie"]

def get_locatie(obiect):
    """
    Da locatia unui obiect
    :param obiect: string
    :return: locatie obiect
    """
    return obiect["locatie"]

def to_string(obiect):
    return "id: {} ,nume: {}, descriere: {},pret achizitie: {},locatie: {}".format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret_achizitie(obiect),
        get_locatie(obiect)
    )