from django.shortcuts import redirect, render
from .models import Especie, Mascota
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required


def home(request):
    return render(request, 'home.html')

def inicioSesion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contraseña = request.POST.get('contraseña')

        print(nombre)
        print(contraseña)
        user = authenticate(request, username=nombre, password=contraseña)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'inicioSesion.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})
    return render(request, 'inicioSesion.html')

def cerrarSesion(request):
    logout(request)
    return redirect('home')

@login_required
@permission_required('refugio.view_mascota', raise_exception=True)
def panelGestion(request):
    mascotas = Mascota.objects.all()
    especies = Especie.objects.all()

    return render(request, 'panelGestion.html', {'mascotas': mascotas, 'especies': especies})

def mostrar_mascotas(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        especie = Especie.objects.get(codigo=codigo)
        mascotas = Mascota.objects.filter(especie=especie)
        listarEspecie = Especie.objects.all()
        return render(request, 'mascotas.html', {'mascotas': mascotas, 'listarEspecie': listarEspecie})
    mascotas = Mascota.objects.all()
    listarEspecie = Especie.objects.all()
    return render(request, 'mascotas.html', {'mascotas': mascotas, 'listarEspecie': listarEspecie})

@login_required
@permission_required('refugio.add_mascota', raise_exception=True)
def agregarMascotas(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        sexo = request.POST.get('sexo')
        edad_aproximada = int(request.POST.get('edad_aproximada'))
        imagen = request.POST.get('imagen')
        especie = request.POST.get('especie')

        especie = Especie.objects.get(codigo=especie)

        Mascota.objects.create(nombre=nombre, descripcion=descripcion, sexo=sexo, edad_aproximada=edad_aproximada, imagen=imagen, especie=especie)
        return redirect('panelGestion')
    especies = Especie.objects.all()

    return render(request, 'agregarMascotas.html', {'especies': especies})

@login_required
@permission_required('refugio.add_especie', raise_exception=True)
def agregarEspecie(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        Especie.objects.create(nombre=nombre, descripcion=descripcion)
        return redirect('panelGestion')

    return render(request, 'agregarEspecie.html')

@login_required
@permission_required('refugio.change_mascota', raise_exception=True)
def editarMascota(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        mascota = Mascota.objects.get(codigo = int(codigo))
        especie = Especie.objects.all()

        return render(request, 'editarMascotas.html', {'mascota': mascota, 'especies': especie})
    return redirect('inicioSesion')

@login_required
@permission_required('refugio.change_mascota', raise_exception=True)
def confirmarCambioMascota(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        mascota = Mascota.objects.get(codigo = int(codigo))

        mascota.nombre = request.POST.get('nombre')
        mascota.descripcion = request.POST.get('descripcion')
        mascota.sexo = request.POST.get('sexo')
        mascota.edad_aproximada = int(request.POST.get('edad_aproximada'))
        mascota.imagen = request.POST.get('imagen')

        especie_codigo = request.POST.get('especie')
        especie = Especie.objects.get(codigo=especie_codigo)
        mascota.especie = especie

        mascota.save()

    return redirect('panelGestion')

@login_required
@permission_required('refugio.change_especie', raise_exception=True)
def editarEspecie(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        especie = Especie.objects.get(codigo = int(codigo))

        return render(request, 'editarEspecie.html', {'especie': especie})
    return redirect('inicioSesion')

@login_required
@permission_required('refugio.change_especie', raise_exception=True)
def confirmarCambioEspecie(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        especie = Especie.objects.get(codigo = int(codigo))

        especie.nombre = request.POST.get('nombre')
        especie.descripcion = request.POST.get('descripcion')

        especie.save()

    return redirect('panelGestion')

@login_required
@permission_required('refugio.change_especie', raise_exception=True)
def eliminarEspecie(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        especie = Especie.objects.get(codigo = int(codigo))
        especie.delete()

    return redirect('panelGestion')

@login_required
@permission_required('refugio.change_mascota', raise_exception=True)
def eliminarMascota(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        mascota = Mascota.objects.get(codigo = int(codigo))
        mascota.delete()

    return redirect('panelGestion')
