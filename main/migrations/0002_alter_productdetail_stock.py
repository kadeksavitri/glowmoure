# Generated by Django 5.1.1 on 2024-09-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
