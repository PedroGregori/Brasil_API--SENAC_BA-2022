class Bank():
    """
    {
        "ispb": "00000000",
        "name": "BCO DO BRASIL S.A.",
        "code": 1,
        "fullName": "Banco do Brasil S.A."
    }
    """
    
    def __init__(self, ispb, name, code, fullName) -> None:
        """ Construtor da classe """
        self.ispb = ispb
        self.name = name
        self.code = code
        self.fullName = fullName

    def print(self):
        print(
            f"Nome: {self.name}, Code.: {self.code}")
    
class Cep():
    def __init__(self, cep, state, city, neighborhood, street, service):
        self.cep = cep
        self.state = state
        self.city = city
        self.neighborhood = neighborhood
        self.street = street
        self.service = service
    
    def print(self):
        print(f"CEP: {self.cep}")
        print(f"Estado: {self.state}")
        print(f"Cidade: {self.city}")
        print(f"Região: {self.neighborhood}")
        print(f"Rua: {self.street}")
        print(f"Serviço: {self.service}")
    
