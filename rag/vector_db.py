from rag.embeddings import gerar_embedding
import numpy as np

base_vetorial = []

def adicionar_documento(texto):
    embedding = gerar_embedding(texto)

    base_vetorial.append({
        "texto": texto,
        "embedding": embedding
    })

def buscar_documentos(pergunta):
    embedding_pergunta = gerar_embedding(pergunta)

    melhor_texto = ""
    melhor_score = -1

    for doc in base_vetorial:
        score = np.dot(
            embedding_pergunta,
            doc["embedding"]
        )

        if score > melhor_score:
            melhor_score = score
            melhor_texto = doc["texto"]

    return melhor_texto
