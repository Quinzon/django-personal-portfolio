# Generated by Django 4.1.3 on 2023-05-14 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(),
        ),
    ]