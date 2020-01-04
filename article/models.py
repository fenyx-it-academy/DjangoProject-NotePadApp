from django.db import models


class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Author")    # istedigimiz isimde gosterilsin istiyorsak parantez bitmeden ,verbose_name="Yazar" diyebiliriz ve admin sayfasinda degismis oldugunu goruruz. bunu diger basliklar icinde yapabiliriz.
    title = models.CharField(max_length=50, verbose_name="Title")
    content = models.TextField(max_length=2000)
    created_date = models.DateTimeField(auto_now=True, verbose_name="Created Date")            # eklenen makale icin otomatik tarih eklesin
    def __str__(self):       # baslik ve diger yazilarin admin kanalinda gorunsun istiyorsak bu fonksiyonu yapmaliyiz
        return self.title

    class Meta:
        ordering = ['-created_date']                  # goruntude islem sirasi
