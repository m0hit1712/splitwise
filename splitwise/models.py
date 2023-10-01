from django.db import models

from user_auth.models import User


class Expense(models.Model):
    class Type(models.TextChoices):
        equal = "EQUAL"
        exact = "EXACT"
        percent = "PERCENT"

    amount = models.IntegerField()
    payer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    notes = models.TextField()
    type = models.CharField(choices=Type.choices, max_length=20)


class Contribution(models.Model):
    percent = models.IntegerField()
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Due(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="due_to_user")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="due_from_user")
    amount = models.IntegerField()
    contribution = models.OneToOneField(Contribution, on_delete=models.CASCADE)


class Transaction(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transaction_to_user")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transaction_from_user")
    amount = models.IntegerField()
    contribution = models.OneToOneField(Contribution, on_delete=models.CASCADE)

