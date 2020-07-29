from heart.models import Videos, Perfil, Coment
from django import forms
from django.contrib.auth.models import User

class Creat_Video(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['Titulo','Categoria','Video','user']
        widgets ={
            'Titulo': forms.TextInput(attrs={'class':'form-control'}),
            'Categoria':forms.TextInput(attrs={'class':'form-control'}),
            'Video':forms.FileInput(attrs={'class':'form-control'}),
            'user': forms.Select(attrs={'class':'form-control'}),
        }

class Creat_Perfil(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['Usuario','NikeName','Historia','Foto']
        widgets = {
            'Usuario': forms.Select(attrs={'class':'form-control'}),
            'NikeName': forms.TextInput(attrs={'class':'form-control'}),
            'Historia': forms.TextInput(attrs={'class':'form-control'}),
            'Foto': forms.FileInput(attrs={'class':'form-control'}),
        }

class Creat_Coment(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ['user','video','Comentario']
        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            'video': forms.Select(attrs={'class':'form-control'}),
            'Comentario':forms.TextInput(attrs={'class':'form-control'}),
        }
class Creat_user(forms.Form):
    Username = forms.CharField(label='entre com o seu nome:',min_length=4,max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    Email = forms.EmailField(label='Digite seu email:',widget=forms.EmailInput(attrs={'class':'form-control'}))
    Password = forms.CharField(label='digite seu senha:',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Confirma senha',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def save(self,commit=True):
        user = User.objects.create_user(
            self.cleaned_data['Username'],
            self.cleaned_data['Email'],
            self.cleaned_data['Password'],
        )
        return user