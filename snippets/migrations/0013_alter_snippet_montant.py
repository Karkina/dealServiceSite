# Generated by Django 3.2.8 on 2021-10-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0012_rename_brower_snippet_borower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='montant',
            field=models.DecimalField(decimal_places=2, max_digits=950),
        ),
    ]