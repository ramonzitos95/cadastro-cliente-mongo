from conexaomongo.conexao import clientdb

db = clientdb['clientes']
clientes_collection = db['cliente']

# Função para inserir um cliente
def inserir_cliente(cliente):
    clientes_collection.insert_one(cliente)

# Função para buscar todos os clientes
def buscar_todos_clientes():
    return list(clientes_collection.find())

# Função para buscar um cliente por ID
def buscar_cliente_por_id(cliente_id):
    return clientes_collection.find_one({'_id': cliente_id})

# Função para atualizar um cliente por ID
def atualizar_cliente(cliente_id, novos_dados):
    clientes_collection.update_one({'_id': cliente_id}, {'$set': novos_dados})

# Função para excluir um cliente por ID
def excluir_cliente(cliente_id):
    clientes_collection.delete_one({'_id': cliente_id})