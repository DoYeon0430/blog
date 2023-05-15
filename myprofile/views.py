from django.shortcuts import render

# Create your views here.
def home(request):
    myprofile_home = {'homepage':'Doyeon0430'}
    return render(request,'myprofile/home.html', myprofile_home)

def main(request):
    main = {'main':'Doyeon0430'}
    return render(request,'myprofile/main.html', main)

def introduce(request):
    introduce = {'introduce':'Doyeon0430'}
    return render(request,'myprofile/introduce.html', introduce)

def story(request):
    story = {'story':'Doyeon0430'}
    return render(request,'myprofile/story.html', story)