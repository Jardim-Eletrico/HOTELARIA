from dao import Database

class Hospede:
    def __init__(self):
        self.db = Database()

    def add(self, nome, email, telefone, cpf):
        #Inserir novo hóspede
        if not nome or len(nome) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres")
        if not cpf or len(cpf) < 11:
            raise ValueError("CPF inválido")
        
        query = f"INSERT INTO hospedes (nome, email, telefone, cpf) VALUES ('{nome}', '{email}', '{telefone}', '{cpf}')"
        self.db.connect()
        cursor = self.db.execute_query(query)
        self.db.disconnect()
        return cursor.lastrowid
    
    def consulta_hospedes(self):
        #LISTAR TODOS OS HÓSPEDES
        self.db.connect()
        query = "SELECT * FROM hospedes ORDER BY nome"
        hospedes = self.db.fetch_all(query)
        self.db.disconnect()
        return hospedes
    
    def consulta_hospede(self, id):
        #BUSCA O HÓSPEDE PELO ID
        self.db.connect()
        query = f"SELECT * FROM hospedes WHERE id = {id}"
        hospede = self.db.fetch_one(query)
        self.db.disconnect()
        return hospede
    
    def update_hospede(self, id, nome, email, telefone, cpf):
        #ATUALIZA AS INFORMAÇÕES DO HOSPEDE
        self.db.connect()
        query = f"UPDATE  hospedes SET nome='{nome}', email='{email}', telefone='{telefone}', cpf='{cpf}' WHERE id = {id}"
        
        self.db.execute_query(query)
        self.db.disconnect()

    def delete_hospede(self, id):
        #EXCLUIR HOSPEDE
        self.db.connect()
        query = f"DELETE FROM hospedes WHERE id = {id}"
        
        self.db.execute_query(query)
        self.db.disconnect()