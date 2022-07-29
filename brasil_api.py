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
    url = f"{URL}cep/v1/{cep}"
    resp = api(url)
    
    if 'neighborhood' in resp and 'street' in resp:
        cp = Cep(resp['cep'],resp['state'],resp['city'],resp['neighborhood'],resp['street'],resp['service'])  
    else: 
        cp = Cep(resp['cep'],resp['state'],resp['city'],'Não tem','Não tem',resp['service'])
    
    """if 'neighborhood' not in resp:
        cp = Cep(resp['cep'],resp['state'],resp['city'],'Não tem',resp['street'],resp['service'])
    
    elif 'street' not in resp:
        cp = Cep(resp['cep'],resp['state'],resp['city'],resp['neighborhood'],'Não tem',resp['service'])"""
    
    return cp
    
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