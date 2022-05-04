from django.http import HttpResponse
from django.shortcuts import render
from .models import Course

def courses_view(request):
    course_list = Course.objects.order_by('id')
    context = {
        'course_list': course_list,
    }
    return render(request, 'courses/index.html',context)

def courses_detail(request, pk):
    course = Course.objects.get(pk = pk)
    context = {
        'course': course,
    }
    return render(request, 'courses/course_detail.html',context)