# Generated by Django 5.0.3 on 2024-04-15 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='generalForStudent',
            fields=[
                ('idOfStudent', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfStudent', models.CharField(max_length=255)),
                ('statusOfLab', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='generalForTeacher',
            fields=[
                ('idOfTeacher', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfTeacher', models.CharField(max_length=255)),
                ('nameOfDiscipline', models.CharField(max_length=255)),
                ('statusOfLab', models.BooleanField(default=False)),
            ],
        ),
    ]
