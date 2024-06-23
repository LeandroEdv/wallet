import sqlite3 as sql
#
# Classe Criada para realizar as operações no banco de dados
#
class connect:
    def __init__(self):
       pass 
   
    def connect_db(self):
        try:
            self.conn = sql.connect('dataBase.db')
            self.cursor = self.conn.cursor()
        except:
            print('Falha na conexão com o Banco de Dados')
        else:
            print('Banco de dados Conectado com sucesso')
               
    def disconnect_db(self):
        self.cursor.close()
        self.conn.close()
        print('Banco de dados desconectado')
        
    def createTable_db(self):
        # Posteriormente inserir a data da compra !
        self.connect_db()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS wallet (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                stockName Text,
                                price REAL NOT NULL,
                                amount INTREGER NOT NULL ) ''') 
        self.conn.commit()
        self.disconnect_db()
        
 # Inserindo dados na tabela       
    def insert_db(self, name, price, amount):
        
        self.connect_db()
        try:
            self.cursor.execute('''INSERT INTO wallet 
                                (stockName, price, amount)
                                VALUES (?, ?, ?)''',( name, price, amount,))
        except sql.Error:
            print(f'Erro ao inserir dados')
            self.disconnect_db()
        else:
            self.conn.commit()
            print(f'Dados inseridos com sucesso')
            self.disconnect_db()
    #
    # mostra todoas os resultados dentro da tabela
    # 
    def showAll_db(self):
        self.connect_db()
        self.cursor.execute('''SELECT * FROM wallet''')
        allData = self.cursor.fetchall()
        for row in allData:
            print(row)
        #return self.allData
    
    # Mostra o nome das açoes sem repetir, servirá para buscas mais complexas !
    def showNames_db(self):
        self.connect_db()
        self.cursor.execute('''SELECT DISTINCT stockName FROM wallet''')
        Data = self.cursor.fetchall()
        for row in Data:
            print(row)
            
    # função para retornar o consolidaddo das açoes da carteira
    def show(self):
        # essa função repetida deve ser retirada na proxima atualização
        self.connect_db()
        
        self.cursor.execute('''SELECT DISTINCT stockName FROM wallet''')
        Data = self.cursor.fetchall()
        #
        for row in Data:
            x = row[0]
            print(x)
            self.cursor.execute(f'''SELECT stockName, SUM(price), SUM(amount) FROM wallet WHERE stockName = '{x}' ''')       
            queryResult = self.cursor.fetchall()
            
            print(queryResult)

comu = connect()
#comu.createTable_db()  
comu.insert_db('knri',13,100)
comu.showAll_db()
#comu.showNames_db()
comu.show()