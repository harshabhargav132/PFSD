# Generated by Django 5.0 on 2024-03-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_packages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='desc',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='packages',
            name='tourcode',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterModelTable(
            name='packages',
            table='packages_table',
        ),
    ]