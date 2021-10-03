# Generated by Django 3.2.7 on 2021-10-03 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shooting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('photographer', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
