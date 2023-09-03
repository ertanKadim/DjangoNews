# Generated by Django 4.2.4 on 2023-09-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Haber', 'verbose_name_plural': 'Haberler'},
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='null', max_length=150),
        ),
    ]