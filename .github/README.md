## 📋 Sobre o Projeto
O CENA é uma iniciativa cultural-tecnológica nascida em Pernambuco com o propósito de combater a precarização estrutural dos trabalhadores da cultura no Brasil. Diferente de plataformas convencionais, o CENA opera sob a filosofia "comunidade primeiro, tecnologia depois", posicionando-se como um movimento que utiliza a tecnologia para aproximar a gestão pública da base artística.

## 🎯 Objetivo
Desenvolver e consolidar um ecossistema digital integrado que conecta artistas, trabalhadores da cultura e coletivos a oportunidades estruturadas de emprego, fomento e capacitação, transformando dados descentralizados em inteligência estratégica para a gestão pública (B2G) e mercado (B2B).

## ⚡ Funcionalidades (Módulo Oportunidades v1.1)
O core inicial do desenvolvimento está concentrado no motor de conexões do ecossistema:
* *Feed Personalizado em Tempo Real:* Cruzamento proativo de perfis com oportunidades baseado em um algoritmo de Score de Afinidade.
* *Matching Bidirecional P2P:* Conexão automatizada entre quem oferece recursos (espaços, equipamentos, serviços) e quem os demanda.
* *Matching por Complementaridade:* Estímulo a parcerias interdisciplinares de capital criativo através de afinidade transversal de perfis.
* *Ideia Rápida (IA):* Campo de busca em linguagem natural mediado por LLM para inclusão e acessibilidade de usuários com baixa literacia digital.
* *Radar da Cultura (SaaS B2G):* Dashboard analítico e inteligência territorial para secretarias de cultura.

## 🛠️ Tecnologias Utilizadas
O ecossistema foi orçado e planejado sob a seguinte stack tecnológica:
* *Frontend Web:* Next.js / React (Painel SaaS e Backoffice)
* *Módulo Mobile:* Flutter (Aplicativo iOS e Android)
* *Backend API:* NestJS / Node.js
* *Inteligência Artificial:* Claude API (LLM de parsing para a funcionalidade Ideia Rápida)
* *Infraestrutura:* AWS (Amazon Web Services)
* *Orquestração de Monorepo:* pnpm Workspaces + Turborepo

## 📁 Estrutura do Projeto

O repositório adota a estratégia de **Monorepo**, organizando aplicações e módulos compartilhados na seguinte estrutura:

```text
cena/
├── apps/
│   ├── api/          → Backend NestJS (API REST)
│   ├── web/          → Frontend Next.js (Backoffice / Plataforma Web)
│   └── agent/        → Agente conversacional integrado ao WhatsApp
│
├── packages/
│   ├── ui/           → Biblioteca de componentes compartilhados
│   ├── database/     → Schemas, migrations e seeds do banco de dados
│   └── shared/       → Tipos TypeScript e utilitários compartilhados
│
├── docs/
│   └── adr/          → Architecture Decision Records (ADRs)
│
├── infra/            → Infraestrutura como Código (Terraform/CDK)
│
└── scripts/          → Scripts utilitários e automações

## 🏗️ Arquitetura

A arquitetura do ecossistema é baseada em microsserviços integrados orientados a eventos, dividida em quatro camadas funcionais:

1 *Camada de Cliente (Superapp):* Mobile-first para gestão de carreira do artista.  
2 *Camada de Gestão (SaaS Web):* Dashboards e analytics para organizações e secretarias.  
3 *Camada de Inclusão (Assistente IA):* Interface conversacional para acessibilidade.  
4 *Camada de Persistência e Processamento:* Banco de dados relacional PostgreSQL rodando rotinas de cálculo do Motor de Matching no servidor (Server-Side).

## 🚀 Instalação e Inicialização Local
