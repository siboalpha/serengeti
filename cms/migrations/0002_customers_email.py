# Generated by Django 4.0.3 on 2022-03-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]