from Domain.obiect import to_string
from Logic.CRUD import modifica_obiect, stergere_obiect, adaugare_obiect
from Logic.Concatenare import concatenare
from Logic.Mutare import mutare_obiect


def ui_adaugare_obiect(lista, lista_specificatii_comanda):
    try:
        id = lista_specificatii_comanda[1]
        nume = lista_specificatii_comanda[2]
        descriere = lista_specificatii_comanda[3]
        pret_achizitie = float(lista_specificatii_comanda[4])
        locatie = lista_specificatii_comanda[5]
        print("Adaugarea a fost efectuata cu succes!")
        return adaugare_obiect(id, nume, descriere, pret_achizitie, locatie, lista)
    except ValueError as ve:
        print('Eroare:', ve)
    return lista


def ui_stergere_obiect(lista, lista_specificatii_comanda):
    try:
        id = lista_specificatii_comanda[1]
        print("Stergerea a fost efectuata cu succes!")
        return stergere_obiect(id, lista)
    except ValueError as ve:
        print('Eroare:', ve)

    return lista


def ui_modifica_obiect(lista, lista_specificatii_comanda):
    try:
        id = lista_specificatii_comanda[1]
        nume = lista_specificatii_comanda[2]
        descriere = lista_specificatii_comanda[3]
        pret_achizitie = float(lista_specificatii_comanda[4])
        locatie = lista_specificatii_comanda[5]
        print("Modificarea a fost efectuata cu succes!")
        return modifica_obiect(id, nume, descriere, pret_achizitie, locatie, lista)
    except ValueError as ve:
        print('Eroare:Nu ati introdus o valoare valida', ve)

    return lista


def show_all(lista):
    for obiect in lista:
        print(to_string(obiect))


def ui_mutare_obiect(lista, lista_specificatii_comanda):
    try:
        locatiedata = lista_specificatii_comanda[1]
        locatienoua = lista_specificatii_comanda[2]
        return mutare_obiect(lista, locatiedata, locatienoua)
    except ValueError as ve:
        print('Eroare:', ve)
        return lista


def ui_concatenare_obiect(lista, lista_specificatii_comanda):
    sir_caractere = lista_specificatii_comanda[1]
    valoare = float(lista_specificatii_comanda[2])
    print("Concatenarea a avut loc cu succes!")

    return concatenare(lista, sir_caractere, valoare)

def printMenu():
    print(
        """
        Adaugare obiect :id_obiect,nume, descriere, pret_achizitie, locatie
        Stergere obiect : id_obiect
        Modificare obiect id_obiect,nume, descriere, pret achizitie, locatie
        Muta toate obiectele dintr-o locatie in alta: locatiedata, locatienoua
        Concateneaza un string la toate descrierile obiectelor cu un pret mai mare decat o anumita valoare : descriere, valoare" 
        Show all
        Iesire
        """
    )

def runMenu2(lista):
        while True:
            printMenu()
            comenzi = input("Introduceti comenzile separate prin ';', iar detaliile pentru fiecare comanda separate prin ',': ")
            comenzi = comenzi.split(sep=";")

            for comanda in comenzi:
                comanda = comanda.split(sep=",")
                lista_specificatii_comanda=[]

                for specificatii_comanda in comanda :
                    lista_specificatii_comanda.append(specificatii_comanda)

                if lista_specificatii_comanda[0] == "Adaugare obiect" :
                    lista = ui_adaugare_obiect(lista, lista_specificatii_comanda)

                elif lista_specificatii_comanda[0] == "Stergere obiect" :
                    ui_stergere_obiect(lista, lista_specificatii_comanda)

                elif lista_specificatii_comanda[0] == "Modificare obiect" :
                    ui_modifica_obiect(lista, lista_specificatii_comanda)

                elif lista_specificatii_comanda[0] == "Concateneaza un string la toate descrierile obiectelor cu un pret mai mare decat o anumita valoare" :
                    ui_concatenare_obiect(lista, lista_specificatii_comanda)

                elif lista_specificatii_comanda[0] == "Show all" :
                    show_all(lista)

                elif lista_specificatii_comanda [0] == "x" :
                    break

                else:
                    print("Nu ati introdus o comanda valida!"
                          "Reincarcati.")







