# Generated by Django 4.1 on 2022-12-25 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='images/noprofile.jpg', null=True, upload_to='profile/image'),
        ),
    ]
