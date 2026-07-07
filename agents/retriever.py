from rag.vector_db import buscar_documentos

def recuperar_contexto(pergunta):
    return buscar_documentos(pergunta)
