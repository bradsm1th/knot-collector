# Generated by Django 5.0 on 2023-12-13 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_knot_type_alter_type_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='TypeOfKnot',
        ),
    ]
