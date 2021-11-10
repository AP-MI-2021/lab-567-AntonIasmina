from Domain.obiect import to_string, creeaza_obiect
from Logic.AfisareSume import suma_pret_locatie
from Logic.CRUD import adaugare_obiect, stergere_obiect, modifica_obiect
from Logic.Concatenare import concatenare
from Logic.Mutare import mutare_obiect
from Logic.Ordonare import ordoneaza_obiecte
from Logic.PretMaximLocatie import determina_pret_maxim_per_locatie
from Logic.UndoRedo import do_undo, do_redo


def printMenu():
    print("1.Adaugare obiect:")
    print("2.Stergere obiect:")
    print("3.Modificare obiect:")
    print("4.Mutarea tuturor obiectelor dintr-o locație în alta.")
    print("5.Concateneaza un string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.")
    print("6.Determina pretul maxim pentru fiecare locatie.")
    print("7.Ordoneaza obiectele crescător după prețul de achiziție.")
    print("8.Afișarea sumelor prețurilor pentru fiecare locație.")
    print("u.Undo")
    print("r.Redo")
    print("a.Afisare obiecte: ")
    print("x.Iesire")


def ui_adaugare_obiect(lista, undo_lista, redo_lista):
    try:
        id_obiect = input("Dati id-ul: ")
        nume = input("Dati nume: ")
        if not nume:
            raise ValueError("Numele nu poate sa fie nul.")
        descriere = input("Dati descriere: ")
        if not descriere:
            raise ValueError("Descrierea nu poate sa fie nula.")
        pret_achizitie = float(input("Dati pret achizitie: "))
        if pret_achizitie < 0:
            raise ValueError("Pretul nu poate fi negativ.")
        locatie = input("Dati locatie: ")
        print("Adaugarea a fost efectuata cu succes!")
        return adaugare_obiect(id_obiect, nume, descriere, pret_achizitie, locatie, lista, undo_lista, redo_lista)
    except ValueError as ve:
        print('Eroare:Nu ati introdus o valoare valida', ve)
        return lista


def ui_stergere_obiect(lista, undo_lista, redo_lista):
    try:
        id_obiect = input("Dati id-ul obiectului de sters: ")
        lista=stergere_obiect(lista, id_obiect, undo_lista, redo_lista)
        print("Stergerea a fost efectuata cu succes!")
        return lista
    except ValueError as ve:
        print('Eroare:Eroare, nu ati introdus o valoare valida pentru ID', ve)
        return lista


def ui_modifica_obiect(lista, undo_lista, redo_lista):
    try:
        id_obiect = input("Dati id-ul obiectului de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret_achizitie = float(input("Dati noul pret de achizitie: "))
        if pret_achizitie < 0:
            raise ValueError("Pretul nu poate fi negativ.")
        locatie = input("Dati noua locatie: ")
        print("Modificarea a fost efectuata cu succes!")
        return modifica_obiect(id_obiect, nume, descriere, pret_achizitie, locatie, lista, undo_lista, redo_lista)
    except ValueError as ve:
        print('Eroare:', ve)
        return lista


def show_all(lista):
    for obiect in lista:
        print(to_string(obiect))


def ui_mutare_obiect(lista, undo_lista, redo_lista):
    try:
        locatiedata = input("Dati loctia obiectelor pe care doriti sa le mutati: ")
        locatienoua = input("Dati noua locatie a obiectelor: ")
        return mutare_obiect(lista, locatiedata, locatienoua, undo_lista, redo_lista)
    except ValueError as ve:
        print('Eroare:', ve)
        return lista


def ui_concatenare_obiect(lista):
    try:
        sir_caractere = input("Dati sirul de caractere pe care doriti sa-l concatenati: ")
        valoare = float(input("Dati valoarea cu care doriti sa comparati pretul: "))
        print("Concatenarea a avut loc cu succes!")

        return concatenare(lista, sir_caractere, valoare)
    except ValueError as ve:
        print('Eroare', ve)
        return lista


def ui_determina_pret_maxim_per_locatie(lista):
    try:
        rezultat = determina_pret_maxim_per_locatie(lista)
        for locatie in rezultat:
            print("Pretul maxim la locatia {} este: {}".format(locatie, rezultat[locatie]))
    except ValueError as ve:
        print('Eroare', ve)
        return lista


def ui_afisare_suma_pret_locatie(lista):
    try:
        rezultat = suma_pret_locatie(lista)
        for locatie in rezultat:
            print("Locatia {} are suma preturilor: {}".format(locatie, rezultat[locatie]))
    except ValueError as ve:
        print('Eroare', ve)
        return lista


def ui_ordoneaza_obiecte(lista):
    try:
        return show_all(ordoneaza_obiecte(lista))
    except ValueError as ve:
        print('Eroare', ve)
        return lista


def ui_undo(lista, undo_lista, redo_lista):
    undo_rez = do_undo(undo_lista, redo_lista, lista)
    if undo_rez is not None:
        return undo_rez
    return lista


def ui_redo(lista, undo_lista, redo_lista):
    redo_rez = do_redo(undo_lista, redo_lista, lista)
    if redo_rez is not None:
        return redo_rez
    return lista



def runMenu():
    lista = []
    undo_lista = []
    redo_lista = []
    while True:
        try:
            printMenu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                lista = ui_adaugare_obiect(lista, undo_lista, redo_lista)
            elif optiune == "2":
                lista = ui_stergere_obiect(lista, undo_lista, redo_lista)
            elif optiune == "3":
                lista = ui_modifica_obiect(lista, undo_lista, redo_lista)
            elif optiune == "4":
                lista = ui_mutare_obiect(lista,undo_lista, redo_lista)
            elif optiune == "5":
                lista = ui_concatenare_obiect(lista)
            elif optiune == "6":
                ui_determina_pret_maxim_per_locatie(lista)
            elif optiune == "7":
                ui_ordoneaza_obiecte(lista)
            elif optiune == "8":
                ui_afisare_suma_pret_locatie(lista)
            elif optiune == "u":
                lista = ui_undo(lista, undo_lista, redo_lista)
            elif optiune == "r":
                lista = ui_redo(lista, undo_lista, redo_lista)
            elif optiune == "a":
                show_all(lista)
            elif optiune == "x":
                break
            else:
                print("Optiunea este gresita!Reincercati: ")
        except Exception as ex:
            print("Eroare, nu ati introdus o valoare valida!", ex)