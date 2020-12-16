from django.db import models


class KtgAmpu(models.Model):
    nama=models.CharField(max_length=10)

    def __str__(self):
        return self.nama

class dataguru(models.Model):
    #id=models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, primary_key=True)
    # norole=models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE,null=True)
    #noid=models.IntegerField(blank=True,null=False)
    nama=models.CharField(max_length=30)
    nohp=models.CharField(max_length=15)
    alamat=models.CharField(max_length=225,null=True)
    biaya=models.IntegerField(blank=True,null=False)
    no_id=models.IntegerField()
    kelamin=models.BooleanField(default=True)
    usia=models.IntegerField(blank=True,null=True)
    link=models.CharField(max_length=100, null=True)
    catatan=models.TextField(null=True)
    foto=models.ImageField(upload_to='img/')
    portofolio=models.FileField(upload_to='document/')

    def __str__(self):
        return self.nama

class datamurid(models.Model):
    #id=models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, primary_key=True)
    # norole=models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE,null=True)
    #noid=models.IntegerField(blank=True,null=False)
    nama=models.CharField(max_length=30)
    nohp=models.CharField(max_length=15)
    alamat=models.CharField(max_length=225,null=True)
    No_id=models.IntegerField()
    pendidikan=models.ForeignKey(KtgAmpu, on_delete=models.CASCADE, null=True)
    kelamin=models.BooleanField(default=True)

    def __str__(self):
        return self.nama

class hari(models.Model):
    NamaHari=models.CharField(max_length=10)

    def __str__(self):
        return self.NamaHari

class paket(models.Model):
    NamaPaket=models.CharField(max_length=30)
    hari=models.ForeignKey(hari, on_delete=models.CASCADE, null=True)
    jam=models.CharField(max_length=20)

    def __str__(self):
        return self.NamaPaket