# Generated by Django 3.2.2 on 2021-06-09 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITSPfrontend', '0012_alter_info_member2name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='member1email',
            field=models.CharField(default='koil@gmail.com', max_length=122),
        ),
        migrations.AlterField(
            model_name='info',
            name='member1name',
            field=models.CharField(default='koil', max_length=122),
        ),
        migrations.AlterField(
            model_name='info',
            name='member1phoneno',
            field=models.CharField(default='9016512712', max_length=12),
        ),
        migrations.AlterField(
            model_name='info',
            name='member2email',
            field=models.CharField(default='koeo@gmail.com', max_length=122),
        ),
        migrations.AlterField(
            model_name='info',
            name='member2name',
            field=models.CharField(default='koeo', max_length=122),
        ),
        migrations.AlterField(
            model_name='info',
            name='member2phoneno',
            field=models.CharField(default='9016512722', max_length=12),
        ),
        migrations.AlterField(
            model_name='info',
            name='member3email',
            field=models.CharField(default='ko@gmail.com', max_length=122),
        ),
        migrations.AlterField(
            model_name='info',
            name='member3name',
            field=models.CharField(default='ko', max_length=122),
        ),
        migrations.AlterField(
            model_name='info',
            name='member3phoneno',
            field=models.CharField(default='9016512710', max_length=12),
        ),
    ]