# Generated by Django 2.0.5 on 2020-10-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=100)),
                ('endtime', models.CharField(max_length=20)),
            ],
        ),
    ]
