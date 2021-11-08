from Domain.rezervare import getClasa, getPret


def pretMaxim(lista):
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