# Generated by Django 3.2.4 on 2021-07-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='owner',
            field=models.CharField(db_index=True, max_length=64, null=True),
        ),
    ]
