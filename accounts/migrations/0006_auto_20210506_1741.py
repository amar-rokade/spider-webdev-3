# Generated by Django 3.0.6 on 2021-05-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_buy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='picture',
            field=models.URLField(),
        ),
    ]
