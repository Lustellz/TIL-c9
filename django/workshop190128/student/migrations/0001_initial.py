# Generated by Django 2.1.5 on 2019-01-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('birthday', models.DateField(max_length=100)),
                ('age', models.IntegerField(max_length=100)),
            ],
        ),
    ]
