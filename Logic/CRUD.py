from Domain.obiect import get_id, creeaza_obiect


def adaugare_obiect(id_obiect, nume, descriere, pret_achizitie, locatie, lista, undo_lista, redo_lista):
    """
    Adauga un obiect intr-o lista
    :param id_:
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :param lista:
    :param undo_lista:
    :param redo_lista:
    :return: lista ce contine obiectele vechi+noul obiect
    """
    if getById(id_obiect, lista) is not None:
        raise ValueError("Exista deja id-ul acesta !Dati alt id!")

    obiect = creeaza_obiect(id_obiect, nume, descriere, pret_achizitie, locatie)
    undo_lista.append(lista)
    redo_lista.clear()
    return lista+[obiect]


def getById(id_obiect, lista: list):
    """
    Da obiectul cu id-ul dat intr-o lista
    :param id_: string
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat
    """

    for obiect in lista:
        if get_id(obiect) == id_obiect:
            return obiect
    return None


def stergere_obiect(id_obiect, lista, undo_lista, redo_lista):
    """
    Sterge un obiect dintr-o lista
    :param id_obiect: string
    :param lista: lista de obiecte
    :param undo_lista:lst
    :param redo_lista:lst
    :return: lista fara obiectul sters
    """
    if getById(id_obiect, lista) is None:
        raise ValueError("Nu exista niciun obiect de sters cu id-ul dat!")

    return[obiect for obiect in lista if get_id(obiect) != id_obiect]
    undo_lista.append(lista)
    redo_lista.clear()



def modifica_obiect(id_obiect, nume, descriere, pret_achizitie, locatie, lista, undo_lista, redo_lista):
    """
    Modifica un obiect dupa id
    :param id_obiect:
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :param lista: lista de obiecte
    :param undo_lista:
    :param redo_lista:
    :return: lista cu obiectul cu id-ul dat,modificat
    """
    if getById(id_obiect, lista) is None:
        raise ValueError("Nu exista niciun obiect cu id-ul dat!")

    lista_noua = []
    for obiect in lista:
        if get_id(obiect) == id_obiect:
            obiectnou = creeaza_obiect(id_obiect, nume, descriere, pret_achizitie, locatie)
            lista_noua.append(obiectnou)
        else:
            lista_noua.append(obiect)
    undo_lista.append(lista)
    redo_lista.clear()
    return lista_noua
