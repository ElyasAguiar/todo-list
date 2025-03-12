from django import forms
from django.contrib.auth.models import User
from .models import Commitment


class CommitmentForm(forms.ModelForm):
    convidados = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False, widget=forms.SelectMultiple)

    class Meta:
        model = Commitment
        fields = [
            "title",
            "describe",
            "status",
            "date_commitmment",
            "category",
            "convidados",
        ]
