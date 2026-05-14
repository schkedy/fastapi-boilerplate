# FastAPI Boilerplate

Estrutura base para projetos backend Python com FastAPI, seguindo arquitetura em camadas.

## Stack

- **FastAPI** — Framework web
- **SQLAlchemy 2.0 async** — ORM
- **PostgreSQL** — Banco de dados
- **Pydantic v2** — Validação e schemas
- **Alembic** — Migrações
- **pytest** — Testes

## Arquitetura

```
app/
  api/v1/endpoints/   # Routers — só recebe request e delega
  core/               # Config, segurança, startup
  models/             # ORM models (SQLAlchemy)
  schemas/            # Schemas de request/response (Pydantic)
  services/           # Regras de negócio
  repositories/       # Acesso ao banco
  utils/              # Helpers reutilizáveis
tests/
  unit/               # Testa services isolados (sem DB)
  integration/        # Testa endpoints com DB real
```

## Como rodar

```bash
cp .env.example .env
docker compose up
```

API disponível em `http://localhost:8000`  
Docs em `http://localhost:8000/docs`

## Testes

```bash
pip install -r requirements.txt
pytest tests/
```
