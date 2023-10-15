# Generated by Django 4.2.4 on 2023-10-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('creator', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
