import flet as ft    
import json
import datetime
import shutil
import os
from banco import insert_registro


# Tela 1
# Alert Dialog
def open_dlg(page,message):
    dialog = ft.AlertDialog(
        title=ft.Text(value='Erro'),
        content=ft.Text(message),)
    page.dialog = dialog
    dialog.open = True
    page.update()

def test(page,ocorrencias):
    hoje = datetime.datetime.now()
    hora = hoje.strftime('%H:%M')



        # Armazena o caminho do arquivo selecionado
    def on_dialog_result(e: ft.FilePickerResultEvent):
        global path
        file_path = json.loads(e.data)
        path = file_path['files'][0]['path']
        print(path)

    def salva_foto(e):
        global path
        x = data_exec.value
        if not x:
           open_dlg(page,message='Preencha a Data.')
        else:
            data_obj = datetime.datetime.strptime(x, '%d-%m-%y')
            data_formatada = data_obj.strftime('%Y-%m-%d')
            print(data_exec, data_obj)
            nome = ocorrencias.value
            if nome:
                try:
                    server_path = f'\\\\ws-eng02\\e$\\Fotos\\{x}'
                    arq = os.path.splitext(os.path.basename(path))[0]
                    print(arq)
                    if not os.path.exists(server_path):
                        os.makedirs(server_path)  
                    shutil.copy(path, server_path)
                    print(type(hora))
                    insert_registro(nome, arq, data_formatada.__str__(), hora)
                    path = ''
                except Exception as e:
                    erro1 = "name 'path' is not defined"
                    erro2 = "name 'path' is not defined"
                    arg = e.args
                    x = e
                    print(arg)
                    if erro1 or erro2 in arg:
                        open_dlg(page,"Escolha uma Foto Para enviar")
                    else: open_dlg(page,e)
                        
            else:
                open_dlg(page,message='Preencha a Ocorrência.')
    style1 = ft.ButtonStyle(
    bgcolor={
        'hovered' : ft.colors.YELLOW_400,
        ''        : ft.colors.WHITE,
    },)
    style2 = ft.ButtonStyle(
    bgcolor={
        'hovered' : ft.colors.GREEN,
        ''        : ft.colors.WHITE,
        
    },)

    drop_text = ft.Text()
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)
    page.update()
    enviar_btn = ft.ElevatedButton(text="Enviar", icon=ft.icons.SAVE, on_click=salva_foto,style=style1,width=400,height=50)
    image_btn = ft.ElevatedButton(text="Buscar Imagem", icon=ft.icons.IMAGE, on_click=lambda _: file_picker.pick_files(()),style=style2,width=400,height=50,)
    data_exec = ft.TextField(label='Prencha a data no formato: DD-MM-YY', expand=True,max_length=8)
    r = ft.Row([enviar_btn,image_btn],alignment=ft.MainAxisAlignment.CENTER)
    l1 = ft.Column([ocorrencias, r, drop_text, data_exec],spacing=50,alignment=ft.alignment.center_right)
    return l1
