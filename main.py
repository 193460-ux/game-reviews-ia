from rag.llm import gerar_resposta
from agents.retriever import recuperar_contexto

pergunta = input("Pergunta: ")

contexto = recuperar_contexto(pergunta)

print("\nContexto encontrado:")
print(contexto)

print("\nGerando resposta...")

resposta = gerar_resposta(contexto, pergunta)

print("\nResposta:")
print(resposta)




