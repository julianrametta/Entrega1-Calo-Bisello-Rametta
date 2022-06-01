from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    altura = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': "1.75 m"}))

class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")


class VehiculoForm(forms.Form):
    marca = forms.CharField(label="Marca",max_length=100)
    modelo = forms.CharField(label="Modelo",max_length=100)
    patente = forms.CharField(label="Patente",max_length=10)
    año = forms.DateField(label="Fecha de fabricacion")

class BuscarVehiculoForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")