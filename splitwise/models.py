from django.db import models


class User(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=12)


class Type(models.TextChoices):
    equal = "EQUAL"
    exact = "EXACT"
    percent = "PERCENT"


class Expense(models.Model):
    amount = models.FloatField()
    payer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    notes = models.TextField()
    type = models.CharField(choices=Type.choices, max_length=20)

    def resolve_dues_cycle(self, new_dues):
        # Resolve all the cycles by checking existing expenses and dues
        pass

    def create_dues(self):
        contributions = self.contributions.all()
        dues = [
            Due(
                from_user=contribution.user,
                to_user=self.payer,
                amount=contribution.amount,
                contribution=contribution
            )
            for contribution in contributions
        ]
        # dues = self.resolve_dues_cycle(dues)
        Due.objects.bulk_create(dues)

    def create_equal_contributions(self, users):
        amount = self.amount
        total_users = len(users)
        percentage_share = round(100 / total_users, 2)
        first_user_share = percentage_share + (100 - total_users * percentage_share)
        contributions = [
            Contribution(
                user=users[0],
                percent=first_user_share,
                amount=round(first_user_share * amount / 100, 5),
                type=Type.equal.value,
                expense=self
            )
        ]
        contributions.extend([
            Contribution(
                user=user,
                percent=percentage_share,
                amount=round(percentage_share * amount / 100, 5),
                type=Type.equal.value,
                expense=self
            )
            for user in users[1:]
        ])
        return Contribution.objects.bulk_create(contributions)


class Contribution(models.Model):
    type = models.CharField(choices=Type.choices, max_length=20)
    percent = models.FloatField(null=True)
    amount = models.FloatField(null=True)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name="contributions")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Due(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="due_from_user")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="due_to_user")
    amount = models.FloatField()
    contribution = models.OneToOneField(Contribution, on_delete=models.CASCADE)


class Transaction(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transaction_from_user")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transaction_to_user")
    amount = models.FloatField()
    contribution = models.OneToOneField(Contribution, on_delete=models.CASCADE)

