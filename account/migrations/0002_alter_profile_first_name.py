# Generated by Django 3.2.9 on 2022-01-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=200, null=True, verbose_name='الاسم الاول'),
        ),
    ]
