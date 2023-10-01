from rest_framework import serializers
from splitwise.models import Transaction, Due, Expense, Contribution


class DueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Due
        fields = [
            "from_user",
            "to_user",
            "amount",
            "expense"
        ]


class ContributionSerializer(serializers.Serializer):

    class Meta:
        model = Contribution
        fields = [
            "percent",
            "user",
            "expense",
        ]


class ExpenseSerializer(serializers.ModelSerializer):
    contributions = ContributionSerializer(write_only=True)

    class Meta:
        model = Expense
        fields = [
            "amount",
            "payer",
            "title",
            "notes",
            "contributions",
        ]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "from_user",
            "to_user",
            "amount",
            "expense"
        ]

