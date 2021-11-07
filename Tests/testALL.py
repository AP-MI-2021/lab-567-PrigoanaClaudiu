from Tests.testCrud import testAdaugaRezervare, testStergeRezervare, testClasaSuperioara
from Tests.testDomain import testDomain


def alltests():
    testDomain()
    testAdaugaRezervare()
    testStergeRezervare()
    testClasaSuperioara()