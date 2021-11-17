from Domain.obiect import get_id, creeaza_obiect


def adaugare_obiect(id_obiect, nume, descriere, pret_achizitie, locatie, lista, undoLista = None, redoLista = None):
    """
    Adauga un obiect intr-o lista
    :param id_obiect:
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :param lista:
    :return: lista ce contine obiectele vechi+noul obiect
    """
    if getById(id_obiect, lista) is not None:
        raise ValueError("Exista deja id-ul acesta !Dati alt id!")
    if undoLista is not None and redoLista is not None:
        undoLista.append(lista)
        redoLista.clear()
    obiect = creeaza_obiect(id_obiect, nume, descriere, pret_achizitie, locatie)
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


def stergere_obiect(id_obiect, lista, undoLista = None, redoLista = None):
    """
    Sterge un obiect dintr-o lista
    :param id_obiect: string
    :param lista: lista de obiect
    :return: lista fara obiectul sters
    """
    if getById(id_obiect, lista) is None:
        raise ValueError("Nu exista niciun obiect de sters cu id-ul dat!")
    if undoLista is not None and redoLista is not None:
        undoLista.append(lista)
        redoLista.clear()
    return[obiect for obiect in lista if get_id(obiect) != id_obiect]


def modifica_obiect(id_obiect, nume, descriere, pret_achizitie, locatie, lista, undoLista = None, redoLista = None):
    """
    Modifica un obiect dupa id
    :param id_obiect:
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: lista cu obiectul cu id-ul dat,modificat
    """
    if getById(id_obiect, lista) is None:
        raise ValueError("Nu exista niciun obiect cu id-ul dat!")
    if undoLista is not None and redoLista is not None:
        undoLista.append(lista)
        redoLista.clear()
    lista_noua = []
    for obiect in lista:
        if get_id(obiect) == id_obiect:
            obiectnou = creeaza_obiect(id_obiect, nume, descriere, pret_achizitie, locatie)
            lista_noua.append(obiectnou)
        else:
            lista_noua.append(obiect)
    return lista_noua
