# Agent

Agente conversacional integrado ao WhatsApp via [Evolution API](https://doc.evolution-api.com/). Recebe mensagens por webhook, processa com LLM (Llama 3.1 via Groq) e responde diretamente ao usuário.

## Stack

- **FastAPI** — servidor HTTP
- **LangChain + Groq** — inferência com `llama-3.1-8b-instant`
- **Evolution API** — envio/recebimento de mensagens WhatsApp

## Como funciona

1. Evolution API envia um `POST /webhook` com a mensagem recebida
2. O serviço filtra mensagens de grupos, do próprio bot e tipos não suportados
3. A mensagem é enviada ao LLM com o system prompt do CENA
4. A resposta é enviada de volta ao usuário via Evolution API

## Variáveis de ambiente

Copie `.env.example` para `.env` e preencha:

| Variável | Descrição |
|---|---|
| `AUTHENTICATION_API_KEY` | Chave de autenticação da aplicação |
| `EVO_BASE_URL` | URL base da instância Evolution API |
| `EVO_INSTANCE_NAME` | Nome da instância WhatsApp |
| `GROQ_API_KEY` | Chave da API Groq |

## Rodando localmente

```bash
uv sync
uv run fastapi dev main.py
```

## Docker

```bash
docker compose up -d
```
