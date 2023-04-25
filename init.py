from flask import Flask
from flask import jsonify, request
from flaskext.mysql import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
 
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'flaskcars'
 
mysql = MySQL(app)

@app.route('/cars', methods = ['GET', 'POST'])
def carsFuntion():
    if request.method == 'GET':
        return get_cars()
    elif request.method == 'POST':
       data = request.get_json()
       brand = data.get('brand', '')
       model = data.get('model', '')
       price = data.get('price', '')
       return makeANewCar(brand, model, price)

@app.route('/car/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def carFunctionId(id):
    if request.method == 'GET':
        return get_car(id)
    elif request.method == 'PUT':
        data = request.get_json()
        brand = data.get('brand', '')
        model = data.get('model', '')
        price = data.get('price', '') 
        return updateACar(id, brand, model, price)
  
    elif request.method == 'DELETE':
        return deleteACar(id)

def get_cars():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars")
    cars = cursor.fetchall()
    conn.close()

    data = []
    for car in cars:
        data.append({
            "id": car[0],
            "model": car[2],
            "brand": car[1],
            "price": car[3]
        })
    return jsonify(data)

def makeANewCar(brand, model, price):
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "INSERT INTO cars (brand, model, price) VALUES (%s, %s, %s)"
    val = (brand, model, price)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()

    data = {
        "brand": brand,
        "model": model,
        "price": price
    }
    return jsonify({'Car created': data})

def get_car(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM cars WHERE id= %s"
    val = (id)
    cursor.execute(sql, val)
    car = cursor.fetchone()
    conn.commit()
    conn.close()
    data = {
        "id": car[0],
        "brand": car[1],
        "model": car[2],
        "price": car[3]
    }
    return jsonify(data)

def updateACar(id, brand, model, price):
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "UPDATE cars SET brand=%s, model=%s, price=%s WHERE id=%s"
    val = (brand, model, price, id)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    data = {
        "id": id,
        "brand": brand,
        "model": model,
        "price": price
    }
    return jsonify({'Car updated': data})

def deleteACar(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "DELETE FROM cars WHERE id= %s"
    val = (id)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    return jsonify({'Deleted': 'Car deleted'})