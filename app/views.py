from django.http.response import HttpResponse
from django.http.request import HttpRequest

def near_hundred_view(request:HttpRequest, num:int) -> HttpResponse:
    if (num in range(90, 111)) or (num in range(190, 211)):
        return HttpResponse(True)
    return HttpResponse(False)

def string_splosion_view(request:HttpRequest, word:str) -> HttpResponse:
    newWord = ''
    count = 1
    while count <= len(word):
        newWord += word[:count]
        count += 1
    return HttpResponse(newWord)

def cat_dog_view(request:HttpRequest, word:str) -> HttpResponse:
    return HttpResponse(word.count('dog') == word.count('cat'))

def lone_sum_view(request:HttpRequest, a:int, b:int, c:int) -> HttpResponse:
    if a == b and b == c:
        return HttpResponse(0)
    elif a == b:
        return HttpResponse(c)
    elif a == c:
        return HttpResponse(b)
    elif c == b:
        return HttpResponse(a)
    else: 
        return HttpResponse(a + b + c)
    
