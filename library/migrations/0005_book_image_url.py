# Generated by Django 5.1.2 on 2024-10-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0004_alter_author_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
