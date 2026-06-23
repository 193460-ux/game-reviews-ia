from agents.planner import planejar
from agents.analyst import analisar
from agents.reviewer import revisar
from rag.vector_db import adicionar_documento
import os

# Carregar arquivos da pasta data
pasta = "data"

for arquivo in os.listdir(pasta):

    if arquivo.endswith(".txt"):

        caminho = os.path.join(
            pasta,
            arquivo
        )

        with open(
            caminho,
            "r",
            encoding="utf-8"
        ) as f:

            texto = f.read()

            adicionar_documento(texto)

print("Documentos carregados!")
print("=== Game Reviews AI ===")

while True:

    pergunta = input(
        "\nDigite sua pergunta (ou sair): "
    )

    if pergunta.lower() == "sair":
        break

    # Agente Planejador
    contexto = planejar(pergunta)

    # Agente Analista
    analise = analisar(
        pergunta,
        contexto
    )

    # Agente Revisor
    resposta_final = revisar(
        analise
    )

    print("\nResposta:")
    print(resposta_final)


