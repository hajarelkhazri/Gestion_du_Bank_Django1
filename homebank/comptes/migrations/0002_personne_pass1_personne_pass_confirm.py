# Generated by Django 4.2 on 2024-05-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='pass1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='personne',
            name='pass_confirm',
            field=models.IntegerField(null=True),
        ),
    ]
