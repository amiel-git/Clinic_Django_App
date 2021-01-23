# Generated by Django 3.1.3 on 2021-01-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.IntegerField()),
                ('birthday', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]