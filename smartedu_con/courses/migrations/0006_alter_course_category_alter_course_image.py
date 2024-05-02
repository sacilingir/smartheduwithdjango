# Generated by Django 5.0.3 on 2024-04-30 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='courses.category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='courses/default_course_image.jpg', upload_to='courses/%Y/%m/%d/'),
        ),
    ]
