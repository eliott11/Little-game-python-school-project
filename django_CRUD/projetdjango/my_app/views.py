from django.shortcuts import render, redirect, get_object_or_404
from .models import Question

def index(request):
    questions = Question.objects.all()
    context = {'questions' : questions,}
    return render(request, 'my_app/index.html', context)

def add(request):
    return render(request, 'my_app/add.html')

def insert(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    question = Question(title=title, description=description)
    question.save()
    return redirect('my_app:index')

def edit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'my_app/edit.html', context)

def update(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.title = request.POST.get('title')
    question.description = request.POST.get('description')
    question.save()
    return redirect('my_app:index')

def delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('my_app:index')