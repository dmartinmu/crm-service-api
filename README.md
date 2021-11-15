# crm-service-api
REST API to manage customer data for a small shop.

## Main features

* API rest built on `Python 3.7` with `Flask` framework due to its lightness and flexibility.
* `PostgreSQL 14.1` as database with test data included (see further information below).
* Use of `SQLAlchemy` as ORM, providing both development and security improvements.
* Endpoints with input validation (`cerberus`) and custom exceptions.
* Authentication and authorization using JSON Web Tokens (JWT).
* 30+ tests covering Users and Customers endpoints.
* Use of `docker` and `docker-compose` for easier deployment and testing.
* Code and API documentation.

## Getting started

Visit repo [wiki](https://github.com/dmartinmu/crm-service-api/wiki) and check API endpoints usage information.

You can also use Swagger UI once API is running:
```
http://localhost:8000/v1/
```
### Running the API
This section details how to deploy and run the API and database.

#### Prerequisites

We need to have docker and docker-compose installed in our machine. See https://docs.docker.com/get-docker/.

#### Local environment

Just execute the command:

```
docker-compose up --build
```

The API Rest will be up and running! Provided `Dockerfile` and `docker-compose.yml` install everything necessary for the application to run. An instance of PostgreSQL database will be up too and preloaded with testing users and customers (see Database section for more detail).

#### Testing environment
In order to test the application use this:

```
docker-compose -f docker-compose-test.yml up --build
```

In this case `docker-compose-test.yml` makes API and database run and execute all tests included. To make sure we are not using modified data is useful to use the next command before launching tests, assuring a clean database initialization:

```
docker-compose down
```

Some users are already created to test application functionality. Try this credentials:

```
user: admin@theagilemonkeys.com
password: admin1234
role: admin

user: user@theagilemonkeys.com
password: user5678
role: regular user
```



#### Production environment
Taking advantage of dockerization, deploying into production environments (on premise servers and cloud environments) is easier because we just have to build and run our API image. `entrypoint.sh` could use `start-api` command to run the API on a uwsgi server (instead of Flask built-in server for development):

```
docker build .
```

### Database

The API uses a PostgreSQL database called `crm` ir order to persist customers and users information. As explained in the previous section provided `Dockerfile` and `docker-compose` files initialize this database and create the structure and data.

Folder `devops/db` includes some scripts to be executed automatically when running official PostgreSQL docker image. We just need to add any scripts to `sql_structure` and `sql_test` folders and they will automatically be processed.

For database models `SQLAlchemy` ORM is used. In `src/models` there are models for both Users and Customers as well as `Flask-Marshmallow` serializing objects. Using an ORM provides some advantages because creates an abstraction layer over the database itself (changing database engine would be easy this way) and avoid some security issues like SQL Injection (no raw SQL queries are used).

### API Design
This API Rest works with two main entities: Users and Customers. Code has been organized as follows:

* `src/api` includes API endpoints with inputs validation (using `Cerberus` package) and custom exceptions.
* `src/controllers` includes code for operations with more "business" needs (not just CRUD operations) like image uploading functionality.
* `src/daos` includes classes to perform database operations.

### Testing
* All test code is included under `test` folder.
* `conftest.py` includes PyTest fixtures to make easier tests initialization (host, tokens, etc.)
* Each entity (users and customers) has its own file called `test_xxx.py`.
* `test_health.py` just test /health/ endpoint to check if API is up and running. This is useful for server monitorization tools like Nagios.

### Debugging
If debugging is needed API could be launched executing `src/app.py` file. Just keep in mind that `crm` database is needed. As explained in Database section it could run using docker or use an existing one in our environment (scripts for structure and data are provided).