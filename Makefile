setup:
    docker build . -t splitwise
    docker compose up -d
    docker exec splitwise-splitwise-1 python manage.py migrate
    docker log splitwise-splitwise-1 -f

start-server:
    docker compose up -d

stop-server:
    docker compose down -v


