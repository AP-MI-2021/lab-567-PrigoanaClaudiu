from Domain.rezervare import toString
from Logic.Ieftinire import IeftinirePret
from Logic.cerinte import pretMaxim
from Logic.clasaSuperioara import UpgradeClasa
from Logic.crud import adaugaRezervare, modificaRezervare, stergeRezervare


def printMenu():
    '''
    meniul afisat
    '''
    print("1.Adauga, sterge sau modifica o rezervare.")
    print("2.Trecerea la o clasa superioara a unui client, dupa nume.")
    print("3.Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("4.Determinarea prețului maxim pentru fiecare clasă.")

    print("a.Afiseaza toate rezervarile.")
    print("x.Iesire.")


def uiAdaugaRezervare(lista):
    '''
    adauga o rezervare
    :param lista: lista de rezervari
    '''
    id=input('Dati id-ul: ')
    nume=input("Dati numele: ")
    clasa=input("Dati clasa: ")
    pret=float(input("Dati pretul: "))
    checkin=input("S-a facut checkin-ul? Da/Nu: ")
    return adaugaRezervare(id,nume,clasa,pret,checkin,lista)


def uiStergeRezervare(lista):
    '''
    sterge o rezervare
    :param lista: lista de rezervari
    '''
    id=input("Dati id-ul rezervarii ce trebuie sterse: ")
    return stergeRezervare(id,lista)


def uiModificaRezervare(lista):
    '''
    modifica o rezervare
    :param lista: lista de rezervari
    '''
    id = input('Dati id-ul rezervarii de modificat: ')
    nume = input("Dati numele nou: ")
    clasa = input("Dati noua clasa: ")
    pret = float(input("Dati noul pret: "))
    checkin = input("S-a facut checkin-ul? Da/Nu: ")
    return modificaRezervare(id,nume,clasa,pret,checkin,lista)


def showAll(lista):
    '''
    afiseaza toate rezervarile facute
    :param lista: rezervarile facute
    '''
    for rezervare in lista:
        print(toString(rezervare))


def meniulDoi(lista):
    '''submeniul pentru optiunea 1'''
    while True:
        print('1.Adauga o rezervare.')
        print('2.Modifica o rezervare.')
        print('3.Sterge o rezervare.')
        print('4.Revenire la cealalta pagina de functionalitati.')
        print('a.Afiseaza lista de rezervari.')
        optiune=input('Alege optiunea: ')
        if optiune == '1':
            lista=uiAdaugaRezervare(lista)
        elif optiune == '2':
            lista = uiModificaRezervare(lista)
        elif optiune == '3':
            lista = uiStergeRezervare(lista)
        elif optiune == 'a':
            showAll(lista)
        elif optiune == '4':
            return lista


def runMenu(lista):
    while True:
        printMenu()
        optiune=input("Dati optiunea: ")
        if optiune == "1":
            lista= meniulDoi(lista)
        elif optiune == 'a':
            showAll(lista)
        elif optiune == '2':
            try:
                numele=input("Dati numele clientului: ")
                lista=UpgradeClasa(lista,numele)
                print("Upgrade-ul s-a realizat.")
            except ValueError as ve:
                print("Eroare", ve)
        elif optiune == '3':
            try:
                procent=float(input("Dati procentul cu care vreti sa se ieftineasca rezervarea:"))
                lista=IeftinirePret(lista,procent)
                print("Preturile au fost reduse.")
            except ValueError as vee:
                print("Eroare",vee)
        elif optiune == '4':
            print(pretMaxim(lista))

        elif optiune == 'x':
            break
        else:
            print("Optiune invalida. Reincercati.")
