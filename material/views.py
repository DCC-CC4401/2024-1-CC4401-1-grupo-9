from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from material.models import Course, Material
from .forms import MaterialForm
import fitz
import os


def material(request: HttpRequest, material_id: int = None) -> HttpResponse:
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
                    context={"materials": materials}
                )

        ## Renderizar pagina de un Material
        else:
            material = Material.objects.filter(id=material_id).first()
            return render(
                    request=request, 
                    template_name='material.html', 
                    context={"material": material}
                )
        

def subirMaterial(request: HttpRequest) -> HttpResponse:
    """ View para subir materiales.

        GET: 
        Obtiene el formulario para subir un nuevo material

        POST:
        Permite subir un archivo PDF y guardarlo en la base de datos.
    """
    if request.method == "GET":
        return render(
                request=request, 
                template_name='material_upload.html', 
                context={'form': MaterialForm}
            )
    
    elif request.method == "POST":
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()

            # Convert PDF to image
            pdf_path = document.file.name
            print(pdf_path)
            pdf = fitz.open(pdf_path)
            page = pdf.load_page(0)  # Portada será la primera página
            pix = page.get_pixmap()
            image_path = os.path.splitext(pdf_path)[0] + '.png'
            pix.save(image_path)
            document.image = image_path
            document.save()

            return redirect('material')  # Redirigir a la página de materiales
        else:
            return render(
                    request=request, 
                    template_name='material_upload.html', 
                    context={'form': form}
                )

