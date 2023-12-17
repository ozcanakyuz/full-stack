# Generated by Django 4.2.7 on 2023-12-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_alter_comment_status_alter_post_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.BooleanField(choices=[(True, 'Ok'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='replycomment',
            name='status',
            field=models.BooleanField(choices=[(True, 'Ok'), (False, 'No')], default=False),
        ),
    ]
