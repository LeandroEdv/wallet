import connect

class call():
    
    def __init__(self, name, phone):
        self.pessoa = connect.pessoa(name)
        self.phone = phone
        
    def ligarPara(self):
        return f'{self.pessoa.apresentar()} meu telefone é: {self.phone}'
    
    

ligar = call('leandro', '1234')
print(ligar.ligarPara())