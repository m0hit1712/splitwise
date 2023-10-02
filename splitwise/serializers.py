from rest_framework import serializers
from splitwise.models import Transaction, Due, Expense, Contribution, Type, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
        ]


class DueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Due
        fields = [
            "from_user",
            "to_user",
            "amount",
        ]
        read_only_fields = (
            "contribution",
        )


class ContributionSerializer(serializers.ModelSerializer):
    amount = serializers.CharField(allow_null=True)
    percent = serializers.CharField(allow_null=True)

    class Meta:
        model = Contribution
        fields = [
            "percent",
            "user",
            "amount",
            "expense"
        ]
        read_only_fields = [
            "expense",
        ]


class ExpenseSerializer(serializers.ModelSerializer):
    contributions = ContributionSerializer(many=True)

    class Meta:
        model = Expense
        fields = [
            "contributions",
            "amount",
            "payer",
            "title",
            "notes",
            "type"
        ]

    def validate(self, attrs):
        if attrs["type"] == Type.percent:
            total_percent = 0
            for contribution in attrs["contributions"]:
                total_percent += float(contribution["percent"])
            if total_percent != 100:
                raise serializers.ValidationError(
                    "Total percentage of all contribution percentage cannot be below or above 100"
                )
        elif attrs["type"] == Type.exact:
            total_contributions_amount = 0
            for contribution in attrs["contributions"]:
                total_contributions_amount += float(contribution["amount"])
            if not total_contributions_amount != attrs["amount"]:
                raise serializers.ValidationError(
                    "Total contributions cannot be lesser or greater than expense amount"
                )
        return super().validate(attrs)

    def create(self, validated_data):
        contributions = validated_data.pop("contributions")
        expense = Expense.objects.create(
            **validated_data
        )
        if expense.type == Type.equal:
            users = [c["user"] for c in contributions]
            expense.create_equal_contributions(users)
        elif expense.type in [Type.percent, Type.exact]:
            contributions = [
                Contribution(
                    **{
                        "type": expense.type,
                        "expense": expense,
                        **contribution
                    }
                )
                for contribution in contributions
            ]
            Contribution.objects.bulk_create(contributions)
        expense.create_dues()
        return expense


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "from_user",
            "to_user",
            "amount",
        ]
        read_only_fields = (
            "contribution",
        )

