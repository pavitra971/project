# Generated by Django 3.2.2 on 2021-06-09 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITSPfrontend', '0006_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='aboutteam',
        ),
        migrations.RemoveField(
            model_name='info',
            name='member1email',
        ),
        migrations.RemoveField(
            model_name='info',
            name='member1name',
        ),
        migrations.RemoveField(
            model_name='info',
            name='member1phoneno',
        ),
        migrations.RemoveField(
            model_name='info',
            name='member2email',
        ),
        migrations.RemoveField(
            model_name='info',
            name='member2name',
        ),
        migrations.RemoveField(
            model_name='info',
            name='member2phoneno',
        ),
        migrations.RemoveField(
            model_name='info',
            name='member3email',
        ),
        migrations.RemoveField(
            model_name='info',
            name='member3name',
        ),
        migrations.RemoveField(
            model_name='info',
            name='member3phoneno',
        ),
        migrations.RemoveField(
            model_name='info',
            name='teamleaderemail',
        ),
        migrations.RemoveField(
            model_name='info',
            name='teamleadername',
        ),
        migrations.RemoveField(
            model_name='info',
            name='teamleaderphoneno',
        ),
        migrations.RemoveField(
            model_name='info',
            name='teamname',
        ),
    ]
