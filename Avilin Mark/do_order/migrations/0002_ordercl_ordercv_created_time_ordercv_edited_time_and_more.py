# Generated by Django 4.2.4 on 2023-09-06 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('do_order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('job_title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('experience', models.TextField()),
                ('skills', models.TextField()),
                ('created_time', models.TimeField(auto_now_add=True)),
                ('edited_time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='ordercv',
            name='created_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordercv',
            name='edited_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ordercv',
            name='fullname',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordercv',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cv_image'),
        ),
        migrations.AlterField(
            model_name='ordercv',
            name='employment_type',
            field=models.CharField(max_length=255),
        ),
    ]
