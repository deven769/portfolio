# Generated by Django 2.1.4 on 2018-12-28 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_quotes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quotes',
            options={'verbose_name_plural': 'Quotes of the day'},
        ),
        migrations.AddField(
            model_name='quotes',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
