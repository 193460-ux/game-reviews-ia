from rag.llm import gerar_resposta
from agents.retriever import recuperar_contexto

pergunta = input("Pergunta: ")

contexto = recuperar_contexto(pergunta)

resposta = gerar_resposta(contexto, pergunta)

print("\nResposta:")
print(resposta)



