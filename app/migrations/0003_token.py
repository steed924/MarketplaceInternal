# Generated by Django 3.2.4 on 2021-07-27 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_withdrawrequest_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_id', models.PositiveBigIntegerField()),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to='app.artwork')),
            ],
        ),
    ]
