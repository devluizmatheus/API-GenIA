from pymongo import MongoClient

def conexao_banco():
    """Função de Conexão com o banco"""
    client = MongoClient("mongodb://localhost:27017/")
    db = client["resposta_ai"]
    collection = db['LizardTI']

    return collection
