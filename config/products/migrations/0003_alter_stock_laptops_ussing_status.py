# Generated by Django 4.2.15 on 2024-09-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_stock_laptops_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_laptops',
            name='ussing_status',
            field=models.CharField(choices=[('کارکرده', 'کارکرده'), ('تازه', 'تازه'), ('استوک.', 'استوک')], max_length=220),
        ),
    ]