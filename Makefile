setup:
	docker build . -t splitwise
	docker compose up -d
	docker exec splitwise-web-1 python manage.py migrate
	docker logs splitwise-web-1 -f

start-server:
	docker compose up -d
	docker logs splitwise-web-1 -f

stop-server:
	docker compose down -v

clean-up:
	docker compose down -v
	docker volume rm splitwise_local_postgres_data | true

