# Generated by Django 4.2 on 2023-04-10 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0004_alter_taskcard_column_delete_projectcolumn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcard',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
    ]
