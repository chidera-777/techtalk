# Generated by Django 4.0.8 on 2022-11-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_user_userregistrar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistrar',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]