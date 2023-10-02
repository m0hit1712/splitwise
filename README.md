
# SplitWise
### This provides the backend and API endpoints to splits the expenses between multiple users

### Requirements:
1. Docker Compose
2. Docker

### Commands
To setup and runserver
> make setup

To run docker containers
> make start-server

To stop docker containers
> make stop-server


### URLs and Testing
For schema and API structure: http://127.0.0.1:8000/redoc/
For API testing: http://127.0.0.1:8000/swagger/


### Model Structure

1. User
2. Expense
3. Transaction
4. Due

### APIs

1. User - Create, Retrieve, Update, Lost
2. Expense - Create, Retrieve, List
3. Transaction - Retrieve, List
4. Due - Retrieve, List, settle


### Notes:
1. User is not inherited from AbstractUser, also does not have any authentication and authorization

