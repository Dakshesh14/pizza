# Generated by Django 3.2.6 on 2021-08-24 09:52

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='')),
                ('pizza_type', models.CharField(choices=[('V', 'Veg'), ('NV', 'Non-Veg')], max_length=2)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
