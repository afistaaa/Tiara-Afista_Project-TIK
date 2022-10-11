from django.db import models

# Create your models here.

class DosenFkip(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class StaffFkip(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class MahasiswaFkip(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)