# Generated by Django 3.2.6 on 2021-08-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_comment_parent_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='nesting_level',
        ),
        migrations.AddField(
            model_name='comment',
            name='uid',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
