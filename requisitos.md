# Gerenciador de Vagas de Emprego e Estágio

## 1. Visão geral do projeto

### 1.1 Objetivo

Construir uma aplicação web para auxiliar pessoas que estão procurando emprego ou estágio a organizar e acompanhar suas oportunidades profissionais.

O sistema deverá permitir que o usuário registre vagas encontradas, acompanhe o processo seletivo, organize suas candidaturas e visualize métricas sobre sua busca por emprego.

O projeto será desenvolvido inicialmente com:

* Backend: Python + Django + Django REST Framework
* Banco: PostgreSQL
* Frontend futuro: React + TypeScript + Vite
* Desenvolvimento: Django local + PostgreSQL em Docker
* Controle de versão: Git + GitHub
* Containerização: Docker
* Servidor web: Nginx
* Servidor da aplicação: Gunicorn
* Testes: Pytest / Django Test
* Qualidade de código: Ruff
* CI/CD: GitHub Actions

A arquitetura deverá permitir que o frontend React seja desenvolvido posteriormente sem necessidade de reescrever o backend.

---

# 2. Visão do produto

## 2.1 Problema

Quem está procurando emprego normalmente acompanha oportunidades através de diversos canais:

* LinkedIn
* Indeed
* Gupy
* sites de empresas
* indicações
* grupos
* e-mails
* plataformas de estágio

Com o tempo, torna-se difícil lembrar:

* quais vagas foram encontradas;
* para quais vagas houve candidatura;
* quando a candidatura foi realizada;
* quais empresas entraram em contato;
* em qual etapa cada processo está;
* quais tecnologias a vaga exige;
* quais processos foram encerrados;
* quais candidaturas ainda estão aguardando retorno.

O sistema pretende centralizar essas informações.

---

# 3. Objetivos

## 3.1 Objetivo principal

Permitir que o usuário organize todo o processo de procura por emprego em um único lugar.

## 3.2 Objetivos secundários

O sistema deverá permitir:

1. cadastrar empresas;
2. cadastrar vagas;
3. registrar candidaturas;
4. acompanhar o estágio de cada processo;
5. visualizar candidaturas em formato Kanban;
6. pesquisar e filtrar vagas;
7. registrar contatos;
8. registrar acontecimentos do processo seletivo;
9. visualizar estatísticas;
10. receber notificações;
11. posteriormente utilizar IA para análise de compatibilidade.

---

# 4. Definição do MVP

Não tente desenvolver tudo de uma vez.

A primeira versão deve responder apenas a uma pergunta:

> "Consigo cadastrar minhas oportunidades e acompanhar em que estágio cada candidatura está?"

A V1 deverá conter:

* cadastro;
* autenticação;
* empresas;
* vagas;
* candidaturas;
* alteração de status;
* Kanban;
* dashboard básico.

## 4.1 Fluxo principal

O fluxo inicial será:

Encontrada
↓
Candidatou-se
↓
Teste
↓
Entrevista
↓
Entrevista técnica
↓
Oferta
↓
Contratado

Também deverá existir:

* Recusado
* Arquivado

---

# 5. Fase 1 — Análise de requisitos

Antes de escrever código, escreva os requisitos.

## 5.1 Requisitos funcionais

### RF01 — Cadastro

O sistema deverá permitir que um usuário crie uma conta.

### RF02 — Login

O usuário deverá conseguir autenticar-se.

### RF03 — Empresas

O usuário deverá conseguir:

* cadastrar empresa;
* editar empresa;
* visualizar empresa;
* excluir empresa;
* listar empresas.

### RF04 — Vagas

Uma vaga deverá possuir informações como:

* título;
* empresa;
* URL;
* localização;
* modalidade;
* tipo de contratação;
* faixa salarial;
* descrição;
* tecnologias;
* data em que foi encontrada;
* observações.

### RF05 — Candidaturas

O usuário deverá conseguir associar uma vaga a uma candidatura.

### RF06 — Status

O usuário deverá conseguir alterar o estágio da candidatura.

### RF07 — Kanban

As candidaturas deverão ser visualizadas em colunas correspondentes aos seus status.

### RF08 — Dashboard

O sistema deverá apresentar informações como:

* total de vagas;
* total de candidaturas;
* candidaturas em andamento;
* entrevistas;
* ofertas;
* processos encerrados.

---

# 6. Requisitos não funcionais

O sistema deverá:

* utilizar API REST;
* possuir autenticação;
* proteger dados de usuários;
* utilizar PostgreSQL;
* utilizar variáveis de ambiente;
* possuir testes automatizados;
* possuir documentação da API;
* utilizar Git;
* possuir pipeline de CI;
* ser executável através de Docker em produção;
* possuir logs;
* utilizar HTTPS em produção.

---

# 7. Regras de negócio

Comece documentando as regras antes dos models.

Exemplos:

### RN01

Um usuário somente pode visualizar suas próprias vagas e candidaturas.

### RN02

Uma candidatura pertence a uma vaga.

### RN03

Uma candidatura pertence a um usuário.

### RN04

Uma empresa pode possuir várias vagas.

### RN05

Uma vaga pode possuir várias tecnologias.

### RN06

Uma candidatura possui apenas um status atual.

### RN07

Uma candidatura pode possuir vários eventos históricos.

### RN08

Uma candidatura encerrada como "Recusado" não deve aparecer entre processos ativos.

Essas regras deverão orientar a implementação dos models e das permissões.

---

# 8. Fase 2 — Modelagem do domínio

Antes de criar tabelas, pense nas entidades.

A primeira versão do domínio pode ser:

```text
User
 │
 ├── Company
 │      └── Job
 │
 └── Application
         │
         ├── Job
         ├── Status
         ├── Event
         └── Contact

Skill
 └── Job
```

---

# 9. Modelagem inicial do banco

## 9.1 User

Inicialmente utilize o sistema de autenticação do Django, preferencialmente com um Custom User desde o começo.

Campos básicos:

```text
User
----------------
id
email
password
first_name
last_name
created_at
updated_at
```

Não utilize o `username` tradicional se o projeto não precisar dele.

---

# 10. Company

Representa uma empresa.

```text
Company
----------------
id
name
website
linkedin_url
description
created_at
updated_at
```

Relacionamento:

```text
User 1 ---- N Company
```

A empresa pertence ao usuário.

---

# 11. Job

Representa uma oportunidade.

```text
Job
----------------
id
company_id
title
description
url
location
work_model
employment_type
salary_min
salary_max
found_at
deadline
notes
created_at
updated_at
```

Exemplos de `work_model`:

```text
REMOTE
HYBRID
ONSITE
```

Exemplos de `employment_type`:

```text
INTERNSHIP
CLT
PJ
TEMPORARY
FREELANCE
```

---

# 12. Skill

Representa uma tecnologia ou competência.

```text
Skill
----------------
id
name
```

Relacionamento:

```text
Job N ---- N Skill
```

Exemplos:

```text
Python
Django
React
PostgreSQL
Docker
AWS
Git
JavaScript
TypeScript
```

---

# 13. Application

Essa será uma das entidades mais importantes.

```text
Application
----------------
id
user_id
job_id
status
applied_at
notes
created_at
updated_at
```

Status:

```text
FOUND
APPLIED
TEST
INTERVIEW
TECHNICAL_INTERVIEW
OFFER
HIRED
REJECTED
ARCHIVED
```

---

# 14. ApplicationEvent

Não dependa apenas do status atual.

Crie histórico.

```text
ApplicationEvent
----------------
id
application_id
event_type
description
event_date
created_at
```

Exemplos:

```text
Candidatura enviada
Teste recebido
Teste enviado
Entrevista marcada
Entrevista realizada
Feedback recebido
Processo encerrado
```

Isso permitirá posteriormente construir uma linha do tempo da candidatura.

---

# 15. Contact

Posteriormente:

```text
Contact
----------------
id
application_id
name
role
email
linkedin_url
phone
notes
created_at
updated_at
```

Isso será útil para registrar recrutadores e outras pessoas envolvidas no processo.

---

# 16. Relacionamentos

A estrutura poderá ficar aproximadamente assim:

```text
User
 │
 ├───────────────┐
 │               │
 ▼               ▼
Company       Application
 │               │
 ▼               ▼
Job ───────── Application
 │               │
 ▼               ├── ApplicationEvent
Skill            │
                 └── Contact
```

---

# 17. Fase 3 — Arquitetura do backend

Utilize Django como framework principal e Django REST Framework para disponibilizar a API.

Uma organização inicial:

```text
backend/
│
├── config/
│   ├── settings/
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/
│   ├── users/
│   ├── companies/
│   ├── jobs/
│   ├── applications/
│   └── dashboard/
│
├── manage.py
├── requirements.txt
├── .env
├── .env.example
├── Dockerfile
└── docker-compose.yml
```

Não coloque toda a aplicação em um único `models.py`, `views.py` e `urls.py`.

Organizar por domínio facilitará a evolução do projeto.

---

# 18. Fase 4 — Configuração inicial

A ordem recomendada é:

### Passo 1

Criar o repositório no GitHub.

### Passo 2

Criar o projeto Django.

### Passo 3

Criar ambiente virtual.

### Passo 4

Configurar `.env`.

Exemplo:

```text
SECRET_KEY=
DEBUG=True

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
```

### Passo 5

Configurar PostgreSQL.

Durante o desenvolvimento, mantenha a estratégia que você já definiu:

```text
Django → máquina local

PostgreSQL → Docker
```

### Passo 6

Configurar Django para utilizar PostgreSQL.

### Passo 7

Executar migrations.

### Passo 8

Criar Custom User.

### Passo 9

Criar os primeiros models.

---

# 19. Fase 5 — Implementação dos models

Implemente nesta ordem:

```text
1. User
2. Company
3. Skill
4. Job
5. Application
6. ApplicationEvent
7. Contact
```

Depois de cada conjunto de models:

```bash
python manage.py makemigrations
python manage.py migrate
```

Depois teste os relacionamentos no Django Shell.

---

# 20. Fase 6 — API REST

Depois do domínio implementado, crie a API.

Estrutura:

```text
/api/v1/
```

Endpoints iniciais:

```text
POST   /api/v1/auth/register/
POST   /api/v1/auth/login/
POST   /api/v1/auth/logout/

GET    /api/v1/companies/
POST   /api/v1/companies/
GET    /api/v1/companies/{id}/
PUT    /api/v1/companies/{id}/
DELETE /api/v1/companies/{id}/

GET    /api/v1/jobs/
POST   /api/v1/jobs/
GET    /api/v1/jobs/{id}/
PUT    /api/v1/jobs/{id}/
DELETE /api/v1/jobs/{id}/

GET    /api/v1/applications/
POST   /api/v1/applications/
GET    /api/v1/applications/{id}/
PATCH  /api/v1/applications/{id}/
DELETE /api/v1/applications/{id}/
```

---

# 21. Autenticação

Como o frontend será React, uma abordagem adequada é utilizar autenticação baseada em tokens.

Uma opção é:

```text
Django REST Framework
+
JWT
```

O fluxo será:

```text
React
   │
   │ login
   ▼
Django API
   │
   │ JWT
   ▼
React
   │
   │ Authorization
   ▼
Django API
```

A autenticação deverá ser implementada antes de construir as funcionalidades principais.

---

# 22. Permissões

Essa parte é extremamente importante.

Nunca confie apenas no frontend para segurança.

O backend deve verificar:

```text
Usuário A
   ↓
pode acessar
   ↓
somente seus próprios dados
```

Por exemplo:

```text
GET /api/v1/applications/
```

não deve retornar candidaturas de outros usuários.

Essa regra deverá ser aplicada na API através das permissões e querysets.

---

# 23. Fase 7 — CRUD

Agora implemente o CRUD.

Ordem recomendada:

```text
Company
↓
Job
↓
Application
```

Primeiro faça funcionar pela API.

Utilize ferramentas como:

* Insomnia
* Postman
* Swagger/OpenAPI

antes de começar o React.

O objetivo é conseguir utilizar o sistema sem frontend.

---

# 24. Fase 8 — Documentação da API

Adicione documentação automática utilizando OpenAPI/Swagger.

A API deverá permitir que você visualize:

```text
endpoint
método
parâmetros
request
response
autenticação
erros
```

Isso será particularmente importante quando você começar o React.

---

# 25. Fase 9 — Testes

Não deixe os testes para o final.

Comece pelos casos mais importantes.

## Testes de models

Verificar:

* relacionamentos;
* constraints;
* valores obrigatórios;
* status.

## Testes de API

Verificar:

```text
Usuário consegue criar vaga?
Usuário consegue visualizar vaga?
Usuário consegue editar vaga?
Usuário consegue excluir vaga?
Usuário consegue acessar dados de outro usuário?
```

O último teste é especialmente importante.

Exemplo:

```text
Usuário A
    ↓
tenta acessar
    ↓
Application do usuário B
```

Resultado esperado:

```text
403 Forbidden
```

ou:

```text
404 Not Found
```

dependendo da estratégia adotada.

---

# 26. Fase 10 — Primeira versão funcional

Quando essas funcionalidades estiverem prontas:

```text
Cadastro
Login
   ↓
Dashboard
   ↓
Empresas
   ↓
Vagas
   ↓
Candidaturas
   ↓
Status
   ↓
Kanban
```

você terá uma primeira versão funcional do backend.

Nesse ponto, faça uma tag:

```text
v0.1.0
```

---

# 27. Fase 11 — Frontend React

Somente depois da API estar relativamente estável, comece o React.

Stack:

```text
React
TypeScript
Vite
```

Estrutura:

```text
frontend/
│
├── src/
│   ├── components/
│   ├── pages/
│   ├── layouts/
│   ├── services/
│   ├── hooks/
│   ├── contexts/
│   ├── types/
│   └── utils/
│
├── package.json
└── vite.config.ts
```

---

# 28. Primeiras telas

Construa nessa ordem:

## Tela 1 — Login

```text
E-mail
Senha
Entrar
```

## Tela 2 — Cadastro

```text
Nome
E-mail
Senha
Confirmar senha
```

## Tela 3 — Dashboard

Mostrar:

```text
Total de vagas
Candidaturas
Entrevistas
Ofertas
Processos ativos
```

## Tela 4 — Lista de vagas

Mostrar:

```text
Empresa
Cargo
Modalidade
Localização
Status
Data
```

## Tela 5 — Detalhes da vaga

Mostrar todas as informações.

## Tela 6 — Kanban

```text
Encontrada
Candidatou-se
Teste
Entrevista
Entrevista técnica
Oferta
Contratado
Recusado
```

---

# 29. Kanban

O Kanban será uma das funcionalidades mais interessantes visualmente.

O usuário poderá mover:

```text
[ Candidatou-se ]
       ↓
[ Entrevista ]
```

O frontend enviará uma requisição:

```text
PATCH /api/v1/applications/{id}/
```

alterando:

```text
status = INTERVIEW
```

O backend será responsável por validar a alteração.

---

# 30. Fase 12 — Busca e filtros

Depois do MVP, implemente:

* busca por cargo;
* busca por empresa;
* localização;
* modalidade;
* tipo de contratação;
* status;
* tecnologias;
* faixa salarial;
* período.

Exemplo:

```text
Python
+
Remoto
+
Estágio
+
Fortaleza
```

---

# 31. Fase 13 — Paginação

Não retorne milhares de registros de uma vez.

Implemente:

```text
?page=1&page_size=20
```

A API deverá devolver:

```text
count
next
previous
results
```

---

# 32. Fase 14 — Histórico

Com `ApplicationEvent`, crie uma timeline:

```text
19/08
Candidatura enviada

21/08
Teste recebido

22/08
Teste enviado

25/08
Entrevista marcada

29/08
Entrevista realizada
```

Essa funcionalidade dará bastante valor ao projeto.

---

# 33. Fase 15 — Contatos

Permita registrar:

```text
Nome
Cargo
Empresa
E-mail
LinkedIn
Observações
```

Exemplo:

```text
Maria Silva
Tech Recruiter
Empresa X
linkedin.com/...
```

---

# 34. Fase 16 — Dashboard

O dashboard poderá evoluir para métricas.

Exemplos:

```text
Total de candidaturas
Taxa de resposta
Taxa de entrevistas
Taxa de aprovação
Número de processos ativos
Número de processos encerrados
```

Exemplo de cálculo:

```text
Taxa de entrevista =
entrevistas / candidaturas × 100
```

Também poderá apresentar:

* candidaturas por mês;
* empresas que mais receberam candidaturas;
* tecnologias mais presentes;
* distribuição por modalidade;
* distribuição por tipo de contratação.

---

# 35. Fase 17 — Notificações

Posteriormente:

```text
Entrevista amanhã
Prazo do teste se aproximando
Processo sem atualização há X dias
Follow-up recomendado
```

A arquitetura poderá evoluir para tarefas assíncronas.

Tecnologias possíveis:

```text
Celery
Redis
```

Não implemente isso na V1.

---

# 36. Fase 18 — IA

IA deve ser uma fase posterior.

Uma possível funcionalidade:

```text
Currículo
   +
Descrição da vaga
   ↓
IA
   ↓
Análise de compatibilidade
```

Resultado:

```text
Compatibilidade: 82%

Pontos fortes:
- Python
- Django
- PostgreSQL

Pontos a desenvolver:
- AWS
- Docker
- CI/CD
```

Também poderá sugerir:

* habilidades ausentes;
* palavras-chave;
* melhorias no currículo;
* preparação para entrevista.

Essa funcionalidade pode formar uma futura V3.

---

# 37. Roadmap de versões

## V0.1 — Backend básico

* [ ] Projeto Django
* [ ] PostgreSQL
* [ ] Custom User
* [ ] Company
* [ ] Job
* [ ] Application
* [ ] API REST
* [ ] Autenticação
* [ ] Permissões
* [ ] Testes básicos

## V0.2 — Produto funcional

* [ ] React
* [ ] Login
* [ ] Dashboard
* [ ] CRUD de empresas
* [ ] CRUD de vagas
* [ ] CRUD de candidaturas
* [ ] Kanban
* [ ] Alteração de status

## V0.3 — Organização

* [ ] Busca
* [ ] Filtros
* [ ] Paginação
* [ ] Histórico
* [ ] Contatos
* [ ] Notificações
* [ ] Gráficos
* [ ] Mais testes

## V0.4 — Produção

* [ ] Docker
* [ ] Nginx
* [ ] Gunicorn
* [ ] HTTPS
* [ ] Banco PostgreSQL
* [ ] Variáveis de ambiente
* [ ] Logs
* [ ] Backup
* [ ] CI/CD
* [ ] Deploy

## V1.0 — Produto inicial completo

* [ ] Backend estável
* [ ] Frontend estável
* [ ] Autenticação
* [ ] Kanban
* [ ] Dashboard
* [ ] Histórico
* [ ] Busca
* [ ] Filtros
* [ ] Notificações
* [ ] Testes
* [ ] Documentação
* [ ] Deploy

## V2 — Recursos avançados

* [ ] Upload de currículo
* [ ] Gestão de múltiplos currículos
* [ ] análise de currículo
* [ ] análise de vagas
* [ ] compatibilidade de habilidades
* [ ] recomendações

## V3 — IA

* [ ] análise automática de vagas
* [ ] matching currículo × vaga
* [ ] sugestões de candidatura
* [ ] preparação para entrevistas
* [ ] geração de insights

---

# 38. Ambiente de desenvolvimento

Durante o desenvolvimento:

```text
┌───────────────────────────┐
│ Computador                │
│                           │
│ Django                    │
│ localhost:8000            │
│                           │
│ React                     │
│ localhost:5173            │
└────────────┬──────────────┘
             │
             │ PostgreSQL
             ▼
┌───────────────────────────┐
│ Docker                    │
│                           │
│ PostgreSQL 17             │
│ localhost:5432            │
└───────────────────────────┘
```

Essa configuração é adequada para o estágio atual do projeto.

---

# 39. Arquitetura de produção

Quando o sistema estiver pronto:

```text
                    INTERNET
                       │
                       ▼
                    HTTPS
                       │
                       ▼
                  ┌─────────┐
                  │  Nginx  │
                  └────┬────┘
                       │
                       ▼
                  ┌─────────┐
                  │ Gunicorn│
                  └────┬────┘
                       │
                       ▼
                  ┌─────────┐
                  │ Django  │
                  │   API   │
                  └────┬────┘
                       │
                       ▼
                ┌──────────────┐
                │ PostgreSQL   │
                └──────────────┘
```

React será disponibilizado como frontend separado ou através do Nginx.

---

# 40. Tecnologias de produção

Uma configuração coerente para o projeto:

## Backend

```text
Python
Django
Django REST Framework
Gunicorn
```

## Banco

```text
PostgreSQL
```

## Frontend

```text
React
TypeScript
Vite
```

## Infraestrutura

```text
Docker
Docker Compose
Nginx
```

## Segurança

```text
HTTPS
Environment Variables
JWT
CORS
CSRF
Secure Cookies
```

## Qualidade

```text
Pytest
Ruff
GitHub Actions
```

---

# 41. CI/CD

Depois que o projeto estiver funcional, crie uma pipeline.

Fluxo:

```text
git push
   ↓
GitHub
   ↓
GitHub Actions
   ↓
Lint
   ↓
Testes
   ↓
Build
   ↓
Deploy
```

A pipeline deverá impedir que código quebrado seja enviado para produção.

---

# 42. Docker em produção

Uma arquitetura possível:

```text
docker-compose.yml

services:

    nginx

    backend

    postgres
```

O backend deverá utilizar Gunicorn.

Exemplo conceitual:

```text
Nginx
 ↓
Gunicorn
 ↓
Django
 ↓
PostgreSQL
```

Não utilize `python manage.py runserver` em produção.

---

# 43. Banco de dados em produção

O PostgreSQL de produção deverá possuir:

* volume persistente;
* backup;
* usuário próprio;
* senha segura;
* acesso restrito;
* migrations controladas.

Não exponha a porta 5432 publicamente sem necessidade.

---

# 44. Segurança

Antes de colocar em produção, revisar:

### Django

```text
DEBUG=False
ALLOWED_HOSTS
SECRET_KEY segura
CSRF
CORS
```

### Banco

```text
senha forte
usuário separado
acesso restrito
backup
```

### API

```text
autenticação
permissões
rate limiting
validação de entrada
```

### Infraestrutura

```text
HTTPS
firewall
logs
atualizações
```

---

# 45. Git

Utilize commits pequenos e descritivos.

Exemplos:

```text
feat: add company model
feat: add job API
feat: implement application status
fix: prevent users from accessing other applications
test: add application API tests
docs: update API documentation
refactor: improve application service
```

Branches:

```text
main
develop
feature/*
fix/*
```

Para um projeto individual, você também pode simplificar e trabalhar diretamente com:

```text
main
feature/*
```

---

# 46. Documentação do projeto

O GitHub deverá possuir um README contendo:

```text
1. Sobre o projeto
2. Problema
3. Objetivo
4. Funcionalidades
5. Tecnologias
6. Arquitetura
7. Como executar
8. Variáveis de ambiente
9. Docker
10. Testes
11. API
12. Screenshots
13. Roadmap
14. Licença
```

---

# 47. Documentação técnica

Além do README, mantenha uma pasta:

```text
docs/
```

Com:

```text
docs/
├── requirements.md
├── architecture.md
├── database.md
├── api.md
├── business-rules.md
├── deployment.md
└── roadmap.md
```

Isso transformará o projeto em algo muito mais próximo de um projeto profissional.

---

# 48. Ordem exata de execução

Não desenvolva aleatoriamente.

Siga esta sequência:

```text
01. Definir problema
        ↓
02. Definir público
        ↓
03. Levantar requisitos
        ↓
04. Definir regras de negócio
        ↓
05. Modelar domínio
        ↓
06. Modelar banco
        ↓
07. Criar projeto Django
        ↓
08. Configurar PostgreSQL
        ↓
09. Criar Custom User
        ↓
10. Criar models
        ↓
11. Criar migrations
        ↓
12. Criar serializers
        ↓
13. Criar API
        ↓
14. Implementar autenticação
        ↓
15. Implementar permissões
        ↓
16. Criar testes
        ↓
17. Documentar API
        ↓
18. Finalizar backend MVP
        ↓
19. Criar projeto React
        ↓
20. Criar autenticação frontend
        ↓
21. Criar dashboard
        ↓
22. Criar CRUD de vagas
        ↓
23. Criar candidaturas
        ↓
24. Criar Kanban
        ↓
25. Criar filtros
        ↓
26. Criar histórico
        ↓
27. Criar métricas
        ↓
28. Dockerizar aplicação
        ↓
29. Configurar Nginx
        ↓
30. Configurar Gunicorn
        ↓
31. Configurar HTTPS
        ↓
32. Criar CI/CD
        ↓
33. Fazer deploy
        ↓
34. Monitorar
        ↓
35. Evoluir produto
```

---

# 49. Como trabalhar em cada etapa

Para evitar se perder, cada etapa deve possuir quatro partes:

## 1. Planejamento

Defina:

```text
O que será feito?
Por que será feito?
Quais são as regras?
```

## 2. Implementação

Escreva o código.

## 3. Validação

Teste manualmente e automaticamente.

## 4. Documentação

Registre:

```text
O que foi decidido?
Por que foi decidido?
Como funciona?
```

Somente depois avance.

---

# 50. Primeiro ciclo de desenvolvimento

Seu primeiro ciclo pode ser:

### Sprint 1

```text
[ ] Criar repositório
[ ] Criar projeto Django
[ ] Criar ambiente virtual
[ ] Configurar .env
[ ] Configurar PostgreSQL Docker
[ ] Configurar Django + PostgreSQL
[ ] Criar Custom User
[ ] Criar migrations
[ ] Criar superuser
```

### Sprint 2

```text
[ ] Company
[ ] Skill
[ ] Job
[ ] Application
[ ] ApplicationEvent
[ ] Testar relacionamentos
```

### Sprint 3

```text
[ ] DRF
[ ] Serializers
[ ] ViewSets
[ ] URLs
[ ] JWT
[ ] Permissions
[ ] API de Company
[ ] API de Job
[ ] API de Application
```

### Sprint 4

```text
[ ] Testes
[ ] Swagger
[ ] Correção de bugs
[ ] Refinamento da API
[ ] README
[ ] Tag v0.1.0
```

Depois disso, comece o React.

---

# 51. O que NÃO fazer agora

É importante controlar o escopo.

Não comece agora por:

```text
IA
Celery
Redis
microservices
Kubernetes
AWS complexa
mensageria
machine learning
```

Primeiro faça:

```text
Django
+
PostgreSQL
+
DRF
+
React
```

funcionar muito bem.

Um monólito Django bem estruturado é suficiente para esse projeto.

---

# 52. Critério para considerar o MVP pronto

Considere a primeira versão pronta somente quando um usuário conseguir realizar este fluxo completo:

```text
Criar conta
    ↓
Fazer login
    ↓
Cadastrar empresa
    ↓
Cadastrar vaga
    ↓
Cadastrar candidatura
    ↓
Visualizar candidatura
    ↓
Alterar status
    ↓
Mover candidatura no Kanban
    ↓
Visualizar dashboard
    ↓
Sair da aplicação
    ↓
Entrar novamente
    ↓
Encontrar seus dados preservados
```

Se esse fluxo funcionar de ponta a ponta, você terá um produto funcional.

---

# 53. Próximo passo recomendado

Não comece criando todos os models imediatamente.

O próximo passo deve ser fazer a **análise formal de requisitos da V1**.

A partir dela, podemos produzir:

```text
Requisitos funcionais
        ↓
Requisitos não funcionais
        ↓
Casos de uso
        ↓
Histórias de usuário
        ↓
Regras de negócio
        ↓
Modelo de domínio
        ↓
Modelo entidade-relacionamento
        ↓
Models Django
```

Depois disso, partimos para a implementação.

A ideia é utilizar este documento como nosso **mapa do projeto**. Quando você estiver, por exemplo, na etapa "modelagem do banco", podemos trabalhar especificamente nela e detalhar entidades, cardinalidades, constraints, índices, migrations e decisões de arquitetura sem precisar reinventar o projeto inteiro.
