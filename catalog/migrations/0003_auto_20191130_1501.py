# Generated by Django 2.2.2 on 2019-11-30 09:31

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20191130_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=('product', 'tax'), separator=''),
        ),
    ]
