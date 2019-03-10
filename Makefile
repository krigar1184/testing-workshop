.PHONY: *

bash:
	docker-compose run app bash

build:
	docker-compose build

rebuild: down up

down:
	docker-compose down

up:
	docker-compose up --build -d

test:
	docker-compose run app pytest

pip-install:
	docker-compose run app sh -c "pip install $(req) && pip freeze > requirements.txt"

lint:
	docker-compose run app flake8
