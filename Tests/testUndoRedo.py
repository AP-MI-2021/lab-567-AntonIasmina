#from Domain.obiect import creeaza_obiect
#from Logic.CRUD import adaugare_obiect
#from Logic.UndoRedo import do_undo, do_redo


#def test_undo_redo():
    #lista = []
    #lista = creeaza_obiect(1, "obiect1", "gen1", 100, "loc1")
    #lista = creeaza_obiect(2, "obiect2", "gen2", 200, "loc2")
    #lista = creeaza_obiect(3, "obiect3", "gen3", 450, "loc3")
    #lista = creeaza_obiect(4, "obiect4", "gen4", 2700, "loc4")

    #undo_lista = []
    #redo_lista = []
    #v_new = adaugare_obiect(5, "obiectnew", "gennew", 2997, "loc5", lista, undo_lista, redo_lista)
    #v_new = do_undo(v_new, undo_lista, redo_lista)
    #assert len(v_new) == len(lista)
    #v_new = do_undo(v_new, undo_lista, redo_lista)
    #assert v_new == None
    #v_new = do_redo(v_new, undo_lista, redo_lista)
    #assert len(v_new) == len(lista) + 1