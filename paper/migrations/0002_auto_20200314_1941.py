# Generated by Django 3.0.4 on 2020-03-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='question_extracted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='paper',
            name='level',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='year',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
