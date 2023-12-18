from repositorios.clienterepositorio import atualizar_cliente, buscar_todos_clientes, atualizar_cliente, excluir_cliente, inserir_cliente, buscar_cliente_por_id, clientdb

# Exemplo de uso:
#cliente1 = {'_id': 1, 'nome': 'Cliente A', 'email': 'cliente.a@email.com', 'telefone': '123456789'}
#cliente2 = {'_id': 2, 'nome': 'Cliente B', 'email': 'cliente.b@email.com', 'telefone': '987654321'}
#cliente1 = {'_id': 3, 'nome': 'Cliente B', 'email': 'cliente.b@email.com', 'telefone': '987654321'}
#cliente2 = {'_id': 4, 'nome': 'Cliente B', 'email': 'cliente.b@email.com', 'telefone': '987654321'}
cliente1 = {'_id': 5, 'nome': 'João Alves', 'email': 'joao.b@email.com', 'telefone': '987654666'}
cliente2 = {'_id': 6, 'nome': 'Maria Renata', 'email': 'maria.b@email.com', 'telefone': '987654555'}

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