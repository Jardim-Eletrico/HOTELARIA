from dao import Database

'''
|===================================================|
|                    |HOSPEDE|                      |
|===================================================|
'''

class Hospede:
    def __init__(self):
        self.db = Database()

    def add_hospede(self, nome, email, telefone, cpf):
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
        query = f"UPDATE hospedes SET nome='{nome}', email='{email}', telefone='{telefone}', cpf='{cpf}' WHERE id = {id}"
        
        self.db.execute_query(query)
        self.db.disconnect()

    def delete_hospede(self, id):
        #EXCLUIR HOSPEDE
        self.db.connect()
        query = f"DELETE FROM hospedes WHERE id = {id}"
        
        self.db.execute_query(query)
        self.db.disconnect()
'''
|===================================================|
|                    |QUARTO|                       |
|===================================================|
'''
class Quarto:
    def __init__(self):
        self.db = Database()

    def add_quarto(self, numero, tipo, valor_diaria, status):
        #INSERIR NOVO QUARTO

        query = f"INSERT INTO quartos (numero, tipo, valor_diaria, status) VALUES ('{numero}', '{tipo}', {valor_diaria}, '{status}')"
        self.db.connect()
        cursor = self.db.execute_query(query)
        self.db.disconnect()
        return cursor.lastrowid
    
    def consulta_quartos(self):
        #LISTA TODOS OS QUARTOS

        self.db.connect()
        query = "SELECT * FROM quartos ORDER BY numero"
        quartos = self.db.fetch_all(query)
        self.db.disconnect()
        return quartos
    
    def consulta_quartos_id(self, id):
        #CONSULTA UM QUARTO VIA ID

        self.db.connect()
        query = f"SELECT * FROM quartos WHERE id = {id}"
        quarto = self.db.fetch_one(query)
        self.db.disconnect()
        return quarto
    
    def update_quarto(self, id, numero, tipo, valor_diaria, status):
        #ATUALIZA AS INFORMAÇÕES DE UM QUARTO

        self.db.connect()
        query = f"UPDATE quartos SET numero='{numero}', tipo='{tipo}', valor_diaria={valor_diaria}, status='{status}' WHERE id={id}"
        quarto = self.db.execute_query(query)
        self.db.disconnect()
        return quarto
    
    def delete_quarto(self, id):
        #EXCLUIR HOSPEDE
        self.db.connect()
        query = f"DELETE FROM quartos WHERE id = {id}"
        
        self.db.execute_query(query)
        self.db.disconnect()
'''
|===================================================|
|                    |RESERVAS|                     |
|===================================================|
'''

class Reserva:
    def __init__(self):
        self.db = Database()

    def add_reserva(self, hospede_id, quarto_id, data_entrada, data_saida):
        if data_entrada >= data_saida:
            raise ValueError("A data de saída deve ser maior que a de entrada")
        
        quarto = Quarto()
        quarto_info = quarto.consulta_quartos_id(quarto_id)
        if not quarto_info or quarto_info["status"] != "disponivel":
            raise ValueError("O quarto não está disponível para reserva")
        
        
        query = f"INSERT INTO reservas (hospede_id, quarto_id, data_entrada, data_saida) VALUES ({hospede_id}, {quarto_id}, '{data_entrada}', '{data_saida}')"
        self.db.connect()
        cursor = self.db.execute_query(query)
        
        self.db.execute_query(f"UPDATE quartos set status='ocupado' WHERE id={quarto_id}")
        self.db.disconnect()
        return cursor.lastrowid
    
    def consulta_reservas(self):
        self.db.connect()
        query = """
            SELECT r.*, 
                h.nome as hospede_nome, 
                q.numero as quarto_numero
            FROM reservas r
            JOIN hospedes h ON r.hospede_id = h.id
            JOIN quartos q ON r.quarto_id = q.id
            ORDER BY r.id
        """
        reservas = self.db.fetch_all(query)
        self.db.disconnect()
        return reservas