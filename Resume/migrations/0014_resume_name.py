# Generated by Django 3.2.5 on 2023-04-29 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0013_alter_extracurricular_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='name',
            field=models.CharField(default='resume', max_length=100),
            preserve_default=False,
        ),
    ]
