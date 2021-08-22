#%%
import MySQLdb

#%%
def conectar():
    """
    Função para conectar ao servidor
    """


    try:
        conn = MySQLdb.connect (
            db='pmysql',
            host='127.0.0.1',
            user='root',
            passwd=''
        ) 
        return conn
    except MySQLdb.Error as e:
        print(f'Erro na conexão ao MySQL server {e}')


#%%
def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()

#%%
def listar():
    """
    Função para listar os produtos
    """


    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando Produtos...')
        print('--------------------')
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'Nome: {produto[1]}')
            print(f'Preço: {produto[2]}')
            print(f'Estoque: {produto[3]}')
            print('--------------------\n\n')
    else: 
        print('Não existem produtos cadastrados \n\n')
    desconectar(conn)    

#%%
def inserir():
    """
    Função para inserir um produto
    """  
    

    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe a quantidade em estoque: '))

    cursor.execute(f" INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso!\n\n')
    else:
        print('Não foi possível inserir o produto\n\n')
    desconectar(conn)


#%%
def atualizar():
    """
    Função para atualizar um produto
    """

    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto a ser atualizado: '))
    nome = input('Informe o novo nome do produto: ')
    preco = float(input('Informe o novo preço do produto: '))
    estoque = int (input('Digite a nova quantidade em estoque: '))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi atualizado com sucesso!\n\n')
    else:
        print(f'Erro ao atualizar o produto!\n\n')
    desconectar(conn)


#%%
def deletar():
    """
    Função para deletar um produto
    """  


    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto a ser deletado: '))
    cursor.execute(f'DELETE FROM produtos WHERE id={codigo}')
    conn.commit()

    if cursor.rowcount == 1:
        print('Produto excluído com sucesso!\n\n')
    else:
        print(f'Não foi possível deletar o produto código {codigo}\n\n')

#%%
def menu():
    """
    Função para gerar o menu inicial
    """


    validador = 1
    while validador == 1:
        print('=========Gerenciamento de Produtos==============')
        print('Selecione uma opção: ')
        print('1 - Listar produtos.')
        print('2 - Inserir produtos.')
        print('3 - Atualizar produto.')
        print('4 - Deletar produto.')
        print('5 - Sair')
        opcao = int(input())
        if opcao in [1, 2, 3, 4]:
            if opcao == 1:
                listar()
            elif opcao == 2:
                inserir()
            elif opcao == 3:
                atualizar()
            elif opcao == 4:
                deletar()
            else:
                print('Opção inválida')
        if opcao == 5:
            validador = 0
            break
        else:
            print('Opção inválida')
            validador = int(input('Digite [1] para continuar ou [Qualquer tecla] para sair! \n'))
                