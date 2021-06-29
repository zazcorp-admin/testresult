from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.views import View
from .forms import *

# Create your views here.
def index(request):
    short = TestResult.objects.order_by('-test_date')
    context = {
        'short':short
    }
    return render(request, 'core/index.html', context)


def loginFunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('AdminPanel')
    return render(request, 'core/login.html')


def logoutFunc(request):
    logout(request)
    return redirect('Home')


def desc(request, pk):
    test = TestResult.objects.get(pk=pk)
    context = {
        'test':test
    }
    return render(request, 'core/desc.html', context)


def adminPanel(request):
    terms = TermsAndCondition.objects.all()
    tests = TestResult.objects.order_by('-test_date')
    context = {
        'tests':tests,
        'terms': terms
    }
    return render(request, 'core/admin_panel.html', context)


def delete_test(request, pk):
    test = TestResult.objects.get(pk=pk)
    if request.method == 'POST':
        test.delete()
        return redirect('AdminPanel')
    context = {
        'test':test
    }

    return render(request, 'core/delete.html', context)

class AddTestView(View):
    def get(self, request):
        form = TestResultForm()
        context = {
            'form':form
        }
        return render(request, 'core/add_test.html', context)
    def post(self, request):
        form = TestResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPanel')

def updateTest(request, pk):
    test = TestResult.objects.get(pk=pk)
    form = TestResultForm(instance=test)
    if request.method == 'POST':
        form = TestResultForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
            return redirect('AdminPanel')
    context = {
        'form':form
    }
    return render(request, 'core/update_test.html', context)


def terms_and_condition(request):
    terms = TermsAndCondition.objects.all()
    context = {'terms':terms}
    return render(request, 'core/terms.html', context)

def update_terms(request, pk):
    terms = TermsAndCondition.objects.get(pk=pk)
    form = TermsForm(instance=terms)
    if request.method == 'POST':
        form = TermsForm(request.POST, instance=terms)
        if form.is_valid():
            form.save()
    context = {
        'form':form
    }
    return render(request, 'core/edit_terms.html', context)


