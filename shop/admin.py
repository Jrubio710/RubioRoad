from django.contrib import admin
from .models import Employer, Tire, Client, Sale, Details





class ClientAdmin(admin.ModelAdmin):
    search_fields = ['name', 'plate'] 
    list_display = ('name', 'plate')  

admin.site.register(Client, ClientAdmin) 

class SaleAdmin(admin.ModelAdmin):
    search_fields = ['client__name', 'employer__name'] 
    list_display = ('client', 'employer', 'date', 'total')

admin.site.register(Sale, SaleAdmin)        

class DetailsAdmin(admin.ModelAdmin):
    search_fields = ['sale__client__name', 'tire__model'] 
    list_display = ('sale', 'tire', 'quantity', 'subtotal')

admin.site.register(Details, DetailsAdmin)

class TireAdmin(admin.ModelAdmin):
    search_fields = ['brand', 'model', 'dimensions']
    list_display = ('brand', 'model', 'dimensions', 'price', 'stock')

admin.site.register(Tire, TireAdmin)

class EmployerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_display = ('name', 'email')

admin.site.register(Employer, EmployerAdmin)