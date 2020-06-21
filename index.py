from flask import Flask, render_template, request, redirect, url_for # Importaciones
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='taskapp'
)

app = Flask(__name__) # Instancia de la clase con el constructor

@app.route('/') # Decorador modifica el comportamiento de una funcion
def index():
    sql = 'SELECT * FROM tasks'
    cur = mydb.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return render_template('home.html', tasks = result)

@app.route('/createtask') # Decorador modifica el comportamiento de una funcion
def createtask():
    return render_template('create-task.html')

@app.route('/addtask', methods=['POST']) 
def addtask():
    if request.method == 'POST':
        taskName = request.form['task'] # Variable name que viene del formulario 
        taskDate = request.form['date'] # Variable date que viene del formulario
        cur = mydb.cursor()
        sql = f"INSERT INTO tasks (task,date) VALUES ('{taskName}','{taskDate}')"
        cur.execute(sql)
        mydb.commit()
        print('taskName: ',taskName, 'taskDate: ', taskDate)
        return redirect(url_for('index'))
    return 'Error'


if __name__== "__main__": # Servidor 
    app.run(debug=True)