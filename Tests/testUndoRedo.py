from Logic.CRUD import adaugare_obiect, getById
from Logic.UndoRedo import undocmd, redocmd


def testUndoRedo():
    lista = []
    undoLista = []
    redoLista = []

    #add 1
    lista = adaugare_obiect("1", "vlad", "economy", 100, "ftda", lista, undoLista, redoLista)
    assert len(lista) == 1

    #add 2
    lista = adaugare_obiect("2", "vlad", "economy", 150, "dahy", lista, undoLista, redoLista)
    assert len(lista) == 2

    #add 3
    lista = adaugare_obiect("3", "andrei", "economy plus", 200, "qwer", lista, undoLista, redoLista)
    assert len(lista) == 3

    #undo 1
    lista = undocmd(lista, undoLista, redoLista)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is None

    #undo 2
    lista = undocmd(lista, undoLista, redoLista)
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

    #undo 3
    lista = undocmd(lista, undoLista, redoLista)
    assert len(lista) == 0
    assert getById("1", lista) is None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

    #undo 4
    lista = undocmd(lista, undoLista, redoLista)
    assert len(lista) == 0
    assert getById("1", lista) is None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

    #add x3
    lista = adaugare_obiect("1", "vlad", "economy", 100, "daxx", lista, undoLista, redoLista)
    lista = adaugare_obiect("2", "vlad", "economy", 150, "dqqa", lista, undoLista, redoLista)
    lista = adaugare_obiect("3", "andrei", "economy plus", 200, "dcca", lista, undoLista, redoLista)

    #redo
    lista = redocmd(lista, undoLista, redoLista)
    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None

    #undo x2
    lista = undocmd(lista, undoLista, redoLista)
    lista = undocmd(lista, undoLista, redoLista)
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

    # redo 1
    lista = redocmd(lista, undoLista, redoLista)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is None

    # redo 2
    lista = redocmd(lista, undoLista, redoLista)
    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None

    # undo x2
    lista = undocmd(lista, undoLista, redoLista)
    lista = undocmd(lista, undoLista, redoLista)
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

    # add
    lista = adaugare_obiect("4", "andrei", "business", 200, "dcca", lista, undoLista, redoLista)
    assert len(lista) == 2

    # redo
    lista = redocmd(lista, undoLista, redoLista)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is not None

    # undo 1
    lista = undocmd(lista, undoLista, redoLista)
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is None

    # undo 2
    lista = undocmd(lista, undoLista, redoLista)
    assert len(lista) == 0
    assert getById("1", lista) is None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is None

    # redo x2
    lista = redocmd(lista, undoLista, redoLista)
    lista = redocmd(lista, undoLista, redoLista)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is not None

    # redo x2
    lista = redocmd(lista, undoLista, redoLista)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is not None