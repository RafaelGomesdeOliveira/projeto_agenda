from django import forms
from django.core.exceptions import ValidationError
from contact.views import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation



class ContactForm(forms.ModelForm):
    
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False,

    )

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',]

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={ #Serve para adicioanr atributos ao input: class, placeholder, etc
        #             'class': 'classe-a classe-b', 
        #             'placeholder': 'Seu nome'
        #         }
        #     )
        # }

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class-a class-b',
                'placeholder': "Seu nome aqui",
            }
        ),
        label='Primeiro nomee',
        help_text='Texto de ajuda para o usuário'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update( #Aqui estou atualizando os wigets do campo
        #         {
        #             'class': 'message error',
        #             'placeholder': "Seu nome aqui",
        #         }
        # ) 

    

    def clean(self): #Aqui eu vou trabalhar quando depender de outros campos
        cleaned_data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg_erro = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )

            self.add_error('first_name', msg_erro)
            self.add_error('last_name', msg_erro)
        

        return super().clean()

    def clean_first_name(self): #Aqui tabalhamos quando temos um campo em específico 
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error( #add_error da continuidade em todos os erros, já o raise para em um único erro
            'first_name',
            ValidationError(
                'Não digite ABC nesse campo',
                code='Invalid'
            )
        )


        return first_name
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        error_messages={
            'required': 'Preencha este campo',
            'min_lenght': 'Nome muito pequeno',

        }
    )

    last_name = forms.CharField(
        required=True,
        min_length=3,
        error_messages={
            'required': 'Preencha este campo',
            'min_lenght': 'Nome muito pequeno',

        }
    )

    email = forms.EmailField()



    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
        )

    def clean_email(self):

        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError
                (
                    'Já existe este email', 
                    code='invalid'
                )
            )

        return email

class RegisterUpdateForm(forms.ModelForm):

    
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username',
        )    

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')
        

        if password:
            user.set_password(password)
        
        if commit:
            user.save()
        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('As senhas não batem')
                )

        return super().clean()


    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)

                )

        return password1
