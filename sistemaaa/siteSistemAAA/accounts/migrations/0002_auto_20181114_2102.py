# Generated by Django 2.0.9 on 2018-11-14 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='cliente',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
