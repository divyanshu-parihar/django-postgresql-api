# Generated by Django 4.0.5 on 2022-06-02 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]