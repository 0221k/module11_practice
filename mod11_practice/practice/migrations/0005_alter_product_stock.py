# Generated by Django 5.1.2 on 2024-10-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]