#%%
from pymongo import MongoClient, errors
from bson.objectid import ObjectId
from bson import errors as b_errors

#%%
def conectar():
    """
    Função para conectar ao servidor
    """

    #conn = MongoClient('177.45.159.125', 27017)
    conn = MongoClient("mongodb+srv://silasmongo:101090@cluster0.t1qlh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    return conn
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
    db = conn.pmongo

    try:
        if db.produtos.count_documents({}) > 0:
            produtos = db.produtos.find()
            print('Listando Produtos')
            print('-----------------')
            for produto in produtos:
                print(f"ID: {produto['_id']}")
                print(f"Produto: {produto['nome']}")
                print(f"Preço: {produto['preco']}")
                print(f"Estoque: {produto['estoque']}")
                print('-----------------\n')
        else:
            print('Não existe produtos cadastrados')
    except errors.PyMongoError as e:
        print(f'Erro ao acessar o banco de dados: {e}')
    desconectar(conn)
    
#%%
def inserir():
    """
    Função para inserir um produto
    """  
    

    conn = conectar()
    db = conn.pmongo

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe o estoque do produto: \n'))

    try: 
        db.produtos.insert_one(
            {
                "nome":nome,
                "preco":preco,
                "estoque":estoque,                
            }
        )
        print(f'O produto {nome} foi inserido com sucesso!!\n')
    except errors.PyMongoError as e:
        print(f'Não foi possivel inserir o produto. {e}')
    desconectar(conn)
        
#%%
def atualizar():
    """
    Função para atualizar um produto
    """
    

    conn = conectar()
    db = conn.pmongo

    _id = input('Informe o ID do produto: ')
    try:
        if db.produtos.count_documents({}) > 0:
            {"_id": ObjectId(_id)}
        try:
        
            if db.produtos.count_documents({}) > 0:
                nome = input('Informe o novo nome do produto: ')
                preco = float(input('Informe o novo preço do produto: '))
                estoque = int(input('Informe o estoque de produtos: '))
                res = db.produtos.update_one (
                    {"_id": ObjectId(_id)},
                    {
                        "$set": {
                            "nome":nome,
                            "preco":preco,
                            "estoque":estoque
                        }
                    }
                )
                if res.modified_count == 1:
                    print(f'O produto {nome} foi atualizado com sucesso!\n')
                else:
                    print(f'Não foi possivel atualizar o produto\n')
            else:
                print('Não existem documentos para serem atualizados!')
        except errors.PyMongoError as e:
            print(f'Erro ao acessar o banco de dados: {e}\n ')  
    
    except b_errors.InvalidId as f:
        print(f'ID inválido. {f}\n')
    desconectar(conn)
    


#%%
def deletar():
    """
    Função para deletar um produto
    """  
    

    conn = conectar()
    db = conn.pmongo

    
    _id = input('Informe o ID do produto: ')
    try:
        if db.produtos.count_documents({}) > 0:
            {"_id": ObjectId(_id)}

        try:
            if db.produtos.count_documents({}) > 0:
                res = db.produtos.delete_one(
                    {
                        "_id": ObjectId(_id)
                    }
                )
                if res.deleted_count > 0:
                    print('Produto deletado com sucesso\n')
                else:
                    print('Não foi possível deletar o produto\n')
            else:
                print('Não existem produtos a serem deletados\n')
        except errors.PyMongoError as e:
            print(f'Erro ao acessar o banco de dados: {e} \n')
    except b_errors.InvalidId as f:
        print(f'ID inválido. {f}\n')
    
    desconectar(conn)


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
        print('5 - Sair\n')
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
        
        elif opcao == 5:
            validador = 0
            break
        else:
            print('Opção inválida')
            validador = int(input('Digite [1] para continuar ou [Qualquer tecla] para sair! \n'))
        validador = int(input('Digite [1] para realizar uma nova transação ou [Qualquer tecla] para sair! \n'))