from wtforms import Form
from wtforms import EmailField
from wtforms import StringField, TelField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email


class UserForm(Form):
    nombre = StringField("nombre")
    email = EmailField("email") #Crear campo de validacion correcto
    apaterno = TelField("apaterno")
    amaterno = TelField("amaterno")
    edad = IntegerField("edad")

