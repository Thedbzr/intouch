# Generated by Django 3.1.4 on 2021-01-06 22:12

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210105_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('domain', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('invite', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='ph_number',
            field=phone_field.models.PhoneField(max_length=31),
        ),
        migrations.AddField(
            model_name='profile',
            name='business',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.business'),
        ),
    ]
