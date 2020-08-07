# Generated by Django 3.0.8 on 2020-08-01 10:03

import courses.fileds
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_content_file_image_text_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=courses.fileds.OrderFiled(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=courses.fileds.OrderFiled(blank=True, default=0),
            preserve_default=False,
        ),
    ]
