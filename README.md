# FastAPI Boilerplate

Base structure for Python backend projects with FastAPI, following a layered architecture.

## Stack

- **FastAPI** — Web framework
- **SQLAlchemy 2.0 async** — ORM
- **PostgreSQL** — Database
- **Pydantic v2** — Validation and schemas
- **Alembic** — Migrations
- **pytest** — Tests

## Architecture

```
app/
  api/v1/endpoints/   # Routers — only receives requests and delegates
  core/               # Config, security, startup
  models/             # ORM models (SQLAlchemy)
  schemas/            # Request/response schemas (Pydantic)
  services/           # Business logic
  repositories/       # Database access
  utils/              # Reusable helpers
tests/
  unit/               # Tests services in isolation (no DB)
  integration/        # Tests endpoints with a real DB
```

## How to run

```bash
cp .env.example .env
docker compose up
```

API available at `http://localhost:8000`  
Docs at `http://localhost:8000/docs`

## Tests

```bash
pip install -r requirements.txt
pytest tests/
```
