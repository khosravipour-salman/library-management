# Generated by Django 3.0.8 on 2020-07-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management_app', '0006_bookmodel_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='cover',
            field=models.ImageField(blank=True, default='default-cover.png', null=True, upload_to=''),
        ),
    ]
