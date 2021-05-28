# Generated by Django 3.1.6 on 2021-05-28 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('task', models.CharField(max_length=100)),
                ('day', models.DateField()),
                ('reminder', models.BooleanField(default=False)),
            ],
        ),
    ]