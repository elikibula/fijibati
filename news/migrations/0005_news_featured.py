# Generated by Django 4.2 on 2023-05-14 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]