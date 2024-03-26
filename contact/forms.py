from django import forms
from django.core.exceptions import ValidationError
from contact.views import Contact


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
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