from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect


from app.forms import UserForm

from django.http import HttpResponse

def home(request):

    uf  = UserForm()

    return render(request,'home.html',{'uf':uf})

def dataview(request):

    if request.method == 'POST':

        name = request.POST['username']


        # return HttpResponse(f'the user is {name}')

        return redirect('nitu')


    return HttpResponse("dataview")

def nitu(request):

    return HttpResponse("this is nitu function")

