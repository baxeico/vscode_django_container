from django.shortcuts import render
from django.http import HttpResponse

from random import choice

def random_todo(request):
    todo_list = [
        'Buy milk',
        'Clean the room'
        'Write tutorial',
        'Read books',
    ]
    return HttpResponse(choice(todo_list))
