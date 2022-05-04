# Generated by Django 4.0.4 on 2022-05-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_title', models.CharField(max_length=100)),
                ('course_description', models.CharField(max_length=250)),
                ('credits', models.IntegerField()),
                ('instructor', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
            ],
        ),
    ]