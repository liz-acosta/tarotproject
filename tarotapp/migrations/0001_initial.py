# Generated by Django 4.2.1 on 2023-07-03 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TarotCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=2)),
                ('arcana', models.BooleanField(default=False)),
                ('image_filename', models.CharField(max_length=200)),
            ],
        ),
    ]