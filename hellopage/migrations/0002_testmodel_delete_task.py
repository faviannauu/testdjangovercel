# Generated by Django 4.2.5 on 2023-09-20 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hellopage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
