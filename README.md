# 🎮 Games Reviews AI

## Autor

**Leonardo Scherer Denkvitts - 193460**

## Descrição

Games Reviews AI é um sistema desenvolvido para a disciplina de Inteligência Artificial.

O projeto utiliza técnicas de Retrieval-Augmented Generation (RAG), realizando busca semântica em documentos sobre jogos eletrônicos através de embeddings vetoriais.

A aplicação recupera informações relevantes da base de conhecimento e utiliza essas informações para responder perguntas do usuário.

---

## Funcionalidades

- Carregamento automático dos documentos da pasta `data`;
- Geração de embeddings utilizando Sentence Transformers;
- Armazenamento em uma base vetorial em memória;
- Busca por similaridade utilizando produto escalar (NumPy);
- Recuperação do documento mais relevante para cada pergunta;
- Arquitetura organizada em agentes.

---

## Estrutura do Projeto

```
Games Reviews AI
│
├── agents
│   ├── planner.py
│   ├── retriever.py
│   ├── analyst.py
│   ├── reviewer.py
│   └── __init__.py
│
├── rag
│   ├── embeddings.py
│   ├── vector_db.py
│
├── data
│   ├── gta5.txt
│   ├── Mario.txt
│   ├── Mortal_kombat.txt
│   ├── Skyrim.txt
│   └── Sonic.txt
│
├── main.py
├── README.md
└── requirements.txt
```

---

## Tecnologias Utilizadas

- Python 3
- Sentence Transformers
- NumPy

---

## Funcionamento

1. O sistema carrega automaticamente todos os arquivos `.txt` presentes na pasta `data`.

2. Cada documento recebe um embedding utilizando o modelo:

```
sentence-transformers/all-MiniLM-L6-v2
```

3. Os embeddings são armazenados em uma base vetorial.

4. Quando o usuário realiza uma pergunta, é gerado um embedding para essa consulta.

5. O sistema calcula a similaridade entre a pergunta e todos os documentos cadastrados.

6. O documento mais relevante é recuperado e utilizado como contexto para responder à consulta.

---

## Instalação

Clone o projeto:

```bash
git clone <URL_DO_REPOSITORIO>
```

Instale as dependências:

```bash
pip install sentence-transformers
pip install numpy
```

ou

```bash
pip install -r requirements.txt
```

---

## Execução

Execute:

```bash
python main.py
```

---

## Base de Conhecimento

A base de conhecimento é composta pelos seguintes documentos:

- GTA V
- Mario
- Mortal Kombat
- Skyrim
- Sonic

Novos documentos podem ser adicionados simplesmente colocando novos arquivos `.txt` na pasta `data`.

---

## Arquitetura

O sistema foi organizado em módulos:

- **Planner:** organiza a consulta do usuário;
- **Retriever:** recupera o contexto mais relevante;
- **Analyst:** analisa o conteúdo recuperado;
- **Reviewer:** revisa a resposta antes da apresentação;
- **Embeddings:** gera vetores utilizando Sentence Transformers;
- **Vector DB:** armazena e consulta os embeddings.

---

## Dependências

```
numpy
sentence-transformers
```

---

## Observações

Este projeto possui uma implementação de recuperação de informações baseada em embeddings vetoriais (RAG), utilizando busca por similaridade para localizar os documentos mais relevantes da base de conhecimento.
