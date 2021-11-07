from Logic.crud import adaugaRezervare
from Tests.testALL import alltests
from UI.console import runMenu


def main():
    alltests()
    lista= adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [])
    lista= adaugaRezervare('2', 'Claudiu', 'business', 202, 'Nu', lista)
    lista = adaugaRezervare('3', 'Claudiu', 'economy', 100, 'Da', lista)
    lista = adaugaRezervare('4', 'Alex', 'economy plus', 50, 'Da', lista)
    lista = adaugaRezervare('5', 'Pop', 'economy', 170, 'Da', lista)
    runMenu(lista)

main()