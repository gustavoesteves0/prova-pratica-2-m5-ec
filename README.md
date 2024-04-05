# Prova Prática 2

## Objetivo

O objetivo desta atividade é montar uma interface web com Flask e HTMX. É necessário também a criação de uma tela de logs para registrar as ações do servidor. 

## Atividades Desenvolvidas

1. Frontend em HTMX:

index.html:
![image](https://github.com/gustavoesteves0/prova-pratica-2-m5-ec/assets/123904558/e7e334ce-6bd0-4fe9-b16d-871b8ba27a97)

logs.html:

![image](https://github.com/gustavoesteves0/prova-pratica-2-m5-ec/assets/123904558/e695aeeb-7874-47b5-96c9-7591378d137e)

2. Backend em Flask e TinyDB

app.py:

![image](https://github.com/gustavoesteves0/prova-pratica-2-m5-ec/assets/123904558/90e8deb1-a235-4cd6-99b8-e10d36c3ad68)

![image](https://github.com/gustavoesteves0/prova-pratica-2-m5-ec/assets/123904558/25314577-6da5-4170-8c37-e97d988326ec)




## Estrutura de Pastas

Os arquivos do repositório estão organizados da seguinte forma:

```
├── src
│  ├── backend /
│  ├── templates /
│  │  ├── index.html
│  │  ├── logs.html
│  ├── app.py
│  db.json
│  package-lock.json

```


## Como utilizar 
Para executar o projeto na sua máquina execute os seguintes passos no terminal.

1º Criar um ambiente virtual na pasta src

<code>python -m venv venv </code>

2º Ativar o ambiente virtual 
 
<code> cd venv </code>

<code> cd Scripts </code>

<code> activate </code>

3º Instalar as dependências 

<code> pip install -r requirements.txt </code>

4º Rodar o arquivo app

<code> python3 app.py  </code>

Pronto, agora é possível utilizar o projeto. 
