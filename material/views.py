from django.shortcuts import render
from material.models import Course, Material


def material(request, material_id: int = None):
    """ View para los materiales.

        GET: 
        Permite obtener información de los materiales,
        o de un solo material.
    """

    if request.method == "GET":
        ## Renderizar pagina de Materiales
        if material_id is None:
            materials = Material.objects.all()
            return render(
                request=request, 
                template_name='materials_main.html', 
                context={"materials": materials})

        ## Renderizar pagina de un Material
        else:
            materials = Material.objects.filter(id=material_id)
            return render(
                request=request, 
                template_name='material.html', 
                context={"materials": materials})

