from django.shortcuts import render,redirect


def  index(request):
    if request.user.is_authenticated():
       return redirect('home')
    else:
        return render(request,'index.html')


def about(request):
    return render(request,'about.html')
