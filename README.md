# ToDo List / Agenda de Lembretes

Todo List ou agenda de Lembretes com Python, Django e Bootstrap.

Nesta aplicação você vai poder cadastrar, exibir, editar e marcar como completada uma determinada tarefa.

## Como Rodar a Aplicação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/todo-list-django.git
    cd todo-list-django
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Realize as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

6. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:8000/
    ```

## Como Criar Usuários

1. Crie um superusuário para acessar o painel administrativo do Django:
    ```bash
    python [manage.py](http://_vscodecontentref_/0) createsuperuser
    ```

2. Siga as instruções no terminal para definir um nome de usuário, email e senha.

3. Acesse o painel administrativo no navegador:
    ```
    http://127.0.0.1:8000/admin/
    ```

4. Faça login com o superusuário criado e adicione novos usuários através da interface administrativa.

## Capturas de Tela

![Captura de tela de 2022-11-27 16-56-08 (1)](https://user-images.githubusercontent.com/27355729/204156937-015697cf-1b55-4783-a2f4-6a98e8c0cbca.png)

![2](https://user-images.githubusercontent.com/27355729/204157036-82042fee-26ea-49e1-a45c-466ce1238aa9.png)