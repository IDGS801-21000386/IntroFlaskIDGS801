from flask import Flask, render_template, request
import forms 
import math

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Definir una ruta y la función asociada a esa ruta
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos", methods={"GET", "POST"})
def alumnos():
    # titulo = "UTL!!!!!"
    # nombres = ["Erick", "Saul", "Rivera", "Chagoya"]
    # return render_template("alumnos2.html", titulo = titulo, nombres = nombres)
    alumno_clase = forms.UserForm(request.form)
    if request.method == "POST":
        nom = alumno_clase.nombre.data
        apa = alumno_clase.apaterno.data
        ama = alumno_clase.amaterno.data
        edad = alumno_clase.edad.data
        email = alumno_clase.email.data
        print(f'Nombre: {nom}')
        print(f'Nombre: {apa}')
        print(f'Nombre: {ama}')
        print(f'Nombre: {edad}')
        print(f'Nombre: {email}')
    return render_template("alumnos2.html", form = alumno_clase, nom=nom, apa=apa, ama=ama, edad=edad, email=email)

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/hola")
def hola():
    return "<h1>Holaaaaaa saludos desde Hola</h1>"

@app.route("/despedida")
def despedida():
    return "<h1>Adioos saludos desde despedida</h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "Hola " + nom

@app.route("/numero/<int:n1>")
def numero(n1):
    return "Numero: {}".format(n1)

@app.route("/user/<int:id>/<string:nom>")
def user(id,nom):
    return "ID: {}, Nombre: {}".format(id,nom)

@app.route("/sumar/<float:n1>/<float:n2>")
def sumar(n1,n2):
    return f"La suma es de {n1} + {n2} es: {n1+n2}"

@app.route("/default")
@app.route("/default/<string:g>")
def default(d = "Erick"):
    return f"El nombre de Usuario es: {d}"

@app.route("/calcular", methods=["GET", "POST"])
def calcular():
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        operador = request.form.get("operador")
        if operador == "+":
            return f"La suma de {n1} + {n2} = {str(int(n1) + int(n2))}"
        elif operador == "-":
            return f"La resta de {n1} - {n2} = {str(int(n1) - int(n2))}"
        elif operador == "*":
            return f"La multiplicacion de {n1} * {n2} = {str(int(n1) * int(n2))}"
        else:
            return f"La division de {n1} / {n2} = {str(int(n1) / int(n2))}"
    else:
        return """
        <form action="/calcular", method="POST">
            <label>N1:</label>
            <input type="text" name="n1"><br>
            <label>N2:</label>
            <input type="text" name="n2"><br>
            <input type="submit"/>
        </form>
"""


@app.route("/operacionBasica")
def operacionBasica():
    return render_template("OperacionBasica.html")

@app.route("/resultado", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        return f"La multiplicacion de {n1} + {n2} = {str(int(n1) * int(n2))}"
    else:
        return """
        <form action="/calcular", method="POST">
            <label>N1:</label>
            <input type="text" name="n1"><br>
            <label>N2:</label>
            <input type="text" name="n2"><br>
            <input type="submit"/>
        </form>
"""
    
# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    # Iniciar el servidor web incorporado de Flask en el puerto por defecto (5000)
    # Habilitar el modo de depuración para facilitar la identificación y solución de errores
    app.run(debug=True)
