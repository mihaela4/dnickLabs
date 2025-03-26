from django.contrib import admin
from .models import Book, Author, Zanr, Preveduvac, Rating

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("naslov", "avtor", "korisnik", "dostapnost")
    exclude = ("korisnik",) #za user samo da ne si go setira
    #inlines = (Rating,)

    def save_model(self, request, obj, form, change):
        obj.korisnik = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.korisnik == request.user:
            return True
        return False
    #ako toj so menja e korisnik onda moze da smeni svoi knigi?

class RatingAdmin(admin.ModelAdmin):
    list_display = ("book", "korisnik","ocenka")

    def has_delete_permission(self, request, obj=None):
        if obj and obj.korisnik == request.user:
            #ako ovoj obj od korisnikot e istiot so ovoj obj so go iame
            return True
        return False

class ZanrAdmin(admin.ModelAdmin):
    list_display = ("ime", "zanrIzbor")

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser
    #zasto za da dodades zanr mora da si superuser

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Zanr, ZanrAdmin)
admin.site.register(Preveduvac)
admin.site.register(Rating, RatingAdmin)