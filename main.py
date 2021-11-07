from Logic.crud import adaugaRezervare
from Tests.testALL import alltests
from UI.console import runMenu


def main():
    alltests()
    lista= adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [])
    lista= adaugaRezervare('2', 'Claudiu', 'business', 202, 'Nu', lista)
    runMenu(lista)

main()