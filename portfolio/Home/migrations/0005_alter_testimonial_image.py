# Generated by Django 5.1.2 on 2024-10-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(upload_to='pictures/'),
        ),
    ]
