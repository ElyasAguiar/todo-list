"""appYoutube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("sigup/", views.sigup, name="sigup"),
    path("sigin/", views.sigin, name="sigin"),
    path("sair/", views.sair, name="sair"),
    path("commitments/", views.commitments, name="commitments"),
    path("criando/tarefa/", views.criando_tarefa, name="criando_tarefa"),
    path("criando/<int:commitment_id>/", views.commitment_detalhe, name="commitment_detalhe"),
    path(
        "criando/<int:commitment_id>/complete", views.complete_tarefa, name="complete_tarefa"
    ),
    path("criando/<int:commitment_id>/delete", views.deletar_tarefa, name="deletar_tarefa"),
    path(
        "exibir_tarefas_completadas",
        views.exibir_tarefas_completadas,
        name="exibir_tarefas_completadas",
    ),
    path("criando/<int:commitment_id>/add_step", views.add_step, name="add_step"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/create/", views.category_create, name="category_create"),
    path("categories/<int:category_id>/", views.category_detail, name="category_detail"),
    path("categories/<int:category_id>/update/", views.category_update, name="category_update"),
    path("categories/<int:category_id>/delete/", views.category_delete, name="category_delete"),
]
