# Generated by Django 4.2.7 on 2023-12-14 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('False', 'False')], default='New', max_length=10),
        ),
    ]
