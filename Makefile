run:
	python -m src

dev:
	docker-compose up

dev-db:
	docker-compose run --build --service-ports db
