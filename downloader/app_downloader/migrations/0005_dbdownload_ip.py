# Generated by Django 4.2.2 on 2023-07-01 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_downloader', '0004_achralarms_achrinf_alarmsrele_confighydra_configpvt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbdownload',
            name='ip',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
