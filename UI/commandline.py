from Domain.rezervare import toString
from Logic.crud import stergeRezervare, adaugaRezervare

def meniu(lista):
    print("Comenzile introduse trebuie separate prin ; acestea putand fi: \n"
                  "Adaugare: add,id,titlu,gen,pret,tip reducere \n"
                  "Stergere: delete,id-ul cartii de sters \n"
                  "Afisare: showall \n"
                  "Atentie !!! Comenzile trebuie introduse exact ca in modelul de mai sus !")


def commandLine(lista):
    while True:
        meniu(lista)
        rezervari= input("Dati comenzile: ").split(";")
        for i in range(len(rezervari)):
            rezervare= rezervari[i].split(",")
            if rezervare[0] == 'add':
                try:
                    lista= adaugaRezervare(rezervare[1], rezervare[2], rezervare[3], rezervare[4], rezervare[5], lista)
                except Exception as e:
                    print("Eroare:", e)
            elif rezervare[0] == 'delete':
                try:
                    lista= stergeRezervare(rezervare[1],lista)
                except ValueError as ve:
                    print("Eroare:", ve)
            elif rezervare[0] == 'showall':
                for rez in lista:
                    print(toString(rez))
            elif rezervare[0] == 'help':
                meniu(lista)
            elif rezervare[0] == 'iesire':
                break
            else:
                print("Reincercati! Comanda gresita!")