from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from .forms import QuestionForm
from django.utils import timezone
import json
import pandas as pd 
import numpy as np
from .models import Post
import ast
from .recommend_system import recommend_book

def index(request):
    database = Post.objects.all()
    database.delete()
    context = {}
    return render(request, 'main.html', context)

def user_check(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        print(form.is_valid())
        if form.is_valid(): #폼 유효성 검사
            color_prefer = request.POST.getlist('color_palettes')
            atmo_prefer = request.POST.getlist('novel_atmo')
            form.instance.color_palettes = color_prefer
            form.instance.novel_atmo = atmo_prefer
            form.save() #form.save를 한 경우
            return redirect('result_page')
    else:
        form = QuestionForm()
        return render(request, 'recommend_page.html', {'form':form})

def show_result(request):
    df = pd.read_csv('D:\\ampick\mirror\\recommend_data.csv')

    novel_atmo = Post.objects.values_list('novel_atmo', flat=True)[0]
    novel_genre = Post.objects.values_list('novel_genre', flat=True)[0]
    patient = Post.objects.values_list('patient', flat=True)[0]
    color_palettes = Post.objects.values_list('color_palettes', flat=True)[0]

    user_input = {
        'novel_atmo': ast.literal_eval(novel_atmo),
        'novel_genre':novel_genre,
        'patient':patient,
        'color_palettes':ast.literal_eval(color_palettes)}
    
    result = recommend_book(df=df, user_input=user_input).to_dict(orient='records')
    result[0]['keyword'] = ast.literal_eval(result[0]['keyword'])
    print(result)
    return render(request, 'result.html', {'result':result})