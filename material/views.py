from django.shortcuts import render
from material.models import Course, Material

# Create your views here.
def material(request):
    materials = Material.objects.all()
    courses = Course.objects.all()

    if request.method == "GET":
        return render(
            request=request, 
            template_name='index.html', 
            context={"materials": materials, "courses": courses})

