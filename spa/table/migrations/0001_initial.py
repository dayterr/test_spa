# Generated by Django 2.2.10 on 2021-12-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20, verbose_name='Дата')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('amount', models.BigIntegerField(verbose_name='Количество')),
                ('distance', models.BigIntegerField(verbose_name='Расстояние')),
            ],
        ),
    ]