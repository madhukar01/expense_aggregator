# Generated by Django 2.1.1 on 2018-09-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='expense_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
    ]
