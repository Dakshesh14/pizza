# Generated by Django 3.2.6 on 2021-08-24 10:08

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='pizza'),
        ),
    ]
