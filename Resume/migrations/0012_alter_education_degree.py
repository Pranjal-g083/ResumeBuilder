# Generated by Django 3.2.5 on 2023-04-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0011_alter_professionalsummary_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='Degree',
            field=models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.tech', 'M.tech'), ('M.Sc', 'M.Sc'), ('P.hd', 'P.hd'), ('M.S.R.', 'M.S.R.'), ('Senior Secondary', 'Senior Secondary'), ('Secondary', 'Secondary')], default=None, max_length=30),
        ),
    ]
