# Generated by Django 4.1 on 2022-09-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('urls', models.CharField(max_length=255)),
            ],
        ),
    ]
