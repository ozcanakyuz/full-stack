# Generated by Django 4.2.7 on 2023-12-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=5),
        ),
    ]
