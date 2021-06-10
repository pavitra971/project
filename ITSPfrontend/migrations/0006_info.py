# Generated by Django 3.2.2 on 2021-06-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ITSPfrontend', '0005_auto_20210609_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=122)),
                ('teamleadername', models.CharField(max_length=122)),
                ('teamleaderphoneno', models.CharField(max_length=12)),
                ('teamleaderemail', models.CharField(max_length=122)),
                ('member1name', models.CharField(max_length=122)),
                ('member1phoneno', models.CharField(max_length=12)),
                ('member1email', models.CharField(max_length=122)),
                ('member2name', models.CharField(max_length=122)),
                ('member2phoneno', models.CharField(max_length=12)),
                ('member2email', models.CharField(max_length=122)),
                ('member3name', models.CharField(max_length=122)),
                ('member3phoneno', models.CharField(max_length=12)),
                ('member3email', models.CharField(max_length=122)),
                ('aboutteam', models.TextField(max_length=500)),
            ],
        ),
    ]
