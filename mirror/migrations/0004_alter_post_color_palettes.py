# Generated by Django 5.1.4 on 2024-12-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirror', '0003_alter_post_color_palettes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='color_palettes',
            field=models.TextField(),
        ),
    ]
