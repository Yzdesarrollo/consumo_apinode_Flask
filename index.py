from flask import Flask, render_template, request, redirect, url_for # Importaciones
import mysql.connector
import requests as req

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='taskapp'
)

app = Flask(__name__) # Instancia de la clase con el constructor

@app.route('/read') # Decorador modifica el comportamiento de una funcion
def read():
    response = req.get('http://localhost:3000/api/listtasks')
    print(response.json())
    sql = 'SELECT * FROM tasks'
    cur = mydb.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    return render_template('home.html', tasks = result)

@app.route('/edit') # Decorador modifica el comportamiento de una funcion
def edit():
    id = request.args.get('id')
    sql = f"SELECT * FROM tasks WHERE id={id}"
    cur = mydb.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    return render_template('edit-task.html', task = result[0])

@app.route('/update', methods=['POST'])
def update():
    id = request.args.get('id')
    taskName = request.form['task'] # Variable name que viene del formulario 
    taskDate = request.form['date']
    sql = f"UPDATE tasks set task = '{taskName}', date = '{taskDate}' WHERE id={id}"
    cur = mydb.cursor()
    cur.execute(sql)
    mydb.commit()
    return redirect(url_for('read'))

@app.route('/delete') # Decorador modifica el comportamiento de una funcion
def delete():
    id = request.args.get('id')
    sql = f"DELETE FROM tasks WHERE id={id}"
    cur = mydb.cursor()
    cur.execute(sql)
    mydb.commit()
    return redirect(url_for('read'))

@app.route('/create')
def create():
    return render_template('create-task.html')

@app.route('/add', methods = ['POST'])
def add():
    task = request.form['task']
    date = request.form['date']
    sql = f"INSERT INTO tasks (task, date) VALUES ('{task}', '{date}')"
    cur = mydb.cursor()
    cur.execute(sql)
    mydb.commit()
    return redirect(url_for('read'))

if __name__== "__main__": # Servidor 
    app.run(debug=True)