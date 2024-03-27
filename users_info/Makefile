.PHONY: remigrate

remigrate:
	alembic downgrade base
	mv src/migrations/versions/2024_03_24_00_flush_migration.py .
	rm -f src/migrations/versions/20*
	mv 2024_03_24_00_flush_migration.py src/migrations/versions/
	alembic upgrade head
	alembic revision --autogenerate -m "initial migrations" --rev-id 01
	alembic upgrade head
