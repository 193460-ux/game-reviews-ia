import requests

URL = "http://localhost:11434/api/generate"
MODELO = "llama3"

def gerar_resposta(contexto, pergunta):
    prompt = f"""
Você é um especialista em jogos eletrônicos.

Responda SEMPRE em português do Brasil.

Use APENAS as informações do contexto abaixo.

Contexto:
{contexto}

Pergunta:
{pergunta}

Se a resposta não estiver no contexto, diga:
"Não encontrei essa informação na base de conhecimento."
"""

    try:
        resposta = requests.post(
            URL,
            json={
                "model": MODELO,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        resposta.raise_for_status()

        dados = resposta.json()

        return dados["response"]

    except Exception as e:
        return f"Erro ao consultar o Llama 3: {e}”

