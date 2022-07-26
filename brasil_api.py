import httpx

URL = 'https://brasilapi.com.br/api/'

def banks():
    return api('https://brasilapi.com.br/api/banks/v1') 

def cep(cep:str):
    url = f"{URL}cep/v1/{cep}"
    data = api(url)
    return data
    
def cnpj(cnpj:str):
    url = f"{URL}cnpj/v1/{cnpj}"
    data = api(url)
    return data

def ddd(ddd:str):
    url = f"{URL}ddd/v1/{ddd}"
    data = api(url)
    return data

def feriado(fer_n:str):
    url = f"{URL}feriados/v1/{fer_n}"
    data = api(url)
    return data

def api(url):
    req = httpx.get(url)
    resp = req.json()
    return resp