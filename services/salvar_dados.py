from datetime import datetime
from datetime import timezone

from database.database import conexao_banco

collection = conexao_banco()

def salvando_dados(pdf: str, pergunta: str, resposta: str):
    """Função para salvar no banco"""
    document = {
        "pdf": pdf,
        "pergunta": pergunta,
        "resposta": resposta,
        "timestamp": datetime.now(timezone.utc)
    }

    collection.insert_one(document)
