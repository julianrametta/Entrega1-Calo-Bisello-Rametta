from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpRequest
from django.template import loader
from django.shortcuts import render
from familia.forms import BuscarVehiculoForm, PersonaForm, BuscarPersonasForm, VehiculoForm, MascotaForm, BuscarMascotaForm

from familia.models import Persona, Vehiculo, Mascota

def index_familiar(request: HttpRequest) -> HttpResponse:
    personas = Persona.objects.all()
    template = loader.get_template('familia/lista_familiares.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))


def agregar_familiar(request: HttpRequest) -> HttpResponse:
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            altura = form.cleaned_data['altura']
            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, altura=altura).save()

            return HttpResponseRedirect("/familiar")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    
    return render(request, 'familia/form_carga.html', {'form': form})


def borrar_familiar(request: HttpRequest, identificador: str) -> HttpResponse:
    '''      
    Vista que permite para un metodo http GET borrar un familiar de la base de datos.      
    '''
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect("/familiar/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def buscar_familiar(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form_busqueda = BuscarPersonasForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarPersonasForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            personas = Persona.objects.filter(nombre__icontains=palabra_a_buscar)

        return  render(request, 'familia/lista_familiares.html', {"personas": personas})
    

def index_mascota(request: HttpRequest) -> HttpResponse:
    mascotas = Mascota.objects.all()
    template = loader.get_template('mascota/lista_mascotas.html')
    context = {
        'mascotas': mascotas,
    }
    return HttpResponse(template.render(context, request))

def agregar_mascota(request: HttpRequest) -> HttpResponse:
    '''
    Vista que para un metodo http GET retorna el formulario hmtl para ingresar una nueva mascota y para un
    metodo http POST carga una nueva mascota en la base de datos y retorna el html con la lista de mascotas.
    '''

    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():

            tipo = form.cleaned_data['nombre']
            raza = form.cleaned_data['raza']
            nombre = form.cleaned_data['nombre']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            Mascota(tipo=tipo, raza=raza, nombre=nombre, fecha_nacimiento=fecha_nacimiento).save()

            return HttpResponseRedirect("/mascota")
    elif request.method == "GET":
        form = MascotaForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    return render(request, 'mascota/form_carga.html', {'form': form})

def borrar_mascota(request: HttpRequest, identificador: str) -> HttpResponse:
    '''
    Vista que permite para un metodo http GET borrar una mascota de la base de datos   
    '''
    if request.method == "GET":
        mascota = Mascota.objects.filter(id=int(identificador)).first()
        if mascota:
            mascota.delete()
        return HttpResponseRedirect("/mascota")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

def buscar_mascota(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form_busqueda = BuscarMascotaForm()
        return render(request, 'mascota/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarMascotaForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            mascotas = Mascota.objects.filter(nombre__icontains=palabra_a_buscar)

        return  render(request, 'mascota/lista_mascotas.html', {"mascotas": mascotas}) 


# Vehiculos
def agregarVehiculo(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():

            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            patente = form.cleaned_data['patente']
            año = form.cleaned_data['año']
            Vehiculo(marca=marca, modelo=modelo, patente=patente, año=año).save()

            return HttpResponseRedirect("/")
        elif request.method == "GET":
            form = VehiculoForm()
        else:
            return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

        
        return render(request, 'Vehiculo/form_carga.html', {'form': form})

def borrarVehiculo(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        vehiculo = Vehiculo.objects.filter(id=int(identificador)).first()
        if vehiculo:
            vehiculo.delete()
        return HttpResponseRedirect("/Vehiculo/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

def buscarVehiculo(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form_busqueda = BuscarVehiculoForm()
        return render(request, 'Vehiculo/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarVehiculoForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            vehiculos = Vehiculo.objects.filter(nombre__icontains=palabra_a_buscar)

        return  render(request, 'Vehiculos/lista_vehiculos.html', {"vehiculos": vehiculos}) 
