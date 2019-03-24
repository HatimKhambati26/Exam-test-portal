from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import DetailsForm, IOTForm, EHForm, ARForm, MLForm
from .models import Detail

abc = None
xyz=None

# Create your views here.
@login_required(login_url='/login')
def details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        post = Detail()
        global abc
        global xyz 
        abc=request.POST.get('name')
        xyz=request.POST.get('phone')
        post.course = request.POST.get('course')
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect("/details/{}/".format(str(post.course)))
    else:
        form = DetailsForm()
        return render(request, 'fpage/details.html')


@login_required(login_url='/details')
def iot(request):
    ch = 0
    if request.method == 'POST':
        form = IOTForm(request.POST)
        post = Detail
        
        post.q1 = request.POST.get('q1')
        if post.q1=='1':
            ch+=1
        
        post.q2 = request.POST.get('q2')
        if post.q2=='2':
            ch+=1
        
        post.q3 = request.POST.get('q3')
        if post.q3=='3':
            ch+=1
        
        post.q4 = request.POST.get('q4')
        if post.q4=='4':
            ch+=1
        
        post.q5 = request.POST.get('q5')
        if post.q5=='1':
            ch+=1
        
        post.q6 = request.POST.get('q6')
        if post.q6=='2':
            ch+=1

        post.q7 = request.POST.get('q7')
        if post.q7=='3':
            ch+=1
        
        post.q8 = request.POST.get('q8')
        if post.q8=='4':
            ch+=1

        post.q9 = request.POST.get('q9')
        if post.q9=='1':
            ch+=1

        post.q10 = request.POST.get('q10')
        if post.q10=='4':
            ch+=1
        
        Detail.objects.filter(name=abc,phone=xyz).update(score=ch)
        return redirect('/logout/')
    else:
        return render(request, 'quest/IOT.html')


@login_required(login_url='/details')
def eh(request):
    ch = 0
    if request.method == 'POST':
        form = EHForm(request.POST)
        post = Detail
        
        post.q1 = request.POST.get('q1')
        if post.q1=='1':
            ch+=1
        
        post.q2 = request.POST.get('q2')
        if post.q2=='2':
            ch+=1
        
        post.q3 = request.POST.get('q3')
        if post.q3=='3':
            ch+=1
        
        post.q4 = request.POST.get('q4')
        if post.q4=='4':
            ch+=1
        
        post.q5 = request.POST.get('q5')
        if post.q5=='1':
            ch+=1
        
        post.q6 = request.POST.get('q6')
        if post.q6=='2':
            ch+=1

        post.q7 = request.POST.get('q7')
        if post.q7=='3':
            ch+=1
        
        post.q8 = request.POST.get('q8')
        if post.q8=='4':
            ch+=1

        post.q9 = request.POST.get('q9')
        if post.q9=='1':
            ch+=1

        post.q10 = request.POST.get('q10')
        if post.q10=='4':
            ch+=1
        
        Detail.objects.filter(name=abc,phone=xyz).update(score=ch)
        return redirect('/logout/')
    else:
        return render(request, 'quest/EH.html')

    

@login_required(login_url='/details')
def ar(request):
    ch = 0
    if request.method == 'POST':
        form = ARForm(request.POST)
        post = Detail
        
        post.q1 = request.POST.get('q1')
        if post.q1=='1':
            ch+=1
        
        post.q2 = request.POST.get('q2')
        if post.q2=='2':
            ch+=1
        
        post.q3 = request.POST.get('q3')
        if post.q3=='3':
            ch+=1
        
        post.q4 = request.POST.get('q4')
        if post.q4=='4':
            ch+=1
        
        post.q5 = request.POST.get('q5')
        if post.q5=='1':
            ch+=1
        
        post.q6 = request.POST.get('q6')
        if post.q6=='2':
            ch+=1

        post.q7 = request.POST.get('q7')
        if post.q7=='3':
            ch+=1
        
        post.q8 = request.POST.get('q8')
        if post.q8=='4':
            ch+=1

        post.q9 = request.POST.get('q9')
        if post.q9=='1':
            ch+=1

        post.q10 = request.POST.get('q10')
        if post.q10=='4':
            ch+=1
        
        Detail.objects.filter(name=abc,phone=xyz).update(score=ch)
        return redirect('/logout/')
    else:
        return render(request, 'quest/AR.html')



@login_required(login_url='/details')
def ml(request):
    ch = 0
    if request.method == 'POST':
        form = MLForm(request.POST)
        post = Detail
        
        post.q1 = request.POST.get('q1')
        if post.q1=='1':
            ch+=1
        
        post.q2 = request.POST.get('q2')
        if post.q2=='2':
            ch+=1
        
        post.q3 = request.POST.get('q3')
        if post.q3=='3':
            ch+=1
        
        post.q4 = request.POST.get('q4')
        if post.q4=='4':
            ch+=1
        
        post.q5 = request.POST.get('q5')
        if post.q5=='1':
            ch+=1
        
        post.q6 = request.POST.get('q6')
        if post.q6=='2':
            ch+=1

        post.q7 = request.POST.get('q7')
        if post.q7=='3':
            ch+=1
        
        post.q8 = request.POST.get('q8')
        if post.q8=='4':
            ch+=1

        post.q9 = request.POST.get('q9')
        if post.q9=='1':
            ch+=1

        post.q10 = request.POST.get('q10')
        if post.q10=='4':
            ch+=1
        
        Detail.objects.filter(name=abc,phone=xyz).update(score=ch)
        return redirect('/logout/')
    else:
        return render(request, 'quest/ML.html')




