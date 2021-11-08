from Tests.testCrud import testAdaugaRezervare, testStergeRezervare, testClasaSuperioara, testIeftinereProcent, \
    testgetById, testModificare
from Tests.testDomain import testDomain


def alltests():
    testDomain()
    testAdaugaRezervare()
    testStergeRezervare()
    testClasaSuperioara()
    testIeftinereProcent()
    testgetById()
    testModificare()