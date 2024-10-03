import PyPDF2

from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile


def upload_pdf(file: UploadFile = File(...)) -> str:
    """Função que faz o upload do PDF"""
    try:
        reader = PyPDF2.PdfReader(file.file)
        text = ""

        for page in range(len(reader.pages)):
            page_text = reader.pages[page].extract_text() or ""
            text += page_text

        return text

    except Exception:
        raise HTTPException(status_code=400, detail="Erro ao processar o arquivo PDF.")
