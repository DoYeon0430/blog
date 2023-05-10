from django.shortcuts import render

# Create your views here.
def home(request):
    myprofile_home = {'homepage':'Doyeon0430'}
    return render(request,'myprofile/home.html', myprofile_home)

def main(request):
    main = {'main':'Doyeon0430'}
    return render(request,'myprofile/main.html', main)

def work(request):
    work = {'work':'Doyeon0430'}
    return render(request,'myprofile/work.html', work)

def ilcense(request):
    ilcense = {'ilcense':'Doyeon0430'}
    return render(request,'myprofile/ilcense.html', ilcense)

def hobby(request):
    hobby = {'hobby':'Doyeon0430'}
    return render(request,'myprofile/hobby.html', hobby)

def school(request):
    school = {'school':'Doyeon0430'}
    return render(request,'myprofile/school.html', school)