start:
   docker build . -t splitwise
   docker compose up -d
   docker exec splitwise-splitwise-1 python manage.py makemigrations
   docker exec splitwise-splitwise-1 python manage.py migrate

stop:
   docker compose down -v






