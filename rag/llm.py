import requests

URL = "http://localhost:11434/api/generate"
MODELO = "llama3"

def gerar_resposta(contexto, pergunta):
    prompt = f"""
Você é um especialista em jogos.

Contexto:
{contexto}

Pergunta:
{pergunta}

Responda utilizando apenas as informações do contexto.
"""

    resposta = requests.post(
        URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    return resposta.json()["response"]
