from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def contact(request):
    return HttpResponse("Hello, You can contact us on socials")

def learn(request):
    my_dict={
        'name':'habib',
        'age':'23',
        'gender':'Male'
    }
    return JsonResponse(my_dict)