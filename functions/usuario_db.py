def cadastrar_usuario(conexao, nome, senha):
    cursor = conexao.cursor()

    sql = f'INSERT INTO usuarios(usuario_name, usuario_senha) VALUES (?, ?)'
    cursor.execute(sql, [nome, senha])
    conexao.commit()
    
    return True

def listar_usuarios():
    pass