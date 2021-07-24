from flask import Flask, render_template, url_for, request, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key = 'Mi_llave_Ultrasecreta'

@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario ya ha hecho login {session["username"]}'
    return 'No ha hecho loging'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('inicio'))

    return render_template('login.html')

@app.route('logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('inicio'))

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404

#REST Representational State Transfer
@app.route('/api/mostrar/<nombre>', methods=['POST', 'GET'])
def mostrar_json(nombre):
    #Cuando el Json es simple no es necesario utilizar la libreria 'jsonify'
    valores = {
        'nombre': nombre,
        'metodo_http': request.method
    }
    return valores