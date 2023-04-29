# Generated by Django 3.2.5 on 2023-04-28 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0007_auto_20230428_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Summary', models.TextField()),
                ('Resume', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='PORs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Club', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Start', models.DateField()),
                ('End', models.DateField()),
                ('Description', models.TextField()),
                ('Resume', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraCurricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity', models.TextField()),
                ('Description', models.TextField()),
                ('Resume', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Certificate', models.TextField()),
                ('CertifiedBy', models.CharField(max_length=100)),
                ('Resume', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Achievement', models.TextField()),
                ('Event', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Resume', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Resume.resume')),
            ],
        ),
    ]