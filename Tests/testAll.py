from Tests.testCRUD import test_adaugare_obiect, test_stergere_obiect, test_modifica_obiect
from Tests.testDomain import test_obiect

def runAllTests():
    test_obiect()
    test_adaugare_obiect()
    test_stergere_obiect()
    test_modifica_obiect()
