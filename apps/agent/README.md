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

| Variável                 | Descrição                           |
| ------------------------ | ----------------------------------- |
| `AUTHENTICATION_API_KEY` | Chave de autenticação da aplicação  |
| `EVO_BASE_URL`           | URL base da instância Evolution API |
| `EVO_INSTANCE_NAME`      | Nome da instância WhatsApp          |
| `GROQ_API_KEY`           | Chave da API Groq                   |

## Setup de desenvolvimento

### 1. Subir a infraestrutura

```bash
docker compose up -d
```

### 2. Rodar o backend

```bash
uv sync
uv run fastapi dev main.py
```

### 3. Expor o backend com ngrok

```bash
ngrok http 8000
```

Anote a URL gerada (ex: `https://xxxx.ngrok-free.app`).

### 4. Configurar a Evolution API

1. Acesse `http://localhost:8080/manager`
2. Informe `EVO_BASE_URL` e `AUTHENTICATION_API_KEY` para fazer login
3. Crie uma nova instância com o nome definido em `EVO_INSTANCE_NAME`
4. Informe o número de telefone no formato `55<DDD>9<número>` (ex: `558199222xxxx`)
5. Conecte escaneando o QR Code com o WhatsApp do número cadastrado (igual ao WhatsApp Web)

### 5. Configurar o webhook

Dentro das configurações da instância criada:

1. Ative o webhook
2. Defina a URL: `<url-do-ngrok>/webhook` (ex: `https://xxxx.ngrok-free.app/webhook`)
3. Ative o evento **MESSAGES_UPSERT**
4. Salve as alterações

### 6. Testar

Envie uma mensagem para o número cadastrado a partir de **outro** WhatsApp e acompanhe os logs do Docker e do backend.
