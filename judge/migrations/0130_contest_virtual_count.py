# Generated by Django 2.2.17 on 2021-05-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0129_merge_20210504_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='virtual_count',
            field=models.IntegerField(default=0, verbose_name='the amount of virtual participants'),
        ),
    ]