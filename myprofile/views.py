from django.shortcuts import render

# Create your views here.
def home(request):
    myprofile_home = {'homepage':'Doyeon0430'}
    return render(request,'myprofile/home.html', myprofile_home)

def main(request):
    main = {'main':'Doyeon0430'}
    return render(request,'myprofile/main.html', main)

def twenty(request):
    twenty = {'twenty':'Doyeon0430'}
    return render(request,'myprofile/twenty.html', twenty)

def twentyone(request):
    twentyone = {'twentyone':'Doyeon0430'}
    return render(request,'myprofile/twentyone.html', twentyone)

def twentytwo(request):
    twentytwo = {'twentytwo':'Doyeon0430'}
    return render(request,'myprofile/twentytwo.html', twentytwo)

def twentythree(request):
    twentythree = {'twentythree':'Doyeon0430'}
    return render(request,'myprofile/twentythree.html', twentythree)