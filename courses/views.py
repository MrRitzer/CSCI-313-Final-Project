from django.http import HttpResponse
from django.template import loader
from .models import Course

def courses_view(request):
    template = loader.get_template('courses/index.html')
    return HttpResponse(template.render())

def courses_detail(request, pk):
    course = Course.objects.get(pk)
    return HttpResponse("You're at courses detail!")