from django import forms
from .models import Compte, Personne


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


    

class PaymentForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['compte_emetteur'].queryset = Compte.objects.filter(proprietaire=user)
    
    compte_emetteur = forms.ModelChoiceField(queryset= Compte.objects.all())
    compte_recepteur = forms.ModelChoiceField(queryset=Compte.objects.all())
    montant = forms.DecimalField()
    
class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['Prenom','Nom','date_naissance','telephone','adresse','email','ville'] 