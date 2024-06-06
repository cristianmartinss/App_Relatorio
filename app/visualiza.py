import flet as ft
import datetime
import os
from banco import lista_datas, busca_registro, deleta_registro

def view(page):

    def delete_item(e: ft.ControlEvent):
        registro_id = e.control.data
        deleta_registro(registro_id)
        atualiza_interface(registro_id)
            
    def atualiza_interface(registro_id):
        for exp in l3.controls:
            new_content = []
            skip_next = False  
            for row in exp.content.controls:
                if skip_next:
                    skip_next = False
                    continue
                if isinstance(row, ft.Row) and any(
                    isinstance(grandchild, ft.IconButton) and grandchild.data == registro_id
                    for grandchild in row.controls
                ):
                    skip_next = True
                    continue
                new_content.append(row)
            exp.content.controls = new_content
        page.update()  

    def sla():
        l3 = ft.ExpansionPanelList(divider_color=ft.colors.BLACK)
        for data in lista_datas(): 
            exp_content = []  
            exp = ft.ExpansionPanel(header= ft.ListTile(
                            title=ft.Text(f"Relatório Dia {data}", size=30),
                                dense=True,))
            for dia in busca_registro(data):
                x = dia[3]
                pasta = datetime.datetime.strftime(x, '%d-%m-%y')
                arquivo = dia[2]
                image_path = os.path.join('E:', 'Fotos', pasta, f"{arquivo}.jpg")
                linha = ft.Text(
                    value=f"{dia[1]} - {dia[4]}",
                        text_align=ft.TextAlign.START,
                            max_lines=2,
                                size=25,)
                botao1 = ft.IconButton(
                    icon=ft.icons.DELETE, 
                        on_click=delete_item, 
                            data=dia[0]
                )
                exp_content.append(ft.Row([linha, botao1]))
                exp_content.append(
                    ft.Image(
                        src=image_path,
                            fit=ft.ImageFit.FILL,
                                width=1000,
                                    height=400,
                                        filter_quality=ft.FilterQuality.HIGH))
            exp.content =ft.Column(exp_content)
            l3.controls.append(exp)
        return l3
    l3 = sla()
    return l3
