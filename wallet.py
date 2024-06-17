import sqlite3

class stock:
    def __init__(self, ticker, price, amount, data):
        self.ticker = ticker
        self.price = price
        self.amount = amount
        self.data = data
        #self.totalPrice = total()
        
      # função para adicionar ao preço os custos de corretagem, emolumentos e outros   
    def total(self, brokerage,emoluments, liquidation):
        # se o usuario deixar zero,vamos admitir o valor padrão dos custos
        if liquidation == 0: liquidation = 0.44
        if emoluments == 0: emoluments = 0.67
        totalPrice = (self.price + (brokerage + emoluments) + liquidation ) * self.amount
        return totalPrice
        self.totalPrice = totalPrice
        
class connect():
    def __init__(self):
        # posteriormente vou criar um nome para a carteira 
        #possibilidade  de criar mais de uma wallet
        pass   
    
    def connect_db(self):
        self.conn = sqlite3.connect('Users.db')
        self.cursor = self.conn.cursor()
        print('conectando ao banco de dados')
        
    def disconnect_db (self):
        self.conn.close()
        print('disconectado do banco de dados')
    
    def create_table(self):
        self.connect_db()
        self.cursor.execute('''CREATE TABLE IF NOT EXITES wallet (id INTRIGER PRIMARY KEY AUTOINCREMENT,
                            ticker TEXT NOT NULL,
                            price REAL NOT NULL,
                            amount INTREGER,
                            data TEXT
                            )''')
        self.conn.commit()
        print('tabela Criada')
        self.disconnect_db()
    
    def inset_tabel(self, ticker, price, amount, data):
        self.connect_db()
        self.cursor.execute('''INSERT INTO wallet VALUES(?, ?, ?, ?)'''),(ticker, price, amount, data)
        self.conn.commit()
        print('tabela atualizada')
        self.disconnect_db()
    
class Wallet ():
    def __init__(self, stock):
        self.stock = stock

    def save(self):
        pass
    def atualize(self):
        pass 
        
    
    
hglg = stock('hglg11',160, 10, '10-12-21')
print(hglg.total(0,0,0))
print(hglg.amount)