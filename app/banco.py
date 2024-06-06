import mysql.connector

def conectar_banco():
    config = {
        'host': 'srv-intra',
        'user': 'cristian',
        'password': 'Selit@85',
        'database': 'plms',
        'port': '3306',
    }
    conexao = mysql.connector.connect(**config)
    return conexao

def lista():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM OCORRENCIAS"
    cursor.execute(sql)
    resultados = cursor.fetchall()  # Obter os resultados da consulta
    conexao.commit()
    cursor.close()
    conexao.close()
    x = []
    for linha in resultados:
        x.append(linha)
    return resultados

def insert_ocorrencia(val):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    if val:
        sql = f"INSERT INTO OCORRENCIAS (Id) VALUES ('{val}')"
        cursor.execute(sql)
        conexao.commit()
        cursor.close()
        conexao.close()
        
def insert_registro(Id,Arquivo,Data, Hora):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    if id and Arquivo:
        sql = f"INSERT INTO REGISTROS (Evento, Arquivo, Data, Hora) VALUES ('{Id}', '{Arquivo}', '{Data}', '{Hora}')"
        cursor.execute(sql)
        conexao.commit()
        cursor.close()
        conexao.close()

def remove_ocorrencia(Valor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = f"DELETE FROM OCORRENCIAS WHERE id = '{Valor}'"
    cursor.execute(sql)
    conexao.commit()
    cursor.close()
    conexao.close()

def lista_datas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "SELECT DISTINCT(Data) FROM registros ORDER BY data asc"
    cursor.execute(sql)
    resultados = cursor.fetchall()  # Obter os resultados da consulta
    cursor.close()
    conexao.close()
    datas = [linha[0] for linha in resultados]
    return datas

def busca_registro(data):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = f"SELECT * FROM registros Where Data = '{data}'"
    cursor.execute(sql)
    resultados = cursor.fetchall()  # Obter os resultados da consulta
    return resultados


def busca_eventos(data):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = f"SELECT COUNT(Id) FROM registros Where Data = '{data}'"
    cursor.execute(sql)
    resultados = cursor.fetchone()  # Obter o resultado da consulta
    cursor.close()
    conexao.close()
    return resultados

def deleta_registro(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = f"DELETE FROM registros WHERE Id = '{id}'"
    print(sql)
    cursor.execute(sql)
    conexao.commit()
    cursor.close()
    conexao.close()

