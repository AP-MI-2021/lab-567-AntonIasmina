from Tests.testAfisareSume import test_afisare_sume
from Tests.testCRUD import test_adaugare_obiect, test_stergere_obiect, test_modifica_obiect
from Tests.testDomain import test_obiect
from Tests.testOrdonare import test_ordoneaza_obiecte
from Tests.testPretMaximLocatie import test_determina_pret_maxim_per_locatie
from Tests.testUndoRedo import testUndoRedo
from Tests.testmutare import test_mutare_obiect
from Tests.testconcatenare import test_concatenare


def runAllTests():
    test_obiect()
    test_adaugare_obiect()
    test_stergere_obiect()
    test_modifica_obiect()
    test_mutare_obiect()
    test_concatenare()
    test_determina_pret_maxim_per_locatie()
    test_ordoneaza_obiecte()
    test_afisare_sume()
    testUndoRedo()