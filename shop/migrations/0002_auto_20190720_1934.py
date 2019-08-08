# Generated by Django 2.2.3 on 2019-07-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='buttOn_text',
            new_name='button',
        ),
        migrations.AddField(
            model_name='banner',
            name='text',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
