# Generated by Django 3.2.4 on 2021-06-29 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('fat', models.FloatField()),
                ('snf', models.FloatField()),
                ('urea', models.FloatField()),
                ('starch', models.FloatField()),
                ('detergent', models.FloatField()),
                ('antibiotic', models.FloatField()),
                ('acidity', models.CharField(max_length=100)),
                ('caustic_sova', models.FloatField()),
                ('desc', models.TextField()),
                ('test_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
