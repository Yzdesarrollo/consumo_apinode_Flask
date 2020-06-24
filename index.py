from flask import Flask, render_template, request, redirect, url_for # Importaciones
import requests as req # 1. Instalar la libreria e importarla

app = Flask(__name__) # Instancia de la clase con el constructor

@app.route('/read') # Decorador modifica el comportamiento de una funcion
def read():
    response = req.get('http://localhost:3000/api/listtasks') # 2.usando el endpoint
    result = response.json()['tasks'] # 3. trayendo los datos
    return render_template('home.html', tasks = result)

@app.route('/edit') # Decorador modifica el comportamiento de una funcion
def edit():
    id = request.args.get('id')
    response = req.get(f'http://localhost:3000/api/gettask?id={id}') # 4.usando el endpoint con parametro id
    result = response.json()['task'] # 3. trayendo los datos
    #print(result)
    return render_template('edit-task.html', task = result)

@app.route('/update', methods=['POST'])
def update():
    id = request.args.get('id')
    taskName = request.form['task'] # Variable name que viene del formulario 
    taskDate = request.form['date']
    editData = {"id":id, "task":taskName, "date":taskDate}
    response = req.put('http://localhost:3000/api/updatetask', json = editData)
    return redirect(url_for('read'))

@app.route('/delete') # Decorador modifica el comportamiento de una funcion
def delete():
    id = request.args.get('id')
    deleteData = {"id":id}
    response = req.delete('http://localhost:3000/api/deletetask', json = deleteData)
    return redirect(url_for('read'))

@app.route('/create')
def create():
    return render_template('create-task.html')

@app.route('/add', methods = ['POST'])
def add():
    task = request.form['task']
    date = request.form['date']
    addData = {"task":task, "date": date}
    response = req.post('http://localhost:3000/api/addtask', json = addData)
    return redirect(url_for('read'))

if __name__== "__main__": # Servidor 
    app.run(debug=True)