from django import forms
from .models import Commitment


class CommitmentForm(forms.ModelForm):
    class Meta:
        model = Commitment
        fields = [
            "title",
            "describe",
            "status",
            "date_commitmment",
            "category",
        ]
