# Generated by Django 4.2.3 on 2023-11-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_delete_profile_pic_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
