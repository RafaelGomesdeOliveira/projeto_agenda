```

python3 -m venv 'nome da venv'
. 'nome da venv'/bin/activate
pip install django
django-admin startproject 'nome do projeto' .

```

Configuração do git e do github

```
git config --global user.name 'Seu nome'
git config --global user.email 'seuemail@gmail.com'
git config --global init.defaultBranch main
#Configurar o gitignore (É bom colocar na raiz)
git init
git add . [Para adicionar na lista os (arquivos que nesse caso são todos) que vou posteriormente comitar]
git commit -m 'Mensagem'

git log  

ssh-keygen -f ~/.ssh/rafaelGomes_rsa -t rsa -b 4096
cat ~/rafaelGomes_rsa.pub
Agora copia e cola no ssh keys do github
git remote add "Nome do Repositório Remoto" git@github.com:RafaelGomesdeOliveira/PROJETO_AGENDA.git (Adicionar um repositório remoto que o associa a repositório PROJETO_AGENDA, só é feito uma unica vez por projeto)

git push o "Nome do Repositório Remoto" main -u (Envia para o github, o -u é pra setar a main como padrão)

git branch -m master main (modificar de master para main)

```

Migração de Dados

```
python3 manage.py makemigrations (Criar as migrações)
python3 manage.py migrate ("Publicar" a migração)
```

Criando e Editando o Super Usuário
```
python3 manage.py createsuperuser
python3 manage.py changepassword 'Nome do super usuário' (Recuperar a senha)
```


CRUD MANUAL

``` python
>>> from contact.models import Contact
>>> Contact
<class 'contact.models.Contact'>
>>> c = Contact(first_name='Pedro')
>>> print(c)
Pedro 
>>> c
<Contact: Pedro >
>>> c.save()
>>> c.last_name = 'Vinicius'
>>> c.save()
>>> c.phone = '77999691979' #Informando um campo que será preenchido
>>> c.sav
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Contact' object has no attribute 'sav'
>>> c.save()
>>> c.delete() #Apaga um contato
(1, {'contact.Contact': 1})
>>> c
<Contact: Pedro Vinicius>
>>> c.save()
>>> c = Contact.objects.get(id=1)
>>> c
<Contact: João Matheus>
>>> c.fisrt_name = 'Tiago'
>>> c.save() #Cria um contato de forma lazy
>>> c.first_name = 'Tiago'
>>> c.save()
>>> c.id
1
>>> c
<Contact: Tiago Matheus>
>>> c.pk
1
>>> c = Contact.objects.get(pk=5) #O GET só retorna um único valor, se for mais ou menos dará um erro
>>> c
<Contact: Pedro Vinicius>
>>> c = Contact.objects.all() #Pega todos os contatos existentes
>>> c
<QuerySet [<Contact: Tiago Matheus>, <Contact: Rafael Gomes>, <Contact: Rafael >, <Contact: Pedro Vinicius>]>

>>> for contato in c: contato.first_name
... 
'Tiago'
'Rafael'
'Rafael'
'Pedro'
>>> for contato in c: contato #Um for imprimindo os contatos
... 
<Contact: Tiago Matheus>
<Contact: Rafael Gomes>
<Contact: Rafael >
<Contact: Pedro Vinicius>
>>> c = Contact.objects.filter(pk=10)
>>> c
<QuerySet []>
>>> c = Contact.objects.filter(pk=5) #Seleciona contatos usando um filtro e retorna uma QuerySet[]
>>> c
<QuerySet [<Contact: Pedro Vinicius>]>
>>> c = Contact.objects.all().order_by('-id') #Imprime todos os id em ordem decrescente 
>>> c
<QuerySet [<Contact: Pedro Vinicius>, <Contact: Rafael >, <Contact: Rafael Gomes>, <Contact: Tiago Matheus>]>
>>> c = Contact.objects.filter(first_name='Rafael').order_by('id') #Selecioan todos os contato com filtro em ordem crescente
>>> c
<QuerySet [<Contact: <Contact: Rafael Gomes>, <Contact: Rafael>]>

>>> c = Contact.objects.create(first_name='Edu', last_name='Antônio') #Cria o contato de uma forma não lazy
>>> c
<Contact: Edu Antônio>

```


