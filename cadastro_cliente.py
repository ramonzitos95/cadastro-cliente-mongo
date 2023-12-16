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

# Exemplo de uso:
cliente1 = {'_id': 1, 'nome': 'Cliente A', 'email': 'cliente.a@email.com', 'telefone': '123456789'}
cliente2 = {'_id': 2, 'nome': 'Cliente B', 'email': 'cliente.b@email.com', 'telefone': '987654321'}

# Inserir clientes
inserir_cliente(cliente1)
inserir_cliente(cliente2)

# Buscar todos os clientes
todos_clientes = buscar_todos_clientes()
print("Todos os clientes:")
print(todos_clientes)

# Buscar cliente por ID
cliente_id_2 = 2
cliente_encontrado = buscar_cliente_por_id(cliente_id_2)
print(f"\nCliente com ID {cliente_id_2}:")
print(cliente_encontrado)

# Atualizar cliente
cliente_id_1 = 1
novos_dados_cliente1 = {'telefone': '999999999'}
atualizar_cliente(cliente_id_1, novos_dados_cliente1)
cliente_atualizado = buscar_cliente_por_id(cliente_id_1)
print(f"\nCliente atualizado com ID {cliente_id_1}:")
print(cliente_atualizado)

# Excluir cliente por ID
excluir_cliente(cliente_id_2)
print(f"\nCliente com ID {cliente_id_2} excluído.")

# Buscar todos os clientes novamente após exclusão
todos_clientes_apos_exclusao = buscar_todos_clientes()
print("\nTodos os clientes após exclusão:")
print(todos_clientes_apos_exclusao)

# Fechar conexão
clientdb.close()