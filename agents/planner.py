from agents.retriver import recuperar_contexto

def planejar(pergunta):
    contexto = recuperar_contexto(pergunta)

    resposta = f"""
Contexto encontrado:

{contexto}

Pergunta:

{pergunta}
"""

    return resposta
