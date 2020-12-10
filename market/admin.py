from django.contrib import admin
from .models import Mall, Shop, Product, User
from django.contrib.auth.admin import UserAdmin


# class AccountAdmin(UserAdmin):
#     list_display= ()
#     search_fields= ()
#     readonly_fields=('date_joined', 'last_login',)

#     filter_horizontal=()
#     list_filter=()
#     fieldsets=()


admin.site.register(Mall)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(User)

