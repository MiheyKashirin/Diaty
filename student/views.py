from django.shortcuts import render
from django.http import HttpResponse

def student_main_page(request):
    return HttpResponse("Главная страница студента")

def lessons_list(request):
    return HttpResponse("Список уроков")

def lesson_details(request, lesson_id):
    return HttpResponse(f"Детали урока {lesson_id}")

def my_grades(request):
    return HttpResponse("Мои оценки")
