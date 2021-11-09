from Domain.obiect import to_string
from Logic.AfisareSume import suma_pret_locatie
from Logic.CRUD import adaugare_obiect, stergere_obiect, modifica_obiect
from Logic.Concatenare import concatenare
from Logic.Mutare import mutare_obiect
from Logic.Ordonare import ordoneaza_obiecte
from Logic.PretMaximLocatie import determina_pret_maxim_per_locatie


def printMenu():
    print("1.Adaugare obiect:")
    print("2.Stergere obiect:")
    print("3.Modificare obiect:")
    print("4.Mutarea tuturor obiectelor dintr-o locație în alta.")
    print("5.Concateneaza un string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.")
    print("6.Determina pretul maxim pentru fiecare locatie.")
    print("7.Ordoneaza obiectele crescător după prețul de achiziție.")
    print("8.Afișarea sumelor prețurilor pentru fiecare locație.")
    print("a.Afisare obiecte: ")
    print("x.Iesire")


def ui_adaugare_obiect(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati nume: ")
        descriere = input("Dati descriere: ")
        pret_achizitie = float(input("Dati pret achizitie: "))
        locatie = input("Dati locatie: ")
        print("Adaugarea a fost efectuata cu succes!")
        return adaugare_obiect(id, nume, descriere, pret_achizitie, locatie, lista)
    except ValueError as ve:
        print('Eroare:', ve)
    return lista


def ui_stergere_obiect(lista):
    try:
        id = input("Dati id-ul obiectului de sters: ")
        print("Stergerea a fost efectuata cu succes!")
        return stergere_obiect(id, lista)
    except ValueError as ve:
        print('Eroare:', ve)
        return lista


def ui_modifica_obiect(lista):
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret_achizitie = float(input("Dati noul pret de achizitie: "))
        locatie = input("Dati noua locatie: ")
        print("Modificarea a fost efectuata cu succes!")
        return modifica_obiect(id, nume, descriere, pret_achizitie, locatie, lista)
    except ValueError as ve:
        print('Eroare:', ve)
        return lista


def show_all(lista):
    for obiect in lista:
        print(to_string(obiect))


def ui_mutare_obiect(lista):
    try:
        locatiedata = input("Dati loctia obiectelor pe care doriti sa le mutati: ")
        locatienoua = input("Dati noua locatie a obiectelor: ")
        return mutare_obiect(lista, locatiedata, locatienoua)
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


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adaugare_obiect(lista)
        elif optiune == "2":
            lista = ui_stergere_obiect(lista)
        elif optiune == "3":
            lista = ui_modifica_obiect(lista)
        elif optiune == "4":
            lista = ui_mutare_obiect(lista)
        elif optiune == "5":
            lista = ui_concatenare_obiect(lista)
        elif optiune == "6":
            ui_determina_pret_maxim_per_locatie(lista)
        elif optiune == "7":
            ui_ordoneaza_obiecte(lista)
        elif optiune == "8":
            ui_afisare_suma_pret_locatie(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiunea este gresita!Reincercati: ")
