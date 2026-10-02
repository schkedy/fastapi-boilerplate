.PHONY: run

run:
	uvicorn app.main:app

migrate-init:
	alembic revision --autogenerate -m "Initial migration"

migrate-upgrade:
	alembic upgrade head

migrate-downgrade:
	alembic downgrade -1