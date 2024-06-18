import sqlite3


class connect():
    def __init__(self): 
        pass   
    
    def connect_db(self):
        self.conn = sqlite3.connect('Users.db')
        self.cursor = self.conn.cursor()
        print('conectando ao banco de dados')
        
    def disconnect_db (self):
        self.conn.close()
        print('disconectado do banco de dados')
    
    # posteriormente vou criar um nome para a carteira 
        #possibilidade  de criar mais de uma wallet
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