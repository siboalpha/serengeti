from django.contrib import admin
from cms.models import Customers
from  django.contrib.auth.models  import  Group



# Register your models here.
@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "email", "phone_number", "address")
    search_fields = ("id", "name", "surname")


admin.site.unregister(Group)
