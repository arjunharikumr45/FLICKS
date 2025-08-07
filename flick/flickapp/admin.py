from django.contrib import admin

from.models import*

admin.site.register(adminpanel)






class Payment1Admin(admin.ModelAdmin):
    list_display = ('username', 'subscription_plan', 'amount', 'cvv', 'paid_at')
    list_filter = ('subscription_plan', 'paid_at')
    search_fields = ('username', 'subscription_plan')

admin.site.register(Payment1, Payment1Admin)