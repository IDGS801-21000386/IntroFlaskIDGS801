from flask import Flask, render_template

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Definir una ruta y la función asociada a esa ruta
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos")
def alumnos():
    titulo = "UTL!!!!!"
    nombres = ["Erick", "Saul", "Rivera", "Chagoya"]
    return render_template("alumnos.html", titulo = titulo, nombres = nombres)

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

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    # Iniciar el servidor web incorporado de Flask en el puerto por defecto (5000)
    # Habilitar el modo de depuración para facilitar la identificación y solución de errores
    app.run(debug=True)
