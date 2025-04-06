from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'home.html', {'name':'Aditya'})
def Add(request):
    val1=int(request.POST['Num1'])
    val2=int(request.POST['Num2'])
    res=val1+val2
    return render(request, 'result.html', {'Result': res})