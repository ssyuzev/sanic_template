al_init:
	docker-compose exec app pipenv run alembic init

revision:
	docker-compose exec app pipenv run alembic revision --autogenerate

upgrade:
	docker-compose exec app pipenv run alembic upgrade head

downgrade:
	docker-compose exec app pipenv run alembic downgrade head

shell:
	docker-compose exec app pipenv run python3

start:
	docker-compose up

rebuild:
	docker-compose build

stop:
	docker-compose down
