# Generated by Django 3.2.5 on 2022-01-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=30)),
                ('e_age', models.CharField(max_length=2)),
                ('e_phone', models.CharField(max_length=10)),
                ('e_desc', models.TextField()),
            ],
        ),
    ]
