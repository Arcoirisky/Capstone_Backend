# Generated by Django 3.2 on 2021-05-06 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[(0, "Manager"), (1, "Zone leader")], default=0, max_length=100
            ),
        ),
    ]
