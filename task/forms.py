from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Commitment
from .models import Step
from .models import Category

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

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
widgets = {
            'date_commitmment': forms.DateInput(attrs={'type': 'date'}),
        }

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['title', 'describe']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
