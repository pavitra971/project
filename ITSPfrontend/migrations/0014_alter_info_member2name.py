# Generated by Django 3.2.2 on 2021-06-09 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITSPfrontend', '0013_auto_20210610_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='member2name',
            field=models.CharField(max_length=122),
        ),
    ]
