run:
	python -m src

dev:
	docker-compose up --build

dev-db:
	docker-compose run --build --service-ports db
