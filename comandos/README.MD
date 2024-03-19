```

python3 -m venv 'nome da venv'
. 'nome da venv'/bin/activate
pip install django
django-admin startproject 'nome do projeto' .

```

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
git remote add "Nome do Repositório Remoto" git@github.com:RafaelGomesdeOliveira/PROJETO_AGENDA.git (Adicionar um repositório remoto que o associa a repositório PROJETO_AGENDA)
git push o "Nome do Repositório Remoto" (Envia para o github)

git branch -m master main (modificar de master para main)

   

```