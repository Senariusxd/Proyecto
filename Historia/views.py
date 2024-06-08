from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Grupos, Historial, EM, EF
from .formsP import PacienteForm

def pacientes_view(request):
    pacientes = Paciente.objects.all().select_related('grupos')
    grupos = Grupos.objects.all()
    context = {
        'pacientes': pacientes,
        'grupos': grupos
    }
    return render(request, 'pacientes.html', context)

def create_patient(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        ci = request.POST['ci']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        ocupacion = request.POST['ocupacion']
        grupos_nombre = request.POST['grupos']

        grupos = Grupos.objects.get(nombre=grupos_nombre)

        paciente = Paciente.objects.create(
            nombre=nombre,
            apellidos=apellidos,
            ci=ci,
            telefono=telefono,
            direccion=direccion,
            ocupacion=ocupacion,
            grupos=grupos
        )

        return redirect('/pacientes/', ci=paciente.ci)
    else:
        grupos = Grupos.objects.all()
        return render(request, 'create_patient.html', {'grupos': grupos})
    
def edit_patient(request, ci):
    paciente = get_object_or_404(Paciente, ci=ci)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('pacientes')
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'edit_patient.html', {'form': form})

def delete_patient(request, ci):
    paciente = get_object_or_404(Paciente, ci=ci)

    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes')
    
    return render(request, 'delete_patient.html', {'paciente': paciente})

def patient_histories(request, ci):
    paciente = get_object_or_404(Paciente, ci=ci)
    historias = Historial.objects.filter(paciente=paciente)
    return render(request, 'patient_histories.html', {'paciente': paciente, 'historias': historias})


def historial_create(request):
    if request.method == 'POST':
        id = request.POST['id']
        fecha = request.POST['fecha']
        paciente_id = request.POST['paciente']
        ExamenMedico = request.POST['ExamenMedico']
        ExamenFisico = request.POST['ExamenFisico']

        paciente = Paciente.objects.get(id=paciente_id)
        historial = Historial.objects.create(
            id=id,
            fecha=fecha,
            paciente=paciente,
            ExamenMedico=ExamenMedico,
            ExamenFisico=ExamenFisico
        )
        return redirect('/patient_histories/')  # Redirige a una vista que muestra la lista de historiales

    pacientes = Paciente.objects.all()
    return render(request, 'historial_create.html', {'pacientes': pacientes})