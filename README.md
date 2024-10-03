# Desafio Lizard TI

O desafio consiste em criar uma API usando **FastAPI** que recebe um arquivo PDF como entrada, processa-o usando uma IA Generativa (como o Gemini) e retorna um JSON com informações extraídas do PDF. A API deve utilizar Engenharia de Prompt para garantir que a IA forneça as informações no formato JSON correto e estruturado. O resultado também deve ser armazenado em um banco de dados NoSQL (como MongoDB).

---

## Primeiros Passos

1. **Crie um arquivo `requirements.txt`** com as dependências necessárias.
   
2. **Instale as dependências** executando o seguinte comando no terminal:
   ```bash
   pip install -r requirements.txt

3. **Execute o Código no Terminal:**
   ```bash
   uvicorn app:app --reload 
