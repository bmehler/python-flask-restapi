# Restful Api with the Python Flask Framework

## Create a virtual environment
```bash
mkdir myproject
$ cd myproject
$ python3 -m venv venv
```
## Activate the environment
```bash
. venv/bin/activate
```

## Install the Flask Framework
```bash
pip install Flask
```

## Install MySQL
```bash
pip install flask-mysql
```

## Install CORS
```bash
pip install Flask-Cors
```

### Connect a Database Connenction
```python
app.config['MYSQL_DATABASE_HOST'] = db_host
app.config['MYSQL_DATABASE_PORT'] = db_port
app.config['MYSQL_DATABASE_USER'] = db_user
app.config['MYSQL_DATABASE_PASSWORD'] = db_password
app.config['MYSQL_DATABASE_DB'] = db_database
```

### Create a Database Table
The database table used in this example is
```bash
cars
```

### Run the Application with
```bash
flask --app init run
```

## Test the api with curl with json content

GET All Request
```bash
curl -X GET http://127.0.0.1:5000/cars
```
GET Single Request
```bash
curl -X GET http://127.0.0.1:5000/car/<id>
```
POST Request
```bash
curl -X POST http://127.0.0.1:5000/cars -H 'Content-Type: application/json' -d '{"brand":"Max","model":"Muster","price":"3000"}'
````
PUT Request
```bash
curl -X PUT http://127.0.0.1:5000/car/<id> -H 'Content-Type: application/json' -d' {"brand":"Max","model":"Muster","price":"5000"}'
```
Delete Request
```bash
curl -X DELETE http://127.0.0.1:5000/car/<id>
```