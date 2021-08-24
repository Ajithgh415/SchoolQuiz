# Generated by Django 2.0.5 on 2020-10-26 13:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_createquiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=1000)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='createquiz',
            name='dob',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
