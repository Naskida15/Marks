# Generated by Django 3.1.7 on 2021-04-14 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory_page', '0006_auto_20210414_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persons_subjects',
            name='subject_id',
        ),
        migrations.AddField(
            model_name='persons_subjects',
            name='subject',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='directory_page.subjects'),
        ),
    ]
