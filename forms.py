from wtforms import Form
from wtforms import StringField, TelField

class UserForm(Form):
    nombre = StringField("nombre")
    email = StringField("email") #Crear campo de validacion correcto
    apaterno = TelField("apaterno")
    amaterno = TelField("amaterno")

