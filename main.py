from frontend.clientegui import create_customer_window
import PySimpleGUI as sg
from repositorios.clienterepositorio import inserir_cliente, generate_fictitious_id


def main():
    window = create_customer_window()
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        
        elif event == 'Cadastrar':
            
            nome = values['nome']
            email = values['email']
            telefone = values['telefone']
            
            try:
                cliente = {
                    '_id': generate_fictitious_id(),
                    'nome': nome,
                    'email': email,
                    'telefone': telefone,
                }
                
                inserir_cliente(cliente)
                
            except Exception as e:
                print(f'Erro ao inserir cliente {nome} Erro: {e}')
            
            
            sg.popup(f'Cliente cadastrado com sucesso {nome}')
            
            window['nome'].update('')
            window['email'].update('')
            window['telefone'].update('')
            
    window.close()
    
if __name__ == '__main__':
    main()
            