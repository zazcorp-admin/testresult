# Generated by Django 3.2.4 on 2021-06-30 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_testresult_test_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testresult',
            name='test_date',
        ),
    ]