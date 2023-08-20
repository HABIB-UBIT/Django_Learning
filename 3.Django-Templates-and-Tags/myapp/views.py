from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict={
        'pages': ['one','two','three','four'],
        'courses':['frontend','backend','AI/ML','DevOps']
    }
    return render(request, 'myapp/index.html', context= my_dict)
 
def home(request):
    return render(request, 'myapp/home.html')