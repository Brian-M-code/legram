# Generated by Django 2.2.9 on 2020-02-13 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='pictures/'),
        ),
    ]
