import os
import brasil_api
op = 0

    
def banks():
        os.system('cls')
        banks = brasil_api.getBanks()
        print('O tamanho da lista é: ', len(banks))
        for bank in banks:
            bank.print()
def cep(): 
        os.system('cls')
        print('::::::::::|Busca por CEP|::::::::::')
        cep = input('Digite o CEP: ')
        cep_lst = brasil_api.getCEP(cep)
        cep_lst.print()
        #print(cep_lst)    
def cnpj():
        os.system('cls')
        ('::::::::::|Busca por CNPJ|::::::::::')
        cnpj = input('Digite o CNPJ: ')
        cnpj_lst = brasil_api.getCNPJ(cnpj)
        for k, v in cnpj_lst.items():
            print(f"{k} : {v}")
    
def ddd():
        os.system('cls')
        print('::::::::::::|Lista de cidades por DDD|::::::::::::')
        ddd = input('Digite o DDD: ')
        ddd_lst = brasil_api.getDDD(ddd)
        print(f"Estado: {ddd_lst['state']}")
        print('Cidades:')
        for v in ddd_lst['cities']:
            print(v)
    
def feriados():
        os.system('cls')
        print(':::::::|Listar os feriados nacionais de determinado ano|:::::::')
        ano = input('Digite o ano: ')
        ano_lst = brasil_api.getFeriado(ano)
        print('-----------------------------------')
        for fer in ano_lst:
            print(f"Nome: {fer['name']}")
            print(f"Data: {fer['date']} - Tipo: {fer['type']}")
            print('-----------------------------------')

while op != 6:
    os.system('cls')
    print('::::::::::::::|Brasil API|::::::::::::::')
    print('[1] - Todos os bancos do Brasil\n[2] - Busca por CEP\n[3] - Busca por CNPJ')
    print('[4] - Lista de cidades por DDD\n[5] - Listar os feriados nacionais de determinado ano\n[6] - Sair')
    op = int(input('O que deseja fazer?: '))
    
    if op == 1:
        banks()
    if op == 2:
        cep()
    if op == 3:
        cnpj()
    if op == 4:
        ddd()
    if op == 5:
        feriados()
    
    input('Aperte ENTER para continuar')
    os.system('cls')
print('Obrigado por usar o sistema!')