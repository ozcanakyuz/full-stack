# Generated by Django 4.2.7 on 2023-12-16 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_rename_comment_replycomment_repcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='replycomment',
            name='comment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.comment'),
            preserve_default=False,
        ),
    ]
