server: migrate
	docker-compose up -t0

shell: migrate
	docker-composerun web ./manage.py shell

migrate:
	docker-compose run web ./manage.py migrate


makemigrations:
	docker-compose run web ./manage.py makemigrations

createsuperuser: migrate
	docker-compose run web ./manage.py createsuperuser