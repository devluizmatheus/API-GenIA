from fastapi import File
from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import HTTPException

from services import upload_pdf
from services import salvando_dados

from models import model

router = APIRouter(prefix="/resposta", tags=["Testes"])

@router.post("")
def chatbot(pergunta: str, pdf: UploadFile = File(...)):
    """Rota que retorna a resposta da pergunta do usuário"""
    if pdf.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="O arquivo enviado não é um PDF.")

    pdf_info = upload_pdf(pdf)

    gemini = model.start_chat(history= [{
        "role": "user",
        "parts": [
            {
                "text": pdf_info
            },
            {
                "text": "Você é um analista de dados de PDF"
            }
        ]
    }])

    resposta = gemini.send_message(pergunta)
    resposta_texto = resposta.candidates[0].content.parts[0].text.replace("\n", "")

    salvando_dados(pdf_info, pergunta, resposta_texto)
    return {
        "mensagem": pergunta,
        "resposta": resposta_texto
    }
