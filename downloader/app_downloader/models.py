from django.db import models


class DbDownload(models.Model):
    object_name = models.CharField(max_length=255, verbose_name = "Наименование объекта")
    equipment_name = models.CharField(max_length=255, verbose_name = "Наименование оборудования")
    file_name = models.CharField(max_length=255, null=True, blank=True )
    version = models.IntegerField( null=True, blank=True)
    file = models.FileField(upload_to='documents', max_length=100, blank=True, verbose_name = "Файл")
    ip = models.CharField(max_length=255, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.object_name
