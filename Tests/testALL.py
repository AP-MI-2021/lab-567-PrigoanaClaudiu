from Tests.testLogic import testAdaugaRezervare, testStergeRezervare, testClasaSuperioara, testIeftinereProcent, \
    testgetById, testModificare, testPretMaxim, testOrdo
from Tests.testDomain import testDomain


def alltests():
    testDomain()
    testAdaugaRezervare()
    testStergeRezervare()
    testClasaSuperioara()
    testIeftinereProcent()
    testgetById()
    testModificare()
    testPretMaxim()
    testOrdo()
