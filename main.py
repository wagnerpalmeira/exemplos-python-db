import sqlite3
from functions.usuario_db import cadastrar_usuario, listar_usuarios, autenticar

conn = sqlite3.connect('aula_database') 
c = conn.cursor()

opc = 0

def main():
    global opc
    while(opc != 4):
        print("1 - Inserir novo usuário\n2-Listar Usuarios\n3 - Autenticar\n4-Deletar\n5 - Buscar Usuario\n6 - Sair do Sistema")
        opc = int(input("Digite a opção: "))
        
        if opc == 1:
            nome = input("Digite o novo usuário: ")
            senha = input("Digite a nova senha: ")
            cadastrar_usuario(conn, nome, senha)
        elif opc == 2:
            usuarios = listar_usuarios(conn)
            print(usuarios)
        elif opc == 3:
            usuario = input("Digite usuario: ")
            senha = input("Digite senha: ")
            usuario_autenticado = autenticar(conn, 
                                             usuario,                         senha)
            print(len(usuario_autenticado) > 0)
        elif opc == 4:
            id = int(input('Digite id para deletar: '))
            sql = 'delete from usuarios where usuario_id=?'
            cursor = conn.cursor()
            cursor.execute(sql, [id])
            conn.commit()
        elif opc == 5:
            busca_nome = input("Digite nome para buscar: ")
            sql = 'select * from usuarios where usuario_name LIKE ?'
            cursor = conn.cursor()
            cursor.execute(sql, [f'%{busca_nome}%'])
            usuarios = cursor.fetchall()
            print(usuarios)
        elif opc == 6:
            break

main()