from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CommitmentForm, UserCreationFormWithEmail
from .models import Commitment, Category
from django.utils import timezone
from django.core.mail import send_mail

import logging
# Create your views here.

# Home do Projeto

logger = logging.getLogger(__name__)

def home(request):
    return render(request, "home.html")


def sigup(request):
    if request.method == "GET":
        return render(request, "sigup.html", {"form": UserCreationFormWithEmail})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                    email=request.POST["email"],  # Adiciona o campo de email
                )
                user.save()
                login(request, user)
                return redirect("commitments")
            except:
                return render(
                    request,
                    "sigup.html",
                    {"form": UserCreationFormWithEmail, "error": "Usuário já existe"},
                )
        return render(
            request,
            "sigup.html",
            {"form": UserCreationFormWithEmail, "error": "senhas são diferentes"},
        )


def sigin(request):

    if request.method == "GET":
        return render(request, "sigin.html", {"form": AuthenticationForm})

    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )

        if user is None:
            return render(
                request,
                "sigin.html",
                {
                    "form": AuthenticationForm,
                    "error": "Usuário ou senha está incorreto",
                },
            )

        else:
            login(request, user)
            return redirect("commitments")


@login_required
def sair(request):
    logout(request)
    return redirect("home")


# @login_required
# def commitments(request):
#     return render(request, "commitments.html")


@login_required
def criando_tarefa(request):

    if request.method == "GET":
        categories = Category.objects.all()
        return render(
            request,
            "criando_tarefa.html",
            {"form": CommitmentForm, "categories": categories},
        )
    else:
        try:
            form = CommitmentForm(request.POST)
            new_commitment = form.save(commit=False)
            new_commitment.user = request.user
            logger.info(f"Usuário {request.user} criou a tarefa {new_commitment.title}")
            new_commitment.save()
            return redirect("commitments")

        except ValueError as e:
            logger.error(f"Erro ao criar a tarefa {e}")
            return render(
                request,
                "criando_tarefa.html",
                {"form": CommitmentForm, "error": "Favor inserir dados validos"},
            )


@login_required
def commitments(request):
    commitments = Commitment.objects.filter(user=request.user).order_by(
        "-date_commitmment"
    )
    return render(request, "commitments.html", {"commitments": commitments})


@login_required
def commitment_detalhe(request, commitment_id):
    if request.method == "GET":
        commitment = get_object_or_404(Commitment, pk=commitment_id, user=request.user)
        form = CommitmentForm(instance=commitment)
        return render(
            request, "commitment_detalhe.html", {"commitment": commitment, "form": form}
        )
    else:
        return update_commitment(request, commitment_id)


# completar tarefa
@login_required
def complete_tarefa(request, commitment_id):
    task = get_object_or_404(Commitment, pk=commitment_id, user=request.user)

    if request.method == "POST":
        task.datecompleted = timezone.now()
        task.save()
        return redirect("commitments")


# deletar tarefa
@login_required
def deletar_tarefa(request, commitment_id):
    task = get_object_or_404(Commitment, pk=commitment_id, user=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("commitments")


# exibir todas as tarefas completadas
@login_required
def exibir_tarefas_completadas(request):
    commitments = Commitment.objects.filter(
        user=request.user,
        status="completed",
    ).order_by
    ("-date_commitmment")
    return render(request, "commitments.html", {"commitments": commitments})

def editar_commitment(request, commitment_id):
    commitment = get_object_or_404(Commitment, id=commitment_id)
    if request.method == 'POST':
        form = CommitmentForm(request.POST, instance=commitment)
        if form.is_valid():
            form.save()
            form.save_m2m()  # Save the many-to-many data for convidados
            return redirect('task:detalhes', commitment_id=commitment.id)
    else:
        form = CommitmentForm(instance=commitment)
    return render(request, 'task/editar_commitment.html', {'form': form})

def update_commitment(request, commitment_id):
    commitment = get_object_or_404(Commitment, id=commitment_id)
    if request.method == 'POST':
        form = CommitmentForm(request.POST, instance=commitment)
        if form.is_valid():
            commitment = form.save()
            # Enviar notificação para os novos convidados
            convidados = form.cleaned_data.get('convidados')
            for convidado in convidados:
                print(convidado)
                send_mail(
                    'Você foi adicionado a um compromisso',
                    f'Você foi adicionado ao compromisso: {commitment.title}',
                    'from@example.com',
                    [convidado.email],
                    fail_silently=False,
                )
            return redirect('commitment_detalhe', commitment_id=commitment.id)
    else:
        form = CommitmentForm(instance=commitment)
    return render(request, 'commitment_detalhe.html', {'form': form, 'commitment': commitment})
