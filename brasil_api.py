import httpx
from api_class import Bank, Cep

URL = 'https://brasilapi.com.br/api/'

def getBanks():
    l_banks = []
    resp = api('https://brasilapi.com.br/api/banks/v1')
    
    for b in resp:
        banks = Bank(b['ispb'], b['name'],b['code'],b['fullName'])
        l_banks.append(banks)
    return l_banks

def getCEP(cep:str):
    l_cep = []
    url = f"{URL}cep/v1/{cep}"
    resp = api(url)
    for c in resp:
        cp = Cep(c['cep'], c['state'], c['city'], c['neighborhood'], c['street'], c['service'])
        l_cep.append(cp)
    return l_cep
    
def getCNPJ(cnpj:str):
    url = f"{URL}cnpj/v1/{cnpj}"
    data = api(url)
    return data

def getDDD(ddd:str):
    url = f"{URL}ddd/v1/{ddd}"
    data = api(url)
    return data

def getFeriado(fer_n:str):
    url = f"{URL}feriados/v1/{fer_n}"
    data = api(url)
    return data

def api(url):
    req = httpx.get(url)
    resp = req.json()
    return resp