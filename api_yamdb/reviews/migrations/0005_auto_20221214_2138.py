# Generated by Django 3.2 on 2022-12-14 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20221214_2113'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='title',
            old_name='categorie',
            new_name='category',
        ),
    ]