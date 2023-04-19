from django.shortcuts import render
from Analysis.similarity import analysis
from .decorators import student_only


def login(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'student/login.html')


@student_only
def exam_test(request):
    if request.method == "POST":
        print(request.POST)
        # return render(request,'student/test.html' ,{'status':})
    return render(request, 'student/test.html')
