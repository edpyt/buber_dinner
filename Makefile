run:
	python -m src

test:
	docker-compose -f 'docker-compose.test.yml' up

dev:
	docker-compose up

dev-db:
	docker-compose run --build --service-ports db
