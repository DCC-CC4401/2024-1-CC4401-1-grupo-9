from django.shortcuts import render, redirect
from material.models import Course, Material
from .forms import MaterialForm

def material(request, material_id = None):
    """ View para los materiales.

        GET: 
        Permite obtener información de los materiales,
        o de un solo material.
    """

    if request.method == "GET":
        ## Renderizar pagina de Materiales
        if material_id is None:
            print("1")
            materials = Material.objects.all()
            return render(
                request=request, 
                template_name='materials_main.html', 
                context={"materials": materials})

        ## Renderizar pagina de un Material
        else:
            print(2)
            material = Material.objects.get(id=material_id)
            print(material.file)
            return render(
                request=request, 
                template_name='material.html', 
                
                context={"material": material})
        
def subirMaterial(request):
    """ View para subir materiales.

        GET: 
        Obtiene el formulario para subir un nuevo material

        POST:
        Permite subir un archivo PDF y guardarlo en la base de datos.
    """
    if request.method == "GET":
        return render(request, 'material_upload.html', {'form': MaterialForm})
    
    elif request.method == "POST":
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('material')  # Redirigir a la página de materiales
        else:
            return render(request, 'material_upload.html', {'form': form})

