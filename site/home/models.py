from django.db import models
from reality import settings


# Create your models here.


class Aim(models.Model):
    aim=models.CharField(max_length=15, blank=True, default="Продажа")
    period=models.CharField(max_length=30, blank=True, default=None)

    def __str__(self):
        return ' %s  %s' % (self.aim, self.period)

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"

class Location(models.Model):
    city=models.CharField(max_length=25, blank=True, default=None)
    district=models.CharField(max_length=25, blank=True, default=None)


    def __str__(self):
        return ' Город %s Округ %s' % (self.city, self.district)

    class Meta:
        verbose_name = "Расположение"
        verbose_name_plural = "Расположения"

class Zone(models.Model):
    name = models.CharField(max_length=25, blank=True, default=None)
    location=models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return ' Район %s ' % (self.name)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Район"

class Status(models.Model):
    name=models.CharField(max_length=20, blank=True, default=None)

    def __str__(self):
        return '  %s' % self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Source_of_proposal(models.Model):
    source = models.CharField(max_length=20, blank=True, default=None)

    def __str__(self):
        return ' %s' % self.source

    class Meta:
        verbose_name = "Источник объявления"
        verbose_name_plural = "Источники объявлений"


class Flat (models.Model):
    name = models.CharField(max_length=50, blank=True, default=None)
    descrip = models.TextField(blank=True, default=None)
    kol_rooms = models.IntegerField(default=1)
    square=models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    price_per_m2 = models.IntegerField(default=0)
    adress=models.CharField(max_length=200)
    aim=models.ForeignKey(Aim, null=True, blank=True, on_delete=models.CASCADE)
    location=models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, blank=True, null=True, on_delete=models.CASCADE)
    source=models.ForeignKey(Source_of_proposal, null=True, blank=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return ' id %s' % self.id

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"

    def save(self, *args, **kwargs):

        price_per= self.price / self.square
        self.price_per_m2=price_per

        super(Flat, self).save(*args, **kwargs)



class House (models.Model):
    name = models.CharField(max_length=50, blank=True, default=None)
    descrip = models.TextField(blank=True, default=None)
    kol_rooms = models.IntegerField(default=1)
    square=models.IntegerField(default=0)
    square_of_area = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    commission=models.IntegerField(default=0)
    price_per_m2 = models.IntegerField(default=0)
    adress=models.CharField(max_length=200)
    aim=models.ForeignKey(Aim, blank=True, null=True, on_delete=models.CASCADE)
    location=models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, blank=True, null=True, on_delete=models.CASCADE)
    source=models.ForeignKey(Source_of_proposal,blank=True, null=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return ' id %s' % self.id

    class Meta:
        verbose_name = "Дом и участок"
        verbose_name_plural = "Дома и участки"


    def save(self, *args, **kwargs):

        price_per= self.price / self.square
        self.price_per_m2=price_per

        super(House, self).save(*args, **kwargs)

class Photo(models.Model):
    image = models.ImageField(upload_to=settings.MEDIA_URL, max_length=500)
    is_main=models.BooleanField(default=True)
    flat = models.ForeignKey(Flat, blank=True, null=True,
                              default=None, on_delete=models.CASCADE)
    house = models.ForeignKey(House, blank=True, null=True,
                              default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return ' id %s' % self.id

    class Meta:
        verbose_name = "Фотка"
        verbose_name_plural = "Фоточки"

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url



class Realtor(models.Model):
    fio=models.CharField(max_length=50, blank=True, default=None)
    phone_number=models.IntegerField(default=0)
    email=models.EmailField()

    def __str__(self):
        return ' id %s' % self.id

    class Meta:
        verbose_name = "Риелтор"
        verbose_name_plural = "Риелторы"




