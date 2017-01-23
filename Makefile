server: migrate
	docker-compose up -t0

shell: migrate
	docker-compose run web ./manage.py shell

migrate:
	docker-compose run web ./manage.py migrate

makemigrations:
	docker-compose run web ./manage.py makemigrations gm

createsuperuser: migrate
	docker-compose run web ./manage.py createsuperuser
