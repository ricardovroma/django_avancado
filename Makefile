all:
	docker-compose up --build
build:
	docker exec application pip3 install --upgrade pip
	docker exec application pip3 install -r requirements.txt
	docker exec application python3 manage.py makemigrations
	docker exec application python3 manage.py migrate

test:
	docker exec application python3 manage.py test

run:
	docker-compose down
	docker-compose up

scrap:
	docker exec application python3 manage.py BSoup

down:
	docker-compose down

coverage:
	docker exec application coverage run manage.py test
	docker exec application coverage report
	docker exec application coverage html

attach:
	docker attach application

inspect:
	docker exec -it application /bin/bash