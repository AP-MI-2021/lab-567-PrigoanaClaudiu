from Domain.rezervare import getClasa, getPret, getNume


def pretMaxim(lista,undoList,redoList):
    '''
    afla pretul maxim pentru fiecare clasa
    :param lista: lista de rezervari
    :return: returneaza un dictionar cu preturile maxime
    '''
    preturi= {}
    for rezervare in lista:
        clasa=getClasa(rezervare)
        pret=getPret(rezervare)
        if clasa in preturi:
            if pret > preturi[clasa]:
                preturi[clasa]=pret
        else:
                preturi[clasa]=pret
    return preturi


def ordo(lista,undoList, redoList):
    '''ordoneaza rezervarile descresc dupa pret'''
    undoList.append(lista)
    redoList.clear()
    return sorted(lista, key=lambda rezervare: getPret(rezervare), reverse=1)


def sumaFiecareNume(lista):
    '''afiseaza suma preturilor fiecarui nume'''
    for rezervare in lista:
        numele = getNume(rezervare)
        s=0
        for rezervare in lista:
            if numele == getNume(rezervare):
                s=getPret(rezervare) + s
        print(f"{numele}: {s}")

