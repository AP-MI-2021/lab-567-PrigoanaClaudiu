from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from Logic.crud import adaugaRezervare, getById, stergeRezervare


def testAdaugaRezervare():
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [])
    assert getId(getById("1", lista)) == '1'
    assert getNume(getById("1", lista)) == "Prigoana"
    assert getClasa(getById("1", lista)) == 'economy'
    assert getPret(getById("1", lista)) == 200
    assert getCheckin(getById("1", lista)) == "Da"


def testStergeRezervare():
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [])
    lista = adaugaRezervare('2', 'Claudiu', 'economy', 200, 'Nu', lista)
    lista = stergeRezervare('1', lista)
    assert len(lista) == 1
    assert getById('1',lista) is None
    lista = stergeRezervare('3', lista)
    assert len(lista) == 1
    assert getById('2', lista) is not None
