# Generated by Django 4.2.3 on 2023-11-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default='path/to/default/file.pdf', upload_to='media/'),
        ),
    ]
