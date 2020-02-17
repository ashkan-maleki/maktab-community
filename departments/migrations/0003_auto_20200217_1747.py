# Generated by Django 3.0.3 on 2020-02-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_auto_20200213_1406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departmentperiod',
            options={'verbose_name': 'Department Period', 'verbose_name_plural': 'Department Periods'},
        ),
        migrations.AlterModelOptions(
            name='selectedcourse',
            options={'verbose_name': 'Selected Course', 'verbose_name_plural': 'Selected Courses'},
        ),
        migrations.RenameField(
            model_name='selectedcourse',
            old_name='cousre',
            new_name='course',
        ),
        migrations.AlterField(
            model_name='room',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
