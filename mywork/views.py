from django.shortcuts import render

def main(request):
    main = {'main':'Doyeon0430'}
    return render(request,'mywork/main.html', main)

def produce(request):
    produce = {'produce':'Doyeon0430'}
    return render(request,'mywork/produce.html', produce)

def preproduction(request):
    preproduction = {'preproduction':'Doyeon0430'}
    return render(request,'mywork/preproduction.html', preproduction)

def production(request):
    production = {'production':'Doyeon0430'}
    return render(request,'mywork/production.html', production)