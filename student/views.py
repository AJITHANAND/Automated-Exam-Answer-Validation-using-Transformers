from django.shortcuts import render, redirect
from .decorators import student_only
from .models import *
from django.core.exceptions import *
import hashlib
from django.db import IntegrityError
from teacher.models import Questions


def password_to_hash(password: str) -> str:
    password_bytes = password.encode('utf-8')
    return hashlib.sha512(password_bytes).hexdigest()


def login(request):
    is_logged = request.session.get('session_identifier')
    if is_logged is not None:
        return redirect('student_test')
    if request.method == "POST":
        email = request.POST['email']
        password = password_to_hash(request.POST['password'])
        try:
            student = Login.objects.get(email=email, password=password)
            request.session['session_identifier'] = student.register_num
            return redirect('student_test')
        except ObjectDoesNotExist:
            return render(request, 'student/login.html', {'error': 'Invalid Credentials'})
    return render(request, 'student/login.html')


def registration(request):
    if request.method == "POST":
        name = request.POST['user-name']
        email = request.POST['user-email']
        password = password_to_hash(request.POST['user-password'])
        std = request.POST['user-class']

        obj = Student()
        obj.name = name
        obj.email = email
        obj.std_class = std
        try:
            obj.save()
        except IntegrityError:
            return render(request, 'student/register.html', {'err': 'duplicate email'})

        student_obj = Student.objects.get(email=email)
        login_obj = Login()
        login_obj.register_num = student_obj.register_num
        login_obj.password = password
        login_obj.student = student_obj
        login_obj.email = email
        login_obj.save()

        return redirect('student_test')
    return render(request, 'student/register.html')


@student_only
def exam_test(request):
    std_obj = Student.objects.get(register_num=request.session['session_identifier'])
    obj = Questions.objects.filter(std=std_obj.std_class)
    questions = obj.values_list('question', flat=True)
    term = obj.get(question=questions[0]).question_code
    if request.method == "POST":
        print(request.POST)
        answer: list = request.POST.getlist('answer')
        term: str = request.POST['term']

        ans_obj = Answers()
        for i in range(len(answer)):
            print(answer[i])
            ans_obj.set_answer(i, answer[i])
        ans_obj.student = std_obj
        ans_obj.question_code = term
        ans_obj.save()
        return redirect('student_home')
    return render(request, 'student/test.html', {'questions': questions, 'term': term, 'regNum': std_obj.register_num,
                                                 'Name': std_obj.name})


def home(request):
    return render(request, 'student/home.html')


def analysis(request):
    pass

