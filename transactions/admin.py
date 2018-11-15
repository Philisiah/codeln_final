from django.contrib import admin

from transactions.models import Candidate, Transaction, TestInvitation


# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    pass


class CandidateInline(admin.TabularInline):
    model = Candidate


admin.site.register(Candidate, CandidateAdmin)


class TransactionAdmin(admin.ModelAdmin):
    inlines = [
        CandidateInline,
    ]


class TestInvitationAdmin(admin.ModelAdmin):
    pass


admin.site.register(TestInvitation, TestInvitationAdmin)
admin.site.register(Transaction, TransactionAdmin)
