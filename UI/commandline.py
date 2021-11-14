from Domain.rezervare import toString
from Logic.crud import stergeRezervare, adaugaRezervare


def commandLine(lista):
    m = input("Da lista de operatii pe care vrei sa le faca programul"
              "(operatii posibile : add, showall, delete, despartite prin ;, in "
              "cadrul comenzii itemele trebuie despartite doar prin virgula, fara spatii albe:")
    lst2 = (m.split(";"))
    map_object = map(str, lst2)
    lst = list(map_object)
    for i in lst:
        lst2 = (i.split(","))
        map_object = map(str, lst2)
        lst3 = list(map_object)
        if lst3[0]=='add':
            lista=adaugare2(lista, lst3)
        elif lst3[0]=='showall':
            for rezervare in lista:
                print(toString(rezervare))
        elif lst3[0]=='delete':
            lista=stergere2(lista, lst3)
    return lista

def stergere2(lista,lst3):
                """
                sterge o rezervare dorita
                :param lista: rezervarile actuale
                :return: rezervarile dupa stergere
                """
                try:
                    id_sters = int(lst3[1])
                    lista = stergeRezervare(id_sters,lista)
                    print("Stergerea a fost efectuata cu succes.")
                    return lista
                except ValueError as ve:
                    print('Eroare:', ve)
                return lista

def adaugare2(lista,lst3):
                """
                adauga in lista o rezervare noua
                :return: lista cu rezervarea adaugata
                """
                try:
                    id = int(lst3[1])
                    nume = lst3[2]
                    clasa = lst3[3]
                    pret = int(lst3[4])
                    checkin = lst3[5]
                    if clasa not in ['economy', 'economy plus', 'business']:
                        raise ValueError(
                            f"Singurele varinate de clase acceptate sunt:economy, economy plus si business")
                    if checkin not in ['Da', 'Nu']:
                        raise ValueError(f'Singurele varinate de checkin acceptate sunt : Da sau Nu')
                    print('Adaugarea a fost inregistrata.')
                    return adaugaRezervare(id, nume, clasa, pret,
                                  checkin, lista)
                except ValueError as ve:
                    print("Eroarea:", ve)
                return lista