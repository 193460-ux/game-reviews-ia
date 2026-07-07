# 🎮 Games Reviews AI

## Autor

**Leonardo Scherer Denkvitts - 193460**

---

# Descrição

Games Reviews AI é um sistema desenvolvido para a disciplina de Inteligência Artificial.

O projeto utiliza a técnica de Retrieval-Augmented Generation (RAG), combinando busca semântica com um Modelo de Linguagem (LLM) executado localmente através do Ollama.

Os documentos da base de conhecimento são convertidos em embeddings utilizando Sentence Transformers. Quando o usuário realiza uma pergunta, o sistema recupera o documento mais relevante e envia esse contexto ao modelo Llama 3 para gerar uma resposta fundamentada.

---

# Funcionalidades

- Carregamento automático dos documentos da pasta `data`;
- Geração de embeddings utilizando Sentence Transformers;
- Armazenamento dos embeddings em memória;
- Busca semântica utilizando similaridade vetorial;
- Recuperação automática do documento mais relevante;
- Integração com o LLM Llama 3 utilizando Ollama;
- Geração de respostas baseadas no contexto recuperado;
- Arquitetura organizada em agentes.

---

# Estrutura do Projeto

```
game-reviews-ia/

├── agents/
│   ├── planner.py
│   ├── retriever.py
│   ├── analyst.py
│   ├── reviewer.py
│   └── __init__.py
│
├── data/
│   ├── gta5.txt
│   ├── Mario.txt
│   ├── Mortal_kombat.txt
│   ├── Skyrim.txt
│   └── Sonic.txt
│
├── rag/
│   ├── embeddings.py
│   ├── vector_db.py
│   └── llm.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Arquitetura

O sistema é dividido em módulos:

- **Planner:** organiza o fluxo da consulta;
- **Retriever:** recupera o contexto mais relevante;
- **Analyst:** realiza análise das informações;
- **Reviewer:** revisa a resposta antes da apresentação;
- **Embeddings:** gera vetores utilizando Sentence Transformers;
- **Vector DB:** armazena e consulta os embeddings;
- **LLM:** comunica-se com o Ollama (Llama 3) para gerar a resposta final.

---

# Tecnologias utilizadas

- Python 3
- NumPy
- Sentence Transformers
- Ollama
- Llama 3
- Requests

---

# Dependências

```
numpy
sentence-transformers
requests
```

---

# Como executar

### 1. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 2. Instalar o Ollama

https://ollama.com

### 3. Baixar o modelo Llama 3

```bash
ollama pull llama3
```

### 4. Iniciar o Ollama

```bash
ollama serve
```

### 5. Executar o projeto

```bash
python main.py
```

---

# Exemplo de uso

Pergunta:

```
Quem desenvolveu GTA 5?
```

Resposta:

```
A Rockstar Games desenvolveu GTA 5.
```

---

# Observações

Este projeto implementa um sistema de Retrieval-Augmented Generation (RAG), utilizando busca vetorial baseada em embeddings para localizar os documentos mais relevantes da base de conhecimento.

A resposta final é gerada pelo modelo **Llama 3**, executado localmente através do **Ollama**, utilizando apenas o contexto recuperado durante a busca.

