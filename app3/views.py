from django.shortcuts import render

# Create your views here.
def hobbies(request):
    return render(request,'hobbies.html')
