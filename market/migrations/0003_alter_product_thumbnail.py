# Generated by Django 4.1.3 on 2022-11-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]