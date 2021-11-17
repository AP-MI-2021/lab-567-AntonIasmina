def undocmd(lista, undoLista, redoLista):
    if len(undoLista) > 0:
        redoLista.append(lista)
        return undoLista.pop()
    return lista


def redocmd(lista, undoLista, redoLista):
    if len(redoLista) > 0:
        undoLista.append(lista)
        return redoLista.pop()
    return lista
