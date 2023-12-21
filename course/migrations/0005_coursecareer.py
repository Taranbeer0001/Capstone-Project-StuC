# Generated by Django 3.2.15 on 2022-10-14 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20220930_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='coursecareer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('skill', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
                ('jobLocation', models.CharField(max_length=100)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]