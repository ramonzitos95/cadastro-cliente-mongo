import PySimpleGUI as sg

def create_customer_window(): 
    botoes = [
        sg.Button('Cadastrar'), 
        sg.Button('Cancelar'),
        sg.Button('Listar')
    ]
    layout = [
        #[sg.Text('Id:', size=(15, 1)), sg.InputText(key='_id')],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText(key='nome')],
        [sg.Text('Email:', size=(15, 1)), sg.InputText(key='email')],
        [sg.Text('Telefone:', size=(15, 1)), sg.InputText(key='telefone')],
        [botoes]
    ]
    
    return sg.Window('Cadastro de cliente', layout, finalize=True)