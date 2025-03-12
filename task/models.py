from django.db import models
from django.contrib.auth.models import User


class Commitment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pendente"),
        ("in_progress", "Em Andamento"),
        ("completed", "Concluído"),
    ]

    title = models.CharField(max_length=100)
    describe = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
        null=True,
        blank=True,
    )
    date_commitmment = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, null=True, blank=True
    )
    convidados = models.ManyToManyField(User, related_name='commitments_convidados', blank=True)

    def __str__(self):
        return self.title + " - by: " + self.user.username


class Step(models.Model):
    title = models.CharField(max_length=100)
    describe = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    commitment = models.ForeignKey("Commitment", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title + " - by: " + self.commitment.user.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Invitation(models.Model):
    commitment = models.ForeignKey("Commitment", on_delete=models.CASCADE)
    invited_user = models.ForeignKey(User, on_delete=models.CASCADE)
    invited_by = models.ForeignKey(
        User, related_name="invitations_sent", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Convite de {self.invited_user.username} para {self.commitment.title} by {self.invited_by.username}"


class Notification(models.Model):
    title = models.CharField(max_length=100)
    describe = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commitment = models.ForeignKey(
        "Commitment", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title + " - by: " + self.user.username
