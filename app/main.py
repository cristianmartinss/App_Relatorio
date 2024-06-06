import flet as ft
from banco import lista
from cadastro import cadastro
from relat import test
from visualiza import view
def main(page: ft.Page):
    page.window_min_height = 734
    page.window_min_width = 734
    page.spacing = 50
    def on_tab_change(event):
        selected_index = event.control.selected_index
        if selected_index == 2:
            page.scroll = True
            t.tabs[2].content = (view(page))
        else: page.scroll = False
        page.update()
    page.bgcolor = ft.colors.WHITE
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLACK))
    page.update()

    def Valor_Drop():
        x = []
        for i in lista():
            i = tuple(str(s).replace("'", " ") for s in i)
            x.append(i)
        if x:
            if len(x) > 1:
                x = ["".join(s) for s in x]
                return x        
            else:
                x = x[0]
                return x    
    def Drop_Montado():
        x = Valor_Drop()
        if x:
            ocorrencias = ft.Dropdown(options=[ft.dropdown.Option(valor) for valor in x], label='Insira a Ocorrência')
            return ocorrencias
        else: return ft.Dropdown(options=[], label='Insira a Ocorrência')  # Dropdown vazio
    x = Drop_Montado()
    a = Valor_Drop()

    t = ft.Tabs(
        selected_index=0,
            animation_duration=300,
                tabs=[
                    ft.Tab(
                        text="Criar Relatório",
                        icon=ft.icons.EDIT,
                        content=ft.Container(content=test(page,x),padding=ft.padding.all(15)),
                    ),
                    ft.Tab(
                        text="Gerenciar Ocorrências",
                        icon=ft.icons.SEARCH,
                        content=ft.Container(content=cadastro(page,x,a), alignment=ft.alignment.top_left, padding=ft.padding.all(15))
                    ),
                    ft.Tab(
                        text="Visualizar Relatórios",
                        icon=ft.icons.REMOVE_RED_EYE_OUTLINED,
                        content=ft.Container(content=view(page)),
                    ),
                ],
                    expand=1,
                        unselected_label_color=ft.colors.BLACK26,
                            on_change=on_tab_change)
    page.add(t)

ft.app(target=main)
