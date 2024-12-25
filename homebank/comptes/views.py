from django.shortcuts import render,redirect, HttpResponse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .forms import LoginForm, PaymentForm, PersonneForm
from django.contrib.auth.decorators import login_required
from .models import Compte, Transaction
from decimal import Decimal
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm





@login_required
def acceuil(request):
    return render(request,'acceuil.html')


def Sign(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'Sign.html',{"form":form})
    
        
    


def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('acceuil')
        else:
            messages.error(request,'Invalid login details')
    return render(request,"login.html", {'form': LoginForm})
    

    


def Comptes(request):
    user_comptes = Compte.objects.filter(proprietaire=request.user)
    return render(request,'Comptes.html', {'user_comptes': user_comptes})

def mesinfo(request):
    user_profile = request.user.personne

    if request.method == 'POST':
        form = PersonneForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('acceuil')
    else:
        form = PersonneForm(instance=user_profile)
    return render(request,'mesinfo.html',{'form':form})



@login_required
def Virements(request):
    if request.method == 'POST':
        form = PaymentForm(request.user, request.POST)
        if form.is_valid():
            compte_emetteur = form.cleaned_data['compte_emetteur']
            compte_recepteur = form.cleaned_data['compte_recepteur']
            montant = Decimal(form.cleaned_data['montant'])
            
            
            if compte_emetteur.solde >= montant:
                compte_emetteur.solde -= montant
                compte_recepteur.solde += montant
                compte_emetteur.save()
                compte_recepteur.save()

                transaction = Transaction.objects.create(emetteur=compte_emetteur, recepteur=compte_recepteur, montant=montant)
                messages.success(request, 'Transaction effectuée avec succès.')
                return redirect('virement_success')
            
            else:
                messages.error(request, 'Solde insuffisant')
    else:
        form=PaymentForm(request.user)        
    
    return render(request, 'Virements.html', {'form': form})
def virement_success(request):
    return render(request, 'virement_success.html')

@login_required   
def transactions(request):
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'transactions.html', {'transactions': transactions})


def logout_view(request):
    logout(request)
    return redirect('login')