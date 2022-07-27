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
    """
    {
        "cep": "89010025",
        "state": "SC",
        "city": "Blumenau",
        "neighborhood": "Centro",
        "street": "Rua Doutor Luiz de Freitas Melro",
        "service": "viacep"
    }
    """
    def __init__(self, cep, state, city, neighborhood, street, service):
        self.cep = cep
        self.state = state
        self.city = city
        self.neighborhood = neighborhood
        self.street = street
        self.service = service
    
    def print(self):
        print(f'CEP: {self.cep}\n \
            Estado: {self.state}\n \
            Cidade: {self.city}\n \
            Região: {self.neighborhood}\n\
            Rua: {self.street}\n \
            Serviço: {self.service}')