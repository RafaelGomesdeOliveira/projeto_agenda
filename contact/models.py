from django.db import models
from django.utils import timezone

# Create your models here.
#ID é automático

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True) #Não precisa informar informar a limitação, mas pode informar
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/') #Se obrigar a ter imagem e conter contatos sem, vai acabar gerando um erro
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True) #Uma categoria para vários contatos linkados 
    #CASCADE apaga os contatos quando eu apagar a categoria // SET_NULL seta como nulo quando apago a categoria, mas eu tenho que informar o blank=True e Null = True
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'