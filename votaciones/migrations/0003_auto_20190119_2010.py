# Generated by Django 2.1.4 on 2019-01-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votaciones', '0002_auto_20190119_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nac',
            field=models.DateField(blank=True, null=True),
        ),
    ]
