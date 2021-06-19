# moove-unified-api
## Description
Moove backend created with django, docker and postgres

## Installation Guide - Docker: Recommended
* Make sure docker desktop is installed in your computer

* Clone this project
    ```bash
    git clone git@github.com:MooveAfrica/moove-unified-api.git
    ```

* Enter project root directory
    ```bash
    cd moove-unified-api
    ```
* build docker image
    ```bash
    docker-compose build
    ```
* start docker images
    ```bash
    docker-compose up
    ```
### How to get into docker container to run migration or genertate migration when you add a new models

* view list of runnung containers
    ```bash
    docker ps
    ```
* get into a container - you can only run django commands inside docker container
    ```bash
    docker exec -it moove-unified-api_unified-backend_1 bash
    ```
## Installation Guide - Virtual env
* check that python is installed
    ```bash
    python --V
    ```
* Install Postgres database

* Clone this project
    ```bash
    git clone git@github.com:MooveAfrica/moove-unified-api.git
    ```
* Enter project root directory
    ```bash
    cd moove-unified-api
    ```
* install virtual env in your terminal at the project root
    ```bash
    pip install virtualenv
    ```
* Activate virtualenv 
    ```bass
    source .env/bin/activate
    ```
* Install packages
    ```bash
    pip install -r requirements.txt
    ```
* In the root directory, open `env/bin/activate` file and add the environmental variable at the bottom of the `activate` file accordingto the sample bellow or export the env variables accordingto the sample bellow:
    ```python
    export DATABASE_URL=<DATABASE_URL>
    ```

* Migrate tables to postgres database
    ```bash
    python manage.py migrate
    ```

* Start the application
    ```bash
    python manage.py runserver
    ```
