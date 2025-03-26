from django.db import models
from django.contrib.auth.models import User  # Import Django's User model


# Create your models here.

class Author(models.Model):
    ime = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.ime
    #ako vo kniga zsakavme da go prikazeme i prezimeto ako go imase onda dali ovde treba kako string

class Zanr(models.Model):
    ZANR_CHOICES = [
        ("N", "NOVEL"),
        ("T", "THRILLER"),
        ("H" ,"HISTORY"),
        ("F" ,"FANTASY"),
        ("B" ,"BIOGRAPHY"),
        ("C" ,"CLASSICS"),
        ("D" ,"DRAMA"),
    ]
    ime = models.CharField(max_length=100)
    opis = models.CharField(max_length=1000)
    zanrIzbor = models.CharField(max_length=1, choices=ZANR_CHOICES)

    def __str__(self):
        return f"{self.get_zanrIzbor_display()}"

class Preveduvac(models.Model):
    ime = models.CharField(max_length=100)
    nacionalnost = models.CharField(max_length=100)
    datumRagjanje = models.DateField()

    def __str__(self):
        return f"{self.ime} ({self.nacionalnost})"




class Book(models.Model):
    naslov = models.CharField(max_length=100)
    avtor = models.ForeignKey(Author, on_delete=models.CASCADE)
    #poso e eden iame foreign key??
    brojStranici = models.IntegerField()
    dostapnost = models.BooleanField()
    korica = models.ImageField(upload_to="book_photos/", null=True, blank=True)
    datumIzdavanje = models.DateField()
    zanrovi = models.ManyToManyField(Zanr)
    preveduvaci = models.ManyToManyField(Preveduvac, blank=True)  # povekje preveduvaci, moze prazno
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.naslov} by {self.avtor.ime} ({self.korisnik.username})"

class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="ratings")
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE)
    ocenka = models.IntegerField(choices=[(1, "★☆☆☆☆"), (2, "★★☆☆☆"), (3, "★★★☆☆"), (4, "★★★★☆"), (5, "★★★★★")])
    komentar = models.TextField(blank=True)

    def __str__(self):
        return f"{self.korisnik.username} rated {self.book.naslov} {self.ocenka} stars"
#class Korisnik(models.Model):


