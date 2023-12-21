# Generated by Django 3.2.15 on 2022-09-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('add_on', models.DateTimeField(auto_now=True)),
                ('update_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]