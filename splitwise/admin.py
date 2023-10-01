from django.contrib import admin

from splitwise.models import Due, Expense, Transaction


# Register your models here.

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass


@admin.register(Due)
class DueAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass





