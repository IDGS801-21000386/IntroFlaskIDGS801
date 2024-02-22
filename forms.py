from wtforms import Form, EmailField, validators
from wtforms import StringField, TelField, IntegerField
from flask_wtf import FlaskForm


class UserForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=10, message="Ingresa un nombre válido")
    ])
    #email = StringField("Email", [
    #    validators.DataRequired(message="El campo es requerido"),
    #    validators.Email(message="Ingrese un correo válido")
    #])
    apaterno = StringField("Apellido Paterno", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=10, message="Ingresa un apellido válido")
    ])
    amaterno = StringField("Apellido Materno", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=10, message="Ingresa un apellido válido")
    ])
    edad = IntegerField("Edad", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=99, message="Ingresa una edad válida")
    ])


