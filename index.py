from flask import Flask, render_template # Importaciones
app = Flask(__name__) # Instancia de la clase con el constructor

@app.route('/') # Decorador modifica el comportamiento de una funcion
def start():
    return render_template('home.html')

@app.route('/home') 
def home():
    return render_template('home.html')

@app.route('/login') 
def login():
    return render_template('login.html')

@app.route('/register') 
def register():
    return render_template('register.html')

if __name__== "__main__": # Servidor 
    app.run(debug=True)