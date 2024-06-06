import flet as ft
from collections.abc import Iterable
from banco import insert_ocorrencia, remove_ocorrencia


def cadastro(page,ocorrencias,a):

    # Insert de ocorrência no banco
    def cadastra(e):
        x = input_cadastro.value
        insert_ocorrencia(x)
        input_cadastro.value = ""
        if not ocorrencias.options:  # Se o dropdown estiver vazio
            ocorrencias.options = [ft.dropdown.Option(x)]
        else:
            ocorrencias.options.append(ft.dropdown.Option(x))
        new_tile = cria_grid(x)
        grid_view.controls.append(new_tile)
        page.update()

    def deleta_ocorrencia(title):
        remove_ocorrencia(title)
        # Remove do dropdown
        ocorrencias.options = [option for option in ocorrencias.options if option.key != title]
        # Remove do GridView
        grid_view.controls = [control for control in grid_view.controls if control.title.value != title]
        page.update()
    
    def cria_grid(title):
        return ft.ListTile(
            leading=ft.Icon(ft.icons.DELETE),title=ft.Text(title),
                on_long_press=lambda _, title=title:deleta_ocorrencia(title),
                    selected=False,selected_color=ft.colors.AMBER)
    
    # Tela 2
    style = ft.ButtonStyle(bgcolor={
        'hovered' : ft.colors.GREEN,
        ''        : ft.colors.WHITE,},)
    
    insert_btn = ft.ElevatedButton(text='Enviar', on_click=cadastra,style=style)
    input_cadastro = ft.TextField(label='Insira a Ocorrência')
    l2 = ft.Row([input_cadastro, insert_btn], expand=False, vertical_alignment=ft.alignment.center_right)
    if a is not None and isinstance(a,Iterable):
        list_tiles = [cria_grid(item) for item in a] 
    else: list_tiles = []
    T1 = ft.Text('Cadastrar Ocorrência',size=20, weight=ft.FontWeight.W_500)
    T2 = ft.Text('Deletar Ocorrência',size=20, weight=ft.FontWeight.W_500)
    grid_view= ft.GridView(
        padding=0,child_aspect_ratio=20
       ,controls=list_tiles,aspect_ratio=2)

    l2_ = ft.Column([T1,l2,T2, grid_view])
    return l2_