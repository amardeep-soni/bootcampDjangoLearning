# Generated by Django 5.1.2 on 2024-10-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_person_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=100)),
                ('service_title', models.CharField(max_length=100)),
                ('service_desc', models.TextField()),
            ],
        ),
    ]
