from wtforms import Form, EmailField, validators
from wtforms import StringField, TelField, IntegerField
from flask_wtf import FlaskForm


class UserForm(Form):
    nombre = StringField("nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4,max=10, message="Ingresa nombre valido")
    ])
    email = EmailField("email", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingrese in correo valido")
    ]) 
    apaterno = TelField("apaterno", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4,max=10, message="Ingresa apellido valido")
    ])
    amaterno = TelField("amaterno", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4,max=10, message="Ingresa apellido valido")
    ])
    edad = IntegerField("edad", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=1,max=2, message="Ingresa una edad valida")
    ])

