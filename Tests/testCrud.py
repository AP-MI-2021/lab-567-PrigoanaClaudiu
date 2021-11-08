from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin, creeazaRezervare
from Logic.Ieftinire import IeftinirePret
from Logic.cerinte import pretMaxim
from Logic.clasaSuperioara import UpgradeClasa
from Logic.crud import adaugaRezervare, getById, stergeRezervare, modificaRezervare


def testAdaugaRezervare():
    '''testeaza daca aduga o rezervare'''
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [])
    assert getId(getById("1", lista)) == '1'
    assert getNume(getById("1", lista)) == "Prigoana"
    assert getClasa(getById("1", lista)) == 'economy'
    assert getPret(getById("1", lista)) == 200
    assert getCheckin(getById("1", lista)) == "Da"


def testStergeRezervare():
    '''testeaza daca sterge o rezervare'''
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [])
    lista = adaugaRezervare('2', 'Claudiu', 'economy', 200, 'Nu', lista)
    lista = stergeRezervare('1', lista)
    assert len(lista) == 1
    assert getById('1',lista) is None
    lista = stergeRezervare('3', lista)
    assert len(lista) == 1
    assert getById('2', lista) is not None


def testgetById():
    '''testeaza daca gaseste o anumita rezervare'''
    lista= adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [])
    assert getById('1',lista) is not None


def testModificare():
    '''testeaza daca modifica corect o rezervare'''
    lista=adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [])
    lista= modificaRezervare('1', 'Prigoana', 'economy plus', 250, 'Nu', lista)
    assert getId(getById("1", lista)) == '1'
    assert getNume(getById("1", lista)) == "Prigoana"
    assert getClasa(getById("1", lista)) == 'economy plus'
    assert getPret(getById("1", lista)) == 250
    assert getCheckin(getById("1", lista)) == "Nu"


def testClasaSuperioara():
    '''testeaza daca upgradeaza corect o clasa'''
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [])
    rezervare1= creeazaRezervare('1', 'Prigoana', 'economy plus', 200, 'Da')
    lista= UpgradeClasa(lista,'Prigoana')
    assert rezervare1 in lista


def testIeftinereProcent():
    '''testeaza daca ieftineste corect cu un procent'''
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [])
    rezervare1= creeazaRezervare('1', 'Prigoana', 'economy', 180, 'Da')
    lista= IeftinirePret(lista,10)
    assert rezervare1 in lista


def testPretMaxim():
    '''testeaza daca gaseste corect preturile maxime al fiecarei clase'''
    lista = adaugaRezervare('1', 'Prigoana', 'economy', 200, 'Da', [])
    lista = adaugaRezervare('2', 'Claudiu', 'business', 250, 'Nu', lista)
    lista = adaugaRezervare('3', 'Claudiu', 'economy', 100, 'Da', lista)
    lista = adaugaRezervare('4', 'Alex', 'economy plus', 50, 'Da', lista)
    lista = adaugaRezervare('5', 'Pop', 'economy', 220, 'Da', lista)
    assert pretMaxim(lista)== {'economy': 220, 'business': 250, 'economy plus': 50}
