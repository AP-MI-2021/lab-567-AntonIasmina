def do_undo(undo_lista: list, redo_lista: list,
            lista_curenta: list):
    '''
    Aplica o actiune de tip "undo" listei de obiecte
    :param undo_lista: o lista care memoreaza lista de obiecte inainte de modificare
    :param redo_lista: o lista care memoreaza lista de obiecte dupa modificare
    :param lista_curenta: lista de obiecte curenta
    :return: lista inainte de ultima modificare
    '''
    if undo_lista:
        t_undo = undo_lista.pop()
        redo_lista.append(lista_curenta)
        return t_undo
    return None

def do_redo(undo_lista: list, redo_lista: list,
            lista_curenta: list):
    '''
    Aplica o actiune de tip "redo" listei de obiecte
    :param undo_lista: o lista care memoreaza lista de obiecte inainte de modificare
    :param redo_lista: o lista care memoreaza lista de obiecte dupa modificare
    :param lista_curenta: lista de obiecte curenta
    :return: lista dupa ultima modificare
    '''
    if redo_lista:
        t_redo = redo_lista.pop()
        undo_lista.append(lista_curenta)
        return t_redo
    return None
